from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#from function_prog import Col

class Col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Launch_driver:
    def __init__(self, dic, x):
        URL = list(dic.values())[x-1]

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument('--hide-scrollbars')
        options.add_argument('--disable-gpu')
        options.add_argument("--log-level=3")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #driver = webdriver.Chrome(options=options, executable_path='driver/chromedriver.exe')
        driver.get(URL)
        main_window = driver.current_window_handle

        sleep(14) #Attendre que la vidéo se lance

        #del_script() #Adblock trouvé ?
        try:
            self.del_id(driver, 'html3')
        except:
            print(Col.FAIL + "Impossible d'enlever html3" + Col.ENDC)
        try:
            self.del_id(driver, 'wrapfabtest')
        except:
            print(Col.FAIL + "Impossible d'enlever la pub du milieu" + Col.ENDC)
        try:
            self.del_new_ad(driver)
        except:
            print(Col.FAIL + "Impossible d'enlever la popup en haut" + Col.ENDC)

        sleep(0.5)

        for i in range(4): #Cliquer tant que la vidéo n'a pas de son
            webdriver.ActionChains(driver).click().perform()
            for j in range(len(driver.window_handles) - 1, 0, -1):
                driver.switch_to.window(driver.window_handles[j])
                driver.close()
                sleep(0.1)
            driver.switch_to.window(main_window)
            sleep(0.5)
    
    def del_id(self, driver, idd):
        js_string = "var element = document.getElementById('" + idd + "');if(element!=null){element.remove();}"
        driver.execute_script(js_string)

    def del_script(self, driver):
        js_string = "var element = document.querySelectorAll('script');for(var i=0; i<element.length; i++){ if(i!=1){element[i].remove();}}"
        driver.execute_script(js_string)

    def del_new_ad(self, driver):
        js_string = "var element = document.querySelectorAll('iframe');if(element!=null){element[element.length - 1].remove();}"
        driver.execute_script(js_string)

    
    



    