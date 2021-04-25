import requests
from os import system
from time import sleep
from bs4 import BeautifulSoup
from colorama import init
from src.color import Col
from src.launch_driver import Launch_driver
from src.function_prog import print_prog
from src.function_prog import text_prog
from src.function_prog import while_valid_number

system('mode con: lines=34 Cols=120')
init()

NB_MORE_CHANNEL = 7
CHANNEL_URL = 'http://channelstream.club/'
ST_URL = []
ST_URL.append("https://cricfree.sc/football-live-stream-5")
ST_URL.append("https://cricfree.sc/rugby-live-stream")
ST_URL.append("https://cricfree.sc/golf-live-streaming-")

dic = {
    "Golf+": "https://channelstream.club/stream/golf.php",
    "Foot+": "https://channelstream.club/stream/foot_plus.php",
    "RMC 1": "https://channelstream.club/stream/rmc_sport-1.php",
    "Canal+": "https://channelstream.club/stream/canal.php",
    "Canal+ Sport": "https://channelstream.club/stream/canal_sport.php",
    "beIN 1": "https://channelstream.club/stream/bein_1.php",
    "Multisports1": "https://channelstream.club/stream/multisport_1.php"
}

r = requests.get(url=CHANNEL_URL)
soup = BeautifulSoup(r.content, 'lxml').find_all('div')

## ------- FAVORI -----------
print(Col.WARNING + "------ TV Pip's ------" + Col.ENDC)
print(Col.HEADER + "*** Favoris ***" + Col.ENDC)
for i, d in enumerate(dic.values()):
    print(str(i + 1) + "- " + list(dic.keys())[i], end='')
    print(print_prog(soup, d))
    i = i + 1

## ------- EN CE MOMENT -----------

print(Col.HEADER + "\n*** En ce moment ***" + Col.ENDC)
if r.status_code == 200 and soup:
    for i in range(NB_MORE_CHANNEL):
        url = soup[i].find_all('input')[1].get('value')
        dic.update( {url.rsplit('/', 1)[-1]: url} )
        print(str(len(dic)) + "-" + Col.OKGREEN + text_prog(soup, soup[i].find('h4')) + Col.ENDC)
else:
    print(Col.WARNING + "Récuparation du programme en direct impossible" + Col.ENDC)

## ------- CHAINE ETRANGERE -----------

print(Col.HEADER + "\n*** Chaines Etrangères ***" + Col.ENDC)
NB_UK_CHANNEL = len(dic)
dic.update( {"Sky Sport MainEvent": "https://channelstream.club/stream/uk_skysport_1.php"} )
dic.update( {"Sky Sport Foot": "https://channelstream.club/stream/uk_skysport_football.php"} )
dic.update( {"Sky Sport Golf": "https://sportscart.xyz/ch/scplayer-70.php"} )
dic.update( {"Sky Sport Arena":"https://channelstream.club/stream/uk_skysport_arena.php"} )
dic.update( {"Sky Sport Action":"https://channelstream.club/stream/uk_skysport_action.php"} )
dic.update( {"Sky Sport 1League": "https://channelstream.club/stream/uk_premier_sports.php"} )
dic.update( {"BT Sport 1    ": "https://channelstream.club/stream/uk_btsport_1.php"} )
dic.update( {"Totalsport Golf" : "https://telerium.tv/embed/25542.html"} )
NB_UK_CHANNEL = len(dic) - NB_UK_CHANNEL
for i in range(len(dic) - NB_UK_CHANNEL, len(dic)):
    print(str(i + 1) + "- " + list(dic.keys())[i], end='')
    print(print_prog(soup, list(dic.values())[i]))

print(Col.OKBLUE + "\nRentre un nombre, puis fais entrer: ", end='' + Col.ENDC)
x = while_valid_number(dic)

## ------- STREAM -----------

ld = Launch_driver(dic, x)