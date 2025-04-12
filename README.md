# 🌐 Site Status Checker

Um script simples em Python para verificar o status HTTP de um ou mais sites, além de medir o tempo de resposta (latência) de cada um.

<img width="515" alt="image" src="https://github.com/user-attachments/assets/ab44c464-16f9-4e85-ade6-e11fdb7c44d5" />


## 🚀 Funcionalidades

- Verifica se um site está online (`status code 200`).
- Mede o tempo de resposta em milissegundos.
- Alerta se a latência estiver alta (acima de 500 ms).
- Aceita múltiplas URLs como argumentos de linha de comando.
- Aceita um arquivo `.txt` com uma lista de URLs.
- Gera automaticamente um arquivo `relatorio_status.txt` com os resultados da verificação (data, hora, status e tempo de resposta).


## 📦 Requisitos


- Python 3.x
- `requests`
- `colorama`

## ✅ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/site-status-checker.git
cd site-status-checker
