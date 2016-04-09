import urllib2
import json
import mysql.connector
import time

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    cursori=cnx.cursor()
    cursorl=cnx.cursor()
    cursoru=cnx.cursor()
    cursors=cnx.cursor()
    cursorv=cnx.cursor()
    select_last=("SELECT CREATE_TS FROM user_query ORDER BY CREATE_TS DESC")
    cursorl.execute(select_last)
    date_data=cursorl.fetchall()
    latest_query=time.strftime("%Y-%m-%d")
    for date in date_data:
        latest_query = date[0]
        print latest_query
        break
    
    cursors.execute("CREATE VIEW temp_query AS SELECT * FROM user_query WHERE CREATE_TS>=%s ORDER BY CREATE_TS ASC"%latest_query)
    cursors.execute("SELECT * FROM temp_query")
    latest_data=cursors.fetchall()
    select_today=("SELECT COUNT(NUM_PLAYGROUNDS),COUNT(NUM_PUBLIC_SCHOOLS),COUNT(NUM_CATHOLIC_SCHOOLS),COUNT(NUM_SINGLE),COUNT(NUM_DUPLEX),COUNT(NUM_ROW_HOUSE),COUNT(NUM_APARTMENT_FIVE),COUNT(NUM_APARTMENT_FOUR),COUNT(NUM_HOTEL),COUNT(NUM_AGE_FOURTEEN),COUNT(NUM_AGE_THIRTYFIVE),COUNT(NUM_AGE_SIXTY),COUNT(NUM_AGE_SIXTYPLUS),COUNT(NUM_EMPLOYMENT_STUDENT),COUNT(NUM_EMPLOYMENT_UNEMPLOYED),COUNT(NUM_EMPLOYMENT_EMPLOYED), CREATE_TS FROM temp_query WHERE CREATE_TS=%s")
    update_latest=("UPDATE daily_query COUNT(NUM_PLAYGROUNDS)=%s,COUNT(NUM_PUBLIC_SCHOOLS)=%s,COUNT(NUM_CATHOLIC_SCHOOLS)=%s,COUNT(NUM_SINGLE)=%s,COUNT(NUM_DUPLEX)=%s,COUNT(NUM_ROW_HOUSE)=%s,COUNT(NUM_APARTMENT_FIVE)=%s,COUNT(NUM_APARTMENT_FOUR)=%s,COUNT(NUM_HOTEL)=%s,COUNT(NUM_AGE_FOURTEEN)=%s,COUNT(NUM_AGE_THIRTYFIVE)=%s,COUNT(NUM_AGE_SIXTY)=%s,COUNT(NUM_AGE_SIXTYPLUS)=%s,COUNT(NUM_EMPLOYMENT_STUDENT)=%s,COUNT(NUM_EMPLOYMENT_UNEMPLOYED)=%s,COUNT(NUM_EMPLOYMENT_EMPLOYED)=%s WHERE CREATE_TS=%")
    insert_today=("INSERT INTO daily_query (NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    for rows in latest_data:
        cursorq.execute(select_today%rows[17])
        query_data=cursorq.fetchall()        
        if cursorq.rowcount>0:
            for row in query_data:
                if row[16]==latest_query:
                    query_update=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
                    cursoru.execute(update_latest)
                else:
                    query_insert=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15])
                    cursori.execute(insert_today,query_insert)
                cnx.commit()
    cursorv.execute("DROP VIEW IF EXISTS user_query")    
    cursorv.close()
    cursorq.close()
    cursori.close()
    cursorl.close()
    cursoru.close()
    cursors.close()    
    cnx.close()       
    
if __name__ == "__main__":
    main()