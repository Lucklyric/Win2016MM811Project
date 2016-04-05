import json
from pprint import pprint
import mysql.connector
import math
from operator import itemgetter
import sys

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    start_end=(start,end)
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
        PLAYGROUNDS["data"].append([row[17],row[1]])
        PUBLIC_SCHOOLS["data"].append([row[17],row[2]])
        CATHOLIC_SCHOOLS["data"].append([row[17],row[3]])
        SINGLE["data"].append([row[17],row[4]])
        DUPLEX["data"].append([row[17],row[5]])
        ROW_HOUSE["data"].append([row[17],row[6]])
        APARTMENT_FIVE["data"].append([row[17],row[7]])
        APARTMENT_FOUR["data"].append([row[17],row[8]])
        HOTEL["data"].append([row[17],row[9]])
        AGE_FOURTEEN["data"].append([row[17],row[10]])
        AGE_THIRTYFIVE["data"].append([row[17],row[11]])
        AGE_SIXTY["data"].append([row[17],row[12]])
        AGE_SIXTYPLUS["data"].append([row[17],row[13]])
        EMPLOYMENT_STUDENT["data"].append([row[17],row[14]])
        EMPLOYMENT_UNEMPLOYED["data"].append([row[17],row[15]])
        EMPLOYMENT_EMPLOYED["data"].append([row[17],row[16]])
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
    print json.dumps(out_array)
    cnx.close()
    
if __name__ == "__main__":
    main()