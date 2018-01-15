from flask import Flask
import requests
import json
import urllib

urlusers="https://jsonplaceholder.typicode.com/users"
urlposts="https://jsonplaceholder.typicode.com/posts"

#Handling users list
response = urllib.urlopen(urlusers)
usersdata = json.loads(response.read())
userscount = len(usersdata)

#Handling posts

response = urllib.urlopen(urlposts)
postsdata = json.loads(response.read())
postscount = len(postsdata)

userpostcount=0
for i in range(0,userscount):
	for j in range(0,postscount):
		if(usersdata[i]["id"]==postsdata[j]["userId"]):
			userpostcount=userpostcount+1	
	print usersdata[i]["name"],userpostcount






