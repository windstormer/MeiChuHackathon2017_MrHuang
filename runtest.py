import requests as rq

# res = rq.get('http://ostrich-beta.kaiwoo.ai/v2/organisations/260/devices/126/survey/packets?interface=2.4GHz&duration=30&output=text&verbosity=low')
res = rq.get('http://ostrich-beta.kaiwoo.ai/v2/organisations/260/devices/126/survey/wifi/probe_reqs?action=start')
print(res)