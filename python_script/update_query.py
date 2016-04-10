import urllib2
import json
import mysql.connector
import time
from pprint import pprint
import datetime
from datetime import date, timedelta as td

def main():   

    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    cursori=cnx.cursor()
    cursorl=cnx.cursor()
    cursoru=cnx.cursor()
    cursorv=cnx.cursor()
    select_last=("SELECT CREATE_TS FROM daily_query ORDER BY CREATE_TS DESC")
    cursorl.execute(select_last)
    date_data=cursorl.fetchall()
    latest_query=time.strftime("%Y-%m-%d")
    for date in date_data:
        latest_query_d = date[0]
        latest_query=latest_query_d.strftime("%Y-%m-%d")
        break
    
    select_today=("SELECT SUM(NUM_PLAYGROUNDS),SUM(NUM_PUBLIC_SCHOOLS),SUM(NUM_CATHOLIC_SCHOOLS),SUM(NUM_SINGLE),SUM(NUM_DUPLEX),SUM(NUM_ROW_HOUSE),SUM(NUM_APARTMENT_FIVE),SUM(NUM_APARTMENT_FOUR),SUM(NUM_HOTEL),SUM(NUM_AGE_FOURTEEN),SUM(NUM_AGE_THIRTYFIVE),SUM(NUM_AGE_SIXTY),SUM(NUM_AGE_SIXTYPLUS),SUM(NUM_EMPLOYMENT_STUDENT),SUM(NUM_EMPLOYMENT_UNEMPLOYED),SUM(NUM_EMPLOYMENT_EMPLOYED), CREATE_TS FROM user_query WHERE CREATE_TS='%s'")
    update_latest=("UPDATE daily_query SET NUM_PLAYGROUNDS=%s,NUM_PUBLIC_SCHOOLS=%s,NUM_CATHOLIC_SCHOOLS=%s,NUM_SINGLE=%s,NUM_DUPLEX=%s,NUM_ROW_HOUSE=%s,NUM_APARTMENT_FIVE=%s,NUM_APARTMENT_FOUR=%s,NUM_HOTEL=%s,NUM_AGE_FOURTEEN=%s,NUM_AGE_THIRTYFIVE=%s,NUM_AGE_SIXTY=%s,NUM_AGE_SIXTYPLUS=%s,NUM_EMPLOYMENT_STUDENT=%s,NUM_EMPLOYMENT_UNEMPLOYED=%s,NUM_EMPLOYMENT_EMPLOYED=%s WHERE CREATE_TS=%s")
    insert_today=("INSERT INTO daily_query (NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED,CREATE_TS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    d1 = latest_query_d
    d2 = datetime.datetime.now()
    delta = d2 - d1
    for i in range(delta.days + 1):
        adate = d1 + td(days=i)
        query_date=adate.strftime("%Y-%m-%d")
        #print adate
        cursorq.execute(select_today%query_date)
        query_data=cursorq.fetchall()        
        for row in query_data:
            #pprint(row[0])
            if i==0:
                query_update=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],query_date)
                cursoru.execute(update_latest,query_update)
            else:
                if row[0] is None:
                    query_insert=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,query_date)
                else:
                    query_insert=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],query_date)
                cursori.execute(insert_today,query_insert)
            cnx.commit()
    cursorv.close()
    cursorq.close()
    cursori.close()
    cursorl.close()
    cursoru.close()
    cnx.close()       
    
if __name__ == "__main__":
    main()