import logging

post_head = "&&&&&\n"
post_end = "$$$$$\n"
post_content_end = "%%%%%"
time_format = "%m/%d/%Y | %H:%M:%S"

log_file_path = "logfile.txt"
post_file_path = "post_content.txt"
userdata_file_path = "login_data.txt"
webdriver_path = "/Users/ydidy/Documents/Coding/Web bot/chromedriver"
linkedin = "https://www.linkedin.com/"

log_report_start = "posting script STARTED at "
log_report_stop = "posting script TERMINATED at "
log_report_valid = "post was found VALID at "
log_report_update = "posts file UPDATED "
log_report_success = "posting SUCCEEDED at "
log_report_fail = "posting FAILED at "

exception_report_success = "posting SUCCEEDED at "
exception_report_fail = "posting FAILED at "
exception_post_border_error = "Post Error: invalid style format. Script terminated"
exception_post_number_error = "Post Error: invalid counting format. Script terminated"

username_field = "session_key"
password_field = "session_password"
posting_field = '//div[2]//div[1]/div[2]//div[2]/div/div/div[1]'
login_button = '//form/button[1]'
writing_button = "//*[@id = 'main']/div[1]/div/div[1]/button"
post_button = "//div[@class = 'share-box_actions']//span[@class = 'artdeco-button__text']"
image_button = "//div[2]//div[2]/div[2]//span[1]/button"
image_select = '//div[3]/div/div/div[2]/div/div/input'
image_path = "C:/image.gif"
video_button = "//div[3]//div[2]//span[2]/button"
video_select = '//div[3]//div[2]//div[1]/div/input'
video_path = "C:/image.gif"
file_complete = '//div[3]//div[2]//div[2]/div/button[2]'
logging.basicConfig(filename=log_file_path,
                    filemode='a',
                    format='%(message)s %(asctime)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

