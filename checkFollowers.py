from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import math

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(15)
        bot.find_element_by_class_name('s4Iyt').click()
        time.sleep(5)
        bot.find_element_by_class_name('HoLwm').click()

    def check_followers(self, name):
        bot = self.bot
        bot.get('https://www.instagram.com/'+name)
        time.sleep(5)
        bot.find_element_by_xpath('//a[@href ="/'+ name + '/followers/"]').click()
        time.sleep(5)
        followersNumberString = bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
        followersNumber = math.ceil(int(followersNumberString)/12)
        for i in range(1, followersNumber):
            followers_list = bot.find_element_by_class_name('isgrP')
            bot.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(2)
        followers = bot.find_elements_by_class_name('FPmhX')
        all_followers = [elem.get_attribute('innerHTML') for elem in followers]
        with open('followers4_'+name+'.txt', "w", encoding="utf-8") as f:
            for follower in all_followers:
                f.write("%s\n" % follower)
    
    def check_following(self, name):
        bot = self.bot
        bot.get('https://www.instagram.com/'+name)
        time.sleep(5)
        bot.find_element_by_xpath('//a[@href ="/'+ name + '/following/"]').click()
        time.sleep(5)
        followingNumberString = bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
        followingNumber = math.ceil(int(followingNumberString)/12)
        for i in range(1, followingNumber):
            following_list = bot.find_element_by_class_name('isgrP')
            bot.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_list)
            time.sleep(2)
        following = bot.find_elements_by_class_name('FPmhX')
        all_following = [elem.get_attribute('innerHTML') for elem in following]
        with open('following4_'+name+'.txt', "w", encoding="utf-8") as f:
            for single_following in all_following:
                f.write("%s\n" % single_following)

    # Fill file_names to compare 
    def read_file(self):
        with open('file_name.txt', 'r') as fin:
            data1 = [i.strip() for i in fin]
        with open('file_name.txt', 'r') as fin:
            data2 = [i.strip() for i in fin]

        print(list(set(data2) - set(data1)))

# Change "username" and "password" on correct to log in to your Instagram account.
user = InstagramBot('username', 'password')

user.login()

# Change "username" on the Instagram name of person which you wanna check followers.
user.check_followers('username')

# Change "username" on the Instagram name of person which you wanna check following.
user.check_following('username')

# Uncomment the function and fill file names to compare arrays.
#user.read_file()