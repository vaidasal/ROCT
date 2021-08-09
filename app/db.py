import psycopg2 as pg2

conn = pg2.connect(database='LOCToolDB', user='vaidas', password='pw')
cur = conn.cursor()
cur.execute('...query...')
cur.fetchone() #returns 1 row
cur.fetchmany(10) #returns 10 rows
data = cur.fetchall()

conn.close()



