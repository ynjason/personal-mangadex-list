import cloudscraper
import time, os, sys, re, json, html

mangas = []

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

def update(category, index, manga_id, lang_code, tld="org"):
    global mangas
    # grab manga info json from api
    scraper = cloudscraper.create_scraper()
    try:
        r = scraper.get(mangas[category][index]["url"])
        manga = json.loads(r.text)
        # print(manga)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        exit(1)

    try:
        title = manga["manga"]["title"]
    except:
        print("Please enter a MangaDex manga (not chapter) URL.")
        exit(1)
    # print("\nTitle: {}".format(html.unescape(title)))

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
    to_download = []
    recent_update = mangas[category][index]['recent_update']
    mostrecent = mangas[category][index]['recent_update']
    # print(chapters_revised)
    for chapter, timestamp in chapters_revised:
        if int(timestamp) > recent_update:
            if int(timestamp) > mostrecent:
                mostrecent = int(timestamp)
            recently_updated.append(chapter)
            # print(recently_updated)
        recently_read = float(mangas[category][index]['recent_read'])
        if recently_read == 0:
            if chapter == '':
                to_download.append(chapter)
        if chapter != '':
            if recently_read < float(chapter):
                to_download.append(chapter)
        
    if manga['manga']['cover_url'].rsplit('/',1)[1] != mangas[category][index]['cover_url'].rsplit('/',1)[1]:
        mangas[category][index]['cover_url'] = mangas[category][index]['cover_url'].rsplit('/',1)[0] + '/' + manga['manga']['cover_url'].rsplit('/',1)[1]
    mangas[category][index]['recent_update'] = mostrecent
    mangas[category][index]['new_update'] = recently_updated
    with open('profile.json', 'w') as outfile:
            json.dump(mangas, outfile)
    # print(recently_updated)
    # print(to_download)
    return recently_updated, to_download




def update_all_mangas(category):
    lang_code = "gb"

    global mangas
    with open('profile.json', 'r') as infile:
        mangas = json.load(infile)

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
    
    mangacat = mangas[category]
    updated_chapters = {}
    to_download_chapters = {}
    for i, manga in enumerate(mangacat):
        try:
            updates, to_download = update(category, i, manga['title_id'], lang_code, manga['tld'])
            updated_chapters[manga['title']] = updates
            to_download_chapters[manga['title']] = to_download
        except:
            print("Error with URL.")
    print("update finished!")
    return updated_chapters, to_download_chapters


if __name__ == "__main__":
    update_all_mangas(0)
