from Psql_Database_Setup import *
import requests, json

engine = create_engine('postgresql://myuser:mypass@localhost:5432/mydb')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

response = requests.get("https://api.github.com/emojis")
response = json.loads(response.text)

for key,value in response.items():
    Emoji = Emojis(name=key, url = value)
    session.add(Emoji)
    session.commit()