import pytest

@pytest.fixture()
def setup():
    print("Launching the Browser Start")
    yield
    print("Closing the browser End")
    
class TestClass:
    def test_Login(self,setup):
        print("This is Login Test")
    def test_Search(self,setup):
        print("This is search test")        
