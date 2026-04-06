import json

def to_pretty_json(data):
    return json.dumps(data, indent=4)
