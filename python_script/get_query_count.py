import json
from pprint import pprint
import mysql.connector
import math
from operator import itemgetter
import datetime
import time

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    cursorq.execute("SELECT * FROM daily_query ORDER BY CREATE_TS")
    query_data=cursorq.fetchall()
    PLAYGROUNDS={"name":"PLAYGROUNDS","data":[]}
    PUBLIC_SCHOOLS={"name":"PUBLIC_SCHOOLS","data":[]}
    CATHOLIC_SCHOOLS={"name":"CATHOLIC_SCHOOLS","data":[]}
    SINGLE={"name":"SINGLE","data":[]}
    DUPLEX={"name":"DUPLEX","data":[]}
    ROW_HOUSE={"name":"ROW_HOUSE","data":[]}
    APARTMENT_FIVE={"name":"APARTMENT_FIVE","data":[]}
    APARTMENT_FOUR={"name":"APARTMENT_FOUR","data":[]}
    HOTEL={"name":"HOTEL","data":[]}
    AGE_FOURTEEN={"name":"AGE_FOURTEEN","data":[]}
    AGE_THIRTYFIVE={"name":"AGE_THIRTYFIVE","data":[]}
    AGE_SIXTY={"name":"AGE_SIXTY","data":[]}
    AGE_SIXTYPLUS={"name":"AGE_SIXTYPLUS","data":[]}
    EMPLOYMENT_STUDENT={"name":"EMPLOYMENT_STUDENT","data":[]}
    EMPLOYMENT_UNEMPLOYED={"name":"EMPLOYMENT_UNEMPLOYED","data":[]}
    EMPLOYMENT_EMPLOYED={"name":"EMPLOYMENT_EMPLOYED","data":[]}

    for row in query_data:
        datetag=time.mktime(row[17].timetuple())
        datetag*=1000
        #datetag=row[17]
        PLAYGROUNDS["data"].append([datetag,row[1]])
        PUBLIC_SCHOOLS["data"].append([datetag,row[2]])
        CATHOLIC_SCHOOLS["data"].append([datetag,row[3]])
        SINGLE["data"].append([datetag,row[4]])
        DUPLEX["data"].append([datetag,row[5]])
        ROW_HOUSE["data"].append([datetag,row[6]])
        APARTMENT_FIVE["data"].append([datetag,row[7]])
        APARTMENT_FOUR["data"].append([datetag,row[8]])
        HOTEL["data"].append([datetag,row[9]])
        AGE_FOURTEEN["data"].append([datetag,row[10]])
        AGE_THIRTYFIVE["data"].append([datetag,row[11]])
        AGE_SIXTY["data"].append([datetag,row[12]])
        AGE_SIXTYPLUS["data"].append([datetag,row[13]])
        EMPLOYMENT_STUDENT["data"].append([datetag,row[14]])
        EMPLOYMENT_UNEMPLOYED["data"].append([datetag,row[15]])
        EMPLOYMENT_EMPLOYED["data"].append([datetag,row[16]])
    out_array=[]
    out_array.append(PLAYGROUNDS)
    out_array.append(PUBLIC_SCHOOLS)
    out_array.append(CATHOLIC_SCHOOLS)
    out_array.append(SINGLE)
    out_array.append(DUPLEX)
    out_array.append(ROW_HOUSE)
    out_array.append(APARTMENT_FIVE)
    out_array.append(APARTMENT_FOUR)
    out_array.append(HOTEL)
    out_array.append(AGE_FOURTEEN)
    out_array.append(AGE_THIRTYFIVE)
    out_array.append(AGE_SIXTY)
    out_array.append(AGE_SIXTYPLUS)
    out_array.append(EMPLOYMENT_STUDENT)
    out_array.append(EMPLOYMENT_UNEMPLOYED)
    out_array.append(EMPLOYMENT_EMPLOYED)
    #get all data count
    cursorall=cnx.cursor()
    cursorall.execute("SELECT SUM(NUM_PLAYGROUNDS),SUM(NUM_PUBLIC_SCHOOLS),SUM(NUM_CATHOLIC_SCHOOLS),SUM(NUM_SINGLE),SUM(NUM_DUPLEX),SUM(NUM_ROW_HOUSE),SUM(NUM_APARTMENT_FIVE),SUM(NUM_APARTMENT_FOUR),SUM(NUM_HOTEL),SUM(NUM_AGE_FOURTEEN),SUM(NUM_AGE_THIRTYFIVE),SUM(NUM_AGE_SIXTY),SUM(NUM_AGE_SIXTYPLUS),SUM(NUM_EMPLOYMENT_STUDENT),SUM(NUM_EMPLOYMENT_UNEMPLOYED),SUM(NUM_EMPLOYMENT_EMPLOYED) FROM daily_query")
    all_count=cursorall.fetchall()
    all_array=[]
    for rrr in all_count:
        for i in range(16):
            all_array.append(int(rrr[i]))
    final_array=[]
    final_array.append(out_array)
    final_array.append(all_array)
    #print final_array
    print json.dumps(final_array)
    cursorq.close()
    cursorall.close()
    cnx.close()
    
if __name__ == "__main__":
    main()