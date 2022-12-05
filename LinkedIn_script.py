from selenium import webdriver
from selenium.webdriver import Keys
from postType import *

logfile = open(log_file_path, 'a', encoding='utf-8')
post_content = open(post_file_path, 'r', encoding='utf-8').readlines()


def post_process():
    post_test = post_content
    if post_test[0] != post_head:
        logging.exception(exception_post_border_error)
        raise Exception(exception_post_border_error)
    post_test.pop(0)
    post_number = post_test[0].split()
    if not post_number[-1].isnumeric():
        logging.exception(exception_post_number_error)
        raise Exception(exception_post_number_error)
    logging.info(log_report_valid)


def tag_name(post_input, name_to_comment):
    post_input.send_keys("@" + name_to_comment)
    sleep(1)
    post_input.send_keys(Keys.ARROW_DOWN)
    sleep(1)
    post_input.send_keys(Keys.ENTER)
    sleep(2)


def addHashTag(post_input):
    names = ["teaching and learning", "software development", "כולא_לייק", "ראובוט"]
    longHashTag = ""
    for name in names:
        hashtag = name.replace(" ", "_")
        longHashTag += ("#" + hashtag + " ")
    post_input.send_keys(longHashTag)


def clean_post():
    """
    Removes the already published post from the post list, so the file won't be too big or cause copy errors.
    """
    update_file = open(post_file_path, encoding='utf-8')
    data = update_file.read()
    data = data[data.index(post_end) + len(post_end):]
    update_file.close()
    update_file = open(post_file_path, 'w', encoding='utf-8')
    update_file.write(data)


def post_to_linkedIn():
    counter = 0
    driver = webdriver.Chrome(executable_path=webdriver_path)
    userdata = open(userdata_file_path).readlines()
    commands = {
        "0user name:": lambda: driver.find_element(By.ID, username_field).send_keys(userdata[0]),
        "1password": lambda: driver.find_element(By.ID, password_field).send_keys(userdata[1]),
        "2login button": lambda: driver.find_element(By.XPATH, login_button).click(),
        "3find typing area": lambda: driver.find_element(By.XPATH, writing_button).click(),
        "@upload": uploadToLinkedin(driver, "image", image_path),
        "@final click": lambda: driver.find_element(By.XPATH, post_button).click(),
        "closing time": lambda: driver.close()
    }
    try:
        driver.get(linkedin)
        waitList = [1, 1, 1, 2, 3, 3, 4, 4]
        for command in commands.values():
            counter += 1
            command()
            if counter == 5:
                post_input = driver.find_element(By.XPATH, posting_field)
                for line in post_content:
                    if line == post_end:
                        break
                    if not line == post_end:
                        post_input.send_keys(line)
                addHashTag(post_input)
            sleep(waitList[counter])
        logging.info(log_report_success)
        return
    except Exception as e:
        print(e)


def main():
    logging.info(log_report_start)
    clean_post()
    try:
        post_process()
        post_to_linkedIn()
        logging.info(log_report_update)
    except:
        logging.info(log_report_fail)


if __name__ == "__main__":
    main()
