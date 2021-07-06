import json
import requests
from flask import Flask,request

import config, loader

app = Flask(__name__)

@app.route("/details/<path:book_id>", methods=["GET"])
def detail_one(book_id):
    ret = {}

    data_loader = loader.Loader()
    data = data_loader.load()

    if book_id not in data.keys():
        return json.dumps({})
    ret = data[book_id]

    rating_url = "{}/{}".format(config.RATING_ENDPOINT, book_id)
    response = requests.get(rating_url)
    if response.status_code == 200:
        ret["rating"] = json.loads(response.text)
    else:
        ret["rating"] = {}

    comment_url = "{}/{}".format(config.COMMENT_ENDPOINT, book_id)
    response = requests.get(comment_url)
    if response.status_code == 200:
        ret["comments"] = json.loads(response.text)
    else:
        ret["comments"] = {}

    return ret

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
