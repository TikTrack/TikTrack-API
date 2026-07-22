import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def user_info(username):
    r = requests.get(f"{BASE}/api/user/userInfo", headers=HEADERS, params={"username": username})
    return r.status_code, r.json()
 
print(user_info("einzzcookie"))
