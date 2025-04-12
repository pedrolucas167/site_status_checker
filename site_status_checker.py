import requests
import sys
import time
from urllib.parse import urlparse
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)


def salvar_relatorio(url, status, response_time):
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("relatorio_status.txt", "a") as f:
        f.write(f"{data_hora} | {url} | {status} | {response_time} ms\n")


def check_site_status(url):
    try:
        if not urlparse(url).scheme:
            url = 'https://' + url

        start_time = time.time()
        response = requests.get(url)
        response_time = round((time.time() - start_time) * 1000, 2)

        if response.status_code == 200:
            print(f"{Fore.GREEN}[{response.status_code}] {Style.BRIGHT}{url} está online! {Style.NORMAL}Tempo de resposta: {response_time} ms")
        else:
            print(f"{Fore.YELLOW}[{response.status_code}] {Style.BRIGHT}{url} está com problemas! {Style.NORMAL}Tempo de resposta: {response_time} ms")

        if response_time > 500:
            print(f"{Fore.RED}⚠️ Atenção: {url} tem alta latência ({response_time} ms).")

        salvar_relatorio(url, response.status_code, response_time)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Erro ao acessar {url}: {e}")
        salvar_relatorio(url, "Erro", "N/A")


def main():
    if len(sys.argv) > 1:
        for url in sys.argv[1:]:
            check_site_status(url)

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
