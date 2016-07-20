import time;
import sys;

import random;
import selenium.webdriver.chrome.service as service;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;


print("Number of names: ")
ammount = raw_input();

# Email address generator

print("Working...");

service = service.Service('chromedriver/chromedriver');
service.start()
capabilities = {'chrome.binary': ''} # Enter path to chrome.exe in windows inside the '' tags.

TenMinuteMail = webdriver.Remote(service.service_url, capabilities);
TenMinuteMail.get('https://10minutemail.com');

Email = TenMinuteMail.find_element_by_id("mailAddress").get_attribute('value');
print Email;

Twitter = webdriver.Remote(service.service_url, capabilities);
Twitter.get('https://twitter.com/signup');


name     = Twitter.find_element_by_id('full-name');
password = Twitter.find_element_by_id('password');
email    = Twitter.find_element_by_id('email');
submit   = Twitter.find_element_by_id('submit_button');

name.clear();
email.clear();
password.clear();

name.send_keys("Goerge Lucky");
email.send_keys(Email);
password.send_keys("xxStarBot123");

submit.click();

time.sleep(1);

#Twitter.close();
TenMinuteMail.close();