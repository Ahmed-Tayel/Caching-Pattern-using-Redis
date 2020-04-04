from flask import Flask, jsonify, make_response
from models.Psql_Database_Dependencies import *


app = Flask(__name__)

engine = create_engine('postgresql://myuser:mypass@postgres:5432/mydb')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/api/v0/postgres/emoji/<name>')
def Get_Emoji(name):
    try:
        url = session.query(Emojis).filter_by(name = name).one().url
    except:
        url = None
    payload = {'emoji': name, 'url': url}
    response = make_response(payload,200)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)