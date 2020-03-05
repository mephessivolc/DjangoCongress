# README #

Inicialmente foi feito o repositório para a aplicação de controladoria do evento SEFIM - Semana de Estudos de Física e Matemática da UEMASUL.
Evento que ocorre no segundo semestre de cada ano, normalmente no fim de outubro, e que visa promover as discussões em torno da pesquisa e prática
docente.

Com a evolução do projeto, objetivou construir uma aplicação para ser utilizada em outros eventos cientificos da universidade quanto para outras
instituições.

Sinta-se a vontade para melhorar o projeto, ou usá-lo. Lembre-se Grandes poderes, vem com grandes responsabilidades (Ben, Tio. 2001).

## Instalação ##

*obs:* é necessário instalar o latex

sudo apt install texlive-full lmodern

Copie o git do projeto:

git clone https://ccaface@bitbucket.org/ccaface/sefim.git

Instale as bibliotecas do projeto:

pip install -r requirements

Crie o ambiente de trabalho e acione.
Crie as Migrações e Construa Banco de Dados:

./manage.py makemigrate

./manage.py migrate

Defina o superusuário:

./manage.py createsuperuser

Colete os arquivos estáticos necessários:

./manage.py collectstatic

(digite 'yes' se necessário)

### Para pip com novas bibliotecas ###

Para atualizar o requirements pelo pip utilizar e resolvendo o problema de
*pkg-resources==0.0.0*:

pip freeze | grep -v "pkg-resources" > requirements.txt

## Links Uteis ##

[latex](https://milq.github.io/install-latex-ubuntu-debian/)

[python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)
