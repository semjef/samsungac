'''
Created on Jul 11, 2018

@author: ilya

curl -s -k -H "Content-Type: application/json" -H
"Authorization: Bearer '+this.token+'" --cert '+this.patchCert+'
--insecure -X GET https://'+this.ip+':8888/devices

curl -X PUT -d \'{"desired": '+temp+'}\' -v -k -H
"Content-Type: application/json" -H "Authorization: Bearer '+this.token+'"
--cert '+this.patchCert+' --insecure
https://'+this.ip+':8888/devices/0/temperatures/0

curl -k -H "Content-Type: application/json" -H
"Authorization: Bearer '+token+'" --cert '+patchCert+' --insecure -X PUT
-d \'{"Operation" : {\"power"\ : \"On"\}}\' https://'+ip+':8888/devices/0

url -X PUT -d \'{"modes": ["Cool"]}\' -v -k -H "Content-Type: application/json"
-H "Authorization: '+this.token+'" --cert '+this.patchCert+'
--insecure https://'+this.ip+':8888/devices/0/mode
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
# Comode_Off, Autoclean_Off, Spi_Off

URL_GET = "https://{}/devices/0"
URL_SET_MODE = "https://{}/devices/0/mode"
URL_SET_TEMP = "https://{}/devices/0/temperatures/0"


class Entity:
    def __init__(self, ip, port, cert, token):
        self.host = '{}:{}'.format(ip, port)
        self.cert = cert
        self.headers = {"Authorization": "Bearer {}".format(token),
                        "Content-Type": "application/json"}

    def get(self):
        url = URL_GET.format(self.host)
        resp = requests.get(url, headers=self.headers, verify=True,
                            cert=self.cert)
        return resp.json()

    def power(self, onoff):
        # {"Operation" : {\"power"\ : \"On"\}}
        data = {"Operation": {"power": onoff}}
        url = URL_SET_MODE.format(self.host)
        resp = requests.put(url, data=data, headers=self.headers, verify=True,
                            cert=self.cert)
        return resp.json()

    def set_mode(self, mode):
        data = {"modes": [mode]}
        url = URL_SET_MODE.format(self.host)
        resp = requests.put(url, data=data, headers=self.headers, verify=True,
                            cert=self.cert)
        return resp.json()

    def set_temp(self, temp):
        # {"desired": '26'}
        data = {"desired": temp}
        url = URL_SET_TEMP.format(self.host)
        resp = requests.put(url, data=data, headers=self.headers, verify=True,
                            cert=self.cert)
        return resp.json()
