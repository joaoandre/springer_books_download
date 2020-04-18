import os

import requests
import pandas as pd
from urllib.parse import urlparse

invalid_chars = '< > : " / \ | ? *'.split()

session = requests.Session()
df = pd.read_csv("books.csv")

for i, book in df.iterrows():
    file_name = f'{book["English Package Name"]}/'
    directory = book["English Package Name"]

    for c in book['Book Title']:
        file_name += '_' if c in invalid_chars else c

    file_name += '.pdf'

    if os.path.isfile(file_name):
        print(f'Ignoring {file_name}. Book already downloaded')
        continue

    if not os.path.exists(directory):
        os.makedirs(directory)

    urlObject = urlparse(book['DOI URL'])
    url = f"https://link.springer.com/content/pdf{urlObject.path}.pdf"
    print(f"Downloading {book['Book Title']} by {book['Author']} on URL {url}")
    print("-------------------------------------------------------------------")
    f = requests.get(url)

    open(file_name, "wb").write(f.content)
