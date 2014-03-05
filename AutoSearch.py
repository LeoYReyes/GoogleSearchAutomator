#!/usr/bin/python
'''
Created on Nov 17, 2013

@author: leoreyes
'''
from google import search
from Crawler import findContactPage

if __name__ == '__main__':
    inputFileName = raw_input("Enter name of input file: ")
    writeFileName = raw_input("Enter name of output file: ")
    writeFile = open(writeFileName, "a")
    with open(inputFileName) as file:
        for line in file:
            searchKeyWord = line
            numTemp=1
            stopTemp=1
            url = search(searchKeyWord,num=numTemp,stop=stopTemp,pause=5.0)
            writeFile.write(url)
            #writeFile.write("\n")
            contactStr = findContactPage(url)
            print contactStr
        if(len(contactStr) > 0):
            contactPage = google.get_page(contactStr[0].get("href"))
            print contactStr[0].get("href")#.find_parents("a")
            soup = BeautifulSoup(contactPage)
            emailStr = soup.find_all(text=re.compile("[\w\.-]+@[\w\.-]+"))
            if(len(emailStr) > 0) :
                writeFile.write("\t" + emailStr + "\n")
                print emailStr
            else:
                print "could not find email"
        else:
            writeFile.write("\n")
            print "could not find contacts page"
    file.close()
    
    pass