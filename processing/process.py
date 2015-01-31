from nltk import *
import re

months = "January,February,March,April,May,June,July,August,September,\
October,November,December,Jan,Feb,Mar,Apr,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")


def text():   
    file = open("raw_data.txt", "r")
    
    for line in file:
        for month in months:
            if (month in line):
                print(find_date(line, month))
                break

def find_date(raw_line, month):
    tokens = word_tokenize(raw_line)
    day = look_around(tokens, valid_date)

    month_abreviations = {("Jan", "January"): "01", ("Feb", "February"): "02", ("Mar", "March"): "03", ("Apr", "April"): "04", ("May"): "05", ("Jun", "June"): "06", ("Jul", "July"): "07", ("Aug", "August"): "08", ("Sep", "September"): "09", ("Oct", "October"): "0100", ("Nov", "November"): "0101", ("Dec", "December"): "0102"}

    for key in month_abreviations:
        if month in key: month_num = month_abreviations[key]

    # Cleaning up some of the values for output
    year = ("2014" if (9 < int(month_num) < 12) else "2015")
    if not day.isnumeric():
        day = day[:-2]
    if len(day) == 1:
        day = "0" + day


    return "-".join([month_num, day, year])

def look_around(tokens, checker):
    '''
    ([str], func) -> int
    Incrementally searches around a month in tokens
    for a token that checker evaluates.
    '''
    index = -1
    for token in tokens:
        if token in months:
            index = tokens.index(token)

    change = 0;
    try:
        # This block checks increasingly ahead of and behind the original index
        while (index + change < len(tokens) or index - change > 0):
            if ((index + change) < len(tokens) and valid_date(tokens[index + change])):
                return tokens[index + change]

            if ((index - change) >= 0 and valid_date(tokens[index - change])):
                return tokens[index + change]
            change += 1

    except IndexError:
        print("Error found.")

    return -1;
                
def valid_date(date):
    '''
    (str) -> bool
    Checks if a toke  is a valid day
    '''
    reg = re.compile("^(3[01]|[12][0-9]|[0[0-9]|[0-9])[\?]{0}((nd)|(th)|(st))?$")
    return (re.match(reg, date) != None)
        
    

if __name__ == '__main__':
    text()
