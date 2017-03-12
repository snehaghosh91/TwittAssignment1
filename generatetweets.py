import csv
import json
import sys

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import boto3
from elasticsearch import Elasticsearch

KEYWORDS = ['morning', 'facebook', 'love', 'central park', 
            'music', 'friends', 'pizza', 'life']

# Variables that contains the user credentials to access Twitter API
# sudo pip install certifi
# sudo pip install elasticsearch
# sudo pip install tweepy
# sudo pip isntall boto3
# pip install awscli
consumer_key='7AwIFBjtRTEKErsWDSPTCcn0V'
consumer_secret='YVft0bAAKtRM38Fu1J0tgOBeS21QvkTMmI5WQpseXMSpqn48Wu'
access_token='113727914-bXEa6uZUDVcctR5w82QRDxkA2AFSiVDMqQjyxK9F'
access_token_secret='Si9xOHksG55HSVjFqdae8O7QZsxwI19aK0ZXA0hxXbMFh'
    
sqs = boto3.client("sqs")
queue = sqs.get_queue_url(QueueName="tweet_queue")

index_name = "twitter-index"
mapping = {"mappings": {
    "tweet": {
        "properties": {
            "tweet": {
                "type": "string"
            },
            "location": {
                "type": "geo_point"
            },
            "sentiment": {
                "type": "string"
            }
        }
    }
}
}
host = ["https://search-mydomain-54whxc437ldzjler77blx3uxw4.us-west-2.es.amazonaws.com"]
es = Elasticsearch(host)
#es.indices.create(index=index_name, body=mapping)

# This is a listener that appends the tweet text, longitude and latitude to a csv file.
class StdOutListener(StreamListener):

    def on_data(self, data):
        global queue
        try:
            json_data = json.loads(data)
            output_data = getData(json_data)
            if output_data:
                print output_data
                responses = sqs.send_message(QueueUrl= queue['QueueUrl'], MessageBody='TweetInfo', MessageAttributes=output_data)
            #queue.send_message(MessageBody="TweetInfo", MessageAttributes=data)
        except Exception as e:
            print ("Error: "+str(e))

    def on_error(self, status):
        print(status)

def addDownloadedTweets():
    jsondict = []
    with open('output.json') as data_file:  
        data = json.load(data_file)
        jsondict = json.loads(data)
    for x in jsondict:
        present = False
        for key in KEYWORDS:
            if key in x['text']:
                print key
                present = True
        if not present:
            continue
        output_data = getData(x)
        if output_data:
            responses = sqs.send_message(QueueUrl= queue['QueueUrl'], MessageBody='TweetInfo', MessageAttributes=output_data)

def getData(json_data):
    tweet = json_data['text']
    id = str(json_data['id'])
    lon = None
    lat = None
    data = {}
    if 'latitude' in json_data.keys() and 'longitude' in json_data.keys():
        lon = float(json_data['latitude'])
        lat = float(json_data['longitude'])
    elif json_data['coordinates']:
        lon = float(json_data['coordinates']['coordinates'][0])
        lat = float(json_data['coordinates']['coordinates'][1])
    elif 'place' in json_data.keys() and json_data['place']:
        lon = float(json_data['place']['bounding_box']['coordinates'][0][0][0])
        lat = float(json_data['place']['bounding_box']['coordinates'][0][0][1])
    elif 'retweeted_status' in json_data.keys() and 'place' in json_data['retweeted_status'].keys() and json_data['retweeted_status']['place']:
        lon = float(json_data['retweeted_status']['place']['bounding_box']['coordinates'][0][0][0])
        lat = float(json_data['retweeted_status']['place']['bounding_box']['coordinates'][0][0][1])
    elif 'quoted_status' in json_data.keys() and 'place' in json_data['quoted_status'].keys() and json_data['quoted_status']['place']:
        lon = float(json_data['quoted_status']['place']['bounding_box']['coordinates'][0][0][0])
        lat = float(json_data['quoted_status']['place']['bounding_box']['coordinates'][0][0][1])
    if lat and lon:
        data =  {
                    'Id': {'DataType': 'Number', 'StringValue': str(id)},
                    'Tweet': {'DataType': 'String', 'StringValue': str(tweet)},
                    'Latitude': {'DataType': 'Number', 'StringValue': str(lat)},
                    'Longitude': {'DataType': 'Number', 'StringValue': str(lon)}
                }
    return data

if __name__ == '__main__':
    addDownloadedTweets()
    # pass
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(languages=['en'], track=KEYWORDS)
