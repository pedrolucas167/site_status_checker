# 🌐 Site Status Checker

Um script simples em Python para verificar o status HTTP de um ou mais sites, além de medir o tempo de resposta (latência) de cada um.

<img width="472" alt="image" src="https://github.com/user-attachments/assets/a3e5fcfe-996d-40d3-8d44-de29f38448b0" />



## 🚀 Funcionalidades

- Verifica o status HTTP de sites usando `requests`
- Mede o tempo de resposta (latência) de cada site
- Alerta para sites com alta latência (> 500ms)
- Pode receber sites via linha de comando ou por um arquivo `.txt`
- Ideal para monitorar rapidamente a disponibilidade e performance de páginas web

## 📦 Requisitos

- Python 3.7+
- [requests](https://pypi.org/project/requests/)

## ✅ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/site-status-checker.git
cd site-status-checker
