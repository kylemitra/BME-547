import requests


server = "http://127.0.0.1:5000"

out_data = {"date": "10/10/1999", "units": "years"}
r = requests.post(server+"/age", json=out_data)
print(r.status_code)
print(r.text)
answer = r.json()
print(type(answer))
print(answer)
