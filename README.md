# TwittAssignment1
Display Tweets on google map.
The twittmap is a web application in Django framework. It is deployed on the ElasticBeanstalk so that it can be scaled. The user can open the web application through the url. They can search for the count of  twitts having a particular keyword (out of given keywords) and the search for those twitts is done through elastic search. The application also searches the incoming twitts and stores them in the Elastic Search storage making them searchable. It also shows count of these new twitts.
There is a heat map shown which shows the twitts in blue (indicating positive tone) and red-yellow (indicating negative tone) on the map. The user can pin point a location on the map and give some distance in kilo meter as radius in the text box given and when hits “Geo-Search” button, the application searches for the twitts having the key word that was selected in the selected area with indication of positive or negative tone.
The following modules are used in the deployment of web application:
 The web application in Django format
Elastic Beanstalk to deploy the application
Elastic Search for indexing the twitts and searching through them
SQS for queuing twitts
SNS for passing the real time twitts from queue (i.e. SQS) to Elastic Search
Alchemi API for sentiment analysis in backend
Google maps API  to show twitts on map
Twitter API for getting streaming twitts from twitter.
 
To install the dependencies run the “install.sh” shell script.

To get started go to url http://my-env.jwbwzuwmmk.us-west-2.elasticbeanstalk.com/ to open the home page of the application.

Sceenshots - 
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



