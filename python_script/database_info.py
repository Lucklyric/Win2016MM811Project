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
    cursoru=cnx.cursor()
    cursori.execute("SELECT CREATE_TS,COUNT(ID) FROM daily_query ORDER BY CREATE_TS DESC")
    daily_info=cursori.fetchall()    
    cursoru.execute("SELECT CREATE_TS,COUNT(ID) FROM user_query ORDER BY CREATE_TS DESC")
    query_info=cursoru.fetchall()
    cursor=cnx.cursor()
    cursor.execute("SELECT * FROM relative_dataset")
    relative_info=cursor.fetchall()
    query_array=[]
    data_array=[]    
    for r in daily_info:
        ddict={"name":"Daily Query","URL":"-","lastUpdate":time.mktime(r[0].timetuple()),"Row Count":r[1]}
        query_array.append(ddict)
        break;
    for rr in query_info:
        ddict={"name":"User Query","URL":"-","lastUpdate":time.mktime(rr[0].timetuple()),"Row Count":rr[1]}
        query_array.append(ddict)
        break;        
    for rrr in relative_info:
        ddict={"name":rrr[1],"URL":rrr[2],"lastUpdate":rrr[3]}
        data_array.append(ddict)
    final_array=[]
    final_array.append(data_array)
    final_array.append(query_array)
    print json.dumps(final_array)
    cursori.close()
    cursoru.close()
    cursor.close()
    cnx.close()
    
if __name__ == "__main__":
    main()