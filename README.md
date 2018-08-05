# pyopenexrates
A simple Python package that wraps https://openexchangerates.org service API.

Currently supports only latest exchange rates API endpoint.


# Usage
Install by running `pip install pyopenexrates` inside your virtualenv.

Example usage:

````python
from pyopenexrates import OpenExchangeRatesApiClient

openexchangerates = OpenExchangeRatesApiClient(api_key="<your api key>")

latest = openexchangerates.latest()

````
