import requests
import re

url = "https://www.revistabula.com/7073-a-lista-definitiva-dos-100-melhores-filmes-de-todos-os-tempos/"
check = []

r = requests.get(url)
html = r.text.encode('utf8')
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))

for link in search:
    if link not in check:
        check.append(link)
        print(link)