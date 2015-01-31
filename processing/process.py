from nltk import *
import re
import sys

months = "January,February,March,April,May,June,July,August,September,\
October,November,December,Jan,Feb,Mar,Apr,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")


def main():
    if len(sys.argv) != 2:
        print("Invalid argument.")
        sys.exit()

    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("File not found.")
        sys.exit()

    for raw_line in file:
        for month in months:
            if (month in raw_line):
                tokens = word_tokenize(raw_line)
                date = find_date(tokens, month)
                evaluation = find_eval(tokens, month)
                if evaluation != -1: print(evaluation, "–", date)
                break

def find_eval(tokens, month):
    evaluation = look_around(tokens, valid_assessment, tokens.index(month))
    if evaluation == -1: return -1

    possible_num_i = tokens.index(evaluation) + 1
    if tokens[possible_num_i].isdigit():
        evaluation += " " + tokens[possible_num_i]
    return evaluation


def find_date(tokens, month):
    '''
    (list of str, month) -> str
    Takes a line of input and the found month and returns the date
    '''

    day = look_around(tokens, valid_date, tokens.index(month))

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

def look_around(tokens, checker, initial_i):
    '''
    (list of str, int, func, [bool]) -> int
    Incrementally searches around a month in tokens
    for a token that checker evaluates.
    '''

    index = initial_i

    change = 0;
    try:
        # This block checks increasingly ahead of and behind the original index
        while ((index + change < len(tokens)) or index - change >= 0):
            if ((index + change) < len(tokens) and checker(tokens[index + change])):
                    return tokens[index + change]
            
            if ((index - change) >= 0 and checker(tokens[index - change])):
                return tokens[index - change]
            change += 1

    except IndexError as e:
        print("Error:", e.errno)

    return -1;
                
def valid_date(token):
    '''
    (str) -> bool
    Checks if a token is a valid day
    '''
    pattern = re.compile("^(3[01]|[12][0-9]|[0[0-9]|[0-9])[\?]{0}((nd)|(th)|(st))?$")
    return (pattern.match(token) != None)
        
def valid_assessment(token):

    pattern = re.compile("assignment|test|essay|quiz|exercise|midterm|lab|a[0-9]")
    return (pattern.match(token.lower()) != None)

if __name__ == '__main__':
    main()
