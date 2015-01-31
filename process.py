months = "January,February,March,April,May,June,July,August,September,\
October,November,December,Jan,Feb,Mar,Apr,Jun,Jul,Aug,Sep,Oct,Nov,Dec".split(",")


def text():   
    file = open("raw_data.txt", "r")

    for line in file:
        for month in months:
            if (month in line):
                print(find_date(line))

def find_date(line):
    return (line)
