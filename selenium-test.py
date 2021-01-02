# Based on the tutorial from https://www.scrapingbee.com/blog/selenium-python/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://www.foxnews.com"

# Setting up options:
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)

def foxNewsHeadline():
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

    URL = "https://www.foxnews.com"
    driver.get(URL)
    XPATH = "//div[@class='collection collection-spotlight has-hero']/div[@class='content']/article[@class='article story-1']/div[@class='info']/header/h2/a"
    headline = driver.find_element_by_xpath(XPATH).text
    return headline


XPATH = "//article[@class='article story-1']/div[@class='info']/header/h2/a"

headline = foxNewsHeadline()
print(headline)


driver.quit()