import requests as rq

# res = rq.get('http://ostrich-beta.kaiwoo.ai/v2/organisations/260/devices/126/survey/packets?interface=5GHz&duration=30&output=text&verbosity=high')
res = rq.get('http://ostrich-beta.kaiwoo.ai/v2/organisations/260/devices/126/survey/wifi/probe_reqs?action=start&interface=5GHz')
# res = rq.get('http://captive.portal.my/verify?res=notyet&uamip=192.168.1.1&uamport=9486&challenge=ae270583a162abde24f6c41663faf102&called=A4-34-D9-95-11-59&mac=F4-8C-50-BA-D5-A6&ip=192.168.1.119&nasid=nas01&sessionid=59f362ed00000005&userurl=http://www.winfarm.com')
print(res)