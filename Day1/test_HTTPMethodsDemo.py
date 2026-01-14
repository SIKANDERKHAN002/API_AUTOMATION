import requests
import pytest

HEADERS = {"Content-Type":"application/json","x-api-key":"reqres-free-v1"}

def test_get_users():
    res = requests.get("https://reqres.in/api/users?page=3",headers=HEADERS)
    print("\n")
    print(f"Response Code ==> \t {res.status_code}")
    print(res.json())
    print(type(res.json()))
    print("---------------------")
    print(res.text)
    print(type(res.text))
    print("#####################")
    print(res.content)
    print(type(res.content))
    
    
    assert  res.status_code == 200,   "Response Code Not Valid"
    assert  res.elapsed.total_seconds < 2, "Too slow"
    
    data = res.json()
      
  
