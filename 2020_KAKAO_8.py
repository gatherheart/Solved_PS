import time
import requests
start_time = time.time()
resp = requests.get('https://www.naver.com')

print(resp)
print("--- %s seconds ---" % (time.time() - start_time))
