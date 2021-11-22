import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, "html.parser")
result_div = soup.find("div", class_="mw-parser-output")
result = result_div.find_all("sup", class_ = "reference")
def get_citations_needed_count(result):
    return len(result)

def get_citations_needed_report(result):
    citations_paragraph = []

    for ci in result:
        citations_paragraph.append(ci.parent.text.strip())
    return '\n'.join(citations_paragraph)

report = get_citations_needed_report(result)
count = get_citations_needed_count(result)
print(type(report))
print(count)
with open("wiki_data.txt", "w") as file:
    file.write(report)
