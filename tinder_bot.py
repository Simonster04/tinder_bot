from selenium import webdriver
from time import sleep
from credentials import username, password
import numpy as np
from prohibited import men_bios, men_names

likes = 0
dislikes = 0
superlikes = 0
matches = 0

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
        sleep(5)

        try:
            cookies_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            cookies_btn.click()
        except:
            pass

        sleep(0.5)
        try:
            fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
            fb_btn.click()
        except:
            more_options = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_options.click()
            sleep(1)
            fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
            fb_btn.click()
        sleep(3)

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
        sleep(9)

        popup_gps = self.driver.find_element_by_css_selector('button[aria-label="Allow"]')
        popup_gps.click()

        popup_notif = self.driver.find_element_by_css_selector('button[aria-label="Enable"]')
        popup_notif.click()

        sleep(4)
        try:
            popup_location = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[2]/button')
            popup_location.click()
        except:
            pass

    def like(self):
        """Click Like button"""
        self.driver.find_element_by_css_selector('button[aria-label="Like"]').click()
        likes += 1


    def dislike(self):
        """Click Dislike button"""
        self.driver.find_element_by_css_selector('button[aria-label="Nope"]').click()
        dislikes += 1

    def super_like(self):
        """Click Superlike button"""
        self.driver.find_element_by_css_selector('button[aria-label="Super Like"]').click()
        superlikes += 1

    def auto_swipe(self):
        """Click Like button undefinitely (50 times in a free version Tinder account)"""
        x = 1
        while x == 1:
            sleep(0.5)
            try:
                like = self.get_all()
                if like == -1:
                    self.dislike()
                else:
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
                like = self.get_all()
                if like == -1:
                    self.dislike()
                else:
                    like = np.random.binomial(n=1, p=0.7, size=None)
                    if like == 1:
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
                like = self.get_all()
                if like == -1:
                    self.dislike()
                else:
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
                like = self.get_all()
                if like == -1:
                    self.dislike()
                else:
                    like = np.random.binomial(n=1, p=0.7, size=None)
                    if like == 1:
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
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()

    def close_match(self):
        """Close match popup"""
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a').click()
            matches += 1
        except:
            self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/a').click()
            matches += 1

    def close_offer(self):
        """Close offer popup"""
        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]').click()
        except:
            pass
    
    def open_profile(self):
        """Open profile"""
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]').click()
        except:
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[6]').click()

    def get_name(self):
        """Finds if the name is on the prohibited list (men_names) and return -1, 2 otherwise"""
        try:
            name = self.driver.find_element_by_xpath(
                       '//*[@id="content"]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h1')
        except:
            try:
                name = self.driver.find_element_by_xpath(
                           '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h1')
            except:
                return None
        name = name.text
        name_list = name.split()
        if len(name_list) >= 2:
            if name_list[1] in men_names:
                print(f'\nALERT!\nHIS name is {name_list[1]}\n')
                return -1
        if name_list[0] in men_names:
            print(f'\nALERT!\nHIS name is {name_list[0]}\n')
            return -1
        return 2

    def get_bio(self):
        """Finds if the bio contains a word from the prohibited list (men_bios) and return -1, 2 otherwise"""
        try:
            bio = self.driver.find_element_by_xpath(
                      '//*[@id="content"]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[2]/div')
        except:
            try:
                bio = self.driver.find_element_by_xpath(
                          '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div')
            except:
                return None
        if bio.text == '':
            dislike_profile = 'failed to get bio'
        bio = bio.text
        bio = bio.split()
        for word in bio:
            if word in men_bios:
                print(f'\nALERT!\nFound <{word}> in HIS profile\n')
                return -1
        return 2

    def insta_pics(self):
        """Check if the profile has Instagram profile linked"""
        try:
            x = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]').text
        except:
            try:
                x = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]').text
            except:
                return -1
        x = x.split()
        for i in range(len(x)):
            if x[i] == 'Recent' and x[i + 1] == 'Instagram' and x[i + 2] == 'Photos':
                return (2)
        return(-1)


    def get_num_pics(self):
        """Check number of pictures. Returns -1 if only has one picture, 2 otherwise"""
        aux = 0
        try:
            pics=self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/div/main/div/div/div[1]/div/div[1]/span/a[2]/div/div[2]')
            num_pics=pics.text[-1]
        except:
            try:
                pics=self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[2]/div/div[2]')
                num_pics=pics.text[-1]
            except:
                print('\nALERT!\nOnly has one picture')
                aux = -1
        if aux == -1 and self.insta_pics() != -1:
            print("but has Instagram. Give her a try")
        if aux == -1 and self.insta_pics() == -1:
            print("and no Instagram. Must be fake\n")
            return -1
        return 2
 
    def get_all(self):
        """Calls open_profile(), get_name(), get_bio(), get_num_pics() methods"""
        self.open_profile()
        aux = self.get_name()
        if aux == -1:
            return aux
        aux = self.get_bio()
        if aux == -1:
            return aux
        aux = self.get_num_pics()
        if aux == -1:
            return aux
        return 2


bot = TinderBot()
bot.login()
sleep(6)
print("----------------------------\nLet's begin----------------------------")
bot.auto_swipe()
print('----------------------------\nStatistics:')
print(f'Likes given: {likes}')
print(f'Dislikes given: {dislikes}')
print(f'Super Likes given: {superlikes}')
print(f'matches: {matches}')
print('----------------------------\nWe are done. Go flirt.\n----------------------------')
