Se voce está comecando a desenvolver uma api com Django, é necessário alguns passos antes de rodar essa aplicacao.

Primeiro é preciso ter instalado em sua máquina:
python versao 3 ou superior
pip versao 3 ou superior [pip](https://pip.pypa.io)
[virtualenv](https://virtualenv.pypa.io)
execute:
virtualenv project-env
source project-env/bin/activate

execute os comandos que sao bibliotecas e o proprio framework django:
pip install django
pip install djangorestframework

rode os comandos para poder deixar a aplicacao pronta para adicionar novas tabelas no banco de dados:
certifique que esteja na raiz do projeto
/apiatendimento/apiatendimento/
atendimentoapp
db.sqlite3
manage.py
README.md

logo após isso, para garantir que a execucao será feita com a versao do python 3 e gere o banco de dados:
python3 manage.py migrate
python3 manage.py runserver

Endpoint para fazer atendimento adicionando os procedimentos do cliente
http://localhost:8000/pedido/
<img width="1280" alt="Screen Shot 2021-08-10 at 06 42 09" src="https://user-images.githubusercontent.com/30245610/128846014-080db14e-2f0b-4eb8-aa67-e40c5c076e54.png">

Endpoint para visualizacao do atendimento com o total a ser pago, comissao e items(procedimentos) solicitados

http://localhost:8000/atendimento/

<img width="1280" alt="Screen Shot 2021-08-10 at 06 42 42" src="https://user-images.githubusercontent.com/30245610/128846037-2c15944f-e4ae-4bb1-848c-12e235924949.png">
