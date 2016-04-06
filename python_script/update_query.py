import urllib2
import json
import mysql.connector

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    cursori=cnx.cursor()
    select_today=("SELECT COUNT(NUM_PLAYGROUNDS),COUNT(NUM_PUBLIC_SCHOOLS),COUNT(NUM_CATHOLIC_SCHOOLS),COUNT(NUM_SINGLE),COUNT(NUM_DUPLEX),COUNT(NUM_ROW_HOUSE),COUNT(NUM_APARTMENT_FIVE),COUNT(NUM_APARTMENT_FOUR),COUNT(NUM_HOTEL),COUNT(NUM_AGE_FOURTEEN),COUNT(NUM_AGE_THIRTYFIVE),COUNT(NUM_AGE_SIXTY),COUNT(NUM_AGE_SIXTYPLUS),COUNT(NUM_EMPLOYMENT_STUDENT),COUNT(NUM_EMPLOYMENT_UNEMPLOYED),COUNT(NUM_EMPLOYMENT_EMPLOYED) FROM user_query WHERE CREATE_TS=subdate(CURRENT_TIMESTAMP, 1)")
    insert_today=("INSERT INTO daily_query (NUM_PLAYGROUNDS,NUM_PUBLIC_SCHOOLS,NUM_CATHOLIC_SCHOOLS,NUM_SINGLE,NUM_DUPLEX,NUM_ROW_HOUSE,NUM_APARTMENT_FIVE,NUM_APARTMENT_FOUR,NUM_HOTEL,NUM_AGE_FOURTEEN,NUM_AGE_THIRTYFIVE,NUM_AGE_SIXTY,NUM_AGE_SIXTYPLUS,NUM_EMPLOYMENT_STUDENT,NUM_EMPLOYMENT_UNEMPLOYED,NUM_EMPLOYMENT_EMPLOYED) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursorq.execute(select_today)
    query_data=cursorq.fetchall()
    if cursorq.rowcount>0:
        for row in query_data:
            query_insert=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15])
            cursori.execute(insert_today,query_insert)
            cnx.commit()
    cursorq.close()
    cursori.close()
    cnx.close()       
    
if __name__ == "__main__":
    main()