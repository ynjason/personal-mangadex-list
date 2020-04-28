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
    try:
        x = float(x)
    except ValueError: # empty string for oneshot
        x = 0
    return x

def zpad(num):
    if "." in num:
        parts = num.split('.')
        return "{}.{}".format(parts[0].zfill(3), parts[1])
    else:
        return num.zfill(3)

def download_specific_manga(manga_id, new_chapters, lang_code="gb", tld="org"):
    # grab manga info json from api
    scraper = cloudscraper.create_scraper()
    try:
        r = scraper.get("https://mangadex.{}/api/manga/{}/".format(tld, manga_id))
        manga = json.loads(r.text)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        return

    try:
        title = manga["manga"]["title"]
    except:
        print("Please enter a MangaDex manga (not chapter) URL.")
        return
    # print("\nTitle: {}".format(html.unescape(title)))

    # check available chapters
    chapters = []

    if "chapter" in manga:
        print("Chapter found in language you requested")
    else:
        print("Chapter not found in the language you requested.")
        return

    for chap in manga["chapter"]:
        if manga["chapter"][str(chap)]["lang_code"] == lang_code:
            chapters.append(manga["chapter"][str(chap)]["chapter"])
    chapters.sort(key=float_conversion) # sort numerically by chapter #

    chapters_revised = ["Oneshot" if x == "" else x for x in chapters]

    # find out which are availble to dl
    chaps_to_dl = []
    for chapter_id in manga["chapter"]:
        try:
            chapter_num = str(float(manga["chapter"][str(chapter_id)]["chapter"])).replace(".0","")
        except:
            chapter_num = ''
            pass # Oneshot
        chapter_group = manga["chapter"][chapter_id]["group_name"]
        if chapter_num in new_chapters and manga["chapter"][chapter_id]["lang_code"] == lang_code:
            if chapter_num != '':
                chaps_to_dl.append((str(chapter_num), chapter_id, chapter_group))
            else:
                chaps_to_dl.append((str(0), chapter_id, chapter_group))
    chaps_to_dl.sort(key=lambda x: float(x[0]))

    if len(chaps_to_dl) == 0:
        print("No chapters available to download!")
        return

    # get chapter(s) json
    print()
    for chapter_id in chaps_to_dl:
        # if chapter_id[0] == str(0):
        #     continue
        print("dsafsd")
        print("Downloading chapter {}...".format(chapter_id[0]))
        try:
            r = scraper.get("https://mangadex.{}/api/chapter/{}/".format(tld, chapter_id[1]))
            print(chapter_id[1])
            print(r)
            chapter = json.loads(r.text)
        except (json.decoder.JSONDecodeError, ValueError) as err:
            print("CloudFlare error: {}".format(err))
            chaps_to_dl.append(chapter_id)
            continue

        # get url list
        images = []
        server = chapter["server"]
        if "mangadex.{}".format(tld) not in server:
            server = "https://mangadex.{}{}".format(tld, server)
        hashcode = chapter["hash"]
        for page in chapter["page_array"]:
            images.append("{}{}/{}".format(server, hashcode, page))
        # print(images)
        # download images
        groupname = chapter_id[2].replace("/","-")
        for url in images:
            filename = os.path.basename(url)
            dest_folder = os.path.join(os.getcwd(), "download", title, "c{} [{}]".format(zpad(chapter_id[0]), groupname))
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            dest_filename = pad_filename(filename)
            outfile = os.path.join(dest_folder, dest_filename)
            # print(url)
            r = scraper.get(url)
            if r.status_code == 200:
                with open(outfile, 'wb') as f:
                    f.write(r.content)
            else:
                print("failed")
                print("Encountered Error {} when downloading.".format(r.status_code))
                images.append(url)

            print(" Downloaded page {}.".format(re.sub("\\D", "", filename)))
            time.sleep(1)

    print("Done!")


# if __name__ == "__main__":
#     print("mangadex-dl v{}".format(A_VERSION))

#     if len(sys.argv) > 1:
#         lang_code = sys.argv[1]
#     else:
#         lang_code = "gb"

#     url = ""
#     while url == "":
#         url = input("Enter manga URL: ").strip()
#     try:
#         manga_id = re.search("[0-9]+", url).group(0)
#         split_url = url.split("/")
#         for segment in split_url:
#             if "mangadex" in segment:
#                 url = segment.split('.')
#         dl(manga_id, lang_code, url[1])
#     except:
#         print("Error with URL.")