import requests
import json
import os
from time import strftime


def passage(ver,book,chp,vrs):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return(data['content'])


def reference(ver,book,chp,vrs):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    data = json.loads(json.dumps(parsed_json['data']))
    return(data['reference'])


def rd(ver,book,chp):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/passages/"+book+"."+chp
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    read = json.loads(json.dumps(parsed_json['data']))
    return read['copyright'], read['reference'], read['content']


def rng(plan, num):
    folder = "br/static/br/"+plan+"/reading.json"
    json_file = open(folder, "r")
    decoded_json = json.loads(json_file.read())
    c = decoded_json["data2"]
    e = c[int(strftime("%j"))]
    f = e[num]
    j = f.split()
    bk = j[0]
    if "-" in j[1]:
        g = j.find("-")
        h = j.find(":")
        beg = j[g:]
        end = j[h:g]
        print(beg, end)
    else:
        ch = j[1]
    return rd("7142879509583d59-04", bk, ch)


# print JOHN 3:16
# print(reference("7142879509583d59-04","JHN","3","16"))
# print(passage("7142879509583d59-04","JHN","3","16"))

# print JOHN 3
# print(chref("7142879509583d59-04","JHN","3"))
# print(chapter("7142879509583d59-04","JHN","3"))
