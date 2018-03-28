from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
caps =webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r"C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")