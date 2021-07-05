from flask import Flask,jsonify,request
import config

app = Flask(__name__)

@app.route('/{}/ratings'.format(config.VERSION),methods=['GET'])
def comments():
    name = 'sfs'
    if 'name' in request.args:
        name = request.args['name']
    data={'data': 'hello ' + name}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
