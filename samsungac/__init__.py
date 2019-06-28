'''
Support for samsung Air Conditioner.
Tested on AR09MSPXBWKNER.

@author: semjef
'''

import requests, warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

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
# Comode_Off, Autoclean_Off, Spi_Off

URL_DEV = "https://{}/devices/0"
URL_SET_MODE = "https://{}/devices/0/mode"
URL_SET_WIND = "https://{}/devices/0/wind"
URL_SET_TEMP = "https://{}/devices/0/temperatures/0"


class Entity:
    def __init__(self, ip, port, cert, token):
        self.host = '{}:{}'.format(ip, port)
        self.cert = cert
        self.headers = {"Authorization": "Bearer {}".format(token),
                        "Content-Type": "application/json"}

    def get(self):
        url = URL_DEV.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.get(url, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp.json()

    def parse_ortions(self, options):
        data = options
        return data

    def power(self, onoff):
        # {"Operation" : {\"power"\ : \"On"\}}
        data = {"Operation": {"power": onoff}}
        url = URL_DEV.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def set_mode(self, mode):
        data = {"modes": [mode]}
        url = URL_SET_MODE.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def set_temp(self, temp):
        # {"desired": '26'}
        data = {"desired": int(temp)}
        url = URL_SET_TEMP.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def set_direction(self, direction):
        data = {"direction": direction}
        url = URL_SET_WIND.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def set_speed(self, speed):
        data = {"speedLevel": speed}
        url = URL_SET_WIND.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def wind(self, onoff):
        data = {"options": ['Comode_Nano' if onoff else 'Comode_Off']}
        url = URL_SET_MODE.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp

    def spi(self, onoff):
        data = {"options": ['Spi_On' if onoff else 'Spi_Off']}
        url = URL_SET_MODE.format(self.host)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=InsecureRequestWarning)
            resp = requests.put(url, json=data, headers=self.headers, verify=False,
                                cert=self.cert)
        return resp
