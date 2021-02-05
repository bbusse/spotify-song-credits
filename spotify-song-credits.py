#!/usr/bin/env python3
#
# spotify-song-credits
# Scrape song credits from Spotify's web player
#
# Copyright (c) 2020 Björn Busse <bj.rn@baerlin.eu>
#

import base64
import configargparse
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import sys
import time
import webdriver_util as wdu

# Logging
log_path = '/tmp/geckobrowser.log'
log_level = 'info'

path_logout = {
    "spotify":   ""
}

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
    browser.find_element_by_id("onetrust-accept-btn-handler").click()
    return True


def spotify_show_song_options(browser):
    browser.find_element_by_xpath("//*[@aria-selected='true']/div/div[3]/button[2]").click()
    return True


def spotify_show_credits(browser):
    browser.find_element_by_xpath("//*[text() = 'Show credits']/parent::button").click()
    return True


def spotify_get_credits(browser):
    credits = {}
    credits['performed_by'] = browser.find_element_by_xpath("//*[text() = 'Performed by']/following::span").text
    credits['written_by'] = browser.find_element_by_xpath("//*[text() = 'Written by']/parent::div").text
    credits['produced_by'] = browser.find_element_by_xpath("//*[text() = 'Produced by']/parent::div").text
    credits['source'] = ""
    credits_json = json.dumps(credits)
    return credits_json


if __name__ == '__main__':
    b = wdu.return_browser_init(log_path, log_level, path_logout)
    spotify_song_credits(b.browser, b.login)
