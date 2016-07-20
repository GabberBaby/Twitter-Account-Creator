import time;
import sys;

import random;
import selenium.webdriver.chrome.service as service;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;


print("Number of emails: ")
ammount = raw_input();

# Email address generator

print("Working...");

service = service.Service('../chromedriver');
service.start()
capabilities = {'chrome.binary': ''} # Enter path to chrome.exe in windows inside the '' tags.

driver = webdriver.Remote(service.service_url, capabilities);
driver.get('https://www.random.org/strings/');

time.sleep(1);

# Enter the ammount of emails into random.org to generate that ammount of strings
stringNumber = driver.find_element_by_name("num");
stringNumber.clear();
stringNumber.send_keys(ammount);

# Enter the length of the strings
stringLength = driver.find_element_by_name("len");
stringLength.clear();
stringLength.send_keys(15);

# Allow uppercase letters
uppercase = driver.find_element_by_name("upperalpha");
uppercase.click();

# Allow lowercase letters
lowercase = driver.find_element_by_name("loweralpha");
lowercase.click();

# Get strings
lowercase.submit();

# All the strings are stored inside var x, then stored inside array called emails

x = driver.find_element_by_class_name("data").text;

# Now the variable x is stored inside a file for the email generating program to use.

file = open("emails.txt", "wb");
file.write(x);

# Close opend file
file.close()


#target_size = 10
#count = len(x) / target_size;

#emails = [ x[i:i+target_size] for i in range(0, len(x), target_size) ];
print("Successfully created emails.txt\n Please open up \"EmailAccountGenerator.py\" and enter in the same ammount of emails as you did here");
driver.close();