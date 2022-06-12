import requests
import re

def get_page_source(url: str) -> str:
    with requests.Session() as session:
        return session.get(url).content.decode('utf-8')

def get_data_blob(page_source: str) -> str:
    comment_re = re.compile("<!--(.*?)-->", flags=re.DOTALL)
    results = comment_re.findall(page_source)
    return results[-1]

def get_data(url: str) -> str:
    page_source = get_page_source(url)
    data_blob = get_data_blob(page_source)
    return data_blob