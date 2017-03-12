### Historical Stock Market Data

This is a Python script that grabs a current list of all NASDAQ tickers and retrieves daily stock prices from Yahoo! Finance.

##### Install requirements.
Execute the following commands:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Pull stock data.

Execute the primary script, `python tickers.py`, with the following arguments:

```bash
$ python tickers.py 				# default = 1980
$ python tickers.py 1980
$ python tickers.py 2015
$ python tickers.py 2015 2015.json 	# default = "result.json"
```

Any result is saved into the `data/` folder given either the default name or the assigned name with the command line argument.

##### When you're done...
Execute the `deactivate` command to turn off your virtual environment.

##### By Jay Ravaliya
