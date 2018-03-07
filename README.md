# back meetup
Código de ejemplo para instalación de back

## Instalaciones de instalación Virtualenv
  - Asegurese de tener instalado python3
  - Cree un virtualenv con el comando : python -m venv venv
  - Active el virtualenv
    - Windows : venv\Scripts\activate
    - Mac and Ubuntu : . venv/bin/activate
  - Instale las dependencias : pip install -r requirements.txt


## Instalaciones de instalación pyenv

Para este procedimiento se presume que tiene instalado pyenv https://github.com/pyenv/pyenv
  - Instale python 3.6.4 `pyenv install 3.6.4`
  - Cree un virtualenv con el comando : `pyenv virtualenv 3.6.4 meetup_back`
  - Active el virtualenv: `pyenv activate meetup_back`
  - Instale las dependencias : `pip install -r requirements.txt`
 
 ## Correr el proyecto
 
Una vez creado el virtualenv ejectute usando `python api.py`
