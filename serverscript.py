import urllib2
import json
from pprint import pprint
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='mm811project')
cursor = cnx.cursor()

#Neighbourhood name
urlNN = "https://data.edmonton.ca/api/views/65fr-66s6/rows.json?accessType=DOWNLOAD"
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
jfile = urllib2.urlopen(urlNN).read()
dataNN = json.loads(jfile)
jfile = urllib2.urlopen(urlNB).read()
dataNB = json.loads(jfile)
jfile = urllib2.urlopen(urlNC).read()
dataNC = json.loads(jfile)

add_neighbourhood = ("INSERT INTO neighbourhood_tmp "
               "(NEIGHBOURHOOD_NAME,NEIGHBOURHOOD_AREA,NEIGHBOURHOOD_LATI,NEIGHBOURHOOD_LONG) "
               "VALUES (%s,%s,%s,%s)")
for i in range(len(dataNC["meta"]["view"]["columns"])):
    pprint(dataNC["meta"]["view"]["columns"][i]["name"])
area=""
latitude=0
longitude=0
for i in range(len(dataNN["data"])):
    for j in range(len(dataNB["data"])):
        if dataNB["data"][i][8] == dataNN["data"][i][8]:
            area = dataNB["data"][i][9]
            break
        
    for j in range(len(dataNC["data"])):
        if dataNC["data"][i][9] == dataNN["data"][i][8]:
            latitude = dataNC["data"][i][10]
            longitude = dataNC["data"][i][11]
            #pprint(latitude);
            break    
    neighbourdata=(dataNN["data"][i][8],area,latitude,longitude)
    cursor.execute(add_neighbourhood, neighbourdata) 
    cnx.commit()
    
update_area = ("UPDATE neighbourhood_tmp"
            "SET NEIGHBOURHOOD_AREA=%s WHERE NEIGHBOURHOOD_NAME=%s")
    


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

cursor.close()
cnx.close()