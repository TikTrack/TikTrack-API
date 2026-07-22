import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def video_shared(video_url):
    r = requests.get(f"{BASE}/api/video/videoShared", headers=HEADERS, params={"url": video_url})
    return r.status_code, r.json()
 
print(video_shared("https://vm.tiktok.com/ZAd8AfXpa/"))
