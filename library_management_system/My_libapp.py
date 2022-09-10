import requests
import json
URL = "http://127.0.0.1:8000/lib_app/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data=json.dumps(data)
    r = requests.get (url=URL, data=json_data)

    data = r.json ()
    print(data)
# get_data()


def post_data():
    data={
        'bname':'manufacturing process',
        'bcode':10,
        'add_date':'10/9/2022'


    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
post_data()



