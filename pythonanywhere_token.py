import requests
username = 'gardenmon'
token = '46142593d03e8929032295c25e135ff80114c1df'

response = requests.get(
  'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
      username=username
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('CPU quota info:')
  print(response.content)
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))