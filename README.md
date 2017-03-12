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

![screen shot 2017-03-12 at 1 42 28 pm](https://cloud.githubusercontent.com/assets/22078080/23834422/9712b3ae-072c-11e7-82d9-4b304aa17d98.png)

![screen shot 2017-03-12 at 1 43 48 pm](https://cloud.githubusercontent.com/assets/22078080/23834397/3c10a86c-072c-11e7-9c8b-eefe25d99536.png)

![screen shot 2017-03-12 at 1 44 45 pm](https://cloud.githubusercontent.com/assets/22078080/23834395/3c0ff1d8-072c-11e7-84c4-c256e603b594.png)

![screen shot 2017-03-12 at 1 57 20 pm](https://cloud.githubusercontent.com/assets/22078080/23834393/3c0df482-072c-11e7-8c7d-3293ff61e9ac.png)




