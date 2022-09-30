# RE-U-BOT - The LinkedIn Posting Bot
<mark> Its pronounced Reubot, like ראובן. Look it up. </mark>

> **IMPORTANT NOTE FOR THE USER**
>
>This code can cause some issues with your user experience with LinkedIn:
> 1. You might get blocked. This bot bypass the bot filteration system on linkedIn, and they don't have any clear guidelines about using THIS type of bot. So please use this code responsibly, and don't cause any damage to the network.
> 2. This is NOT the right way to use LinkedIn. This network is based on real-life connections and experiences. Make sure you use this code wisely and don't turn the network into a bot-society.

### Vision
The idea behind the creation of this bot is to help the user to focus on posting with no distractions.
Many users on LinkedIn that enter the platform to post content finds it difficult to ignore their friends posts that prompt them upon entrance, cutting out their thread of thought and leaving them to spend too much time scrolling down on posts.

This bot is here to change the way content creators engage with the platform.

### How it works?
The code has 3 layers:
1. The main python script, which uses Selenium's library to process the web browser.
2. A library of strings, so the main code would look much more pythonic.
3. The user's identification info - email and password.

### Getting started
Please follow those steps so your code will run properly:
1. Clone the repo to your pc.
2. Download and install the Chrome-Driver for your machine here: https://chromedriver.chromium.org/downloads. Then paste the full path AND file extension of the .exe driver file on to line 10 in strings.py.
3. Make sure all the files exist. There are default added files in the repository you should use. 

### The Post-Bank text file
The code needs your post-bank text file to contain three control-strings, labeled as "post_head", "post_end" and "post_content_end".
Those strings are contained in the strings.py file, you need them for your code to run properly.
If the file won't contain one of those strings - an format exception will be raised, and the code will terminate.

Every post needs to be wrapped with those strings, and at the end of the file you need to add the file closer, to make sure there are no bugs with the copying functions of the code.

The second line of every post must contain an integer, if there is no number - an counting exception will be raised and the code will terminate.

### The Posting Process

:warning: After a successful login - the current post will be REMOVED from the post-bank, so verify one of the following:

>1. You are happy with the post and once it's published you have no need of it.
>2. You have a backup of your posts. If you'll try to post again and again and again - you might find after a few trials that all your posts are gone.
>3. You are just testing - so everyone please be quiet.

<br>
:round_pushpin: As a default, to avoid inconvenience - the posting button command is deactivated by a comment at first use. To activate it simply remove the # sign and return the line to the right indentation.

### Bonus - Use the windows task scheduler to automate this code
Use this tutorial (not by me) step-by-step, if you want to automate this code: https://www.youtube.com/watch?v=x7aD2YFOMbE

## What's new?

### **Version 1.5.1**
Added a hands-on entrance example and files required to run the code. Edit for your personal use

### **Version 1.5**
In this version we added HASHTAG and NAMETAG editorial functions, just make sure you are tagging the right person, add it at the end of the post (and before the button press) and the LinkedIn members will be tagged.

### **Version 1.0**
First version of this project.
This code can run only on your personal PC (windows only), with no server application in the near future.

### Troubleshooting
##### The posting file is empty.
&nbsp;This problem occurres when you didn't created a backup file for your posts, or trying many times to post and you we're unsuccessful. Please read again about the text file format.
##### My program terminates before the post was published.
&nbsp;This problem is caused mostly due to your internet connection. Make sure your posts are backed-up, and try again later.
