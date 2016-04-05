import urllib2
import json
import mysql.connector
import datetime
import time

def main():
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursori=cnx.cursor()
    cursori.execute("SELECT * FROM daily_query ORDER BY CREATE_TS DESC")
    daily_info=cursori.fetchall()
    #get all data count
    cursor=cnx.cursor()
    cursor.execute("SELECT * FROM relative_dataset")
    final_array=[]    
    relative_info=cursor.fetchall()
    for row in daily_info:
        print row[17]
        ddict={"name":"Daily Query","URL":"-","lastUpdate":time.mktime(row[17].timetuple())}
        final_array.append(ddict)
        break;
    for roow in relative_info:
        ddict={"name":roow[1],"URL":roow[2],"lastUpdate":roow[3]}
        final_array.append(ddict)
    #print final_array
    print json.dumps(final_array)
    cursori.close()
    cursor.close()
    cnx.close()
    
if __name__ == "__main__":
    main()