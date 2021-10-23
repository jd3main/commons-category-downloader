import pywikibot
from pywikibot import pagegenerators
import argparse
from pathlib import Path


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('category', type=str, help='''Name of the category. Prefixing "Category:" is optional.''')
    parser.add_argument('-p', '--path', type=str, default="./images", help='Output path')
    parser.add_argument('-q', '--quiet', action='store_true', help='print nothing')
    args = parser.parse_args()

    cat_name = args.category
    if not cat_name.startswith("Category:"):
        cat_name = "Category:" + cat_name

    download_path = args.path
    Path(download_path).mkdir(parents=True, exist_ok=True)

    quiet = args.quiet

    site = pywikibot.Site("commons", "commons")
    cat = pywikibot.Category(site, cat_name)
    gen = pagegenerators.CategorizedPageGenerator(cat)
    for page in gen:
        filename = page.title()[5:]
        if not quiet:
            print(filename)
        page.download(f'{download_path}/{filename}')
