import urllib2
import json
from pprint import pprint
import mysql.connector
from init_server import *

#Neighbourhood name
urlNNmeta="https://data.edmonton.ca/api/views/65fr-66s6"
#Neighbourhood Boundaries
urlNBmeta = "https://data.edmonton.ca/api/views/nckr-nnqj"
#Neighbourhoods (Centroid Point)
urlNCmeta="https://data.edmonton.ca/api/views/3b6m-fezs"
#Playgrounds
urlPmeta="https://data.edmonton.ca/api/views/c4nr-3quz"
#Edmonton Public Schools (2015 - 2016)
urlEPSmeta="https://data.edmonton.ca/api/views/ehbr-emhe"
#Edmonton Catholic Schools (2015 - 2016)
urlECSmeta="https://data.edmonton.ca/api/views/f6w2-hzex"
#Dwelling Unit By Structure Type (Neighbourhood) 
urlDUSTmeta="https://data.edmonton.ca/api/views/bjgi-976r"
#employment status
urlEmeta="https://data.edmonton.ca/api/views/aaar-q4e3"
#age
urlAmeta="https://data.edmonton.ca/api/views/44iw-gmaw"

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='mm811project')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM relative_dataset")
init=0
dataset_info=cursor.fetchall()
if cursor.rowcount==0:
    init=1

cursordel=cnx.cursor()
del_relative_data=("TRUNCATE relative_data")
del_relative_dataset=("TRUNCATE relative_dataset")
del_major_dataset=("TRUNCATE major_dataset")
del_major_neighbourhood_tmp=("TRUNCATE neighbourhood_tmp")
delall=0
delpart=0
for row in dataset_info:
    jfile = urllib2.urlopen(urlNNmeta).read()
    dataNNmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlNBmeta).read()
    dataNBmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlNCmeta).read()
    dataNCmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlPmeta).read()
    dataPmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlEPSmeta).read()
    dataEPSmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlECSmeta).read()
    dataECSmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlDUSTmeta).read()
    dataDUSTmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlEmeta).read()
    dataEmeta = json.loads(jfile)
    jfile = urllib2.urlopen(urlAmeta).read()
    dataAmeta = json.loads(jfile)    
 
    if dataNNmeta["name"].lower()==row[1]:
        if dataNNmeta["viewLastModified"]-row[3]>0:
            delall=1
    elif dataNBmeta["name"].lower()==row[1]:
        if dataNBmeta["viewLastModified"]-row[3]>0:    
            delall=1
    elif dataNCmeta["name"].lower()==row[1]:
        if dataNCmeta["viewLastModified"]-row[3]>0:    
            delall=1
    elif dataPmeta["name"].lower()==row[1]:
        if dataPmeta["viewLastModified"]-row[3]>0:     
            delpart=1
    elif dataEPSmeta["name"].lower()==row[1]:
        if dataEPSmeta["viewLastModified"]-row[3]>0: 
            delpart=1
    elif dataECSmeta["name"].lower()==row[1]:
        if dataECSmeta["viewLastModified"]-row[3]>0:     
            delpart=1          
    elif dataDUSTmeta["name"].lower()==row[1]:
        if dataDUSTmeta["viewLastModified"]-row[3]>0: 
            delpart=1
    elif dataEmeta["name"].lower()==row[1]:
        if dataEmeta["viewLastModified"]-row[3]>0:    
            delpart=1
    elif dataAmeta["name"].lower()==row[1]:
        if dataAmeta["viewLastModified"]-row[3]>0:
            delpart=1

if delall==1 and init==0:
    cursordel.execute(del_relative_data)
    cursordel.execute(del_relative_dataset) 
    cursordel.execute(del_major_dataset) 
    cursordel.execute(del_major_neighbourhood_tmp)
    insert_to_neibourhood()
    insert_to_major()
    insert_to_relative_data()
    insert_to_relative_dataset()
elif delall==0 and delpart==1 and init==0:
    cursordel.execute(del_relative_data)
    cursordel.execute(del_relative_dataset) 
    cursordel.execute(del_major_dataset) 
    insert_to_major()
    insert_to_relative_data()
    insert_to_relative_dataset()     

elif init==1:
    insert_to_neibourhood()
    insert_to_major()
    insert_to_relative_data()
    insert_to_relative_dataset()
    
cursor.close()
cnx.close()