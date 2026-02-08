# saving the fixtures in one global file
import pytest

@pytest.fixture
def pre_setup_work(scope="module"):
    print("This is conftest")
    
#scope="class" when the function is inside the class.
#scope="module" to run it once across the whole module
#scope="function" to run it once in the functions
#conftest me we can define the fixtures. global file name should always be conftest and same path in as testcases




