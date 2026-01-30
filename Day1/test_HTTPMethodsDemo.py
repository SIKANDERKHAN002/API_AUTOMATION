import requests
import pytest

HEADERS = {"Content-Type":"application/json","x-api-key":"reqres_7715095785d74641ba3e4b04a4f0b2f4"}


@pytest.mark.order(1)
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
    assert  res.elapsed.total_seconds()<2, "Too slow"
    
    data = res.json()
    assert data.get("page") == 3, "Wrong Page"
    assert "Caddy" in res.text, "Email not found"
    

@pytest.mark.dependency()
@pytest.mark.order(2)
def test_create_user():
    global user_id
    payload = {"name":"madhan3345","job":"trainer"}
    res = requests.post("https://reqres.in/api/users",json=payload,headers=HEADERS)
    assert res.status_code == 201, "Wrong status"
    print(res.headers)
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"      
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    print(data) 
    
    assert data.get("name") == "madhan3345", "Name Mismatch"
    assert data.get("job")  == "trainer", "Job Mismatch"
    assert "id" in data, "ID Missing"
    user_id  = data["id"]     
    
@pytest.mark.order(3)
@pytest.mark.dependency(depends=["test_create_user"])    
def test_update_user():
    payload = {"name":"khanBan","job":"teacher"}
    res = requests.put(f"https://reqres.in/api/users/{72}",json=payload,headers=HEADERS)
    assert res.status_code == 200, "Wrong status"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong Content Type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    assert data.get("name")  == "khanBan", "Name mismatch"
    assert data.get("job")   == "teacher", "Job mismatch"
    assert "updatedAt" in data, "Missing update info"
    print(data)
    
@pytest.mark.order(4)
@pytest.mark.dependency(depends=["test_create_user"])
def test_delete_user():
    res = requests.delete(f"https://reqres.in/api/users/72",headers=HEADERS)
    assert res.headers["Connection"] == "keep-alive", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    assert res.status_code == 204, "Wrong status"
    print("---------------")
    print(res.text)
    assert res.text == "", "Response not empty"
    print("User deleted successfully")