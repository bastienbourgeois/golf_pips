import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from colorama import init
from os import system

system('mode con: lines=34 cols=120')
init()

NB_MORE_CHANNEL = 7
CHANNEL_URL = 'http://channelstream.club/'
ST_URL = []
ST_URL.append("https://cricfree.sc/football-live-stream-5")
ST_URL.append("https://cricfree.sc/rugby-live-stream")
ST_URL.append("https://cricfree.sc/golf-live-streaming-")

class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

dic = {
    "Golf+": "https://channelstream.club/stream/golf.php",
    "Foot+": "https://channelstream.club/stream/foot_plus.php",
    "RMC 1": "https://channelstream.club/stream/rmc_sport-1.php",
    "Canal+": "https://channelstream.club/stream/canal.php",
    "Canal+ Sport": "https://channelstream.club/stream/canal_sport.php",
    "beIN 1": "https://channelstream.club/stream/bein_1.php",
    "Multisports1": "https://channelstream.club/stream/multisport_1.php"
}

print(col.WARNING + "------ TV Pip's ------" + col.ENDC)
print(col.HEADER + "*** Favoris ***" + col.ENDC)

r = requests.get(url=CHANNEL_URL)
while r.status_code != 200:
    print("ChannelStream ne réponds pas, 5 secondes avant nouvelle essaie")
    sleep(5)
    r = requests.get(url=CHANNEL_URL)
soup = BeautifulSoup(r.content, 'lxml').find_all('div')

def text_prog(h):
    i = ""
    if h.find('i') != None:
        i = h.find('i').text
        h.find('i').decompose()
    else:
        i = col.HEADER + "présent dans les favoris" + col.ENDC
    s = h.text + " -> " + i
    return s

def print_prog(d):
    s = col.WARNING + "\t-sans programme-" + col.ENDC
    for j in range(len(soup)):
        if soup[j].find_all('input')[1].get('value') == d:
            s = text_prog(soup[j].find('h4'))
            return col.OKGREEN + "\t" + s + col.ENDC
    return s

for i, d in enumerate(dic.values()):
    print(str(i + 1) + "- " + list(dic.keys())[i], end='')
    print(print_prog(d))
    i = i + 1

print(col.HEADER + "\n*** En ce moment ***" + col.ENDC)

for i in range(NB_MORE_CHANNEL):
    url = soup[i].find_all('input')[1].get('value')
    dic.update( {url.rsplit('/', 1)[-1]: url} )
    print(str(len(dic)) + "-" + col.OKGREEN + text_prog(soup[i].find('h4')) + col.ENDC)

## ETRANGER

print(col.HEADER + "\n*** Chaines Etrangères ***" + col.ENDC)
NB_UK_CHANNEL = len(dic)

dic.update( {"Sky Sport MainEvent": "https://channelstream.club/stream/uk_skysport_1.php"} )
dic.update( {"Sky Sport Foot": "https://channelstream.club/stream/uk_skysport_football.php"} )
dic.update( {"Sky Sport Golf": "https://sportscart.xyz/ch/scplayer-70.php"} )
dic.update( {"Sky Sport Arena":"https://channelstream.club/stream/uk_skysport_arena.php"} )
dic.update( {"Sky Sport Action":"https://channelstream.club/stream/uk_skysport_action.php"} )
dic.update( {"Sky Sport 1League": "https://channelstream.club/stream/uk_premier_sports.php"} )
dic.update( {"BT Sport 1    ": "https://channelstream.club/stream/uk_btsport_1.php"} )
#dic.update( {"Totalsport Golf" : "http://totalsport.me//golf.html"} )
dic.update( {"Totalsport Golf" : "https://telerium.tv/embed/25542.html"} )

NB_UK_CHANNEL = len(dic) - NB_UK_CHANNEL

for i in range(len(dic) - NB_UK_CHANNEL, len(dic)):
    print(str(i + 1) + "- " + list(dic.keys())[i], end='')
    print(print_prog(list(dic.values())[i]))

print(col.OKBLUE + "\nRentre un nombre, puis fais entrer: ", end='' + col.ENDC)

x = 0
while True:
    s = input()
    if s.isnumeric():
        x = int(s)
    if not s.isnumeric():
        print(col.FAIL + "Fait un effort, ce n'est même pas un nombre ça : " + s + ", " + col.OKBLUE + " test 1 idiiiiot: ", end='' + col.ENDC)
    elif not (x > 0 and x < len(dic) + 1):
        print(col.FAIL + "Ce nombre n'est pas dans la liste," + col.OKBLUE + " test un autre: ", end='' + col.ENDC)
    else:
        break

## STREAM 

URL = list(dic.values())[x-1]

def del_id(idd):
    js_string = "var element = document.getElementById('" + idd + "');if(element!=null){element.remove();}"
    driver.execute_script(js_string)

def del_script():
    js_string = "var element = document.querySelectorAll('script');for(var i=0; i<element.length; i++){ if(i!=1){element[i].remove();}}"
    driver.execute_script(js_string)

def del_all_tag(tag):
    js_string = "var element = document.querySelectorAll('" + tag + "');for(var i=0; i<element.length; i++){if(element!=null){element[i].remove();}}"
    driver.execute_script(js_string)

def del_xpath(x):
    js_string = "result = str.replace(/(<p[^>]+?>|<p>|<\\/p>)/img, \"\");"
    driver.execute_script(js_string)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options = options, executable_path = 'driver/chromedriver.exe')
driver.get(URL)
main_window = driver.current_window_handle

sleep(14) #Attendre que la vidéo se lance

del_script()
del_all_tag('noscript')
del_id('html3')
del_id('wrapfabtest')

sleep(0.5)

for i in range(4): #Cliquer tant que la vidéo n'a pas de son
    webdriver.ActionChains(driver).click().perform()
    for j in range(len(driver.window_handles) - 1, 0, -1):
        driver.switch_to.window(driver.window_handles[j])
        driver.close()
        sleep(0.1)
    driver.switch_to.window(main_window)
    sleep(0.5)