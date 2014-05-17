import json


def instance_json(instance):
    if instance:
        return instance.get_json()
    else:
        return instance

def to_json(instance):
    try:
        json_instance = json.dumps(instance.jsonify().__dict__)
    except AttributeError:
        json_instance = json.dumps(instance.__dict__)
    return json_instance