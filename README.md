# Cloud Computing Course: Assignment 1 Twitt Map

### Assignment Team

|Net ID | Name|
|----|----|
| ppd241 | Parita Piyush Dhandha
| sg3533 | Sneha Ghosh

**Description**:
The Twitt Map is a web application in **Django framework**. It is a scalable application deployed on the **ElasticBeanstalk**.

The application provides following functionalities-

1. Search for tweets having a particular keyword (out of given keywords).
2. Search scans both downloaded and live tweets.
3. It shows count of new tweets getting indexed.
4. The search results are displayed as a heat map showing the tweets in blue (indicating positive tone) and red-yellow (indicating negative tone) for better visualization. 
5. Geo-Spatial Search is also implemented. Use can place a marker on the map and give distance in kilo meter as radius in the text box and hit “Geo-Search” button, the application searches for the tweets within the geo distance from marker and displays them on map.

The following modules are used in the Web Application:

- Django framework and Python
- Elastic Beanstalk - Deploy application.
- Elastic Search - indexing the tweets and searching the indexed data.
- SQS - Message Queue service for queuing tweets and notifications.
- SNS - Push Notification Service to index data to Elastic Search.
- NaturalLanguageUnderstandingV1 - Sentiment Analysis.
- Google maps API - Render tweets on map.
- Twitter API - Streaming tweets from Twitter.
- Twitter Bootstrap Framework- CSS.

To install the dependencies run the “install.sh” shell script.

Web Application URL - http://my-env.jwbwzuwmmk.us-west-2.elasticbeanstalk.com/

Sceenshots-
Web Application functionalities and AWS configurations - 

Selected keyword 'friends' from the dropdown and clicked on "Search Tweets".

![screen shot 2017-04-22 at 12 45 03 pm](https://cloud.githubusercontent.com/assets/22078080/25306452/65ed1126-275b-11e7-9d61-ef560c2c8f2b.png)

Displaying the results with sentiments(Positive, Negative, Neutral) on Google Map.

![screen shot 2017-04-22 at 12 44 02 pm](https://cloud.githubusercontent.com/assets/22078080/25306455/6cd2e95c-275b-11e7-8660-ceb7bf13be94.png)

GeoSpatial Search Feature - User places marker on Map and hits "Geo Search".

![screen shot 2017-04-22 at 12 52 06 pm](https://cloud.githubusercontent.com/assets/22078080/25306458/7ca23ea0-275b-11e7-8127-ef8d3419fce0.png)

GeoSpatial Search Results - Rendering Geo Search Data on Map.

![screen shot 2017-04-22 at 12 52 31 pm](https://cloud.githubusercontent.com/assets/22078080/25306460/7f1bb620-275b-11e7-84bc-0c17eac816df.png)

AWS Configurations - 

Elastic Search

![screen shot 2017-04-22 at 1 02 48 pm](https://cloud.githubusercontent.com/assets/22078080/25306500/114bca30-275c-11e7-9b5e-291fa6a636c4.png)

Showing data indexed in Elastic Search -

![screen shot 2017-04-22 at 1 06 43 pm](https://cloud.githubusercontent.com/assets/22078080/25306523/9902992c-275c-11e7-987f-af9056e4b3f9.png)

SQS Message Queue - 

![screen shot 2017-03-12 at 1 47 13 pm](https://cloud.githubusercontent.com/assets/22078080/23834653/76fb1594-0730-11e7-9149-ae9729453f21.png)

SQS - Diaplying Message Details

![screen shot 2017-03-12 at 1 48 59 pm](https://cloud.githubusercontent.com/assets/22078080/23834652/76faa622-0730-11e7-9917-06a56ea68956.png)

SQS - Displaying Notification Detail received from SNS.

![screen shot 2017-03-12 at 1 50 03 pm](https://cloud.githubusercontent.com/assets/22078080/23834651/76fa53c0-0730-11e7-8586-99e919c0fbc5.png)

SNS Configuration - Topic and subscription.

![screen shot 2017-03-12 at 2 40 02 pm](https://cloud.githubusercontent.com/assets/22078080/23834742/e0e4ab5e-0731-11e7-999e-de946c175827.png)



