import json

class AppConfiguration(object):
    def __init__(self, data=None):
        if data is None:
            with open("cfg.json") as fh:
                data = json.loads(fh.read())
        else:
            data = dict(data)

        for key, val in data.items():
            a = setattr(self, key, self.compute_attr_value(val))
            print(a)

    def compute_attr_value(self, value):
        if type(value) is list:
            return [self.compute_attr_value(x) for x in value]
        elif type(value) is dict:
            return AppConfiguration(value)
        else:
            return value