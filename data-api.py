import requests

root = "https://ensembledata.com/apis"
endpoint = "/tt/music/info"
params = {
  "name": "fix%20you",
  "cursor": 0,
  "sorting": "0",
  "filter_by": "0",
  "token": "CSQJjrr7J6qLPzI8"
}

res = requests.get(root+endpoint, params=params)
print(res.json())

