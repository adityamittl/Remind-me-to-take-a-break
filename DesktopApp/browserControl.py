from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebAccess:
    def __init__(self):
        self.runningState = True
        self.root = r"C:\webdrivers\chromedriver.exe"
        self.driver = webdriver.Chrome(self.root)
        self.driver.maximize_window()
    
    def Netflix(self,username,password,Mname):
        url = "https://www.netflix.com/browse"
        self.driver.get(url)
        self.driver.find_element_by_id("id_userLoginId").send_keys(username)
        self.driver.find_element_by_id("id_password").send_keys(password)
        self.driver.find_elements_by_tag_name("button")[1].click()
        self.driver.find_elements_by_class_name('profile-link')[0].click()
        url = "https://www.netflix.com/search?q=" + Mname
        self.driver.get(url)
        self.driver.find_elements_by_class_name("title-card")[0].click()

    def youtube(self,title):
        url = "https://www.youtube.com/results?search_query="+title
        self.driver.get(url)
        self.driver.find_elements_by_class_name("ytd-video-renderer")[0].click()
    def switchState(self):
        if self.runningState:
            self.driver.find_element_by_tag_name('video').click()
            print("Paused")
            self.runningState = False
        else:
            self.driver.find_element_by_tag_name('video').click()
            print("Playing")
            self.runningState = True
    
    def enterFullScreen(self):
        self.driver.find_element_by_tag_name('video').send_keys("f")


if __name__ == "__main__":
    web = WebAccess()
    web.youtube("Hello world")
    sleep(10)
    web.switchState()
    print("Paused")


