from nltk import *
import re

months = "January,February,March,April,May,June,July,August,September,\
October,November,December,Jan,Feb,Mar,Apr,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")

def text():   
    file = open("raw_data.txt", "r")
    
    for line in file:
        for month in months:
            if (month in line):
                find_date(line, month)

def find_date(raw_line, month):
    tokens = word_tokenize(raw_line)
    # print(tokens)
    day = look_around(tokens, valid_date)

    # print(month + "-" + day)

def look_around(tokens, checker):
    '''
    ([str], str) -> int
    Find the match to checker closest to list[i]
    '''
    index = -1
    for token in tokens:
        if token in months:
            index = months.index(token)

    change = 0;
    try:
        while (index + change < len(tokens) or index - change > 0):
            if ((index + change) < len(tokens) and valid_date(tokens[index + change])):
                return tokens[index + change]
            if ((index - change) >= 0 and valid_date(tokens[index - change])):
                return tokens[index + change]
            change += 1
    except IndexError:
        print("Error", tokens, index, change)

    return -1;
                    

def valid_date(date):
    reg = re.compile("^(3[01]|[12][0-9]|[0[0-9]|[0-9])[\?]{0}((nd)|(th)|(st))?$")
    return (re.match(reg, date) != None)
        
    

if __name__ == '__main__':
    text()
