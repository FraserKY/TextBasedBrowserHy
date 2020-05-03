
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

URL = ''
URL_http = ''

list1 = []
cur_page = []

history = []

args = sys.argv
tabs_directory = args[1]
path1 = '/Users/fraserkearsey/PycharmProjects/Text-Based Browser/Text-Based Browser/task/' + tabs_directory

# See if directory exists, if not create the directory
if not os.path.exists(path1):
    os.makedirs(path1)
    # print('Directory: ', tabs_directory, 'Created')

#
# else:
    # print('Directory: ', tabs_directory, 'Already Exists')

while URL != 'exit':

    URL = input()

    # check if web page has already been stored/ check it is valid by seeing if there is a dot
    if '.' not in URL and URL != 'back' and URL != 'exit':
        # if input -'.com' is saved in file, print the contents of the file
        if os.path.isfile(path1 + '/' + URL + '.txt'):
            with open(path1 + '/' + URL + '.txt', 'r') as file:
                print(file.read())
                history.append(URL)

        else:
            print('Error: Invalid Input1')

    if URL == 'back':
        if len(history) > 0:
            history.pop()
            path = os.path.join('/Users/fraserkearsey/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs',
                                history.pop()) + '.txt'
            with open(path, 'r') as fl:
                print(fl.read())

    if '.' in URL:
        # Add 'https://' if not already in URL
        if "https://" not in URL:
            URL_http = "http://" + URL

        # Get data from website
        r = requests.get(URL_http)

        list1 = r.text.split('\n')

        for x in range(len(list1)):
            # Convert html string to readable format
            soup = BeautifulSoup(list1[x], 'html.parser')

            # Check to see if current string contains a link
            if '<a' in list1[x]:
                print(Fore.BLUE + str(soup.get_text()))
            else:
                print(str(soup.get_text()))

            cur_page.append(str(soup.get_text()))

        history.append(URL.rstrip('.com'))

        # Save output in a file to be opened later
        New_File = URL.rstrip('.com')
        New_File_Name = New_File + '.txt'
        path = os.path.join('/Users/fraserkearsey/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/',
                            New_File_Name)
        with open(path, 'w', encoding='UTF-8') as fp:
            fp.write("\n".join(cur_page))

