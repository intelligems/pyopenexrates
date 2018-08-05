# pyopenexrates
A simple Python package that wraps https://openexchangerates.org service API.

Currently supports only latest exchange rates API endpoint.


# Usage

````python
from pyopenexrates import OpenExchangeRatesApiClient

openexchangerates = OpenExchangeRatesApiClient(api_key="<your api key>")

latest = openexchangerates.latest()

````
