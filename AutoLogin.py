import time
from selenium import *
from selenium import webdriver


class WebDriver:
  def __init__(self) -> None:
      pass

  def open_driver(self):
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument("--incognito")
    driverOptions.add_argument("--disable-gpu")
    driverOptions.add_argument("--start-maximized")
    driverOptions.add_argument("--log-level=3")
    driverOptions.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
    web_driver = webdriver.Chrome(executable_path="chromedriver.exe", options=driverOptions)
    return web_driver

class AutoLogin():
    def __init__(self, Token: str) -> None:
        self.WebDriver = WebDriver()
        self.WebDriver = self.WebDriver.open_driver()
        self.Token = Token
        self.Script = """
        let token = "%s";

function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }

login(token)""" % Token

    def MainPage(self):
        self.WebDriver.get('https://discord.com/login')
        time.sleep(5)
        self.WebDriver.execute_script(self.Script)
        input('')


Atl = AutoLogin(input('Token :: ')) 
Atl.MainPage()