# integration-reactjs-django
básic integraction with reactjs and the python framework called django

This project has hot-reload desactived because have dependencies problems with 
the version of React "15.4.1" that do not have ReactMount anymore and react-hot-loader": "1.3.1" still needed it

Obs.: Accepting Pull requests.

# Instaling

## Python Dependencies
Obs.: Go outside project folder and create a virtualenv to python dependencies (just 1 lvl outside)
```bash
sudo apt-get install virtualenv
virtualenv vm
source vm/bin/activate

cd integration-reactjs-django
pip install -r requirements.txt
```

## Javascript Dependencies
```bash
npm install
```

## Run node server (localhost:3000)
```bash
node server.js
```

## Run Django server (localhost:8000)
```bash
python manage.py migrate (creating sqlite3 database)
python manage.py runserver
```