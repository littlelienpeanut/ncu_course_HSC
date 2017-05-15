from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def get_file():

    original_url = "http://tisvcloud.freeway.gov.tw/history/TDCS/M03A/"
    print(original_url)
    bsObj = BeautifulSoup(original_url)
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            try:
                if link.attrs['href'][0] == 'T':
                    urlretrieve(original_url+link.attrs['href'], link.attrs['href'])
                    print(link.attrs['href'])
            except:
                print("FAIL\n")

def main():

    get_file()


if __name__ == '__main__':
    main()
