import requests, threading

URL_TO_MIRROR="https://www.wienerlinien.at/ogd_realtime/monitor?rbl=90"
PATH_TO_FILE="/var/www/html/wl.paulhoeller.at/result_90.json"

def fetch_and_save():
	threading.Timer(10.0, fetch_and_save).start()
	with open(PATH_TO_FILE,"w") as result_file:
		res = requests.get(URL_TO_MIRROR)
		result_file.write(res.text)
		#print(res.text)
fetch_and_save()
