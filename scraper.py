from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

firefox_driver = webdriver.Firefox(executable_path='webdriver/geckodriver.exe')


class InstagramScraper:
    def sign_in(self, username, password):
        # loading the instagram login page
        firefox_driver.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        # finding username element from the website
        firefox_driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input"
        ).send_keys(username)
        # finding password element from the website
        firefox_driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input"
        ).send_keys(password)
        # finding login button element from the website
        firefox_driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button"
        ).click()
        sleep(3)
        # finding not now button from save login info page
        firefox_driver.find_element(
            By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"
        ).click()
        sleep(3)
        # finding not now button in the pop notification
        WebDriverWait(firefox_driver, 10).until(
            element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]"))).click()
        # taking screen shot on the feed page
        firefox_driver.get_screenshot_as_file('screenshot.png')


if __name__ == '__main__':
    insta_scrap = InstagramScraper()
    insta_scrap.sign_in(username='hawayi6319@stvbz.com', password='hawayi@6319@')
