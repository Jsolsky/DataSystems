import json
import http.client
import time
import boto3
import datetime as dt
import pandas as pd

print('Start')

cities = [
    # 'Albury',
    # 'Coffs%20Harbour',
    'Sydney',
    # 'Broken%20Hill',
    # 'Goulburn',
    # 'Dubbo',
    # # 'Newcastle',
    # 'Orange',
    # 'Wagga Wagga',
    # 'Maitland',
    # 'Wollongong',
    # 'Cessnock',
    # 'Griffith',
    # 'Armidale',
    # 'Grafton',
    # 'Queanbeyan',
    # 'Lismore',
    # 'Lithgow',
    # 'Nowra',
    # 'Tamworth',
    # 'Bathurst',
    # 'Ulladulla',
    # 'Taree',
    # 'Batemans Bay',
    # 'Port Macquarie',
    # 'Parkes',
    # 'Ballina',
    # 'Muswellbrook',
    # 'Kempsey',
    # 'Bowral',
    # 'Central Coast',
    # 'Kurri Kurri',
    # 'Singleton',
    # 'Tweed Heads',
    # 'Raymond Terrace',
    # 'Wauchope',
    # 'Mudgee',
    # 'Gunnedah',
    # 'Moree',
    # 'Byron Bay',
    # 'Inverell',
    # 'Casino',
    # 'Cooma',
    # 'Katoomba', # couldn't find on the api explorer
    # 'Leeton',
    # 'Deniliquin',
    # 'Narrabri',
    # 'Yamba',
    # 'Cowra',
    # 'Yass',
    ]
    
for city in cities:
    print(city)
    conn = http.client.HTTPSConnection("api.weatherapi.com")
    conn.request("GET", '/v1/current.json?key=30dc2bf00de44d26a5862046230803&q=' + city + '&aqi=no')
    res = conn.getresponse()
    print("res: ", res)
    data = res.read()
    print("date: ",data)
    decodedData = data.decode("utf-8")
    print("decodedData: ", decodedData)
    # decodedData_json = json.read(decodedData)
    decodedData_json = json.loads(decodedData)
    print("location: ", decodedData_json["location"])
    print("curret: ", decodedData_json["current"])
    
    print()
    location_df = pd.DataFrame(data = decodedData_json["location"], index = [city])
    print(location_df)