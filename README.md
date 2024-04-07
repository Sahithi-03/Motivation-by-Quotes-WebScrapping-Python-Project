# Motivation by Quotes
#### Description:
This project aims to provide **Motivational Quotes** the user's choice. It provides four options which are *'Inspiration', 'Love', 'Life', 'Friends', and 'Random'*. Each choice has its function.

By selecting an option, randomly a quote is printed on the screen based on the preference. Even if any option is not selected as input the program gives the user a random quote. The program is on a loop even after printing the quote asking for the user's preference on whether to _keep going?_ or not. If the option 'Y' is given as input then it continues to ask for the preference of the user on the next quote and the same repeats until the user gives input as 'N'.

The file `project.py` contains a total of eight functions namely `main(), process()` for choosing an option and whether or not to continue the loop. The functions `inspiration()` for option *a*, `love()` for option *b*, `life()` for option *c*, `friends()` for option *d*, `all()` for option *e* and `scrapping_website(url)` which contains the procedure of scrapping the quote and the author of the quote and it returns the quote and its author to the respective caller function. A **_List_** and **_Dictionary_** were used to store the Quotes for particular preferences and passing to other functions.

The file `test_project.py` contains three functions which test `inspiration(), love(), life()` functions. As the random module is used for selecting the quote randomly, in the test file from the `unittest.mock()` library I imported the `patch()` function to mimic the random module `choice()` function which already expects the result and gives the exact result without actually doing the scrapping. For this, I accessed special help from CS50 Duck Debugger as it is a new topic to be explored.

This project was done by **_Web Scrapping_** to collect quotes from the website [Quotes to Scrape](https://quotes.toscrape.com/).
As the information is scrapped from a single website I created a single function `scrapping_website()` to scrape the quotes for different options.

By completing this project I learned quite a lot of things about different libraries like **random, time, requests, bs4**. For _time_ to delay the printing information on the screen using `time.sleep(n)` with n: the number of seconds to delay and _requests_ to get the url of the website using `requests.get(url)` with url containing the actual URL of the website, etc in code.

This was my beginner project on Web Scrapping. I learned quite a lot about Web Scrapping. I researched the tools used to scrape the information from websites using Python like **_BeautifulSoup, Selenium_,** etc. BeautifulSoup is easy to handle for a beginner to Web Scrapping with some knowledge about **_HTML_** elements. For syntax and knowledge about the tools, I used help from multiple resources.

