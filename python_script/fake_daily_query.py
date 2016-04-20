import urllib2
import json
import mysql.connector
import datetime
import time
import random
from random import randint
"""
This python file creates fake daily queries.
"""
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

# return a random date
def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursor=cnx.cursor()
    fake_sql=("INSERT INTO user_query (NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED,CREATE_TS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    for i in range(200):
        rand_date=randomDate("2016-1-1", "2016-1-8", random.random())
        fake_data=(randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1),rand_date)        
        cursor.execute(fake_sql,fake_data)
        cnx.commit()
    date_list=["2016-1-1","2016-1-2","2016-1-3","2016-1-4","2016-1-5","2016-1-6","2016-1-7"]
    insert_daily=("INSERT INTO daily_query (NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED,CREATE_TS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursord=cnx.cursor()
    for j in range(7):
        #ddate=time.mktime(time.strptime(date_list[j], '%Y-%m-%d'))
        cursord.execute("SELECT SUM(NUM_PLAYGROUNDS),SUM(NUM_PUBLIC_SCHOOLS),SUM(NUM_CATHOLIC_SCHOOLS),SUM(NUM_SINGLE),SUM(NUM_DUPLEX),SUM(NUM_ROW_HOUSE),SUM(NUM_APARTMENT_FIVE),SUM(NUM_APARTMENT_FOUR),SUM(NUM_HOTEL),SUM(NUM_AGE_FOURTEEN),SUM(NUM_AGE_THIRTYFIVE),SUM(NUM_AGE_SIXTY),SUM(NUM_AGE_SIXTYPLUS),SUM(NUM_EMPLOYMENT_STUDENT),SUM(NUM_EMPLOYMENT_UNEMPLOYED),SUM(NUM_EMPLOYMENT_EMPLOYED) FROM user_query WHERE Date(CREATE_TS)='%s'"%date_list[j])
        datad=cursord.fetchall()
        cursori=cnx.cursor()
        for row in datad:
            daily_data=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],date_list[j])
            cursori.execute(insert_daily,daily_data)
            cnx.commit()
        cursori.close()
    cursord.close()
    cursor.close()
    cnx.close()
    
if __name__ == "__main__":
    main()