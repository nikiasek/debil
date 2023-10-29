import requests
import json
from datetime import datetime
import sys

while True:
    cara = "\n----------------------"
    def tabulka(api):
        jsonData = api.json()
        print(cara, "\n", api.url, "\n")
        print("valid:", api.status_code, "\type:", api.encoding)
        print(jsonData)
        fileWrite(api)

    def requestBuilder(rawKey, rawApi):
        if rawApi !="":
            if rawKey !="":
                api = requests.get(rawApi + "&apiKey=" + rawKey)
                tabulka(api)
            else:
                api = requests.get(rawApi)
                tabulka(api)
        else:
            print("nezadal si api debile")
            sys.exit()

    def fileWrite(api):
        soubor = open("log.txt", "a")

        list = []
        list.append(cara)
        list.append(datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
        list.append("\n" + api.url)
        list.append("\nvalid: " + str(api.status_code))
        list.append("\ntype: " + api.encoding)
        soubor.writelines(list)
        soubor.writelines("\n" + str(api.json()))
        soubor.write(cara)
        sys.exit()

    requestBuilder(rawApi = input("yo, zadej api\n"), rawKey = input("zadej key\n"))