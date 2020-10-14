import requests


server = "http://127.0.0.1:5000"
r = requests.get(server+"/info")
print(r.status_code)
print(r.text)

out_data = {"a": 5, "b": 10}
r = requests.post(server+"/add", json=out_data)
print(r.status_code)
print(r.text)
answer = r.json()
print(type(answer))
print(answer)
print(answer[0])

a = input('First Number:')
b = input('Second Number:')
r = requests.get(server+"/add_numbers/{}/{}".format(a, b))
answer = r.text
print(answer)