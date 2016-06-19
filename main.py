'''

api call 		http://codeforces.com/api/user.rating?handle=aditya_jain

get data in list

count number of contest

for each contest: old rating, new rating, number of submissions, succesful submissions. accuracy percentage.



'''

import sys
import requests
import json

codeforces_api_link = "http://codeforces.com/api/user.rating?handle="

if(len(sys.argv) < 2):
	print("Enter valid string")
	exit()

string_query = sys.argv[1]

url = codeforces_api_link + string_query
response = requests.get(url)

data=json.loads(response.text)

data=data['result']

no_of_contest=len(data)

print("\n\nUser Handle:" + string_query)

print("Total rated contests participated:\t" + str(no_of_contest))
print("\n")


adi={}
adi['handle']=string_query

cont=[]
for i in data:
	j={}
	j['Contest Name']=i['contestName']
	j['Contest ID']=i['contestId']
	j['Old Rating']=i['oldRating']
	j['New Rating']=i['newRating']
	cont.append(j)

adi['contests']=cont

adi=json.dumps(adi)
print(adi)

exit()