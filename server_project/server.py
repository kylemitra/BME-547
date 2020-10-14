import requests


server = "http://vcm-6764.vm.duke.edu:5000"

# student_data = {"name": "Kyle Mitra", "net_id": "km423", "e-mail": "km423@duke.edu"}
# r = requests.post("http://vcm-6764.vm.duke.edu:5000/student", json=student_data)
# print(r.json())

r = requests.get("http://vcm-6764.vm.duke.edu:5000/list")
print(r.json())

added_numbers = {"a": 32, "b": 23}
r = requests.post("http://vcm-6764.vm.duke.edu:5000/sum", json=added_numbers)
print(r.json())
