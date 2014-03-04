#!/usr/bin/python
'''
Created on Nov 17, 2013

@author: leoreyes
'''
from google import search

if __name__ == '__main__':
    inputFileName = raw_input("Enter name of input file: ")
    writeFileName = raw_input("Enter name of output file: ")
    writeFile = open(writeFileName, "a")
    with open(inputFileName) as file:
        for line in file:
          searchKeyWord = line
          numTemp=1
          stopTemp=1
          url = search(searchKeyWord,num=numTemp,stop=stopTemp,pause=2.0)
          writeFile.write(url)
          writeFile.write("\n")
          print(url)
    file.close()
    
    pass