from flask import Flask,jsonify,request
import config, loader

app = Flask(__name__)

@app.route("/comments/<path:book_id>",methods=["GET"])
def comments(book_id):
    data_loader = loader.Loader()
    data = data_loader.load()
    if book_id not in data.keys():
        return json.dumps({})
    return data[book_id]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
