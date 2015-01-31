from nltk import *
import re
import sys
import urllib

months = "January,February,March,April,May,June,July,August,September,\
October,November,December,Jan,Feb,Mar,Apr,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")


def main():  
    if not (2 <= len(sys.argv) <= 3):
        print("Invalid argument.")
        sys.exit()

    d = {}
    if len(sys.argv) == 3 and sys.argv[1] == '-u':
        urllib.urlretrieve(sys.argv[2], 'tmp.txt')
    elif len(sys.argv) == 3:
        print("Invalid option.")
        sys.exit()
    
    cache = [[], [], []]
    with open('tmp.txt') as file:
        for raw_line in file:
            tokens = word_tokenize(raw_line.decode('utf-8'))
            for token in tokens:
                if (token in months):
                    date = find_date(tokens, token)
                    evaluation = find_eval(tokens, token, cache)
                    if evaluation != -1 and date != -1:
                        d[date] = evaluation
            cache.append(tokens)
            if len(cache) > 3:
                cache = cache[1:]

    if d == {}:
        print("No dates found.")

    with open("output.csv", "w") as out:
        for date, evaluation in d.items():
            print(evaluation + ": " + date)
            out.write((evaluation + "," + date + "\n"))

def find_eval(tokens, month, cache=None):
    evaluation = look_around(tokens, valid_assessment, tokens.index(month))
    if evaluation == -1: 
        if cache != None and len(cache) > 0:
            more_tokens = cache[-1] + tokens
            return find_eval(more_tokens, month, cache[:-1])
        return -1
    
    pattern = re.compile("assignment|test|essay|quiz|exercise|midterm|lab|[at][t]?[0-9]")
    matched_evaluation = pattern.match(evaluation.lower()).group()

    possible_num_i = tokens.index(evaluation) + 1
    if tokens[possible_num_i].isdigit():
        matched_evaluation += " " + tokens[possible_num_i]
    return matched_evaluation


def find_date(tokens, month):
    '''
    (list of str, month) -> str
    Takes a line of input and the found month and returns the date
    '''

    try:
        day = look_around(tokens, valid_date, tokens.index(month))
        if day == -1: return -1
    except ValueError:
        print(tokens)
        return -1

    month_abreviations = {("Jan", "January"): "01", ("Feb", "February"): "02", ("Mar", "March"): "03", ("Apr", "April"): "04", ("May"): "05", ("Jun", "June"): "06", ("Jul", "July"): "07", ("Aug", "August"): "08", ("Sep", "September"): "09", ("Oct", "October"): "0100", ("Nov", "November"): "0101", ("Dec", "December"): "0102"}

    for key in month_abreviations:
        if month in key: month_num = month_abreviations[key]

    # Cleaning up some of the values for output
    year = ("2014" if (9 < int(month_num) < 12) else "2015")
    if not day.isdigit():
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
        print("Error: " + e.errno)

    return -1;
                
def valid_date(token):
    '''
    (str) -> bool
    Checks if a token is a valid day
    '''
    pattern = re.compile("^(3[01]|[12][0-9]|[0[0-9]|[0-9])[\?]{0}((nd)|(th)|(st))?$")
    return (pattern.match(token) != None)
        
def valid_assessment(token):

    pattern = re.compile("assignment|test|essay|quiz|exercise|midterm|lab|[at][t]?[0-9]")
    return (pattern.match(token.lower()) != None)

if __name__ == '__main__':
    main()
