from datetime import date, datetime, timezone
# Firebase imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pytz

cred = credentials.Certificate("/usr/src/app/headline-vs-headline-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

def cite(headline, source, link, HTMLclass, author=""):
    """
    Return a MLA-ish citation for a given headline in HTML. Adds citation along with headline info to firestore. Delets old headline from that source.
    """
    dateAccessed = datetime.now()
    citation = ""
    
    if author == "":
        # HTML formated citation, if there is no author.
        citation = f'<p class="citation">"{headline}" <em>{source},</em>\n\t{link}. Accessed {dateAccessed}</p>'
    
    else:
        # HTML formated citation, if there is an author.
        firstAndLastName = author.split()
        formatedName = firstAndLastName[1] + ", " + firstAndLastName[0]
        citation = f'<p class="citation">{formatedName}. "{headline}" <em>{source},</em><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{link}">{link}</a>. Accessed {dateAccessed}</p>'

    dbAllreadyInit = addToDb(headline, source, link, author, citation, dateAccessed, HTMLclass)
    return citation

def addToDb(headline, source, link, author, citation, dateAccessed, HTMLclass):
    """
        Add a headline listing to the database, and provide it's citation. This will later be acsessed by the web server.
    """
        
    db = firestore.client()
    doc_ref = db.collection(u'headlines').document(source)
    doc_ref.set({
        u'text': headline,
        u'link': link,
        u'timedate': dateAccessed,
        u'author': author,
        u'citation': citation,
        u'source': source,
        u'HTMLclass': HTMLclass
    })

    return True

def shouldReloadNewsSource(source):
    #return True # uncomment this line to force a DB update.
    """
        Tests to see if the last update from a given sources
        was more than TIME minuets ago. If so, return True, if not, False.
    """

    TIME = 15 # NOTE: Make this longer if you only want to check every 60 minuets, for example.

    db = firestore.client()
    doc_ref = db.collection(u'headlines').document(source)
    headline = doc_ref.get()

    if not headline.exists:
        print(u'No such document!')
        exit(3)

    headlineDict = headline.to_dict()
    now = datetime.now(pytz.timezone("US/Eastern"))
    timeDif = (now - headlineDict['timedate'])
    print(f'Minutes sense last update: {timeDif.seconds / 60}')

    return timeDif.seconds / 60 >= TIME 
    # NOTE: - 300 to deal with stupid timezones. Should hold up, but if the function breaks, I'd look here.
    # Huh... now the -300 broke it. Did firebase change? I don't remember changing my code. "Should hold up"
def getHeadlineFromDb(source):
    db = firestore.client()
    doc_ref = db.collection(u'headlines').document(source)
    headline = doc_ref.get()

    if not headline.exists:
        print(u'No such document!')
        exit(3)

    headlineDict = headline.to_dict()

    return headlineDict