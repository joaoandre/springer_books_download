import os

import requests
import pandas as pd
from urllib.parse import urlparse


session = requests.Session()
df = pd.read_csv("books.csv")


def sanitize_name(name):
    invalid_chars = '< > : " / \ | ? *'.split()
    new_name = ""

    for c in name:
        new_name += '_' if c in invalid_chars else c
    return new_name


for i, book in df.iterrows():
    file_name = sanitize_name(book["Book Title"])
    directory = sanitize_name(book["English Package Name"])
    file_path = f"{directory}/{file_name}.pdf"

    if os.path.isfile(file_path):
        print(f'Ignoring {file_path}. Book already downloaded')
        continue

    if not os.path.exists(directory):
        os.makedirs(directory)

    urlObject = urlparse(book['DOI URL'])
    url = f"https://link.springer.com/content/pdf{urlObject.path}.pdf"
    print(f"Downloading {book['Book Title']} by {book['Author']} on URL {url}")
    print("-------------------------------------------------------------------")
    f = requests.get(url)

    open(file_name, "wb").write(f.content)
