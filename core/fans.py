import requests
import os
from datetime import datetime




def get_fans():
    url = 'https://www.instagram.com/api/v1/friendships/18428658/followers/?count=12&search_surface=follow_list_page'
    headers = {
        "Cookie": r'mid=ZLPgvwAEAAGuF849x9ryANbMw2Og; ig_did=FBBD2FB9-C47E-4383-B6FE-9FAC4596100F; ig_nrcb=1; datr=tOCzZPjREu6iaobiWINtN6r5; csrftoken=5vhOhRRIw4hbuSpL7lwzLxcCv7qeyNi4; ds_user_id=60687318633; sessionid=60687318633%3AZlJ6KkHpNGq6o4%3A1%3AAYeQ5VP8PkV9lR2LBK1CfP-UafCOyjjIGqssGPqPSQ; rur="NHA\05460687318633\0541721891529:01f77af138852a069add70a012ee39494a25570732885b3dc421b1ebaa6239977d2b5192"',
        "User-Agent": r'Instagram 2019.0.0.12.117 Android'
    }
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }
    req = requests.get(url=url, headers=headers, proxies=proxies)
    if req.status_code == 200:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(base_path, 'log')
        json_res = os.path.join(log_path, 'requests'+ datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + ".json")
        with open(json_res, 'w') as f:
            f.write(req.content.decode())
    else:
        print("error")