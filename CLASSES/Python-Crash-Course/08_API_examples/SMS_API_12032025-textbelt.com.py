import requests

# this works - TJS -1203-2025 850pm
resp = requests.post('https://textbelt.com/text', {
  'phone': '2109740254',
  'message': 'Hello from Dads python program 06212005',
  'key': 'aff78de27e57501288e30b4255d3b43219eaee57gpEDSvZbIlwriJIB4W63DIwjQ',
})
print(resp.json())

