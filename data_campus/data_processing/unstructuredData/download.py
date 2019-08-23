import requests
def download(method, url, header=None, param=None, data=None, timeout=1, maxretries=3):
    try:
        resp = requests.request(method, url, headers=header, params=param, data=data)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and maxretries>0:
            time.sleep(timeout)
            print('시도 {}'.format(maxretries))
            download(method, url, header, param, data, timeout, maxretries-1)
        else:
            print(e.response.status_code)
            print(e.response.reason)
    return resp