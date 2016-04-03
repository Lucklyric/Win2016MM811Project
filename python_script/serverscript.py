import urllib2
import json
from pprint import pprint
import mysql.connector
import math
from operator import itemgetter

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

def convert_to_list(polygon):
    coords=get_polygon(polygon)
    coords_list=[]
    for i in range(len(coords)):
        plist=[]
        coord=coords[i]
        for j in coord.split():
            plist.append(j.strip())
        coords_list.append(plist)
    #pprint(coords_list)
    return coords_list

def json_output(user_query):
    cursorm = cnx.cursor()
    maxs=[]
    select_max=("SELECT DATA_MAX_VALUE FROM relative_data")
    cursorm.execute(select_max)
    mdata = cursorm.fetchall()
    for rr in mdata:
        maxs.append(rr[0])
    cursorm.close()
    
    out_array=[]    
    cursor = cnx.cursor()    
    cursor.execute("SELECT * FROM major_dataset")
    data = cursor.fetchall()
    for row in data:
        #print(row[1])
        cursorn=cnx.cursor()
        cursorn.execute("SELECT * FROM neighbourhood_tmp WHERE NEIGHBOURHOOD_NAME='%s'"%row[1])
        ndata = cursorn.fetchall()
        #pprint(cursorn.rowcount)
        if cursorn.rowcount>0:
            area=[]
            centroid=[]   
            latitude=0
            longitude=0
            for r in ndata:
                if r[1]!="" and r[1] is not None:
                    area=convert_to_list(r[1])
                latitude=r[2]
                longitude=r[3]
            if area==[] or latitude==0 or latitude is None or longitude ==0 or longitude is None:
                nothing=1
            else:
                neibourhood={}
                neibourhood["name"]=row[1]
                neibourhood["attributes"]=[row[2],row[3],row[4],row[5],row[6],row[7],row[9],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]]
                neibourhood["area"]=area
                neibourhood["latitude"]=latitude
                neibourhood["longitude"]=longitude   
                neibourhood["score"]=((4.0-calculate_score(neibourhood["attributes"],user_query,maxs))/4)*100                
                if neibourhood["score"]>0:
                    #print neibourhood["score"]
                    out_array.append(neibourhood)
            cursorn.close()
    cursor.close()       
    rank = sorted(out_array, key=itemgetter('score'), reverse=True)   
    with open('output.json', 'wb') as outfile:
        json.dump(rank, outfile)   

def ioio():
    with open('output.json') as data_file:    
        data = json.load(data_file)
    print data    

def euclidean_distance(x,y):
    dist=0;
    for i in range(len(x)):
        dist += (float(x[i])-float(y[i]))**2;
    return math.sqrt(dist)
    
def calculate_score(attributes,user_query,maxs):
    x=[] #data attributes
    y=[] #user query
    for i in range(len(user_query)):
        if user_query[i]==0:
            continue       
        else:
            normalize= float(attributes[i])/float(maxs[i])
            x.append(normalize)
            y.append(user_query[i])
    return euclidean_distance(x,y)
    
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='mm811project')
user_query=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
json_output(user_query)
#ioio()

cnx.close()           
