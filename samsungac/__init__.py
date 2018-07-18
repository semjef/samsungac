'''
Created on Jul 11, 2018

@author: ilya
'''

import requests

MODES_LIST = {
    'OPMODE': ["Auto", "Cool", "Dry", "Wind", "Heat"],
    'COMODE': {
        "Auto": [],
        "Cool": [],
        "Dry": [],
        "Wind": [],
        "Heat": []
    },
    'POWER': ["On", "Off"]
}

URL_GET = "https://{}/devices/0"
URL_GET = "https://{}/devices/0"


class Entity:
    def __init__(self, ip, port, cert, token):
        self.host = '{}:{}'.format(ip, port)
        self.cert = cert
        self.headers = {"Authorization": "Bearer {}".format(token),
                        "Content-Type": "application/json"}

    def get(self):
        url = URL_GET.format(self.host)
        resp = requests.get(url, headers=self.headers, verify=False, cert=self.cert)
        return resp.json()

    def set(self, data):
        
        return True
