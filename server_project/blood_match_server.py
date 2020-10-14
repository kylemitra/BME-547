import requests


server = "http://vcm-7631.vm.duke.edu:5002"

net_id = 'km423'
r = requests.get(server+'/get_patients/{}'.format(net_id))
print(r.json())
output = r.json()
donor = output['Donor']
recipient = output['Recipient']

donor_type = requests.get(server+'/get_blood_type/{}'.format(donor))

recipient_type = requests.get(server+'/get_blood_type/{}'.format(recipient))

if donor_type == recipient_type:
    ans = 'Yes'
else:
    ans = 'No'
match_check = {"Name": net_id, "Match": ans}
r = requests.post(server+'/match_check', json=match_check)
print(r)
