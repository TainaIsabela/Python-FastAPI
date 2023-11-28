# Python-FastAPI
Este repositório é dedicado ao treinamento "Criando uma API com Python e FastAPI" da LinuxTips.
Toda a aplicação é dockerizada.

## Para executar:
### Pré-requisitos:
   - Ter o Docker instalado na sua máquina, pois toda a aplicação será subida em containers no Docker.
### Passo a Passo:
   - Clone o repositório:
   ```
   git clone https://github.com/tainaisabela/Python-FastAPI.git
   ```
   - Entre na pasta do projeto:
   ```
   cd Python-FastAPI
   ```
   - Execute o comando para construir o container da aplicação:
   ```
   docker build -f Dockerfile.dev -t pamps:latest .
   ```
   - Execute o seguinte comando para rodar toda a aplicação (Python, Postgres):
   ```
   docker compose up
   ```
   - Para acessar a documentação no Swagger da aplicação, acesse o endereço abaixo: 
   ```
   http://localhost:8000/
