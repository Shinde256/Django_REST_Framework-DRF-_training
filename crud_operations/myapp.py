import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = { }
    if data is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL,data= json_data)
    data= r.json()
    print(data)
#get_data(3)
def post_data():
    data = {'name':'supriya',
            'roll':302,
            'city':'kalyan'}
    json_data =json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
#post_data()

def update_data():
    data = {'id':2,
            'name':'shruti',
            'roll':32,
            'city':'terkhada'}
    json_data =json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
#update_data()


def delete_data():
    data = {'id':4}
    json_data =json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
delete_data()


