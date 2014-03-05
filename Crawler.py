import google
import re
from bs4 import BeautifulSoup


def findContactPage(url):
    html = google.get_page(url)
    soup = BeautifulSoup(html)
    contactStr = soup.find_all('a', href=re.compile(".*?contact", re.IGNORECASE))
    return contactStr


if __name__ == "__main__":
    url = "http://www.wrangler.com/"
    contactStr = findContactPage(url)
    if(len(contactStr) > 0):
        contactPage = google.get_page(contactStr[0].get("href"))
        print contactStr[0].get("href")#.find_parents("a")
        soup = BeautifulSoup(contactPage)
        emailStr = soup.find_all(text=re.compile("[\w\.-]+@[\w\.-]+"))
        if(len(emailStr) > 0) :
            print addressStr
        else:
            print "could not find email"
    else:
        print "could not find contacts page"