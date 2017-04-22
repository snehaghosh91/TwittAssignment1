import multiprocessing
import time
import boto3
import json
import responses
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import WatsonException
from watson_developer_cloud.natural_language_understanding.features import (
    v1 as features)

sqs = boto3.resource('sqs')
sns = boto3.client('sns')

# Insert values from root.csv file given as part of assignment submission to run 
# this file on local for live tweets.
# sqs = boto3.client("sqs", region_name='us-west-2', aws_access_key_id="",
#   aws_secret_access_key="")
# sns = boto3.client('sns', region_name='us-west-2', aws_access_key_id="",
#   aws_secret_access_key="")

queue = sqs.get_queue_by_name(QueueName='tweet_queue')
sentiment = ["positive","negative","neutral"]
arn = 'arn:aws:sns:us-west-2:682777743357:mytopic'

natural_language_understanding = NaturalLanguageUnderstandingV1(url='https://gateway.watsonplatform.net/natural-language-understanding/api',
                                     version='2017-02-27',
                                     username='4a2440c9-48d1-49e7-b481-0ad1ae2f3aab',
                                     password='Lj8FSwFIuUGL')
def worker_main(queue):
    while True:
        messages = queue.receive_messages(MessageAttributeNames=['Id', 'Tweet', 'Latitude', 'Longitude'])
        print("Received messages")
        if len(messages)>0:
            for message in messages:
                # Get the custom author message attribute if it was set
                if message.message_attributes is not None:
                    id = message.message_attributes.get('Id').get('StringValue')
                    tweet = message.message_attributes.get('Tweet').get('StringValue')
                    lat = message.message_attributes.get('Latitude').get('StringValue')
                    lng = message.message_attributes.get('Longitude').get('StringValue')
                    try:
                        response = natural_language_understanding.analyze(
                            text=tweet, features=[features.Sentiment()])
                        senti = response["sentiment"]["document"]["label"]
                        print senti
                        # senti = response.get('docSentiment').get('type')
                    except Exception as e:
                        print("ERROR: "+str(e))
                        senti = "neutral"
                    # Using SNS
                    sns_message = {"id":id, "tweet":tweet, "lat":lat, "lng": lng, "sentiment":senti}
                    print("SNS messsage: "+str(sns_message))
                    sns.publish(TargetArn=arn, Message=json.dumps({'default':json.dumps(sns_message)}))
                # print('Id: {0}; Tweet: {1}; Latitude: {2}; Longitude: {3}; sentiment: {4}'.format(id,tweet,lat,lng,senti))
                # Let the queue know that the message is processed
                message.delete()
        else:
            time.sleep(1)

pool = multiprocessing.Pool(10, worker_main, (queue,))

while True:
    pass
'''
{
  "url": "https://gateway-a.watsonplatform.net/calls",
  "note": "It may take up to 5 minutes for this key to become active",
  "apikey": "354656d61227e678ad152a63dbd5b93cdeea4b93"
}
'''
