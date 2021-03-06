#!/usr/bin/python3
import os
import sys
import psycopg2

configPath = os.path.abspath("../config")
sys.path.append(configPath)
from config import config

filename=configPath + '/database.ini' 
section='postgres'
 
 
def get_vendors():
    """ insert a new vendor into the vendors table """
    sql = """SELECT * FROM vendors;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config(filename=filename, section=section)        
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()

        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__=='__main__':
    get_vendors()
