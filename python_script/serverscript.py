import urllib2
import json
from pprint import pprint
import mysql.connector


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

def json_output():
    cursor = cnx.cursor()    
    with open('output.json', 'wb') as outfile:
        out_array=[]
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
                    #pprint(r[1])
                    area=convert_to_list(r[1])
                    latitude=r[2]
                    longitude=r[3]
                sequence={}
                sequence["attributes"]=[row[2],row[3],row[4],row[5],row[6],row[7],row[9],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]]
                sequence["area"]=area
                sequence["latitude"]=latitude
                sequence["longitude"]=longitude   
                sequence["score"]=0 
                neibourhood={}        
                neibourhood[row[1]]=sequence
                out_array.append(neibourhood)
                cursorn.close()
        if len(out_array)>0 and latitude!=0 and longitude!=0:
            json.dump(out_array, outfile)  
            
        cursor.close()

def ioio():
    with open('output.json') as data_file:    
        data = json.load(data_file)
    print data    

def calculate_score(attributes):
    score=0
    for i in range(len(attributes)):
        if attributes[i]==-1:
            nothing=1        
    
    
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='mm811project')
json_output()
#ioio()

cnx.close()           
