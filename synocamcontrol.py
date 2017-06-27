#!/usr/bin/env python3

import json
import logging
import requests
import sys
import config

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

def apicall(api, payload):
    log.info('apicall '+api)
    apiURI = config.URI + "/webapi/" + APILIST["data"][api]["path"]
    log.info(apiURI)
    payload['api'] = api
    if 'SID' in globals():
        payload['_sid'] = SID
    r = requests.get(apiURI, params=payload)
    log.info(r.url)
    log.info(r.status_code)
    #log.info(r.headers['content-type'])
    #log.info(r.text)
    log.info(r.json())
    return r.json()

log.info('Moo')

payload = {'api': 'SYNO.API.Info', 'version': '1', 'query': 'ALL', 'method': 'Query'}
r = requests.get(config.URI+'/webapi/query.cgi', params=payload)
#log.info(r.url)
#log.info(r.status_code)
#log.info(r.headers['content-type'])
#log.info(r.text)
#log.info(r.json())

APILIST = r.json()

print(APILIST)

SID = apicall('SYNO.API.Auth', config.CREDENTIALS)["data"]["sid"]
log.info(SID)

payload = {'method': 'List', 'version': '8', 'basic': 'true'}
cameraList = apicall('SYNO.SurveillanceStation.Camera', payload)
log.info(cameraList)
