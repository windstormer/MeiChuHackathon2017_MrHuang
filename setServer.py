#!/usr/bin/env python3


import requests as rq

config = {
            "creator_id": 1,
            "publish": {
                "packet_dump": {
                    "http": {
                        "url": "140.114.77.33:9487",
                        "token": "huang_packet_dump"
                    }
                },
                "probe_reqs": {
                    "http" : {
                        "url": "140.114.77.33:9488",
                        "token": "huang_probe_reqs"
                    }
                }
            }
        }

url = 'http://ostrich-beta.kaiwoo.ai/v2/organisations/260/networks/47/settings'

resp = rq.post(url, json=config)
print(resp.text)
