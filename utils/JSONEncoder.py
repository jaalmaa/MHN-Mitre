import json
from datetime import datetime
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):

    def default(self, object):
        if isinstance(object, ObjectId):
            return str(object)
        elif isinstance(object, datetime):
            return str(object)
        else:
            return json.JSONEncoder.default(self, object)