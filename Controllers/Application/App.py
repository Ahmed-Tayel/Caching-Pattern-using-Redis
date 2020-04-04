from flask import Flask, render_template, request, redirect, jsonify, url_for, make_response
import requests

app = Flask(__name__)


@app.route('/')
def Welcome_page():
    return render_template('main_page.html')


@app.route('/api/v0/query/emoji/<name>')
def Query_Url(name):
    url = 'http://rediscontroller:5000/api/v0/redis/emoji/%s' % (name)
    result = requests.get(url).json()['url']
    if result == None:
        url = 'http://postgrescontroller:8000/api/v0/postgres/emoji/%s' % (name)
        result = requests.get(url).json()['url']
        if result != None:
            url = 'http://rediscontroller:5000/api/v0/redis/emoji/'
            payload = {'emoji': name , 'url': result}
            requests.post(url,params = payload)
            return(redirect(result))
        else:
            response = make_response(render_template('error.html')  ,404)
            return response


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)