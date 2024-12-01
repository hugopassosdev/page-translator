import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    """
    Extrai o texto de um artigo a partir de uma URL.

    Args:
        url (str): A URL da página do artigo.

    Returns:
        str: O texto extraído do artigo.
    """
    try:
        # Faz a requisição HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verifica erros na requisição

        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Identifica a tag principal do artigo
        # Altere o seletor abaixo com base na estrutura do site
        article = soup.find('article') or soup.find('div', class_='post-content')

        if article:
            # Extrai o texto do artigo
            paragraphs = article.find_all('p')
            text = "\n".join(paragraph.text for paragraph in paragraphs)
            return text.strip()
        else:
            return "Não foi possível encontrar o artigo na página."

    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a URL: {e}"

def main():
    print("=== Extrator de Texto de Artigos ===")
    url = input("Insira a URL do artigo: ").strip()
    print("\nExtraindo texto...\n")
    article_text = extract_article_text(url)
    print("Texto extraído:\n")
    print(article_text)

if __name__ == "__main__":
    main()
