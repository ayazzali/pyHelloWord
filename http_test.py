# def getVkUrl(METHOD_NAME,[]PARAMETERS,ACCESS_TOKEN)
# url = 'https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN'
import requests
url = 'https://api.vk.com/method/board.getTopics?group_id=406973&preview=1&access_token=abf359efabf359efabf359ef77abac28a2aabf3abf359eff1f57b8998000f94ce511bb9'
payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get(url)
print(r.text)

# # GET with params in URL
# r = requests.get(url, params=payload)

# # POST with form-encoded data
# r = requests.post(url, data=payload)

# # POST with JSON 
# import json
# r = requests.post(url, data=json.dumps(payload))

# # Response, status etc
# r.text
# r.status_code