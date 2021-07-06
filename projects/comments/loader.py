import json

class Loader(object):
    def __init__(self):
        pass

    def load(self):
        with open("./sample_data.json", "r") as f:
            data = json.load(f)

        return data 