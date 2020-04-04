from Psql_Database_Dependencies import *

def connect():
    return psycopg2.connect(user='myuser', host='localhost', dbname='mydb', password='mypass')

engine = create_engine('postgresql://', creator=connect)
Base.metadata.create_all(engine)
