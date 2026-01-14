import pytest


@pytest.mark.dependency()
#@pytest.mark.order(1)  
def test_open_app():
    print("App Opened")
    #assert False
    

@pytest.mark.dependency(depends=['test_open_app'])  
#@pytest.mark.order(2)
def test_login():
    print("Login Successfull") 
    
    
@pytest.mark.dependency(depends=['test_login'])
#@pytest.mark.order(3)
def test_dashboard():
    print("Dashboard Loaded")

      