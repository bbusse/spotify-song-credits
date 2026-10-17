#!/usr/bin/env python3
#
# spotify-song-credits
# Scrape song credits from Spotify's web player
#
# Copyright (c) 2020 Björn Busse <bj.rn@baerlin.eu>
#

import json
import time

from selenium.webdriver.common.by import By

import webdriver_util as wdu


def spotify_song_credits(browser, login):
    # TODO: Use the WebDriverWait() function
    # https://selenium-python.readthedocs.io/waits.html
    time.sleep(15)
    spotify_accept_cookies(browser)
    time.sleep(3)
    browser.get(login['url_payload'])
    time.sleep(15)
    spotify_show_song_options(browser)
    time.sleep(3)
    spotify_show_credits(browser)
    time.sleep(3)
    credits = spotify_get_credits(browser)
    print(credits)


def spotify_accept_cookies(browser):
    print("Accepting cookies")
    browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
    return True


def spotify_show_song_options(browser):
    browser.find_element(By.XPATH, "//*[@aria-selected='true']/div/div[3]/button[2]").click()
    return True


def spotify_show_credits(browser):
    browser.find_element(By.XPATH, "//*[text() = 'Show credits']/parent::button").click()
    return True


def spotify_get_credits(browser):
    credits = {}
    credits['performed_by'] = browser.find_element(By.XPATH, "//*[text() = 'Performed by']/following::span").text
    credits['written_by'] = browser.find_element(By.XPATH, "//*[text() = 'Written by']/parent::div").text
    credits['produced_by'] = browser.find_element(By.XPATH, "//*[text() = 'Produced by']/parent::div").text
    credits['source'] = ""
    credits_json = json.dumps(credits)
    return credits_json


if __name__ == '__main__':
    b = wdu.browser_from_args()
    spotify_song_credits(b.browser, b.login)
