import json,httplib
connection = httplib.HTTPSConnection('10.8.0.1',8080)
connection.set_tunnel('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/pic.jpg', open('INTERSTELLAR.jpg', 'rb').read(), {
       "X-Parse-Application-Id": "iNUUU9wcOd9ICQbsLuIbxEuymmB8YltZERMjjAQS",
       "X-Parse-REST-API-Key": "HxFMo2YMGo9MV5Pj6ExR4U4BFJ3ZbHQ53bAAhTnk",
       "Content-Type": "image/jpeg"
     })
result = json.loads(connection.getresponse().read())
print result