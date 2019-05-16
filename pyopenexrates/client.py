"""
Simple Python package that wraps openexchangerates.org API. Supports Python 3.4 and later.
"""
from datetime import date

import requests

from .exceptions import OpenExchangesRatesApiRequestException

__author__ = 'Konstantinos Livieratos <kostas@intelligems.eu> for Intelligems Technologies'
__copyright__ = 'Copyright 2018 Intelligems Technologies OU'

API_URL = 'http://openexchangerates.org/api'
LATEST_DATA_ENDPOINT = API_URL + '/latest.json'
HISTORICAL_DATA_ENDPOINT = API_URL + '/historical/{}.json'


class OpenExchangeRatesApiClient:

    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.params.update(
            {
                'app_id': api_key
            }
        )

    def latest(self, base='USD'):
        """
        A call to openexchangerates.org retrieving latest exchange rate data. Base currency has USD as a fallback.
        """
        try:
            response = self.session.request(
                method='get',
                url=LATEST_DATA_ENDPOINT,
                params={
                    'base': base
                }
            )
            response.raise_for_status()

        except OpenExchangesRatesApiRequestException as e:
            raise OpenExchangesRatesApiRequestException(e)

        return response.json()

    def historical(self, in_date: date, base='USD'):
        """
        A call to openexchangerates.org historical endpoint.
        """
        try:
            response = self.session.request(
                method='get',
                url=HISTORICAL_DATA_ENDPOINT.format(in_date.isoformat()),
                params={
                    'base': base
                }
            )
            response.raise_for_status()
        except OpenExchangesRatesApiRequestException as e:
            raise OpenExchangesRatesApiRequestException(e)

        return response.json()
