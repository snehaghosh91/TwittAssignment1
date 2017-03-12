#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, London,
#    and outputs them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *

import sys
import json

latitude = 30.6619958	# geographical centre of search
longitude = -70.9888796	# geographical centre of search
max_range = 10000000			# search range in kilometres
num_results = 500		# minimum results to obtain
outfile = "output.json"

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
exec(open("./config.py").read(), config)
#execfile("config.py", config)
  
#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# open a file to write (mode "w"), and create a CSV writer object
#-----------------------------------------------------------------------
#csvfile = file(outfile, "w")
with open(outfile, 'w') as jsonfile:

#-----------------------------------------------------------------------
# add headings to our CSV file
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
#-----------------------------------------------------------------------
   
        last_id = None
        #-----------------------------------------------------------------------
        # perform a search based on latitude and longitude
        # twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
        #-----------------------------------------------------------------------
        query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 1000, max_id = last_id, lang="en")
        output_dict = []
        for result in query["statuses"]:
                #-----------------------------------------------------------------------
                # only process a result if it has a geolocation
                #-----------------------------------------------------------------------
                if result["geo"]:
                        x = {}
                        Id = result["id"]
                        text = result["text"]
                        text = text.encode('ascii', 'replace')
                        latitude = result["geo"]["coordinates"][0]
                        longitude = result["geo"]["coordinates"][1]
                        x['id'] = Id
			x['text'] = text
			x['latitude'] = latitude
			x['longitude'] = longitude
                        output_dict.append(x)

       

	# Transform python object back into json
	output_json = json.dumps(output_dict)

	# Show json
	print output_json

        json.dump(output_json, jsonfile)

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
jsonfile.close()

print ("written to %s" % outfile)

