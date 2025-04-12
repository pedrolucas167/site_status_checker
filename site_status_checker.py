import requests
import sys
import time
from urllib.parse import urlparse
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Função para verificar status e tempo de resposta de um site
def check_site_status(url):
    try:
        # Verifica se a URL tem esquema (http:// ou https://), se não, adiciona https://
        if not urlparse(url).scheme:
            url = 'https://' + url
        
        # Começa a medir o tempo
        start_time = time.time()
        
        # Faz a requisição GET
        response = requests.get(url)
        
        # Calcula o tempo de resposta
        response_time = round((time.time() - start_time) * 1000, 2)  # em milissegundos
        
        # Verifica o status
        if response.status_code == 200:
            print(f"{Fore.GREEN}[{response.status_code}] {Style.BRIGHT}{url} está online! {Style.NORMAL}Tempo de resposta: {response_time} ms")
        else:
            print(f"{Fore.YELLOW}[{response.status_code}] {Style.BRIGHT}{url} está com problemas! {Style.NORMAL}Tempo de resposta: {response_time} ms")
        
        # Se o tempo de resposta for maior que 500ms, destaca a latência alta
        if response_time > 500:
            print(f"{Fore.RED}⚠️ Atenção: {url} tem alta latência ({response_time} ms).")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Erro ao acessar {url}: {e}")

# Função principal
def main():
    # Verifica se os argumentos foram passados via linha de comando
    if len(sys.argv) > 1:
        for url in sys.argv[1:]:
            check_site_status(url)
    # Caso tenha sido passado um arquivo com sites
    elif len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as file:
                urls = file.readlines()
                for url in urls:
                    check_site_status(url.strip())
        except FileNotFoundError:
            print(f"{Fore.RED}Arquivo {sys.argv[1]} não encontrado.")
    else:
        print(f"{Fore.RED}Uso: python site_status_checker.py <site1> <site2> ...")
        print(f"{Fore.RED}Ou: python site_status_checker.py sites.txt")

if __name__ == "__main__":
    main()
