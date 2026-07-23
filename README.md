# TikTrack-API
Offical TikTrack API Documentation for unoffical TikTok Backend

#### Next Release:
- User QR Code
- Risk Link Checker

## Site: https://tiktrack.einzzcookie.org/ <-- Here you can get your free/paid API key
## API: https://tiktrack.einzzcookie.org/api/


### User Info
Example Code:
```py
import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def user_info(username):
    r = requests.get(f"{BASE}/api/user/userInfo", headers=HEADERS, params={"username": username})
    return r.status_code, r.json()
 
print(user_info("einzzcookie"))
```

Example Output:
```
{
  "success": true,
  "data": {
    "secUid": "MS4wLjABAAAAsNmlHZAoKMe9uZ__0Ce4G3eEo70dr-ceUeiIsSl8Svb1fGsx2k-DP_dRRp042gW-",
    "username": "einzzcookie",
    "nickname": "EinzzCookie",
    "userId": "7276962527903777824",
    "signature": "A pawn can be everything if he pushed forward far enough",
    "createTime": "2024-11-30T11:11:32.000Z",
    "avatarLarger": "https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-avt-0068c001-no/42fc6dddf8d836da5f86bcf0ea363ba2~tplv-tiktokx-cropcenter:1080:1080.jpeg?...",
    "region": DE,
    "regionName": "Deutschland",
    "regionFlag": ":DE:",
    "language": "de",
    "isVerified": false,
    "isPrivate": false,
    "isBusiness": false,
    "isMuted": false,
    "bioLink": null,
    "isEmbedBanned": false,
    "ttSeller": false,
    "openFavorite": false,
    "followingVisibility": 2,
    "nickNameModifyTime": "2024-11-30T11:11:53.000Z",
    "followerCount": 61,
    "followingCount": 13,
    "heart": 0,
    "videoCount": 0,
    "totalVideoCount": 0,
    "hiddenVideoCount": 0,
    "friendCount": 9,
    "totalStoryCount": 1,
    "lastStoryTime": "2026-07-23T01:12:40.020Z"
  }
}
```


### User Shared
Example Code:
```py
import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def user_shared(share_url):
    r = requests.get(f"{BASE}/api/user/userShared", headers=HEADERS, params={"url": share_url})
    return r.status_code, r.json()
 
print(user_shared("https://www.tiktok.com/@tikt0kstalker?_r=1&_t=ZG-9896CAogDcf"))
```

Example Output:
```
{
  "success": true,
  "data": {
    "sharedUserSecUid": "MS4wLjABAAAAsNmlHZAoKMe9uZ__0Ce4G3eEo70dr-ceUeiIsSl8Svb1fGsx2k-DP_dRRp042gW-",
    "sharerUserSecUid": "MS4wLjABAAAALukAIEi-J7_WP9ZPZ7BQkNobobVbw3dJFJsg-2GJLKYsHE7L95lLxmbFhNfstLoy",
    "utmMedium": "android",
    "utmSource": "copy",
    "timestamp": "2026-07-18T21:08:32.000Z",
    "sharedUsername": "einzzcookie",
    "sharerUsername": "tikt0kstalker"
  }
}
```


### Video Info
Example Code:
```py
import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def video_info(video_url):
    r = requests.get(f"{BASE}/api/video/info", headers=HEADERS, params={"url": video_url})
    return r.status_code, r.json()
 
print(video_info("https://www.tiktok.com/@tikt0kstalker/video/7643799305836334368"))
```

Example Output:
```
{
  "success": true,
  "data": {
    "id": "7643799305836334368",
    "desc": "Tiktok Stalker 💅",
    "tags": "#joegoldberg, #stalker, #controlfreak, #relationshipgoals, #obsessed",
    "createTime": "2026-05-25T12:05:17.000Z",
    "location": "DE",
    "labels": [
      "Random Shoot",
      "Others"
    ],
    "video": {
      "width": 576,
      "height": 1024,
      "duration": 15,
      "cover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oU2...",
      "dynamicCover": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oQc...",
      "playUrl": "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-ve...",
      "downloadUrl": "https://webapp-no1a.tiktok.com/ddfdfea2e5aaad5b282eba4acfebeeb1/6a5e8e..."
    },
    "music": {
      "id": "7642765501039527953",
      "title": "stalk ur socials",
      "author": "s0rrow",
      "duration": 60,
      "cover": "https://p16-sign-sg.tiktokcdn.com/tos-alisg-v-2774/oIfoASmA1WDQJQtEB9F...",
      "playUrl": "https://sf16-music-sign.tiktokcdn.com/obj/tos-alisg-ve-2774/ooN5fodOQE...",
      "album": "very sorrow days"
    },
    "stats": {
      "plays": 1182,
      "likes": 41,
      "comments": 1,
      "shares": 8,
      "saves": 6
    },
    "stickers": [],
    "challenges": [
      { "id": "1621510483313829", "title": "joegoldberg", "videos": 684119 },
      { "id": "19718", "title": "stalker", "videos": 1115885 },
      { "id": "495459", "title": "controlfreak", "videos": 22032 },
      { "id": "11739", "title": "relationshipgoals", "videos": 5376722 },
      { "id": "13398", "title": "obsessed", "videos": 3892228 }
    ],
    "author": {
      "id": "7524464901264360470",
      "username": "tikt0kstalker",
      "nickname": "TTStalker",
      "secUid": "MS4wLjABAAAALukAIEi-J7_WP9ZPZ7BQkNobobVbw3dJFJsg-2GJLKYsHE7L95lLxmbFhNfstLoy",
      "avatar": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-avt-0068-euttp/1...",
      "bio": "https://tiktok.einzzcookie.org/",
      "verified": false,
      "followerCount": 39,
      "followingCount": 1,
      "heartCount": 819,
      "videoCount": 7
    }
  }
}
```


### Video Shared
Example Code:
```py
import requests
 
BASE = "https://tiktrack.einzzcookie.org"
API_KEY = "tt_####_#############################"
HEADERS = {"X-API-Key": API_KEY}
 
def video_shared(video_url):
    r = requests.get(f"{BASE}/api/video/videoShared", headers=HEADERS, params={"url": video_url})
    return r.status_code, r.json()
 
print(video_shared("https://vm.tiktok.com/ZAd8AfXpa/"))
```

Example Output:
```
{
  "success": true,
  "data": {
    "success": true,
    "videoId": "7639280088791977249",
    "username": "tikt0kstalker",
    "sharerId": "7276962527903777824",
    "sharerUsername": "einzzcookie",
    "device": "android",
    "sharedAt": "2026-06-23T17:52:45.000Z",
    "landingUrl": "https://www.tiktok.com/@tikt0kstalker/video/7639280088791977249?_d=ex...",
    "shareRegion": "DE",
    "originalUrl": "https://vm.tiktok.com/ZAd8AfXpa/"
  }
}
```
