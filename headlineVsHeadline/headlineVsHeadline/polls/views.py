from django.shortcuts import render
from django.http import HttpResponse
import sys
import sys
sys.path.append("/usr/src/app/") # NOTE: Replace this with the path to the root of this repo.
from newsSources import *
from citations import cite
#from models import HeadlineListing

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