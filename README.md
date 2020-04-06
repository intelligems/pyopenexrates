# pyopenexrates
A simple Python package that wraps https://openexchangerates.org service API.

# Repository unmaintained
As Intelligems has stopped operations since Aug19, this repository remains unmaintained. Whoever may be interested to keep it up-to-date or extend it, DM [koslib](twitter.com/koslib) to arrange project transfer.

Currently supports 
 1) latest exchange rates API endpoint
 2) historical data exchange rates API endpoint


# Usage
Install by running `pip install pyopenexrates` inside your virtualenv.

Example usage:

````python
from pyopenexrates import OpenExchangeRatesApiClient

openexchangerates = OpenExchangeRatesApiClient(api_key="<your api key>")

latest = openexchangerates.latest()

````
