import requests
import json

url = "https://nsxapp-01a.corp.local/api/v1/fabric/virtual-machines"
headers = {
    'Content-Type': "application/json",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    }
cert=("pi-nsx-t-superuser.crt","pi-nsx-t-superuser.key")

def addnewtag_VMs(json_data,new_tag):
	for i in json_data['results']:
		a= [];
		for p in i['tags']:

			tag = {"scope": p['scope'], "tag":p['tag']}
			a.append(dict(tag))
		a.append(dict(new_tag))
		payload = {"external_id": i['external_id'],"tags": a}
		postresponse = requests.request("POST", url, cert=cert, verify=False, headers=headers, data=json.dumps(payload),  params=querystring)
		print("new tag has been added VMs")

def removealltags_VMs(json_data):
	for i in json_data['results']:
		a= [];
		payload = {"external_id": i['external_id'],"tags": a}
		postresponse = requests.request("POST", url, cert=cert, verify=False, headers=headers, data=json.dumps(payload),  params=querystring)
		print("all tags have been removed from VMs")
		
def removespecifictag_VMs(json_data,scope,tag):
	for i in json_data['results']:
		a= [];
		for p in i['tags']:
			if p['scope'] == scope and p['tag'] == tag: 
				continue
			tag = {"scope": p['scope'], "tag":p['tag']}
			a.append(dict(tag))
		a.append(dict(new_tag))
		payload = {"external_id": i['external_id'],"tags": a}
		postresponse = requests.request("POST", url, cert=cert, verify=False, headers=headers, data=json.dumps(payload),  params=querystring)
		print("new tag has been added VMs")
		
querystring = {"action":"update_tags"}
new_tag= {"scope": "windows", "tag": "hello"}
getresponse = requests.request("GET", url, cert=cert, verify=False)
json_data = json.loads(getresponse.text)

#removealltags_VMs(json_data)
#addnewtag_VMs(json_data,new_tag)
#removespecifictag_VMs(json_data,scope,tag)