# Leal Challenge
Repositório para armazenamento e exposição de resultados da tarefa.

## Como executar?
* Clonar o repositório
* Executar a instalação das dependências
  ```shell script
  pip install -r requirements.txt
  ```
* Executar a aplicação
    * Padrão
    ```shell script
    flask run
    ```
    * Gunicorn (standalone server)
        * script
        ```shell script
        ./startup.sh
        ```
        * comando
        ```shell script
        gunicorn --workers=5 --bind=0.0.0.0:5000 --access-logfile - --error-logfile - 'run:app'
        ```

## Aplicação em execução (Heroku)
    
A inda falta ser implementado as funcionalidades. Não pretendo trabalhar muito no front-end, se eu tiver
um tempo posso poersonalizar mais.
    
Link: [lealchalenge](https://lealchalenge.herokuapp.com/)
    
## Dockerizar

Ainda vou dockerizar essa aplicação, mas somente após a finalização dela.