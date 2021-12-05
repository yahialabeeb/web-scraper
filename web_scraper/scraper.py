import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(result):
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, "html.parser")
    result = soup.find_all('a',title ="Wikipedia:Citation needed")
    return len(result)

def get_citations_needed_report(url):
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, "html.parser")
    citations_paragraph = []
    result = soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    for ci in result:
        citations_paragraph.append(ci.parent.get_text().strip())
        print(ci)
    return '\n'.join(citations_paragraph)

report = get_citations_needed_report(url)
count = get_citations_needed_count(url)

print(count)
with open("wiki_data.txt", "w") as file:
    file.write(report)
