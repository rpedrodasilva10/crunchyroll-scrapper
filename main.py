import os
import requests
import json
import re
from lxml import html
from htmldom import htmldom


# TODO - We need to read the list from a file (could be a .txt)
# anime = 'naruto'
anime = "black-clover"

# TODO - We need to treat different seasons of an anime (ex: Naruto)
# Read a page and retrieve its content
res = requests.get(f"https://www.crunchyroll.com/pt-br/{anime}")

if res.ok:
    tree = html.fromstring(res.content)
    ep_holders = tree.xpath('//li[contains(@id, "showview_videos_media_")]')
    eps = []
    for ep in ep_holders:
        ep_string = ep.text_content()
        ep_string = " ".join(ep_string.split())
        print(ep_string)

        # List with the episodes
        eps.append(ep_string)


else:
    print("Oops, bad request.")

