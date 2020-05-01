from selenium import webdriver
from time import sleep
from credentials import username, password
import numpy as np
from numpy import random


class TinderBot():
    """Class with all the methods to automate the bot"""

    def __init__(self):
        """Initialize Tinder Bot: Opening Chrome"""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)

    def login(self):
        """Enter the credentials and close gps and notifications popups"""
        self.driver.get('https://tinder.com')
        sleep(9)

        try:
            cookies_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_btn.click()
        except:
            pass

        try:
            fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
            fb_btn.click()
        except:
            more_options = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_options.click()
            fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
            fb_btn.click()
        sleep(5)

        """switch to login popup"""
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        """enter email"""
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        """enter password"""
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        """login click"""
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)
        sleep(10)

        popup_gps = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_gps.click()

        popup_notif = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_notif.click()

        sleep(10)
        try:
            popup_location = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[2]/button')
            popup_location.click()
        except:
            pass

    def like(self):
        """Click Like button"""
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        """Click Dislike button"""
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        dislike_btn.click()

    def super_like(self):
        """Click Superlike button"""
        superlike = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/button')
        superlike.click()

    def auto_swipe(self):
        """Click Like button undefinitely (50 times in a free version Tinder account)"""
        x = 1
        while x == 1:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_offer()
                        x = 0

    def auto_swipe_alt(self):
        """Click Like button undefinitely (50 times in a free version Tinder account)
        with a probability of 70%. If not, Dislike will be clicked"""
        x = 1
        while x == 1:
            sleep(0.5)
            try:
                coin = np.random.binomial(n=1, p=0.7, size=None)
                if coin == 1:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_offer()
                        x = 0

    def auto_super(self):
        """Click Superlike button once. Then, click Like button undefinitely
        (50 times in a free version Tinder account)"""
        self.super_like()
        x = 1
        while x == 1:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
                    x = 0

    def auto_super_alt(self):
        """Click Superlike button once. Then, click Like button undefinitely
        (50 times in a free version Tinder account) with a probability of 70%.
        If not, Dislike will be clicked"""
        self.super_like()
        x = 1
        while x == 1:
            sleep(0.5)
            try:
                coin = np.random.binomial(n=1, p=0.7, size=None)
                if coin == 1:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
                    x = 0

    def close_popup(self):
        """Close popup"""
        popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        """Close match popup"""
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_offer(self):
        """Close offer popup"""
        try:
            offer_popup = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            offer_popup.click()
        except:
            pass


bot = TinderBot()
bot.login()
