# pyStock
Basic stock exchange app written in python, based on the tutorial by EODHD APIs.

# Prerequisites
This app is developped in python 3.9. In newer version a virtual environment has to be created.

Clone teh repo.

```
git clone git@github.com:spuzzelsnest/pyStock.git

cd pyStock

```

## Creating a python 3.9 environment
To create the python enviroment run the following command.

```
python3.9 -m venv venv

source venv/bin/activate

```

## install modules
Modules are added in the "requirements.txt" file. To install them run the following command.

```
python3 -m pip install -r requirements.txt -U

```

## Edit the config file

Make a copy of the config-EXAMPLE.py file to config.py. You can register a free api key from the website https://eodhd.com/cp/api


```
cp config-EXAMPLE.py config.py

```

## App Content
The app content is running from the HTML files in the template folder.


# Running the APP
To run the app, run the following command.

```
python3 app.py --host 127.0.0.1 --port 5000 --debug

```

You can now visit the website through your browser on the addres http://localhost:5000

