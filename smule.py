#!/usr/bin/env python3

import os
import sys
import requests
from bs4 import BeautifulSoup

def parseLink(res):
    meta = {}
    soup = BeautifulSoup(res, "html.parser")
    collab_link = soup.find(attrs={"name": "twitter:player:stream"})['content']
    collab_title = soup.find(attrs={"name": "twitter:description"})['content'].replace('amp;','')
    meta["link"] = collab_link
    meta["title"] = collab_title[:collab_title.index("on Sing!")].strip().replace("/"," - ")
    return meta

def downloadMedia(meta):
    res = requests.get(meta["link"], stream=True)
    res.raise_for_status()
    filename = meta['title'] + ".mp4"
    with open(filename, "wb+") as handle:
        for block in res.iter_content(1024):
            handle.write(block)

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    downloadMedia(parseLink(r.text))