import requests
from flask import Flask, render_template, request, json
status = Flask(__name__)

@status.route("/")
def main() :
	return render_template("index.html")

@status.route("/func", methods = ['POST'])
def func() :
	codeforces_api_link = "http://codeforces.com/api/user.rating?handle="
	
	string_query = request.form['handle']
	
	url = codeforces_api_link + string_query
	response = requests.get(url)

	data=json.loads(response.text)

	data=data['result']

	adi={}
	
	contest=[]
	for i in data:
		j={}
		j['Contest Name']=i['contestName']
		j['Contest ID']=i['contestId']
		j['Old Rating']=i['oldRating']
		j['New Rating']=i['newRating']
		contest.append(j)

	adi['usr_contests']=contest
	adi['handle']=string_query

	adi=json.dumps(adi)
	return adi





if __name__ == "__main__" :
	status.run()