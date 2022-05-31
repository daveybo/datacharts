import json


def get_constants_data():

    f = open('settings.json')
    data = json.load(f)
    f.close()
    return data

# enddef