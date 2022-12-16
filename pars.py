import requests
from bs4 import BeautifulSoup as BS

for p in range(1, 2):
    result_list = []
    r = requests.get(f'https://dom.ria.com/uk/arenda-kvartir/kiev?page={p}')
    html = BS(r.content, 'html.parser')
    prise = html.find_all("b", class_="size18")
      
    for el in prise:
        result_list.append(el.text)

print(result_list)
