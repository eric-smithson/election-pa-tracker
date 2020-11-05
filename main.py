# Prints the difference in vote count in PA every minute

from bs4 import BeautifulSoup
import requests
import time


def print_vote_difference(state_name: str, url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    presidents = soup.find(id="president-preview")
    vote_counts = presidents.findAll(attrs={"class": "font-xxxxs font-xxs-ns gray-dark"})
    joe = int(vote_counts[0].contents[0].replace(',', ''))
    trump = int(vote_counts[1].contents[0].replace(',', ''))
    lead = trump - joe
    if lead >= 0:
        leader_text = "Trump Leads"
    else:
        leader_text = "Biden Leads"
        lead = -lead
    print("{}: {} {:,}".format(state_name, leader_text, lead))
    return


if __name__ == '__main__':
    urls = {
        'Pennsylvania': 'https://www.washingtonpost.com/elections/election-results/pennsylvania-2020/',
        'Georgia': 'https://www.washingtonpost.com/elections/election-results/georgia-2020/',
        'Nevada': 'https://www.washingtonpost.com/elections/election-results/nevada-2020/',
        'Arizona': 'https://www.washingtonpost.com/elections/election-results/arizona-2020/'
    }
    while True:
        for state_name, url in urls.items():
            print_vote_difference(state_name, url)
        print()  # prints a space
        time.sleep(600)
