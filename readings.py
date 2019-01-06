import requests
import json
import os
from time import strftime
from django.core.cache import cache

versions = {
    "ASV": "06125adad2d5898a-01",
    "engDRA": "179568874c45066f-01",
    "enggnv": "c315fa9f71d4af3a-01",
    "enKJVe": "de4e12af7f28f599-01",
    "enKJVp": "de4e12af7f28f599-02",
    "engojp": "bf8f1c7f3f9045a5-01",
    "engRV": "40072c4a5aba4022-01",
    "GNT": "61fd76eafa1577c2-02",
    "GNTD": "61fd76eafa1577c2-01",
    "T4T": "0bc8836afa7427fa-01",
    "WEBE": "9879dbb7cfe39e4d-01",
    "WEBC": "9879dbb7cfe39e4d-02",
    "WEBO": "9879dbb7cfe39e4d-03",
    "WEBP": "9879dbb7cfe39e4d-04",
    "WEBBEE": "7142879509583d59-01",
    "WEBBEC": "7142879509583d59-02",
    "WEBBEO": "7142879509583d59-03",
    "WEBBEP": "7142879509583d59-04",
    "WMB": "f72b840c855f362c-04",
    "WMBBEM": "04da588535d2f823-04"
}


def readings_today(plan):
    key = plan+"readings"
    if cache.get(key, "False") == "False":
        cache.set(key, [jr(plan, 0), jr(plan, 1), jr(plan, 2), jr(plan, 3)], 600)
        return cache.get(key)
    else:
        return cache.get(key)


def rad(ver, query):
    url = "https://api.scripture.api.bible/v1/bibles/"+ver+"/search"
    header = {'api-key': '0bd22eae4a6c8ff30cbcd5ec72220900'}
    querystring = {"query": query, "limit": "1"}
    response = requests.request("GET", url, headers=header, params=querystring)
    parsed_json = json.loads(response.text)
    request_data = json.loads(json.dumps(parsed_json['data']))
    request_passages = request_data["passages"]
    read = request_passages[0]
    return read['copyright'], read['reference'], read['content']


def jr(plan, num):
    folder = "/home/meco/etcc/br/static/br/plans/" + plan
    json_file = open(folder+"/reading.json", "r")
    decoded_json = json.loads(json_file.read())
    all_readings = decoded_json["data2"]
    json_file.close()
    today_reading = all_readings[int(strftime("%j"))-1]
    current_reading = today_reading[num]
    return current_reading


def rng(plan, num, bible_ver):
    current_reading = readings_today(plan)[num]
    ver = versions[bible_ver]
    key = plan + str(num) + ver
    if cache.get(key, "False") == "False":
        cache.set(key, rad(ver, current_reading), 3600)
        return cache.get(key, ["", "<span class='text-red'>ERROR :(</span>", "An error occurred while fetching the reading. Please try again later or contact the developers <a href='/developers/'>here.</a>"])
    else:
        return cache.get(key, ["", "<span class='text-red'>ERROR :(</span>", "An error occurred while fetching the reading. Please try again later or contact the developers <a  href=/'developers/'>here.</a>"])
