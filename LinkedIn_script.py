import codecs
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from strings import *

logfile = open(log_file_path, 'a', encoding='utf-8')
post_content = open(post_file_path, 'r', encoding='utf-8').readlines()  # the entire post

def report_start():
    now = datetime.now().strftime("%m/%d/%Y | %H:%M:%S")
    logfile.write(log_report_start + now + '\n')


def post_success():
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


def post_list_update():
    post_update = open(post_file_path, 'w', encoding='utf-8')
    start_copy_here = False
    for line in post_content:
        if line == post_end and start_copy_here is False:
            start_copy_here = True
            continue
        if start_copy_here:
            if line != post_content_end:
                post_update.writelines(line)
    now = datetime.now().strftime(time_format)
    logfile.write(log_report_start + now + '\n')

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
        post_list_update()
        sleep(4)
        driver.find_element(By.XPATH, post_button).click()
        post_success()
        driver.close()
        return
    except Exception as e:
        print(e)


def main():
    report_start()
    post_list_update()
    try:
        post_process()
        post_to_linkedIn()
    except:
        post_fail()


if __name__ == "__main__":
    main()
