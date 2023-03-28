import time
import requests
import json
print("Request data from server")
url='http://kodr.anhive.net/get_data.php'
try:
     while True:
          r = requests.get(url)
          rt = json.loads(r.text)
          temp = float(rt['data']['temperature'])
          humidity = float(rt['data']['humidity'])
          print("Temperature: %.2fC" %temp)
          print("Humidity: %.2f%%RH" %humidity)
          time.sleep(5)
except KeyboardInterrupt:
     pass
