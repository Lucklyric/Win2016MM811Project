import urllib2
import json
from pprint import pprint
import mysql.connector

#Neighbourhood Boundaries
urlNB = "https://data.edmonton.ca/api/views/nckr-nnqj/rows.json?accessType=DOWNLOAD"
#Neighbourhoods (Centroid Point)
urlNC="https://data.edmonton.ca/api/views/3b6m-fezs/rows.json?accessType=DOWNLOAD"
#Playgrounds
urlP="https://data.edmonton.ca/api/views/c4nr-3quz/rows.json?accessType=DOWNLOAD"
#Tennis Courts
urlTC="https://data.edmonton.ca/api/views/25b5-e682/rows.json?accessType=DOWNLOAD"
#Edmonton Public Schools (2015 - 2016)
urlEPS="https://data.edmonton.ca/api/views/ehbr-emhe/rows.json?accessType=DOWNLOAD"
#Edmonton Catholic Schools (2015 - 2016)
urlECS="https://data.edmonton.ca/api/views/f6w2-hzex/rows.json?accessType=DOWNLOAD"
#Dwelling Unit By Structure Type (Neighbourhood) 
urlDUST="https://data.edmonton.ca/api/views/bjgi-976r/rows.json?accessType=DOWNLOAD"
#Trees 
urlT="https://data.edmonton.ca/api/views/eecg-fc54/rows.json?accessType=DOWNLOAD"

#read all urls
jfile = urllib2.urlopen(urlNB).read()
data = json.loads(jfile)
pprint(data["meta"]["view"]["columns"][9]["name"])
pprint(len(data["data"]))


#jfile = urllib2.urlopen(urlNC).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlP).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlTC).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlEPS).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlECS).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlDUST).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

#jfile = urllib2.urlopen(urlT).read()
#data = json.loads(jfile)
#pprint(data["meta"]["view"]["name"])

