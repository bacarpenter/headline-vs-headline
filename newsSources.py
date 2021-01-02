from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from citations import cite, shouldReloadNewsSource, getHeadlineFromDb

"""
NOTE: The functions in this file are purley being used 
      for academic purposeses, and are the equivalent to using a web browser to 
      vist the site yourself. If you inted to use it for other, make sure to provide 
      the given citations. I am not responsable.
"""


def setup():
    """
    Returns a webdriver object.
    """
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def cleanUp(driver):
    """
    Closes the passed in driver. 
    """
    driver.quit()


def foxNewsHeadline(driver):
    """
        Return the current headline of foxnews.com. 

        This is purley being used 
        for academic purposeses, and is the equivalent to using a web browser to 
        vist the site yourself. If you inted to use it, make sure to provide citations.

        Furthermore: 
        NOTE: I am using Fox news purley as an example. Please be informed by media bias 
        when choosing a news source. 
        Check out a chart on the topic
        here here: https://www.adfontesmedia.com/interactive-media-bias-chart-2/
    """
    if shouldReloadNewsSource("Fox News"):
        print("From Fox...  ", end="")
        headline = {}
        headline['source'] = "Fox News"

        #Load URL into the web driver
        URL = "https://www.foxnews.com"
        driver.get(URL)

        # Get headline via XPATH
        XPATH = "//div[@class='collection collection-spotlight has-hero']/div[@class='content']/article[@class='article story-1']/div[@class='info']/header/h2/a"
        URL2 = driver.find_element_by_xpath(XPATH).get_attribute("href")
        headline['text'] = driver.find_element_by_xpath(XPATH).text

        # Generate Citation (which also adddes to the database.)
        headline['citation'] = cite(headline['text'], headline['source'], URL2, HTMLclass="fox")

        # Add addtional information to                   NOTE: I did it like this so that I am
        # the headline dict                                    not re-reading from the DB, 
        #                                                      while allo the infromation is 
        #                                                      still in memory

        headline['HTMLclass'] = "fox"
        headline['link'] = URL2
        
        headline['timedate'] = datetime.now()

        print("done!")
    else:
        # If we don't need to reload the headline, then grab it from the database.
        print("From Db... ", end="")
        headline = getHeadlineFromDb("Fox News")
        # The speed here still makes me smile 🚅🚋🚋🚋🚋🚋💨
        print("Done!")
    return headline


def msnbcHeadline(driver):
    """
        Return the current headline of msnbc.com. 
    """
    print("From MSNBC...  ", end="")

    if shouldReloadNewsSource("MSNBC"):
        headline = {}
        headline['source'] = "MSNBC"
        # Load webpage
        URL = "https://www.msnbc.com"
        driver.get(URL)
        XPATH = "//h2[@class='tease-card__headline tease-card__title relative']/a"

        # Format for reutrn value
        headline['text'] = driver.find_element_by_xpath(XPATH).text

        URL2 = driver.find_element_by_xpath(XPATH).get_attribute('href')
        headline["citation"] = cite(headline['text'], headline["source"], URL2, HTMLclass="msnbc")


        print("done!")
        headline['HTMLclass'] = "msnbc"
        headline['link'] = URL2
        
        headline['timedate'] = datetime.now()

    else:
        print("From Db... ", end="")
        headline = getHeadlineFromDb("MSNBC")
        print("Done!")

    return headline


def nytHeadline(driver):
    """
        Return the current headline of nytimes.com. 
    """
    print("From NYT...  ", end="")
    if shouldReloadNewsSource("The New York Times"):
        headline = {}
        headline['source'] = "The New York Times"
        URL = "https://www.nytimes.com"
        driver.get(URL)
        XPATH = "//span[@class='balancedHeadline']"

        headline['text'] = driver.find_element_by_xpath(XPATH).text
        URL2 = driver.find_element_by_xpath(f"{XPATH}/../../..").get_attribute('href')
        headline["citation"] = cite(headline['text'], headline["source"], URL2, "nyt")

        headline['HTMLclass'] = "nyt"
        headline['link'] = URL2
        
        headline['timedate'] = datetime.now()
        print("done!")

    else:
        print("From Db... ", end="")
        headline = getHeadlineFromDb("The New York Times")
        print("Done!")

    return headline

def wpHeadLine(driver):
    """
        Return the current headline of www.washingtonpost.com. Why is this one so much 
        slower than the rest? Bad website?
    """
    if shouldReloadNewsSource("The Washington Post"):
        headline = {}
        headline['source'] = "The Washington Post"
        print("From WP...  ", end="")
        URL = "https://www.washingtonpost.com/"
        driver.get(URL)
        XPATH = "//h2[@class=' font--headline font-size-lg font-bold left relative']/a"
        headline['text'] = driver.find_element_by_xpath(XPATH).text
        URL2 = driver.find_element_by_xpath(XPATH).get_attribute('href')
        headline["citation"] = cite(headline['text'], headline["source"], URL2, "wp")

        headline['HTMLclass'] = "wp"
        headline['link'] = URL2
        
        headline['timedate'] = datetime.now()

        print("done!")
    
    else:
        print("From Db... ", end="")
        headline = getHeadlineFromDb("The Washington Post")
        print("Done!")

    return headline