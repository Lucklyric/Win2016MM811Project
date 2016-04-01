import urllib2
import json
from pprint import pprint
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='mm811project')
cursor = cnx.cursor()
def get_polygon(poly):
    coords=[]
    polysplit=poly.split(',')
    plen=len(polysplit)
    for i in range(plen):
        coord=polysplit[i];
        if i==0:
            coord=coord[16:]
        elif i==plen-1:
            coord=coord[:len(coord)-3]
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
    with open('output.json', 'wb') as outfile:
        out_array=[]
        cursor.execute("SELECT * FROM major_dataset")
        data = cursor.fetchall()
        for row in data:
            #print(row[1])
            cursorn=cnx.cursor()
            cursorn.execute("SELECT * FROM neighbourhood_tmp",row[1])
            ndata = cursorn.fetchall()
            pprint(cursorn.rowcount)
            area=[]
            centroid=[]       
            for r in ndata:
                #pprint(r[1])
                area=convert_to_list(r[1])
                latitude=r[2]
                longitude=r[3]
            attributes={}
            attributes["attributes"]=[row[2],row[3],row[4],row[5],row[6],row[7],row[9],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]]
            area_dist={}
            area_dist["area"]=area;
            lati_dist={}
            longi_dist={}
            lati_dist["latitude"]=latitude
            longi_dist["longitude"]=longitude
            sequence=[attributes,area_dist,lati_dist,longi_dist]
            neibourhood={}        
            neibourhood[row[1]]=sequence
            out_array.append(neibourhood)
            cursorn.close()
        json.dump(out_array, outfile)               

def ioio():
    with open('output.json') as data_file:    
        data = json.load(data_file)
    
    print data    

#json_output()
ioio()
cursor.close()
cnx.close()    