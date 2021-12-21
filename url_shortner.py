# url shortener using python
# Author: Aejaz Ayaz 12/21/21

import pyshorteners             # importing module for shortening any given URL
import validators               # importing module to validate an URL

link = input("Enter the link to be shortened: ")
if validators.url(link):                                    # this checks if the entered url is valid. 
    print(pyshorteners.Shortener().tinyurl.short(link))
else:                                                       # if you give input which is other than a valid link, it prints below.
    print("Not a valid link")


# Sample link: https://en.wikipedia.org/wiki/Wikipedia:URLShortener#What_is_the_URL_Shortener_doing?

# Is there any better way to handle the errors? If yes, then please add your code below. Thanks. 
