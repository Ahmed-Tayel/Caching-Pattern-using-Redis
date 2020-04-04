from models.Redis_Objects import *
from flask import Flask, jsonify, make_response, request
import json

app = Flask(__name__)
Handler = Cache_DB(100)


@app.route('/api/v0/redis/emoji/<name>')
def Get_Emoji_Redis(name):
    url = Handler.get_emoji_url(name)
    if url != None:
        url = url.decode('ascii')
    payload = {'emoji': name, 'url': url}
    response = make_response(payload,200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/v0/redis/emoji')
def Post_Emoji_Redis():
    emoji = request.args.get('emoji')
    url = request.args.get('url')
    Handler.add_emoji(emoji,url)
    response = make_response(json.dumps('Your record has been submitted'),200)
    response.headers['Content-Type'] = 'application/json'
    return response




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)