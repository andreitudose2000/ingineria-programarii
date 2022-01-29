# SPAtaREST

SPAtaREST este o aplicație IoT pentru un scaun de birou inteligent.

## Instalare

Utilizati package manager-ul [pip](https://pip.pypa.io/en/stable/) pentru a instala dependințele specificate în fișierul `requriements.txt`.
```bash
pip install -r requirements.txt
```

## Utilizare

```bash
# Setări server Flask
set FLASK_ENV=development
set FLASK_APP=flask_app

# Inițializarea bazei de date SQLite
flask init-db

# Pornirea serverului
flask run --host=0.0.0.0 --port=5000
```

## Testare

S-au folosit pachetele [pytest](https://docs.pytest.org/en/6.2.x/) pentru testare și [coverage](https://coverage.readthedocs.io/en/6.3/) pentru test coverage. 
Configurația pentru *coverage* se află în fișierul `.coveragerc`, așa că trebuie să rulați doar:
```bash
coverage run
coverage report
```
