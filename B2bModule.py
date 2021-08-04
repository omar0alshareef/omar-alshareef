def B2b ():
    import urllib.request
    import os
    from typing import Optional
    import pandas as pd
    from gspread import Worksheet
    from pushbullet import Pushbullet
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import datetime
    import time

    timed = datetime.date.today()
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    cred = ServiceAccountCredentials.from_json_keyfile_name("crede.json", scope)
    client = gspread.authorize(cred)
    sheet7 = client.open("looty sales 2021").worksheet("B2B")
    sheet2 = client.open("looty sales 2021").worksheet("creds")
    '''API_key = "o.S2I8zN6so7mWUwsHG5atZoZbJ0mtWwry"
    pb = Pushbullet(API_key)
    push = pb.get_pushes()
    latest = push[0]
    url = latest['file_url']
    path = "chat.txt"
    urllib.request.urlretrieve(url, path)'''
    path = "chat.txt"

    with open(path, mode='r', encoding="utf8") as f:
        data = f.readlines()

    dataset = data[1:]
    cleaned_data = []
    for line in dataset:
        # grab the info and cut it out
        date = line.split(":")[2]
        if "PM" not in date:
            cleaned_data.append(date)

    sleep = 0.82
    x = 0
    for d in cleaned_data:
        b = 1

        try:
            name = cleaned_data[x].split("/")[0]
        except:
            name = " "

        try:
            cookies = cleaned_data[x].split("/")[1]
        except:
            cookies = " "

        try:
            bonus = cleaned_data[x].split("/")[2]
        except:
            bonus = " "

        try:
            sandwich = cleaned_data[x].split("/")[3]
        except:
            sandwich = " "

        try:
            note = cleaned_data[x].split("/")[4]
        except:
            note = " "

        b2b = sheet2.cell(2, 2).value
        sheet7.update_cell(b2b, b, name)
        b += 1
        time.sleep(sleep)
        sheet7.update_cell(b2b, b, note)
        b += 1
        time.sleep(sleep)
        sheet7.update_cell(b2b, b, cookies)
        b += 1
        time.sleep(sleep)
        sheet7.update_cell(b2b, b, sandwich)
        b += 1
        time.sleep(sleep)
        sheet7.update_cell(b2b, b, bonus)
        b += 3
        time.sleep(sleep)
        sheet7.update_cell(b2b, b, str(timed))
        sheet2.update_cell(2, 2, int(b2b) + 1)
        x += 1
        time.sleep(sleep)

        print(name)
        print(cookies)
        print(bonus)
        print(sandwich)
        print(note)

    '''
    def senddata():
        t = 2
        tt = 0.3
        x = 0
        z = 1

        def dateday() :
            date = timed
            d = date.day
            d -= 1
            dd = date.replace(day=d)
            return dd

        for d in cleaned_data:
            key = cleaned_data[x].split(":")[0]
            value = cleaned_data[x].split(":")[1]




    while True :

        API_key = "o.S2I8zN6so7mWUwsHG5atZoZbJ0mtWwry"
        pb = Pushbullet(API_key)
        push = pb.get_pushes()
        latest = push[0]
        url = latest['file_url']
        path = "chat.txt"
        urllib.request.urlretrieve(url, path)

        with open(path, mode='r', encoding="utf8") as f:
            data = f.readlines()

        dataset = data[1:]
        cleaned_data = []
        for line in dataset:
            # grab the info and cut it out
            date = line.split("-")[0]
            if "PM" not in date:
                cleaned_data.append(date)




        if olddata == data :
            print("sleep")
            time.sleep(60*60)

        elif olddata != data :
            urllib.request.urlretrieve(url, path2)
            senddata()







    dateday()
    '''

B2b()


