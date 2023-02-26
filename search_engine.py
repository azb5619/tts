#!/bin/python3

from bs4 import BeautifulSoup
import requests, re

def getContent(url):
    html = requests.get(url).text
    s = BeautifulSoup(html, 'html.parser')
    results = s.find_all('p')
    print(i, sep = '\n')


def getHTML(prompt):
    url = "+".join(prompt.split())
    return requests.get("https://www.mojeek.com/search?q="+url)

def toText(prompt):
    html = getHTML(prompt).text
    s = BeautifulSoup(html, "html.parser")
    results = s.find_all("a", class_="title")
    return [(i.contents,i.get("href")) for i in results]


if __name__ == "__main__":
    print(toText('hello'))
