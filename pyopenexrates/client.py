"""
Simple Python package that wraps openexchangerates.org API. Supports Python 3.4 and later.
"""

import requests

from .exceptions import OpenExchangesRatesApiRequestException

__author__ = 'Konstantinos Livieratos <kostas@intelligems.eu> for Intelligems Technologies'
__copyright__ = 'Copyright 2018 Intelligems Technologies OU'

API_URL = 'http://openexchangerates.org/api'
LATEST_DATA_ENDPOINT = '/latest.json'


class OpenExchangeRatesApiClient:

    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.params.update(
            {
                'app_id': api_key
            }
        )

    def latest(self, base=None):
        """
        A call to openexchangerates.org retrieving latest exchange rate data. Base currency has USD as a fallback.
        """

        base = base or 'USD'
        url = API_URL + LATEST_DATA_ENDPOINT
        try:
            response = self.session.request(
                method='get',
                url=url,
                params={
                    'base': base
                }
            )
            response.raise_for_status()

        except OpenExchangesRatesApiRequestException as e:
            raise OpenExchangesRatesApiRequestException(e)

        return response.json()
