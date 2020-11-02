from requests import get
import argparse
from PIL import Image
from io import BytesIO


def arg_creator():
    arg_parser = argparse.ArgumentParser(description="Name of the manga")
    arg_parser.add_argument(
        "-n", type=str, help="Specify the name of the desire manga")
    return arg_parser.parse_args()


# /manga/page/[pagenumber]
Manga_Update_Url = "https://mangamint.kaedenoki.net/api/manga/page/"

# /manga/popular/[pageNumber]
Popular_Manga_Url = "https://mangamint.kaedenoki.net/api/manga/popular/"

# /manga/detail/[ Manga Name ]
Detail_Manga_Url = "https://mangamint.kaedenoki.net/api/manga/detail/"

# /chapter/[chapterEndpoint]
Chapter_finder = "https://mangamint.kaedenoki.net/api/chapter/"

manga_name = arg_creator().n

data = get(f"{Detail_Manga_Url}{manga_name}").json()
chapter_title = data["chapter"][0]["chapter_title"]
chapter_Url = data["chapter"][0]["chapter_endpoint"]


if "270" in chapter_title:
    def get_manga_images():
        manga_images_url = f"{Chapter_finder}{manga_name}-{chapter_title.split()[0].lower()}-270"
        manga_images_data = get(manga_images_url).json()
        return get(manga_images_data["chapter_image"][1]["chapter_image_link"])

    manga_image = Image.open(BytesIO(get_manga_images().content))
else:
    print("no new chapters today")
