from newsSources import *


headlines = []

# Get input
print("Possible sources:\n[0] Fox News\n[1] MSNBC\n[2] New York Times\n[̶3̶]̶ ̶O̶A̶N̶\n[4] Washington Post\n[5] All")
testNum = int(input("Which of these sources would you like to test? "))

if testNum > 5 or testNum < 0 or testNum == 3:
    print("Bad input")
    exit(1)

showCitations = input("Show citations? (y/n)    ") == "y"

# Setup is down here so that program is not so slow to launch
driver = setup()

# Append selected sources to headlines.
if testNum == 5:
    print("Getting the latest news from all sources...")
    headlines.append(foxNewsHeadline(driver))
    headlines.append(msnbcHeadline(driver))
    headlines.append(nytHeadline(driver))
    headlines.append(wpHeadLine(driver))

elif testNum == 0:
    print("Getting the latest from Fox ...")
    headlines.append(foxNewsHeadline(driver))
elif testNum == 1:
    print("Getting the latest from MSNBC ...")
    headlines.append(msnbcHeadline(driver))
elif testNum == 2:
    print("Getting the latest from The New York Times ...")
    headlines.append(nytHeadline(driver))
elif testNum == 4:
    print("Getting the latest from The Washington Post ...")
    headlines.append(wpHeadLine(driver))
else:
    print("Bad input.")

for headline in headlines:
    print(f"---\n* From {headline['source']}: {headline['text']}")
    if (showCitations):
        print(headline['citation'])

cleanUp(driver)