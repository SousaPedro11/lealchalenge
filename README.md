# Leal Challenge
Repositório para armazenamento e exposição de resultados da tarefa.

## Como executar?
* Clonar o repositório
  ```shell script
  git clone https://github.com/SousaPedro11/lealchalenge.git
  ```
* Criar o arquivo '.env' com o seguinte conteúdo

  Nomeei DATABASE_URI ao invés de DATABASE_URL devido o Heroku definir a url sem o driver que utilizo.
  * Formato
  ```.env
  DATABASE_URI = user:pass@host:port/database
  ```
  **user**: usuário do banco de dados <br>
  **pass**: senha do banco de dados <br>
  **host**: ip ou url de acesso ao banco <br>
  **port**: porta utilizada pelo banco <br>
  **database**: nome da base de dados a ser utilizada
  * Exemplo para banco local
  ```.env
  DATABASE_URI = naoe12345:pedro@localhost:5432/lealchallenge
  ```
* Substituir o driver do banco (se necessário)
  * Troque o driver na linha <code>SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DATABASE_URI}'</code> dentro do
  arquivo [config.py](config.py).<br>
  O driver utilizado (*postgresql+psycopg2*) é para o PostgreSQL, banco que estou utilizando.
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
        ou
        ```shell script
        gunicorn run:app
        ```

## Aplicação em execução (Heroku)
    
A inda falta ser implementado as funcionalidades. Não pretendo trabalhar muito no front-end, se eu tiver
um tempo posso poersonalizar mais.
    
Link: [lealchalenge](https://lealchalenge.herokuapp.com/)
    
## Dockerizar

Ainda vou dockerizar essa aplicação, mas somente após a finalização dela.