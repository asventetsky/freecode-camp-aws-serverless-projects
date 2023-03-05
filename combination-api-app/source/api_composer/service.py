# pylint: disable=import-error

""" Service for sending request to external resource """

import logging
import os

import requests

logging.getLogger().setLevel(logging.INFO)


def fetch_joke():
    """ Get joke from remote resource """
    response = fetch_response()
    if response.status_code != 200:
        logging.error('Non 200 status received: %s', response)
        return None

    return extract_joke(response)


def fetch_response():
    """ Get joke from remote resource """

    try:
        url = os.environ['JOKES_URL']
        timeout = os.environ['JOKES_TIMEOUT']
        return requests.get(url, headers={'Accept': 'application/json'}, timeout=timeout)
    except requests.exceptions.RequestException as error:
        logging.error('Error occurred while sending request: %s', error)
        return None


def extract_joke(response):
    """ Extract joke from response """

    try:
        return response.json()['joke']
    except requests.exceptions.JSONDecodeError as error:
        logging.error('Error on extracting the joke: %s', error)
        return None
