from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard
class zoom_bot:
	def join(self, meeting_link):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.bot.get(meeting_link)
		time.sleep(5)
		keyboard.send('tab', do_press=True, do_release=True)
		keyboard.send('tab', do_press=True, do_release=True)
		keyboard.send('enter', do_press=True, do_release=True)
		time.sleep(5)
		keyboard.send('tab', do_press=True, do_release=True)
		keyboard.send('tab', do_press=True, do_release=True)
		keyboard.send('tab', do_press=True, do_release=True)
		keyboard.send('enter', do_press=True, do_release=True)

		self.bot.quit()


link = open("meeting_link.txt","r").read()
obj = zoom_bot()
obj.join(link)