from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pyautogui import press
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from strings import *

logfile = open(log_file_path, 'a', encoding='utf-8')
post_content = open(post_file_path, 'r', encoding='utf-8').readlines()


def report_start():
    now = datetime.now().strftime("%m/%d/%Y | %H:%M:%S")
    logfile.write(log_report_start + now + '\n')


def post_success():
    sleep(6)
    now = datetime.now().strftime(time_format)
    logfile.write(log_report_success + now + '\n')
    raise Exception(exception_report_success + now + '\n')


def post_fail():
    now = datetime.now().strftime(time_format)
    logfile.write(log_report_fail + now + '\n')
    raise Exception(exception_report_fail + now + '\n')


def post_process():
    post_test = post_content
    if post_test[0] != post_head:
        raise Exception(exception_post_border_error)
    post_test.pop(0)
    post_number = post_test[0].split()
    if not post_number[-1].isnumeric():
        raise Exception(exception_post_number_error)
    now = datetime.now().strftime(time_format)
    logfile.write(log_report_valid + now + '\n')


def tag_name(post_input, name_to_comment):
    post_input.send_keys("@" + name_to_comment)
    sleep(1)
    post_input.send_keys(Keys.ARROW_DOWN)
    sleep(1)
    post_input.send_keys(Keys.ENTER)
    sleep(2)


def hash_tag(post_input, name_to_comment):
    hashtag = name_to_comment.replace(" ", "_")
    post_input.send_keys("#" + hashtag)
    sleep(1)
    post_input.send_keys(Keys.ARROW_DOWN)
    sleep(1)
    post_input.send_keys(Keys.ENTER)
    sleep(2)


def clean_post():
    update_file = open(post_file_path, encoding='utf-8')
    data = update_file.read()
    data = data[data.index(post_end) + len(post_end):]
    update_file.close()
    update_file = open(post_file_path, 'w', encoding='utf-8')
    update_file.write(data)


def uploadImage(driver, image_path):
    driver.find_element(By.XPATH, image_button).click()
    sleep(1)
    press('esc')
    driver.find_element(By.XPATH, image_select).send_keys(image_path)
    wait = WebDriverWait(driver, 5)
    pressButton = wait.until(ec.visibility_of_element_located((By.XPATH, image_complete)))
    sleep(1)
    pressButton.click()


def post_to_linkedIn():
    driver = webdriver.Chrome(executable_path=webdriver_path)
    linkedin = linkedin_path
    userdata = open(userdata_file_path).readlines()
    try:
        driver.get(linkedin)
        sleep(1)
        driver.find_element(By.ID, username_field).send_keys(userdata[0])
        driver.find_element(By.ID, password_field).send_keys(userdata[1])
        driver.find_element(By.XPATH, login_button).click()
        sleep(2)
        driver.find_element(By.XPATH, writing_button).click()
        sleep(2)
        post_input = driver.find_element(By.CLASS_NAME, posting_field)
        for line in post_content:
            if line == post_end:
                break
            if not line == post_end:
                post_input.send_keys(line)
        sleep(2)
        hash_tag(post_input,"ראובוט")

        uploadImage(driver, image_path)
        sleep(6)
        driver.find_element(By.XPATH, post_button).click() # deactivated. to re-activate - remove # sign
        post_success()
        driver.close()
        return
    except Exception as e:
        print(e)


def main():
    # report_start()
    # clean_post()
    try:
        # post_process()
        post_to_linkedIn()
        now = datetime.now().strftime(time_format)
        logfile.write(log_report_update + now + '\n')
    except:
        post_fail()


if __name__ == "__main__":
    main()
