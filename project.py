#Motivation by Quotes

#Neseccary libraries
import time
from bs4 import BeautifulSoup
import requests
import random

#Contians loop code
def main():
    print("_-"*40 + "Need Motivation" + "_-"*40)
    option=True
    while(option == True):
        process()
        o = input("Keep Going? (Y/N): ")
        match o:
            case 'Y':
                option=True
            case 'N':
                option=False

#For selection of options by user preferences.
def process():
    time.sleep(1)
    print("\nChoose from below:\ta)Inspirational\t\tb)Love\t\tc)Life\t\td)Friends\t\te)Random\n")
    time.sleep(2)
    ans = input("Option: ")
    if ans == 'a':
        print(inspiration())
    elif ans == 'b':
        print(love())
    elif ans == 'c':
        print(life())
    elif ans == 'd':
        print(friends())
    else:
        print(all())

#For inspirational quotes
def inspiration():
    url = 'https://quotes.toscrape.com/tag/inspirational/'
    t = scrapping_website(url)
    return t

#For love quotes
def love():
    url = 'https://quotes.toscrape.com/tag/love/'
    t = scrapping_website(url)
    return t

#For quotes on life
def life():
    url = 'https://quotes.toscrape.com/tag/life/'
    t = scrapping_website(url)
    return t

#For quotes on friends and friendships
def friends():
    URL = ['https://quotes.toscrape.com/tag/friends/','https://quotes.toscrape.com/tag/friendship/']
    url=random.choice(URL)
    t = scrapping_website(url)
    return t

#For random quotes without preference aside from options
def all():
    URL = ['https://quotes.toscrape.com/','https://quotes.toscrape.com/tag/humor/','https://quotes.toscrape.com/tag/books/','https://quotes.toscrape.com/tag/reading/','https://quotes.toscrape.com/tag/truth/','https://quotes.toscrape.com/tag/simile/']
    url=random.choice(URL)
    t = scrapping_website(url)
    return t

#Scrapping the website procedure
def scrapping_website(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    inspire = soup.find_all('div',class_='quote')
    d={}                                            #Dictionary
    for i in inspire:
        d[i.find("small",class_='author').text] = i.find("span",class_='text').text
    l = list(d.keys())                             #List
    ch = random.choice(l)                          #To choose a random quote
    return "\n" + d[ch] + "\n- by " + ch + "\n"

#Calling main function
if __name__ == "__main__":
    main()

