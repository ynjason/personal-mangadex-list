import cloudscraper
import time, os, sys, re, json, html


def pad_filename(str):
    digits = re.compile('(\\d+)')
    pos = digits.search(str)
    if pos:
        return str[1:pos.start()] + pos.group(1).zfill(3) + str[pos.end():]
    else:
        return str

def float_conversion(x):
    y = x[0]
    try:
        y = float(y)
    except ValueError: # empty string for oneshot
        y = 0
    return y

def update(manga_id, lang_code, manga_dict, tld="org"):
    # grab manga info json from api
    scraper = cloudscraper.create_scraper()
    try:
        r = scraper.get(manga_dict["url"])
        manga = json.loads(r.text)
        print(manga)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        exit(1)

    try:
        title = manga["manga"]["title"]
    except:
        print("Please enter a MangaDex manga (not chapter) URL.")
        exit(1)
    print("\nTitle: {}".format(html.unescape(title)))

    # check available chapters
    chapters = []

    if "chapter" not in manga:
        print("Chapter not found in the language you requested.")
        exit(1)

    for chap in manga["chapter"]:
        if manga["chapter"][str(chap)]["lang_code"] == lang_code:
            chapters.append((manga["chapter"][str(chap)]["chapter"], manga["chapter"][str(chap)]["timestamp"]))
    chapters.sort(key=float_conversion) # sort numerically by chapter #

    chapters_revised = ["Oneshot" if x == "" else x for x in chapters]
    
    recently_updated = []
    recent_update = manga_dict['recent_update']
    mostrecent = 0
    print(chapters_revised)
    for chapter, timestamp in chapters_revised:
        print("here")
        if chapter == '':
            continue
        if int(timestamp) > recent_update:
            if int(timestamp) > mostrecent:
                mostrecent = int(timestamp)
            recently_updated.append(chapter)
            print(recently_updated)

    manga_dict['recent_update'] = mostrecent
    with open('profile.json', 'w') as outfile:
            json.dump(manga_dict, outfile)

    return recently_updated




def update_all_mangas(mangas):
    lang_code = "gb"

    # with open('profile.json', 'r') as infile:
    #     mangas = json.load(infile)

    # url = ""
    # while url == "":
    #     url = input("Enter new manga url or none for done: ").strip()
    #     if url == "none":
    #         break

    #     manga_id = re.search("[0-9]+", url).group(0)
    #     split_url = url.split("/")
    #     for segment in split_url:
    #         if "mangadex" in segment:
    #             url = segment.split('.')
    #     title_url = "https://mangadex.{}/api/manga/{}/".format(url[1], manga_id)
    #     new = {
    #            "title": split_url[-1],
    #            "title_id": manga_id,
    #            "url": title_url,
    #            "cover_url": 'TODO make this input during making of frontend',
    #            "recent_read": 0,
    #            "recent_update": 0,
    #            "tld": url[1]
    #           }
    #     mangas.append(new)
    #     with open('profile.json', 'w') as outfile:
    #         json.dump(mangas, outfile)
    
    updated_chapters = {}
    for manga in mangas:
        try:
            updated_chapters[manga['title']] = update(manga['title_id'], lang_code, manga, manga['tld'])
        except:
            print("Error with URL.")
    return updated_chapters


if __name__ == "__main__":
    with open('profile.json', 'r') as infile:
        mangas = json.load(infile)
    update_all_mangas(mangas[0])
