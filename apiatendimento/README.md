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

remova o banco de dados db.sqlite3:
cd apiatendimento
rm db.sqlite3

logo após isso, para garantir que a execucao será feita com a versao do python 3:
python3 manage.py migrate
python3 manage.py runserver

fazer atendimento adicionando os procedimentos do cliente
http://localhost:8000/pedido/

visualizacao do atendimento com o total a ser pago, comissao e items(procedimentos) solicitados

http://localhost:8000/atendimento/
