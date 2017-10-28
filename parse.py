import json


def parsejson() :	
	
	user_input = input("Filename ")

	f = open(user_input)
	input = json.load(f)
	mac_rssiMap = {}

	for i in range(len(input['observations'])):
    		mac_rssiMap[input['observations'][i]['sender_mac']] = input['observations'][i]['rssi']


	print(len(mac_rssiMap))
	return mac_rssiMap
