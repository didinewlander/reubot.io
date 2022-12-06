from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from strings import *
from time import sleep
from pyautogui import press


def uploadToLinkedin(driver, upload, path):
    button_path, input_path, accept_path = "", "", ""
    if upload == "image":
        button_path = image_button
        input_path = image_select
        accept_path = file_complete
    elif upload == "video":
        button_path = video_button
        input_path = video_path
        accept_path = file_complete

    else:
        raise Exception("New features are unavailable")
    '''
    elif upload== "document":
        button_path = image_button
        input_path = image_select
        accept_path = file_complete
    elif upload == "celebrate":
        
    elif upload == "hire":
        
    elif upload== "find":
        
    elif upload == "survey":
        
    elif upload == "offer":
        
    elif upload== "event":'''
    wait = WebDriverWait(driver, 5)
    pressButton = wait.until(ec.visibility_of_element_located((By.XPATH, button_path)))
    pressButton.click()
    driver.find_element(By.XPATH, button_path).click()
    sleep(1)
    press('esc')
    driver.find_element(By.XPATH, input_path).send_keys(path)

    pressButton = wait.until(ec.visibility_of_element_located((By.XPATH, accept_path)))
    sleep(1)
    pressButton.click()
