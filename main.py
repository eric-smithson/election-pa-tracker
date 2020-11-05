# Prints the difference in vote count in PA every minute

from bs4 import BeautifulSoup
import requests
import time

def print_vote_difference():
    url = 'https://www.washingtonpost.com/elections/election-results/pennsylvania-2020/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    presidents = soup.find(id="president-preview")
    vote_counts = presidents.findAll(attrs={"class":"font-xxxxs font-xxs-ns gray-dark"})
    joe = int(vote_counts[0].contents[0].replace(',', ''))
    trump = int(vote_counts[1].contents[0].replace(',', ''))
    print("{:,}".format(trump - joe))
    return

if __name__ == '__main__':
    while True:
        print_vote_difference()
        time.sleep(60)
