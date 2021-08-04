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
import order_analysis


timed = datetime.date.today()
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("crede.json",scope)
client = gspread.authorize(cred)
sheet = client.open("looty sales 2021").worksheet("B2C")
sheet2 = client.open("looty sales 2021").worksheet("creds")
sheet3 = client.open("looty sales 2021").worksheet("pick up")
sheet4 = client.open("looty sales 2021").worksheet("talabat")
sheet5 = client.open("looty sales 2021").worksheet("swift")
sheet6 = client.open("looty sales 2021").worksheet("free")
sheet7 = client.open("looty sales 2021").worksheet("B2B")


def start ():

    def dateday() :
        date = timed
        d = date.day
        d -= 1
        dd = date.replace(day=d)
        return dd
    #B2c
    t = 2
    tt = 0.3
    x = 0
    z = 1
    # B2b
    sleep = 0.82
    x1 = 0


    for d in cleaned_data:
        #B2c
        if "الاسم:" in line or "الاسم " in line or " فاتورة ماما لوتي" in line or "الرقم " in line or "الرقم: " in line or "العنوان " in line or "العنوان:" in line or "الاوردر " in line or "الاوردر:" in line or "سعر البكج " in line or "سعر البكج:" in line or "سعر التوصيل " in line or "سعر التوصيل:" in line or "السعر مع توصيل " in line or "السعر مع توصيل:" in line or "طريقة الدفع " in line or "طريقة الدفع:" in line or "نوت " in line or "موعد التسليم " in line or "موعد التسليم:" in line or "نوت: " in line:

            key = d.split(":")[0]
            value = d.split(":")[1]
            if key == "الاسم " or key == "الاسم:" or key == "الاسم :":
                name = value
                time.sleep(t)

            elif key == "الرقم " or key == "الرقم" or key == "الرقم :" :
                number = value
                time.sleep(t)

            elif key == "العنوان " or key == "العنوان":
                location = value
                time.sleep(t)

            elif key == "الاوردر " or key == "الاوردر":
                order = value
                time.sleep(t)

            elif key == "سعر البكج " or key == "سعر البكج":
                package_price = value
                time.sleep(t)

            elif key == "سعر التوصيل " or key == "سعر التوصيل" :
                delivery = value
                time.sleep(t)

            elif key == "السعر مع توصيل " or key == "السعر مع توصيل":
                total = value
                time.sleep(t)

            elif key == "طريقة الدفع" or key == "طريقة الدفع ":
                pay = value
                time.sleep(t)

            elif key ==  "نوت " or key ==  "نوت":
                note = value
                location1 = location
                location = ""
                for index in location1 :
                    if index != "*" :
                        location += index
                    
                        

                if "free " in note or "فري " in note or "تصوير" in note or  "تصوير" in package_price or" فري" in note or "دعاية" in note  or "للتصوير" in note or "دعاية" in package_price :
                    fre = sheet2.cell(2, 6).value
                    sheetsource = sheet6

                    sheet6.update_cell(fre, z, name)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, number)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, location)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, order)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, total)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, delivery)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, package_price)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, pay)
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, str(dateday()))
                    z += 1
                    time.sleep(tt)

                    sheet6.update_cell(fre, z, note)
                    sheet2.update_cell(2, 6, int(fre) + 1)
                    z = 1

                elif " بيك" in location or  " بيكاب" in location :
                    p = sheet2.cell(2, 3).value
                    sheetsource = sheet3

                    sheet3.update_cell(p, z, name)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, number)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, location)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, order)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, total)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, delivery)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, package_price)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, pay)
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, str(dateday()))
                    z += 1
                    time.sleep(tt)
                    sheet3.update_cell(p, z, note)
                    sheet2.update_cell(2, 3, int(p) + 1)
                    z = 1

                elif "عمان_" in location or " عمان ,  " in location or " عمان _" in location or " عمان ،" in location:
                    y = sheet2.cell(2, 1).value
                    sheetsource = sheet

                    sheet.update_cell(y, z, name)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, number)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, location)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, order)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, total)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, delivery)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, package_price)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, pay)
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, str(dateday()))
                    z += 1
                    time.sleep(tt)

                    sheet.update_cell(y, z, note)

                    order_analysis.orders007(order,y,sheetsource)

                    sheet2.update_cell(2, 1, int(y) + 1)
                    z = 1

                elif " طلبات" in location or " طبلات" in location or " طلبات" in location:
                    ta = sheet2.cell(2, 4).value
                    sheetsource = sheet4

                    sheet4.update_cell(ta, z, name)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, number)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, location)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, order)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, total)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, delivery)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, package_price)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, pay)
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, str(dateday()))
                    z += 1
                    time.sleep(tt)

                    sheet4.update_cell(ta, z, note)
                    sheet2.update_cell(2, 4, int(ta) + 1)
                    z = 1

                elif " عمان_" not in location or " طلبات" not in location or " طبلات" not in location or " بيك" not in location or " عمان ،" not in location:
                    sw = sheet2.cell(2, 5).value
                    sheetsource = sheet5

                    sheet5.update_cell(sw, z, name)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, number)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, location)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, order)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, total)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, delivery)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, package_price)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, pay)
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, str(dateday()))
                    z += 1
                    time.sleep(tt)

                    sheet5.update_cell(sw, z, note)
                    sheet2.update_cell(2, 5, int(sw) + 1)
                    z = 1

            x += 1
            print("B2C")
            print(key)
            print(value)
        #B2b
        else:

            try:
                name = d.split("/")[0]
            except:
                name = " None "

            try:
                cookies = d.split("/")[1]
            except:
                cookies = " 0 "

            try:
                bonus = d.split("/")[2]
            except:
                bonus = " 0 "

            try:
                sandwich = d.split("/")[3]

                if sandwich == "\n":
                    sandwich = 0

            except:
                sandwich = " 0 "

            try:
                note = d.split("/")[4]
            except:
                note = " None "

            b = 1
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
            sheet7.update_cell(b2b, b, str(dateday()))
            sheet2.update_cell(2, 2, int(b2b) + 1)
            time.sleep(sleep)

            x1 += 1
            print("B2B")
            print(name)
            print(cookies)
            print(bonus)
            print(sandwich)
            print(note)


while True :

    API_key = "o.v1Exd2CDj0rCXtwCJPw2EEHC8EQnOwdY"
    pb = Pushbullet(API_key)
    push = pb.get_pushes()
    latest = push[0]
    url = latest['file_url']
    path = "chat.txt"
    path2 = "oldchat.txt"
    urllib.request.urlretrieve(url, path)




    with open(path, mode='r', encoding="utf8") as f:
        data = f.readlines()


        dataset = data[1:]
        cleaned_data = []

        for line in dataset:
            if "الاسم:"  in line or "الاسم "  in line or " فاتورة ماما لوتي"  in line or "الرقم " in line or  "الرقم: " in line or "العنوان " in line or "العنوان:" in line or "الاوردر " in line or "الاوردر:" in line or "سعر البكج " in line or "سعر البكج:" in line or "سعر التوصيل " in line or "سعر التوصيل:" in line or "السعر مع توصيل " in line or "السعر مع توصيل:" in line or "طريقة الدفع " in line or "طريقة الدفع:" in line or "نوت " in line or "موعد التسليم " in line or "موعد التسليم:" in line or "نوت: " in line :
                # grab the info and cut it out
                date = line.split("-")[0]
                if "PM" not in date and "AM" not in date:
                    cleaned_data.append(date)
                    print(line)

                else :
                    print(line)

            else:
                print(line)
                # grab the info and cut it out
                date = line.split(":")[2]
                try :
                    if "PM" not in date and "AM" not in date:
                        cleaned_data.append(date)
                except :
                    continue

    with open(path2, mode='r', encoding="utf8") as f1:
        olddata = f1.readlines()


    if olddata == data :
        print("sleep")
        time.sleep(60*30)

    elif olddata != data :
        urllib.request.urlretrieve(url, path2)
        start()


















'''
x = 0
z = 1
for d in cleaned_data:
    y = sheet2.cell(2, 1).value
    print(y)
    key = cleaned_data[x].split(":")[0]
    value = cleaned_data[x].split(":")[1]
    if key == "الاسم " :
        sheet.update_cell(y,z,value)
        z += 1
    elif key == "الرقم " :
        sheet.update_cell(y,z,value)
        z += 1
    elif key == "العنوان " :
        sheet.update_cell(y,z,value)
            # if "بيك اب" in key :
            # pickup()
        z += 1
    elif key == "الاوردر " :
        sheet.update_cell(y,z,value)
        z += 3
    elif key == "سعر البكج " :
        sheet.update_cell(y,z,value)
        z -= 1
    elif key == "سعر التوصيل " :
        sheet.update_cell(y,z,value)
        z -= 1
    elif key ==  "السعر مع توصيل " :
        sheet.update_cell(y,z,value)
        z += 3
    elif key == "طريقة الدفع " :
        sheet.update_cell(y,z,value)
        z += 1
        sheet.update_cell(y, z, str(timed))
        z += 1
    elif key == "نوت " :
        sheet.update_cell(y,z,value)
        z = 1
        sheet2.update_cell(2,1,int(y)+1)

    time.sleep(0.7)
    x += 1
    print(key)
    print(value)
'''