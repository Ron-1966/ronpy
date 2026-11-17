from bs4 import BeautifulSoup
import requests

# pegar o conteúdo de uma página
url = "https://www.python.org/"
resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')

# Extrair o título da página
titulo = soup.title.string
print(f"Título da página : {titulo} ")
