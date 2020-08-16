import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from colorama import init

init()

CHANNEL_URL = 'http://channelstream.club/'
NB_CHANNEL = 9

r = requests.get(url=CHANNEL_URL)
soup = BeautifulSoup(r.text, 'lxml').find_all('div')

class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print(col.WARNING + "------ TV Pip's ------" + col.ENDC)
print(col.HEADER + "*** Favoris ***" + col.ENDC)
print(col.OKGREEN + "1- Golf plus")
print("2- Foot plus")
print("3- RMC 1")
print("4- Canal plus")
print("5- Canal sport")
print("6- beIN 1" + col.ENDC)
print(col.HEADER + "\n*** En ce moment ***" + col.ENDC)

channel = []
channel.append("https://channelstream.club/stream/golf.php")
channel.append("https://channelstream.club/stream/foot_plus.php")
channel.append("https://channelstream.club/stream/rmc_sport-1.php")
channel.append("https://channelstream.club/stream/canal.php")
channel.append("https://channelstream.club/stream/canal_sport.php")
channel.append("https://channelstream.club/stream/bein_1.php")

for i in range(NB_CHANNEL):
    print(col.OKGREEN + str(i + len(channel) + 1) + "-" + soup[i].find('h4').get_text() + col.ENDC)

for i in range(NB_CHANNEL):
    channel.append(soup[i].find_all('input')[1].get('value'))

print(col.OKBLUE + "\nRentre un nombre, puis fais entrer: ", end='' + col.ENDC)

x = 0
while True:
    s = input()
    if s.isnumeric():
        x = int(s)
    if not s.isnumeric():
        print(col.FAIL + "Fait un effort, ce n'est même pas un nombre ça : " + s + ", " + col.OKBLUE + " test 1 idiiiiot: ", end='' + col.ENDC)
    elif not (x > 0 and x < len(channel) + 1):
        print(col.FAIL + "Ce nombre n'est pas dans la liste," + col.OKBLUE + " test un autre: ", end='' + col.ENDC)
    else:
        break

## STREAM 

URL = channel[x-1]

CHROME_DRIVER_PATH = 'driver/chromedriver.exe'
EXTENSION_PATH = 'driver/ub.crx'

def del_id(idd):
    js_string = "var element = document.getElementById('" + idd + "');if(element!=null){element.remove();}"
    driver.execute_script(js_string)

def del_script():
    js_string = "var element = document.querySelectorAll('script');for(var i=0; i<element.length; i++){ if(i!=1){element[i].remove();}}"
    driver.execute_script(js_string)

def del_iframe():
    js_string = "var element = document.querySelectorAll('iframe');for(var i=0; i<element.length; i++){ if(i!=1){element[i].remove();}}"
    driver.execute_script(js_string)

def del_all_tag(tag):
    js_string = "var element = document.querySelectorAll('" + tag + "');for(var i=0; i<element.length; i++){ element[i].remove();}"
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

driver = webdriver.Chrome(options = options, executable_path = CHROME_DRIVER_PATH)
driver.get(URL)
main_window = driver.current_window_handle

sleep(14)

del_script()
del_all_tag('noscript')
del_all_tag('style')
#del_iframe()
del_id('html3')

stream = driver.find_element_by_tag_name('iframe')
if (stream != None):
    driver.switch_to.frame(stream)

sleep(0.5)

del_all_tag('script')
del_all_tag('iframe')
del_all_tag('object')
del_id('wrapfabtest')

sleep(1.5)

for i in range(3):
    webdriver.ActionChains(driver).click().perform()
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        sleep(0.2)
        driver.switch_to.window(main_window)
        sleep(0.5)