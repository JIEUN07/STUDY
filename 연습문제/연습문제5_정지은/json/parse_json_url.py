# !/urs/bin/python

import json
import urllib.request

hres = urllib.request.urlopen('http://time.jsontest.com')

data = json.loads(hres.read())

print('Unix time: {}'.format(data['milliseconds_since_epoch']))
print('Time:{}'.format(data['time']))
print('Date:{}'.format(data['date']))

# Unix time: 1636873420923
# Time:07:03:40 AM
# Date:11-14-2021