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
    cnx = mysql.connector.connect(user='root', password='',host='localhost',database='mm811project')
    
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
    cnx.close()
def insert_to_major():
    cnx = mysql.connector.connect(user='root', password='',host='localhost',database='mm811project')
    
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
            #print row[0]            
            if row[1] is None or row[1]=="":
                min_max=[]
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
                    NUM_EMPLOYMENT_UNEMPLOYED+=int(dataE["data"][i][16])
                    NUM_EMPLOYMENT_UNEMPLOYED+=int(dataE["data"][i][19])
                    NUM_EMPLOYMENT_EMPLOYED+=int(dataE["data"][i][17])
                    NUM_EMPLOYMENT_EMPLOYED+=int(dataE["data"][i][18])   
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
            #print(data_array)
            insert_major=("INSERT INTO major_dataset "
                   "(NEIGHBOURHOOD_NAME,NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED) "
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            majordata=(row[0],data_array[0],data_array[1],data_array[2],data_array[3],data_array[4],data_array[5],data_array[6],data_array[7],data_array[8],data_array[9],data_array[10],data_array[11],data_array[12],data_array[13],data_array[14],data_array[15])
            cursorm = cnx.cursor()   
            cursorm.execute(insert_major, majordata) 
            cnx.commit()
            cursorm.close()
    cursor.close()
    cnx.close()
def insert_to_relative_data():
    cnx = mysql.connector.connect(user='root', password='',host='localhost',database='mm811project')
    
    insert_relative=("INSERT INTO relative_data "
           "(DATA_NAME,DATA_MAX_VALUE) "
           "VALUES (%s,%s)") 
    select_max_major=("SELECT MAX(NUM_PLAYGROUNDS),MAX(NUM_PUBLIC_SCHOOLS),MAX(NUM_CATHOLIC_SCHOOLS),MAX(NUM_SINGLE),MAX(NUM_DUPLEX),MAX(NUM_ROW_HOUSE),MAX(NUM_APARTMENT_FIVE),MAX(NUM_APARTMENT_FOUR),MAX(NUM_HOTEL),MAX(NUM_AGE_FOURTEEN),MAX(NUM_AGE_THIRTYFIVE),MAX(NUM_AGE_SIXTY),MAX(NUM_AGE_SIXTYPLUS),MAX(NUM_EMPLOYMENT_STUDENT),MAX(NUM_EMPLOYMENT_UNEMPLOYED),MAX(NUM_EMPLOYMENT_EMPLOYED) FROM major_dataset")
    cursorr=cnx.cursor()
    cursormm=cnx.cursor()
    cursormm.execute(select_max_major)
    mmdata = cursormm.fetchall()
    for row in mmdata:
        PLAYGROUNDS=("PLAYGROUNDS",row[0])
        PUBLIC_SCHOOLS=("PUBLIC_SCHOOLS",row[1])
        CATHOLIC_SCHOOLS=("CATHOLIC_SCHOOLS",row[2])
        SINGLE=("SINGLE",row[3])
        DUPLEX=("DUPLEX",row[4])        
        ROW_HOUSE=("ROW_HOUSE",row[5])
        APARTMENT_FIVE=("APARTMENT_FIVE",row[6]) 
        APARTMENT_FOUR=("APARTMENT_FOUR",row[7]) 
        HOTEL=("HOTEL",row[8]) 
        AGE_FOURTEEN=("AGE_FOURTEEN",row[9]) 
        AGE_THIRTYFIVE=("AGE_THIRTYFIVE",row[10]) 
        AGE_SIXTY=("AGE_SIXTY",row[11]) 
        AGE_SIXTYPLUS=("AGE_SIXTYPLUS",row[12]) 
        EMPLOYMENT_STUDENT=("EMPLOYMENT_STUDENT",row[13]) 
        EMPLOYMENT_UNEMPLOYED=("EMPLOYMENT_UNEMPLOYED",row[14]) 
        EMPLOYMENT_EMPLOYED=("EMPLOYMENT_EMPLOYED",row[15])
        cursorr.execute(insert_relative,PLAYGROUNDS)
        cursorr.execute(insert_relative,PUBLIC_SCHOOLS)
        cursorr.execute(insert_relative,CATHOLIC_SCHOOLS)
        cursorr.execute(insert_relative,SINGLE)
        cursorr.execute(insert_relative,DUPLEX)
        cursorr.execute(insert_relative,ROW_HOUSE)
        cursorr.execute(insert_relative,APARTMENT_FIVE)
        cursorr.execute(insert_relative,APARTMENT_FOUR)
        cursorr.execute(insert_relative,HOTEL)
        cursorr.execute(insert_relative,AGE_FOURTEEN)
        cursorr.execute(insert_relative,AGE_THIRTYFIVE)
        cursorr.execute(insert_relative,AGE_SIXTY)
        cursorr.execute(insert_relative,AGE_SIXTYPLUS)
        cursorr.execute(insert_relative,EMPLOYMENT_STUDENT)
        cursorr.execute(insert_relative,EMPLOYMENT_UNEMPLOYED)
        cursorr.execute(insert_relative,EMPLOYMENT_EMPLOYED)        
        cnx.commit() 
        cursorr.close()
    cursormm.close()
    cnx.close()
def insert_to_relative_dataset():
    cnx = mysql.connector.connect(user='root', password='',host='localhost',database='mm811project')
    
    insert_relative_dataset=("INSERT INTO relative_dataset "
               "(DATASET_NAME,DATASET_URL,DATASET_LASTUPADE) "
               "VALUES (%s,%s,%s)")     
    PLAYGROUNDS=(dataP["meta"]["view"]["name"],urlP,dataP["meta"]["view"]["viewLastModified"])
    PUBLIC_SCHOOLS=(dataEPS["meta"]["view"]["name"],urlEPS,dataEPS["meta"]["view"]["viewLastModified"])
    CATHOLIC_SCHOOLS=(dataECS["meta"]["view"]["name"],urlECS,dataECS["meta"]["view"]["viewLastModified"])
    STRUCTURE_TYPE=(dataDUST["meta"]["view"]["name"],urlDUST,dataDUST["meta"]["view"]["viewLastModified"])
    AGE=(dataA["meta"]["view"]["name"],urlA,dataA["meta"]["view"]["viewLastModified"]) 
    EMPLOYMENT=(dataE["meta"]["view"]["name"],urlE,dataE["meta"]["view"]["viewLastModified"]) 
    cursord=cnx.cursor()
    cursord.execute(insert_relative_dataset,PLAYGROUNDS)
    cursord.execute(insert_relative_dataset,PUBLIC_SCHOOLS)
    cursord.execute(insert_relative_dataset,CATHOLIC_SCHOOLS)
    cursord.execute(insert_relative_dataset,STRUCTURE_TYPE)
    cursord.execute(insert_relative_dataset,AGE)  
    cursord.execute(insert_relative_dataset,EMPLOYMENT)   
    cnx.commit()
    cursord.close()
    cnx.close()
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
##insert
#insert_to_neibourhood()
#insert_to_major()
#insert_to_relative_data()
#insert_to_relative_dataset()
