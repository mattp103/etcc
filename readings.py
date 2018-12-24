import requests
import json
import os
from time import strftime


# def passage(ver,book,chp,vrs):
#     url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
#     header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
#     response = requests.request("GET", url, headers=header)
#     parsed_json = json.loads(response.text)
#     data = json.loads(json.dumps(parsed_json['data']))
#     return data['content']
#
#
# def reference(ver,book,chp,vrs):
#     url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/verses/"+book+"."+chp+"."+vrs
#     header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
#     response = requests.request("GET", url, headers=header)
#     parsed_json = json.loads(response.text)
#     data = json.loads(json.dumps(parsed_json['data']))
#     return data['reference']


def rd(ver, book, chp):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/passages/"+book+"."+chp
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    response = requests.request("GET", url, headers=header)
    parsed_json = json.loads(response.text)
    print(parsed_json)
    read = json.loads(json.dumps(parsed_json['data']))
    print(read)
    return read['copyright'], read['reference'], read['content']

# this is the only good code :)
def rad(ver, query):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/search"
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    querystring = {"query": query, "limit": "1"}
    response = requests.request("GET", url, headers=header, params=querystring)
    parsed_json = json.loads(response.text)
    print(parsed_json)
    request_data = json.loads(json.dumps(parsed_json['data']))
    request_passages = request_data["passages"]
    read = request_passages[0]
    return read['copyright'], read['reference'], read['content']


def jr(num):
    folder = "br/static/br/plans/testplan1"
    json_file = open(folder+"/reading.json", "r")
    decoded_json = json.loads(json_file.read())
    all_readings = decoded_json["data2"]
    json_file.close()
    today_reading = all_readings[int(strftime("%j"))]
    current_reading = today_reading[num]

    return current_reading


def rng(plan, num):
    folder = "br/static/br/plans/"+plan
    json_file = open(folder+"/reading.json", "r")
    decoded_json = json.loads(json_file.read())
    all_readings = decoded_json["data2"]
    json_file.close()
    today_reading = all_readings[int(strftime("%j"))]
    print(today_reading)
    current_reading = today_reading[num]
    print(current_reading)
    if os.path.isfile(folder+"/reading"+str(num)+".cache"):
        try:
            cache_file = open(folder + "/reading"+str(num)+".cache", "r")
            cache_json = json.loads(cache_file.read())
            reading_cache = cache_json[current_reading]
            print("cache file read")
            return reading_cache[0], reading_cache[1], reading_cache[2]
        except:
            cache_file = open(folder + "/reading"+str(num)+".cache", "w")
            cache_data = rad("7142879509583d59-04", current_reading)
            compiled_data = {current_reading: [cache_data[0], cache_data[1], cache_data[2]]}
            json.dump(compiled_data, cache_file)
            cache_file.close()
            print("cache file written")
            cache_output = compiled_data[current_reading]
            return cache_output[0], cache_output[1], cache_output[2]
    else:
        cache_file = open(folder + "/reading" + str(num) + ".cache", "w")
        cache_data = rad("7142879509583d59-04", current_reading)
        compiled_data = {current_reading: [cache_data[0], cache_data[1], cache_data[2]]}
        json.dump(compiled_data, cache_file)
        cache_file.close()
        print("cache file written v2")
        return compiled_data[0], compiled_data[1], compiled_data[2]

# print JOHN 3:16
# print(reference("7142879509583d59-04","JHN","3","16"))
# print(passage("7142879509583d59-04","JHN","3","16"))

# print JOHN 3
# print(chref("7142879509583d59-04","JHN","3"))
# print(chapter("7142879509583d59-04","JHN","3"))
