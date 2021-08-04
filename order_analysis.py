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



def orders007(cleaned_data , y ,sheetsource) :
    timed = datetime.date.today()
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    cred = ServiceAccountCredentials.from_json_keyfile_name("crede.json", scope)
    client = gspread.authorize(cred)
    sheet = client.open("looty sales 2021").worksheet("B2C")
    sheet2 = client.open("looty sales 2021").worksheet("creds")
    sheet3 = client.open("looty sales 2021").worksheet("pick up")
    sheet4 = client.open("looty sales 2021").worksheet("talabat")
    sheet5 = client.open("looty sales 2021").worksheet("swift")
    sheet6 = client.open("looty sales 2021").worksheet("free")
    sheet7 = client.open("looty sales 2021").worksheet("B2B")


    '''with open(path, mode='r', encoding="utf8") as f:
        data = f.readlines()'''

    '''dataset = data[0:]
    cleaned_data = []
    for line in dataset:
        # grab the info and cut it out
        date = line.split("-")[0]
        if "PM" not in date and " ماما لوتي" not in date and "AM" not in date:
            cleaned_data.append(date)'''


    order = cleaned_data
    '''x = 0
    for d in cleaned_data:
        try:

            key = cleaned_data[x].split(":")[0]
            value = cleaned_data[x].split(":")[1]
            if key == "الاوردر ":
                order.append(value)

        except :
            continue



        x += 1'''

    order = ''.join(order)

    norder = ''
    for l in order :
        if l != '/' and l != '"' and l != '(' :
            norder += l
        else :
            l = '،'
            norder += l


    norder = norder.split("،")
    print(norder)





    for I in norder:




    # cookies

        # double
        if "دبل" in I and "بدل" not in I :
            double = I.split("دبل")[0]
            if double == " " or double == "" or double == "  " :
                double = "1"
                double = int(double)
                print("double = " + str(double))
            else :
                double = int(double)
                print("double = " + str(double))
            sheetsource.update_cell(y, 27, double)

        elif "كوكيز" in I and "بدل" not in I :
            cookies = I.split("كوكيز")[0]
            if cookies == " " or cookies == "" or cookies == "  " :
                try :
                    cookies = "1"
                    cookies = int(cookies)
                    double += cookies
                    print("double = " + str(double))
                except :
                    cookies = "1"
                    double = int(cookies)
                    print("double = " + str(double))


            else :
                try:
                    cookies = int(cookies)
                    double += cookies
                    print("double = " + str(double))
                except :
                    cookies = int(cookies)
                    double = cookies
                    print("double = " + str(double))

            sheetsource.update_cell(y,27,double)


        # white
        elif "وايت" in I and "بدل" not in I :
            white = I.split("وايت")[0]
            if white == " " or white == "" or white == "  " :
                white = "1"
                white = int(white)
                print("white = " + str(white))
            else :
                white = int(white)
                print("white = " + str(white))
            sheetsource.update_cell(y, 28, white)

        # brownie
        elif "براوني" in I and "بدل" not in I  :
            brownie = I.split("براوني")[0]
            if brownie == " " or brownie == "" or brownie == "  " :
                brownie = "1"
                brownie = int(brownie)
                print("brownie = " + str(brownie))
            else :
                brownie = int(brownie)
                print("brownie = " + str(brownie))
            sheetsource.update_cell(y, 29, brownie)


        # red
        elif "ريد" in I and "بدل" not in I :
            red = I.split("ريد")[0]
            if red == " " or red == "" or red == "  " :
                red = "1"
                red = int(red)
                print("red = " + str(red))
            else :
                red = int(red)
                print("red = " + str(red))
            sheetsource.update_cell(y, 30, red)

        # apple
        elif "ابل" in I  and "بدل" not in I :
            apple = I.split("ابل")[0]
            if apple == " " or apple == "" or apple == "  " :
                apple = "1"
                print("apple = " + apple)
            else :
                apple = int(apple)
                print("apple = " + str(apple))
            sheetsource.update_cell(y, 31, apple)




    # bomb

        elif "بومب" in I  and "بدل" not in I and "متشكلص" not in I :
            bomb = I.split("بومب")[0]
            if bomb == " " or bomb == "" or bomb == "  " :
                bomb = "1"
                bomb = int(bomb)
                print("bomb = " + str(bomb))
            else :
                bomb = int(bomb)
                print("bomb = " + str(bomb))
            sheetsource.update_cell(y, 32, bomb)

        elif "شكلنص" in I  and "بدل" not in I:
            shakalans = I.split("شكلنص")[0]
            if shakalans == " " or shakalans == "" or shakalans == "  " :
                shakalans = "1"
                shakalans = int(shakalans)
                print("shakalans = " + str(shakalans))
            else :
                bomb = int(shakalans)
                print("shakalans = " + str(shakalans))
            sheetsource.update_cell(y, 33, shakalans)

        elif "بومب متشكلص" in I  and "بدل" not in I:
            shakalans = I.split("بومب متشكلص")[0]
            if shakalans == " " or shakalans == "" or shakalans == "  " :
                shakalans = "1"
                shakalans = int(shakalans)
                print("shakalans = " + str(shakalans))
            else :
                bomb = int(shakalans)
                print("shakalans = " + str(shakalans))
            sheetsource.update_cell(y, 33, shakalans)



    # sandwiches :


        # kinder
        elif "كندر" in I  and "بدل" not in I :

            kinder = I.split("كندر")[0]
            if kinder == " " or kinder == "" or kinder == "  " :
                kinder = "1"
                kinder = int(kinder)
                print("kinder = " + str(kinder))

            else:
                kinder = int(kinder)
                print("kinder = " + str(kinder))
            sheetsource.update_cell(y, 34, kinder)

        elif "كيندر" in I and "بدل" not in I :

            kinder = I.split("كيندر")[0]
            if kinder == " " or kinder == "" or kinder == "  ":
                kinder = "1"
                kinder = int(kinder)
                print("kinder = " + str(kinder))

            else:
                kinder = int(kinder)
                print("kinder = " + str(kinder))
            sheetsource.update_cell(y, 34, kinder)

        elif "ساندوش" in I  and "بدل" not in I:

            sand = I.split("ساندوش")[0]
            if sand == " " or sand == "" or sand == "  " :
                try:
                    sand = "1"
                    sand = int(sand)
                    kinder += sand
                    print("kinder = " + str(kinder))
                except :
                    sand = "1"
                    kinder = int(sand)
                    print("kinder = " + str(kinder))


            else:
                try:
                    sand = int(sand)
                    kinder += sand
                    print("kinder = " + str(kinder))

                except :
                    sand = int(sand)
                    kinder = sand
                    print("kinder = " + str(kinder))
            sheetsource.update_cell(y, 34, kinder)
        elif "ساندوتيش" in I  and "بدل" not in I:

            sand = I.split("ساندوتيش")[0]
            if sand == " " or sand == "" or sand == "  " :
                try:
                    sand = "1"
                    sand = int(sand)
                    kinder += sand
                    print("kinder = " + str(kinder))
                except :
                    sand = "1"
                    kinder = int(sand)
                    print("kinder = " + str(sand))


            else:
                try:
                    sand = int(sand)
                    kinder += sand
                    print("kinder = " + str(kinder))

                except :
                    sand = int(sand)
                    kinder = sand
                    print("kinder = " + str(kinder))
            sheetsource.update_cell(y, 34, kinder)


        # lotus
        elif "لوتس" in I and "بدل" not in I:
            lotus = I.split("لوتس")[0]
            if lotus == " " or lotus == "" or lotus == "  ":
                lotus = "1"
                lotus = int(lotus)
                print("lotus = " + str(lotus))
            else:
                lotus = int(lotus)
                print("lotus = " + str(lotus))
            sheetsource.update_cell(y, 35, lotus)


        # reese's
        elif "رييسز" in I and "بدل" not in I:
            reeses = I.split("رييسز")[0]
            if reeses == " " or reeses == "" or reeses == "  ":
                reeses = "1"
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            else:
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            sheetsource.update_cell(y, 36, reeses)

        elif "ريسز" in I and "بدل" not in I:
            reeses = I.split("ريسز")[0]
            if reeses == " " or reeses == "" or reeses == "  ":
                reeses = "1"
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            else:
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            sheetsource.update_cell(y, 36, reeses)

        elif "ريسيز" in I and "بدل" not in I:
            reeses = I.split("ريسيز")[0]
            if reeses == " " or reeses == "" or reeses == "  ":
                reeses = "1"
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            else:
                reeses = int(reeses)
                print("reeses = " + str(reeses))
            sheetsource.update_cell(y, 36, reeses)


        # marshmallow
        elif "مارشميلو" in I and "بدل" not in I:
            marshmallow = I.split("مارشميلو")[0]
            if marshmallow == " " or marshmallow == "" or marshmallow == "  ":
                marshmallow = "1"
                marshmallow = int(marshmallow)
                print("marshmallow = " + str(marshmallow))
            else:
                marshmallow = int(marshmallow)
                print("marshmallow = " + str(marshmallow))
            sheetsource.update_cell(y, 38, marshmallow)


        # ferrero
        elif "فريرو" in I and "بدل" not in I:
            ferrero = I.split("فريرو")[0]
            if ferrero == " " or ferrero == "" or ferrero == "  ":
                ferrero = "1"
                ferrero = int(ferrero)
                print("ferrero = " + str(ferrero))
            else:
                ferrero = int(ferrero)
                print("ferrero = " + str(ferrero))
            sheetsource.update_cell(y, 37, ferrero)

        elif "فيريرو" in I and "بدل" not in I:
            ferrero = I.split("فيريرو")[0]
            if ferrero == " " or ferrero == "" or ferrero == "  ":
                ferrero = "1"
                ferrero = int(ferrero)
                print("ferrero = " + str(ferrero))
            else:
                ferrero = int(ferrero)
                print("ferrero = " + str(ferrero))
            sheetsource.update_cell(y, 37, ferrero)


        # cheesecake
        elif "تشيز كيك" in I and "بدل" not in I:
            cheesecake = I.split("تشيز كيك")[0]
            if cheesecake == " " or cheesecake == "" or cheesecake == "  ":
                cheesecake = "1"
                cheesecake = int(cheesecake)
                print("cheesecake = " + str(cheesecake))
            else:
                cheesecake = int(cheesecake)
                print("cheesecake = " + str(cheesecake))
            sheetsource.update_cell(y, 39, cheesecake)

        elif "تشيزكيك" in I and "بدل" not in I:
            cheesecake = I.split("تشيزكيك")[0]
            if cheesecake == " " or cheesecake == "" or cheesecake == "  ":
                cheesecake = "1"
                cheesecake = int(cheesecake)
                print("cheesecake = " + str(cheesecake))
            else:
                cheesecake = int(cheesecake)
                print("cheesecake = " + str(cheesecake))
            sheetsource.update_cell(y, 39, cheesecake)

        # pistachio
        elif "بيستاشيو" in I and "بدل" not in I:
            pistachio = I.split("بيستاشيو")[0]
            if pistachio == " " or pistachio == "" or pistachio == "  ":
                pistachio = "1"
                pistachio = int(pistachio)
                print("pistachio = " + str(pistachio))
            else:
                pistachio = int(pistachio)
                print("pistachio = " + str(pistachio))
            sheetsource.update_cell(y, 40, pistachio)

        elif "بستاشيو" in I and "بدل" not in I:
            pistachio = I.split("بستاشيو")[0]
            if pistachio == " " or pistachio == "" or pistachio == "  ":
                pistachio = "1"
                pistachio = int(pistachio)
                print("pistachio = " + str(pistachio))
            else:
                pistachio = int(pistachio)
                print("pistachio = " + str(pistachio))
            sheetsource.update_cell(y, 40, pistachio)


        #mellow
        elif "ميلو" in I and "مارشميلو" not in I and "بدل" not in I :
            mellow = I.split("ميلو")[0]
            if mellow == " " or mellow == "" or mellow == "  ":
                mellow = "1"
                mellow = int(mellow)
                print("mellow = " + str(mellow))
            else:
                mellow = int(mellow)
                print("mellow = " + str(mellow))
            sheetsource.update_cell(y, 42, mellow)


        #kunafah
        elif "كنافه" in I and "بدل" not in I:
            kunafah = I.split("كنافه")[0]
            if kunafah == " " or kunafah == "" or kunafah == "  ":
                kunafah = "1"
                kunafah = int(kunafah)
                print("kunafah = " + str(kunafah))
            else:
                kunafah = int(kunafah)
                print("kunafah = " + str(kunafah))
            sheetsource.update_cell(y, 41, kunafah)


        elif "كنافة" in I and "بدل" not in I:
            kunafah = I.split("كنافة")[0]
            if kunafah == " " or kunafah == "" or kunafah == "  ":
                kunafah = "1"
                kunafah = int(kunafah)
                print("kunafah = " + str(kunafah))
            else:
                kunafah = int(kunafah)
                print("kunafah = " + str(kunafah))
            sheetsource.update_cell(y, 41, kunafah)




    # baby

        # bobo
        elif "بوبو" in I and "كب" not in I and "مكس" not in I and "بدل" not in I and "بكج " not in I  :
            bobo = I.split("بوبو")[0]
            if bobo == " " or bobo == "" or bobo == "  " :
                bobo = "1"
                bobo = int(bobo)
                print("bobo = " + str(bobo))
            else:
                bobo = int(bobo)
                print("bobo = " + str(bobo))
            sheetsource.update_cell(y, 43, bobo)

        elif "بكج بوبو" in I and "كب" not in I and "مكس" not in I and "بدل" not in I  :
            bobo = I.split("بكج بوبو")[0]
            if bobo == " " or bobo == "" or bobo == "  " :
                bobo = "1"
                bobo = int(bobo)
                print("bobo = " + str(bobo))
            else:
                bobo = int(bobo)
                print("bobo = " + str(bobo))
            sheetsource.update_cell(y, 43, bobo)

        # abo samra
        elif "ابو سمرة" in I and "كب" not in I and "بدل" not in I :
            abo_samra = I.split("بوبو")[0]
            if abo_samra == " " or abo_samra == "" or abo_samra == "  " :
                abo_samra = "1"
                abo_samra = int(abo_samra)
                print("abo_samra = " + str(abo_samra))
            else:
                abo_samra = int(abo_samra)
                print("abo_samra = " + str(abo_samra))
            sheetsource.update_cell(y, 44, abo_samra)

        # bobo mix
        elif "بوبو مكس" in I  and "بدل" not in I:
            bobo_mix = I.split("بوبو مكس")[0]
            if bobo_mix == " " or bobo_mix == "" or bobo_mix == "  " :
                bobo_mix = "1"
                bobo_mix = int(bobo_mix)
                print("bobo_mix = " + str(bobo_mix))
            else:
                bobo_mix = int(bobo_mix)
                print("bobo_mix = " + str(bobo_mix))
            sheetsource.update_cell(y, 45, bobo_mix)


        # bobo cup
        elif "بوبو كب" in I and "مكس" not in I and "بدل" not in I :
            bobo_cup = I.split("بوبو كب")[0]
            if bobo_cup == " " or bobo_cup == "" or bobo_cup == "  " :
                bobo_cup = "1"
                bobo_cup = int(bobo_cup)
                print("bobo_cup = " + str(bobo_cup))
            else:
                bobo_cup = int(bobo_cup)
                print("bobo_cup = " + str(bobo_cup))
            sheetsource.update_cell(y, 46, bobo_cup)



        elif "بوبوكب" in I and "مكس" not in I  and "بدل" not in I:
            bobo_cup = I.split("بوبوكب")[0]
            if bobo_cup == " " or bobo_cup == "" or bobo_cup == "  " :
                bobo_cup = "1"
                bobo_cup = int(bobo_cup)
                print("bobo_cup = " + str(bobo_cup))
            else:
                bobo_cup = int(bobo_cup)
                print("bobo_cup = " + str(bobo_cup))
            sheetsource.update_cell(y, 46, bobo_cup)


        # bobo cup mix
        elif "بوبو كب مكس" in I and "بدل" not in I :
            bobo_cup_mix = I.split("بوبو كب مكس")[0]
            if bobo_cup_mix == " " or bobo_cup_mix == "" or bobo_cup_mix == "  " :
                bobo_cup_mix = "1"
                bobo_cup_mix = int(bobo_cup_mix)
                print("bobo_cup_mix = " + str(bobo_cup_mix))
            else:
                bobo_cup_mix = int(bobo_cup_mix)
                print("bobo_cup_mix = " + str(bobo_cup_mix))
            sheetsource.update_cell(y, 47, bobo_cup_mix)


        elif "بوبوكب مكس" in I and "بدل" not in I :
            bobo_cup_mix = I.split("بوبوكب مكس")[0]
            if bobo_cup_mix == " " or bobo_cup_mix == "" or bobo_cup_mix == "  " :
                bobo_cup_mix = "1"
                bobo_cup_mix = int(bobo_cup_mix)
                print("bobo_cup_mix = " + str(bobo_cup_mix))
            else:
                bobo_cup_mix = int(bobo_cup_mix)
                print("bobo_cup_mix = " + str(bobo_cup_mix))
            sheetsource.update_cell(y, 47, bobo_cup_mix)


        # abo samra cup
        elif "ابو سمرة كب" in I and "بدل" not in I :
            abo_samra = I.split("ابو سمرة كب")[0]
            if abo_samra_cup == " " or abo_samra_cup == "" or abo_samra_cup == "  " :
                abo_samra_cup = "1"
                abo_samra_cup = int(abo_samra_cup)
                print("abo_samra_cup = " + str(abo_samra_cup))
            else:
                abo_samra_cup = int(abo_samra_cup)
                print("abo_samra_cup = " + str(abo_samra_cup))
            sheetsource.update_cell(y, 48, abo_samra_cup)





    # new item
        # ta3 boord
        elif "تع بورد" in I and "بكج" not in I and "بدل" not in I :
            ta3_boord = I.split("تع بورد")[0]
            if ta3_boord == " " or ta3_boord == "" or ta3_boord == "  " :
                ta3_boord = "1"
                ta3_boord = int(ta3_boord)
                print("ta3 boord = " + str(ta3_boord))
            else:
                ta3_boord = int(ta3_boord)
                print("ta3 boord = " + str(ta3_boord))
            sheetsource.update_cell(y, 49, ta3_boord)






    # packages names :

        # packages names
        elif "بكج " in I and "بدل" not in I :
            package_name = I
            print("package name = " + package_name)
            sheetsource.update_cell(y, 26, package_name)


    # Others
        else:
            other = I
            print("Others = " + other)
            sheetsource.update_cell(y, 50, other)
















    '''if "بكج " in I :
            package_name = ''
            packages = I.split("بكج ")[1:]
            for ls in packages:
                if ls != "'" and ls != "[" and ls != "]" :
                    package_name += ls
                else:
                    ls = "،"
                    package_name += ls
            print("package name = " +"بكج " + package_name)'''






















    '''all = [double, cookies,white,brownie,red,apple,bomb,kinder,sand,lotus,reeses,cheesecake,pistachio,marshmallow,ferrero,bobo,bobo_cup,bobo_mix,bobo_cup_mix,abo_samra_cup,abo_samra,kunafah,mellow]
    for item in all :
        print(type(item))'''

























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