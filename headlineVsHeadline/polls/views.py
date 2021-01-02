from django.shortcuts import render
from django.http import HttpResponse
import sys
import sys
sys.path.append("/usr/src/app/")
from newsSources import *

# Create your views here.
def index(request):
    headlines = []
    driver = setup()

    print("Getting the latest news from all sources...")
    fox = foxNewsHeadline(driver)
    msnbc = msnbcHeadline(driver)
    nyt = nytHeadline(driver)
    wp = wpHeadLine(driver)

    headlines.append(msnbc)
    headlines.append(nyt)
    headlines.append(wp)
    headlines.append(fox)

    return render(request, "polls/index.html", {
        "headlines": headlines,
    })

def about(request):
    return render(request, "polls/about.html")