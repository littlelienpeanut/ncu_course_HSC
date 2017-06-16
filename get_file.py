from urllib.request import urlretrieve
from datetime import datetime, date, timedelta

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def get_file(input):
    #M03A_20161008.tar.gz
    #http://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_20170312.tar.gz
    #http://tisvcloud.freeway.gov.tw/history/TDCS/M03A/M03A_20160101.tar.gz
    original_url = "http://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_"
    url = original_url + input + ".tar.gz"
    file_name = input + ".tar.gz"
    urlretrieve(url, file_name)

def main():

    #get_file()
    begin = date(2016, 5, 1)
    end = date(2016, 11, 1)
    delta = end - begin

    for i in range(delta.days + 1):
        day = str(begin + timedelta(days=i))
        day = day.replace("-","")
        get_file(day)
        print(day)


if __name__ == '__main__':
    main()
