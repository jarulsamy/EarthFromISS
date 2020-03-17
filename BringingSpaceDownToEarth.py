##############################################
#                                            #
#            \\\\        \\\\                #
#            \\\\  -o-   \\\\                #
#      o0000000000000000000000000o           #
#            ||||   0     ||||               #
#           ||||   -0-   ||||                #
#                                            #
#                                            #
#          _..._                             #
#        .'     '.      _                    #
#       /    .-""-\   _/ \                   #
#    .-|   /:.   |  |   |                    #
#     |  \  |:.   /.-'-./                    #
#     | .-'-;:__.'    =/                     #
#     .'=  *=|NASA _.='                      #
#    /   _.  |    ;                          #
#   ;-.-'|    \   |                          #
#  /   | \    _\  _\                         #
#  \__/'._;.  ==' ==\                        #
#           \    \   |                       #
#           /    /   /                       #
#           /-._/-._/                        #
#           \   `\  \                        #
#            `-._/._/                        #
#                                            #
# Web Scraping program: High Resoluation     #
# Photography from the ISS Astronauts,       #
# Automatically downloaded. Bringing space,  #
# down to earth.                             #
#                                            #
# Search for more information about the      #
# photos you download:                       #
# https://eol.jsc.nasa.gov/SearchPhotos/     #
#                                            #
# Use the "NASA Photo ID Search" at the      #
# bottom of the page and enter the file name #
# the photo was saved as.                    #
#                                            #
# Astronaut ASCII Art:                       #
# https://www.asciiart.eu/space/astronauts   #
#                                            #
# Prerequisites:                             #
#   pip install requests                     #
#                                            #
# Written by:                                #
# caffeine_bos - 03/2020                     #
# jarulsamy - 03/2020 (Incremental Update)   #
##############################################
import os
import random
from pathlib import Path
from urllib.parse import urlparse

import requests


# This will setup the file to read where this script is located.
root_directory = os.path.dirname(os.path.abspath(__file__))

# Folder to store images in.
image_directory = Path(root_directory, "EarthFromISS")
if not os.path.exists(image_directory):
    os.mkdir(image_directory)

# Read all the URLs in the file
# Easy way to check if urls already exist.
# Not the best way, memory intensive.
validURLs = Path(root_directory, "ValidURLs.txt")
if os.path.isfile(validURLs):
    with open(validURLs, "r") as f:
        urls = f.readlines()
else:
    urls = []

with open(validURLs, "a") as f:
    for _ in range(20):
        # Random mission number between 10 and 62
        mission = random.randint(10, 62)
        # Random photo number between 1 and 250,000
        photonum = random.randint(1, 250000)
        # Define the format of the URL to be generated.
        URL = f"https://eol.jsc.nasa.gov/DatabaseImages/ESC/Large/ISS0{mission}/ISS0{mission}-E-{photonum}.jpg"

        response = requests.get(URL)
        # Check to see if it was a 404 error, or successful.
        URLfalse = response.status_code

        # If the text file already contains the URL that was generated, skip.
        if URL in urls:
            continue
        elif URLfalse != 404:
            # Extract the filename from the URL
            fname = os.path.basename(urlparse(URL).path)
            # Open the file to save it with the name.
            with open(Path(image_directory, fname), "wb") as img_f:
                for chunk in response.iter_content(25000000):
                    img_f.write(chunk)

            # Append the URL
            f.write(URL)
            f.write("\n")
