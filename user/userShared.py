import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def user_shared(share_url):
    r = requests.get(f"{BASE}/api/user/userShared", headers=HEADERS, params={"url": share_url})
    return r.status_code, r.json()
 
print(user_shared("https://www.tiktok.com/@tikt0kstalker?_r=1&_t=ZG-9896CAogDcf"))
