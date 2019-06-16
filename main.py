import os
import requests
import json
import re
from lxml import html
from htmldom import htmldom


# TODO - We need to read the list from a file (could be a .txt)

anime_list = ["naruto", "black clover", "my hero academia"]

# TODO - We need to treat different seasons of an anime (ex: Naruto)
# Read a page and retrieve its content
err = False
rv = {}
for anime in anime_list:
    anime_query = anime.replace(" ", "-")
    anime_name = anime.capitalize()
    res = requests.get(f"https://www.crunchyroll.com/pt-br/{anime_query}")

    if res.ok:
        tree = html.fromstring(res.content)
        ep_holders = tree.xpath('//li[contains(@id, "showview_videos_media_")]')
        eps = []
        for ep in ep_holders:
            ep_string = ep.text_content()
            ep_string = " ".join(ep_string.split())

            # List with the episodes
            eps.append(ep_string)

        rv[anime_name] = {"last_episode": eps[0], "episodes": eps}

    else:
        print(f"Oops, bad request on {anime_name}.")
        err = True

if not err:
    with open("./animes.json", "w", encoding="utf-8") as f:
        json.dump(rv, f, ensure_ascii=False, indent=2)

