from idlelib.rpc import response_queue

from Calculator import add,sub,multiply,div
import requests

print(add(1,2))
print(sub(10,5))
print(multiply(10,5))
print(div(10,5))
print(div(10,0))


response = requests.get("https://api.github.com/users/ryan-tensen")
print(response.status_code)
print(response.json())

# Username: ryan-tensen
# Public repos: 1
# Account created: 2026-06-01T16:29:14Z

data = response.json()
print(f"Username: {data['login']}"
      f"\nPublic repos: {data['public_repos']}"
      f"\nAccount created:{data['created_at']}")


import requests
response = requests.get("https://api.github.com/users/ryan-tensen/repos")
print(response.json())
data = response.json()
for i in data:
    print(i['name'])

print(len(data))
