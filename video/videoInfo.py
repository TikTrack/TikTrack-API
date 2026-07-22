import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def video_info(video_url):
    r = requests.get(f"{BASE}/api/video/info", headers=HEADERS, params={"url": video_url})
    return r.status_code, r.json()
 
print(video_info("https://www.tiktok.com/@tikt0kstalker/video/7643799305836334368"))
