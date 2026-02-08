import pytest

@pytest.fixture(scope="function")
def second_work():
    print("setup is started")
    yield
    print("Running at the end")

def test_prework(pre_setup_work, second_work):
    assert "Setup the browser to find the correct values" == "Setup the browser to find the correct values"
    print("Let's see if it works")
    
def test_run_file(pre_setup_work, second_work): #the fixture will be used as the presetup and passing the fixture name will run those before this.
    assert "running the file later" == "running the file later"
    print("Hope it runs after the fixture")


    
    
#to identify the file as test file, it needs to be named as test_

