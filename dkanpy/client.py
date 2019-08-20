import requests


class Client:

    def __init__(self):
        self.url = 'https://offenedaten-koeln.de/'
        self.access = self._access()

    @staticmethod
    def _access():
        response = requests.get('https://offenedaten-koeln.de/api/3/action/site_read')
        return response.json()['success']

