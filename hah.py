import requests

id = input('Whats The id ')
page = input(" page number ")
req = requests.get("https://gdbrowser.com/api/comments/"+id+"?page="+page)
jsons = req.text

f = open("output.json", "w")
f.write(jsons)
f.close()