import subprocess
import os
import webbrowser
import random


def sayhi():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                                                           $")
    print("$  #########   ########    #######     ##    ##           ##      #####       ###      ##   $")
    print("$  ##          ##          ##    ##           ##         ##     ##     ##     ####     ##   $")
    print("$  ##          ##          ##    ##    ##      ##       ##     ##       ##    ## ##    ##   $")
    print("$  #######     ########    ## ###      ##       ##     ##      ##       ##    ##   ##  ##   $")
    print("$  ##          ##          ## ##       ##        ##   ##       ##       ##    ##    ## ##   $")
    print("$  ##          ##          ##   ##     ##         ## ##         ##     ##     ##     ####   $")
    print("$  ##          ########    ##     ##   ##          ###            #####       ##      ###   $")
    print("$                                                                                           $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def metro():
    subprocess.Popen('D:\\SteamLibrary\\steamapps\\common\\Metro Exodus Enhanced Edition\\MetroExodus.exe')
    os.system("Spotify.exe")


def fallout():
    subprocess.Popen('D:\\SteamLibrary\\steamapps\\common\\Fallout 4\\fallout4.exe')
    os.system("Spotify.exe")


def noman():
    subprocess.Popen('D:\\SteamLibrary\\steamapps\\common\\No Man\'s Sky\\Binaries\\NMS.exe')
    os.system("Spotify.exe")


def lol():
    subprocess.Popen('D:\\Riot Games\\League of Legends\\LeagueClient.exe')
    os.system("Spotify.exe")


def dyinglight():
    subprocess.Popen('D:\\SteamLibrary\\steamapps\\common\\Dying Light\\DyingLightGame.exe')
    os.system("Spotify.exe")


def randomgame():
    randomnumber = random.randint(0, 6)


# programs:

def visualstudio():
    subprocess.Popen('C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe')
    webbrowser.open("http://youtube.com", new=1)


def jagannathahora():
    subprocess.Popen('C:\\Program Files (x86)\\Jagannatha Hora\\bin\\jhora.exe')
    os.system("Spotify.exe")


def youtube():
    webbrowser.open("http://youtube.com", new=1)


def discord():
    subprocess.Popen('C:\\Users\\fahre\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc.exe')
    os.system("Spotify.exe")


def atom():
    subprocess.Popen('C:\\Users\\fahre\\AppData\\Local\\atom\\atom.exe')
    webbrowser.open("https://www.youtube.com/watch?v=OK_JCtrrv-c&t=3612s", new=1)


def pycharm():
    subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe')
    webbrowser.open("https://www.youtube.com/watch?v=rfscVS0vtbw&t=12544s", new=1)


def spotify():
    os.system("Spotify.exe")


sayhi()
print("I am trying to understand that.")
print("Do you want to play a game \nOr are you trying to open an program?")
What_I_want = input("Write there : ")

if What_I_want == "game" or What_I_want == "1":
    print("playing Metro Exodus       Type 1 or No Man")
    print("playing Fallout 4          Type 2 or fallout")
    print("playing No Man's sky       Type 3 or No Man")
    print("playing League of legends  type 4 or lol")
    print("Playing Dying Light        Type 5 or dying")
    print("Playing Random game        Type 6 or random")

    Which_Game = input("Input there: ")

    if Which_Game == "1" or Which_Game == "No Man":
        metro()
    elif Which_Game == "2" or Which_Game == "fallout":
        fallout()
    elif Which_Game == "3" or Which_Game == "No Man":
        noman()
    elif Which_Game == "4" or Which_Game == "lol":
        lol()
    elif Which_Game == "5" or Which_Game == "dying":
        dyinglight()
    elif Which_Game == "6" or Which_Game == "random":
        randomGame()
    else:
        print("You made an error!!")

elif What_I_want == "program" or What_I_want == "2":
    print("opening Visual Studio    type 1 or visual")
    print("opening Jagannatha Hora  type 2 or jagan")
    print("opening Youtube          type 3 or yt")
    print("opening Discord          type 4 or dc")
    print("opening Atom             type 5 or Atom")
    print("opening PyCharm          type 6 or PyCharm")
    print("opening Spotify          type 7 or spoti")
    Which_Program = input("Input there: ")

    if Which_Program == "1" or Which_Program == "visual":
        visualstudio()
    elif Which_Program == "2" or Which_Program == "jagan":
        jagannathahora()
    elif Which_Program == "3" or Which_Program == "yt":
        youtube()
    elif Which_Program == "4" or Which_Program == "dc":
        discord()
    elif Which_Program == "5" or Which_Program == "Atom":
        atom()
    elif Which_Program == "6" or Which_Program == "PyCharm":
        pycharm()
    elif Which_Program == "7" or Which_Program == "spoti":
        spotify()
    else:
        print("You made an error!!")
else:
    print("you made an error")
    print("You are quiting right now")
    print("Would you want to try again?")
    Quiting = input("type quit: ")
