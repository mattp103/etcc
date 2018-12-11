import requests
import json


def chp(ver,book,chp):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/passages/"+book+"."+chp
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return data['content']


def chref(ver,book,chp):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/passages/"+book+"."+chp
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return data['reference']


def passage(ver,book,chp,vrs):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return data['content']


def reference(ver,book,chp,vrs):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return data['reference']


# print JOHN 3:16
# print(reference("7142879509583d59-04","JHN","3","16"))
# print(passage("7142879509583d59-04","JHN","3","16"))

# print JOHN 3
# print(chref("7142879509583d59-04","JHN","3"))
# print(chapter("7142879509583d59-04","JHN","3"))
