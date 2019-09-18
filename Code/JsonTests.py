import json
jsonData = '{"name": "Frank", "age": 39}'
py = json.loads(jsonData)
print py['name']
