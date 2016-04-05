import json
from pprint import pprint
import mysql.connector
import math
from operator import itemgetter
import sys

def main(start,end):
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='mm811project')
    cursorq=cnx.cursor()
    start_end=(start,end)
    cursorq.execute("SELECT * FROM daily_query WHERE CREATE_TS BETWEEN %s AND %s"%start_end)
    query_data=cursorq.fetchall()
    for row in query_data:
        print row[17]
    cnx.close()     
    
if __name__ == "__main__":
    main(argv[1],argv[2])