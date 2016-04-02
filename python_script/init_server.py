import urllib2
import json
from pprint import pprint
import mysql.connector

#function defination
def get_polygon(poly):
    coords=[]
    poly=poly.replace("(","")
    poly=poly.replace(")","")
    poly=poly.replace("MULTIPOLYGON ","")
    polysplit=poly.split(',')
    plen=len(polysplit)
    for i in range(plen):
        coord=polysplit[i];
        coords.append(coord)        
    return coords

def get_min_max(polygon):
    coords=get_polygon(polygon)
    latis=[];
    longis=[];
    for i in range(len(coords)):
        longi = coords[i].split()[0]
        lati = coords[i].split()[1]
        longi=longi.strip()
        lati=lati.strip()
        latis.append(float(lati.strip()))
        longis.append(float(longi.strip()))
    latis.sort()
    longis.sort()
    min_max=[]
    min_max.append(latis[0])
    min_max.append(latis[len(latis)-1])
    min_max.append(longis[0])
    min_max.append(longis[len(longis)-1])
    return min_max

def check_inside(latitude,longitude,min_max):
    if latitude>=min_max[0] and latitude<=min_max[1] and longitude>=min_max[2] and longitude<=min_max[3]:
        return True

def insert_to_neibourhood():
    cursor = cnx.cursor()    
    poly = get_min_max(dataNB["data"][0][9])
    add_neighbourhood = ("INSERT INTO neighbourhood_tmp "
                   "(NEIGHBOURHOOD_NAME,NEIGHBOURHOOD_AREA,NEIGHBOURHOOD_LATI,NEIGHBOURHOOD_LONG) "
                   "VALUES (%s,%s,%s,%s)")
    for i in range(len(dataNN["data"])):
        area=""
        latitude=0
        longitude=0       
        for j in range(len(dataNB["data"])):
            if dataNB["data"][j][8].lower().strip() == dataNN["data"][i][8].lower().strip():
                area = dataNB["data"][j][9]
                break
        for k in range(len(dataNC["data"])):
            if dataNC["data"][k][9].lower().strip() == dataNN["data"][i][8].lower().strip():
                latitude = dataNC["data"][k][10]
                longitude = dataNC["data"][k][11]
                break    
        neighbourdata=(dataNN["data"][i][8],area,latitude,longitude)
        cursor.execute(add_neighbourhood, neighbourdata) 
        cnx.commit()
    cursor.close()
    
def insert_to_major():
    cursor = cnx.cursor()
    cursor.execute("select * from neighbourhood_tmp")
    neibourhood_data=cursor.fetchall()
    if cursor.rowcount>0:
        for row in neibourhood_data: 
            NUM_PLAYGROUNDS=0
            NUM_PUBLIC_SCHOOLS=0
            NUM_CATHOLIC_SCHOOLS=0
            NUM_SINGLE=0
            NUM_DUPLEX=0
            NUM_ROW_HOUSE=0
            NUM_APARTMENT_FIVE=0
            NUM_APARTMENT_FOUR=0
            NUM_HOTEL=0
            NUM_AGE_FOURTEEN=0
            NUM_AGE_THIRTYFIVE=0
            NUM_AGE_SIXTY=0
            NUM_AGE_SIXTYPLUS=0
            NUM_EMPLOYMENT_STUDENT=0
            NUM_EMPLOYMENT_UNEMPLOYED=0
            NUM_EMPLOYMENT_EMPLOYED=0  
            la=0
            lo=0
            print row[0]            
            if row[1] is None or row[1]=="":
                continue
            else:
                min_max=[]
                min_max=get_min_max(row[1])
                for i in range(len(dataP["data"])):
                    la=dataP["data"][i][10]
                    lo=dataP["data"][i][9]
                    if check_inside(float(la.strip()),float(lo.strip()),min_max):
                        NUM_PLAYGROUNDS+=1
                for i in range(len(dataEPS["data"])):
                    la=dataEPS["data"][i][20]
                    lo=dataEPS["data"][i][21]
                    if check_inside(float(la.strip()),float(lo.strip()),min_max):
                        NUM_PUBLIC_SCHOOLS+=1
                for i in range(len(dataECS["data"])):
                    la=dataECS["data"][i][20]
                    lo=dataECS["data"][i][21]
                    if check_inside(float(la.strip()),float(lo.strip()),min_max):
                        NUM_CATHOLIC_SCHOOLS+=1
                for i in range(len(dataDUST["data"])):
                    if dataDUST["data"][i][10].lower()==row[0].lower():
                        NUM_SINGLE+=int(dataDUST["data"][i][11])
                        NUM_DUPLEX+=int(dataDUST["data"][i][12])
                        NUM_ROW_HOUSE+=int(dataDUST["data"][i][13])
                        NUM_APARTMENT_FIVE+=int(dataDUST["data"][i][14])
                        NUM_APARTMENT_FOUR+=int(dataDUST["data"][i][15])
                        NUM_HOTEL=float(dataDUST["data"][i][18])                    
                for i in range(len(dataA["data"])):
                    if dataA["data"][i][10].lower()==row[0].lower():
                        age_str=dataA["data"][i][11]
                        if age_str=="85+":
                            age_str=85
                        elif age_str=="No Response":
                            age_str=1000
                        if int(age_str)<=14:
                            NUM_AGE_FOURTEEN+=int(dataA["data"][i][12])
                            NUM_AGE_FOURTEEN+=int(dataA["data"][i][13])
                        elif int(age_str)>14 and int(age_str)<=35:
                            NUM_AGE_THIRTYFIVE+=int(dataA["data"][i][12])
                            NUM_AGE_THIRTYFIVE+=int(dataA["data"][i][13])                        
                        elif int(age_str)>35 and int(age_str)<=60:
                            NUM_AGE_SIXTY+=int(dataA["data"][i][12])
                            NUM_AGE_SIXTY+=int(dataA["data"][i][13])  
                        elif int(age_str)>60 and int(age_str)<200:
                            NUM_AGE_SIXTYPLUS+=int(dataA["data"][i][12])
                            NUM_AGE_SIXTYPLUS+=int(dataA["data"][i][13])
                for i in range(len(dataE["data"])):
                    if dataE["data"][i][10].lower()==row[0].lower():
                        NUM_EMPLOYMENT_STUDENT+=int(dataE["data"][i][11])
                        NUM_EMPLOYMENT_STUDENT+=int(dataE["data"][i][12])
                        NUM_EMPLOYMENT_STUDENT+=int(dataE["data"][i][13])
                        NUM_EMPLOYMENT_STUDENT+=int(dataE["data"][i][14])
                        NUM_EMPLOYMENT_STUDENT+=int(dataE["data"][i][15])
                        NUM_EMPLOYMENT_UNEMPLOYED+=int(dataE["data"][i][17])
                        NUM_EMPLOYMENT_UNEMPLOYED+=int(dataE["data"][i][18])
                        NUM_EMPLOYMENT_EMPLOYED+=int(dataE["data"][i][19])   
            data_array=[]
            data_array.append(NUM_PLAYGROUNDS)
            data_array.append(NUM_PUBLIC_SCHOOLS)
            data_array.append(NUM_CATHOLIC_SCHOOLS)
            data_array.append(NUM_SINGLE)
            data_array.append(NUM_DUPLEX)
            data_array.append(NUM_ROW_HOUSE)
            data_array.append(NUM_APARTMENT_FIVE)
            data_array.append(NUM_APARTMENT_FOUR)
            data_array.append(NUM_HOTEL)
            data_array.append(NUM_AGE_FOURTEEN)
            data_array.append(NUM_AGE_THIRTYFIVE)
            data_array.append(NUM_AGE_SIXTY)
            data_array.append(NUM_AGE_SIXTYPLUS)
            data_array.append(NUM_EMPLOYMENT_STUDENT)
            data_array.append(NUM_EMPLOYMENT_UNEMPLOYED)
            data_array.append(NUM_EMPLOYMENT_EMPLOYED)
            print(data_array)
    cursor.close()
    
    

#Neighbourhood name
urlNN = "https://data.edmonton.ca/api/views/65fr-66s6/rows.json?accessType=DOWNLOAD"
#Neighbourhood Boundaries
urlNB = "https://data.edmonton.ca/api/views/nckr-nnqj/rows.json?accessType=DOWNLOAD"
#Neighbourhoods (Centroid Point)
urlNC="https://data.edmonton.ca/api/views/3b6m-fezs/rows.json?accessType=DOWNLOAD"
#Playgrounds
urlP="https://data.edmonton.ca/api/views/c4nr-3quz/rows.json?accessType=DOWNLOAD"
#Edmonton Public Schools (2015 - 2016)
urlEPS="https://data.edmonton.ca/api/views/ehbr-emhe/rows.json?accessType=DOWNLOAD"
#Edmonton Catholic Schools (2015 - 2016)
urlECS="https://data.edmonton.ca/api/views/f6w2-hzex/rows.json?accessType=DOWNLOAD"
#Dwelling Unit By Structure Type (Neighbourhood) 
urlDUST="https://data.edmonton.ca/api/views/bjgi-976r/rows.json?accessType=DOWNLOAD"
#employment status
urlE="https://data.edmonton.ca/api/views/aaar-q4e3/rows.json?accessType=DOWNLOAD"
#age
urlA="https://data.edmonton.ca/api/views/44iw-gmaw/rows.json?accessType=DOWNLOAD"
#read all urls
jfile = urllib2.urlopen(urlNN).read()
dataNN = json.loads(jfile)
jfile = urllib2.urlopen(urlNB).read()
dataNB = json.loads(jfile)
jfile = urllib2.urlopen(urlNC).read()
dataNC = json.loads(jfile)
#process the attribute data and put in the database
jfile = urllib2.urlopen(urlP).read()
dataP = json.loads(jfile)
jfile = urllib2.urlopen(urlEPS).read()
dataEPS = json.loads(jfile)
jfile = urllib2.urlopen(urlECS).read()
dataECS = json.loads(jfile)
jfile = urllib2.urlopen(urlDUST).read()
dataDUST = json.loads(jfile)
jfile = urllib2.urlopen(urlE).read()
dataE = json.loads(jfile)
jfile = urllib2.urlopen(urlA).read()
dataA = json.loads(jfile)

#main script
#connect to database
cnx = mysql.connector.connect(user='root', password='',host='localhost',database='mm811project')
#insert
#insert_to_neibourhood()
insert_to_major()
cnx.close()