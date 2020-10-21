#!/usr/bin/env python
import requests
import re
import argparse
from bs4 import BeautifulSoup

def partone():
    url = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    phonenumber = "^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
    email = "1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?"

def createparser():
    parser = argparse.ArgumentParser(description='Scrapes Website')
    parser.add_argument('web', help='Website to be scraped')
    return parser


def main():
    args = createparser().parse_args()
    print(args)
    url = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    phonenumber = r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?"
    email = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    page = requests.get(args.web)

    soup = BeautifulSoup(page.content, 'html.parser')
    print("HREFS on This page are:")
    for link in soup.find_all('a'):
        print(link.get('href'))
    print("Images on This page are:")
    for link in soup.find_all('img'):
        print(link.get('src'))
    print("URLS on This page are:")
    match_urls = re.finditer(url, page.text)
    for match in match_urls:
        print(match.group(0))
    print("Emails on This page are:")
    match_emails = re.finditer(email, page.text)
    for match in match_emails:
        print((match.group(0)))
    print("Phone Numbers on This page are:")
    phonenumber_match = re.finditer(phonenumber, page.text)
    for match in phonenumber_match:
        if match not in phonenumber_match:
            print((match.group(0)))


if __name__ == '__main__':
    main()
