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
- Alchemy API - Sentiment Analysis.
- Google maps API - Render tweets on map.
- Twitter API - Streaming tweets from Twitter.
- Twitter Bootstrap Framework- CSS.

To install the dependencies run the “install.sh” shell script.

Web Application URL - http://my-env.jwbwzuwmmk.us-west-2.elasticbeanstalk.com/

Sceenshots-
Web Application functionalities and AWS configurations - 

Selected keyword 'love' from the dropdown and clicked on "Search Tweets".

![screen shot 2017-03-12 at 1 42 28 pm](https://cloud.githubusercontent.com/assets/22078080/23834422/9712b3ae-072c-11e7-82d9-4b304aa17d98.png)

Displaying the results with sentiments(Positive, Negative) on Google Map.

![screen shot 2017-03-12 at 1 43 48 pm](https://cloud.githubusercontent.com/assets/22078080/23834397/3c10a86c-072c-11e7-9c8b-eefe25d99536.png)

GeoSpatial Search Feature - User places marker on Map and hits "Geo Search".

![screen shot 2017-03-12 at 1 44 45 pm](https://cloud.githubusercontent.com/assets/22078080/23834395/3c0ff1d8-072c-11e7-84c4-c256e603b594.png)

GeoSpatial Search Results - Rendering Geo Search Data on Map.

![screen shot 2017-03-12 at 1 57 20 pm](https://cloud.githubusercontent.com/assets/22078080/23834393/3c0df482-072c-11e7-8c7d-3293ff61e9ac.png)

AWS Configurations - 

Elastic Search

![screen shot 2017-03-12 at 1 46 43 pm](https://cloud.githubusercontent.com/assets/22078080/23834654/76fb0f2c-0730-11e7-8d0d-168f48167121.png)

Showing data indexed in Elastic Search -

![screen shot 2017-03-12 at 2 41 52 pm](https://cloud.githubusercontent.com/assets/22078080/23834761/21e7ff48-0732-11e7-9b69-ef49c1b54b57.png)

SQS Message Queue - 

![screen shot 2017-03-12 at 1 47 13 pm](https://cloud.githubusercontent.com/assets/22078080/23834653/76fb1594-0730-11e7-9149-ae9729453f21.png)

SQS - Diaplying Message Details

![screen shot 2017-03-12 at 1 48 59 pm](https://cloud.githubusercontent.com/assets/22078080/23834652/76faa622-0730-11e7-9917-06a56ea68956.png)

SQS - Displaying Notification Detail received from SNS.

![screen shot 2017-03-12 at 1 50 03 pm](https://cloud.githubusercontent.com/assets/22078080/23834651/76fa53c0-0730-11e7-8586-99e919c0fbc5.png)

SNS Configuration - Topic and subscription.

![screen shot 2017-03-12 at 2 40 02 pm](https://cloud.githubusercontent.com/assets/22078080/23834742/e0e4ab5e-0731-11e7-999e-de946c175827.png)



