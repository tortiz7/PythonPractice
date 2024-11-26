import pytest

from application import application  # This imports all the functiones with 'application' in the beginning of the name into the test file for testing

def test_homepage():
    application.testing = True
    client = application.test_client()

    response = client.get('/dashboard')     # This is an http GET rquest to the path that takes us to the homepage of the Banking app
    print(response)
    assert response.status_code == 200    # assert tests if something is True. So if response returns "200 OK", then we know all is well and assert will not intervene - we append ".status code" to the response so we only get the status code from the response variable
    assert response != 200        # If response returns anything but "200 OK", then the script will print an AssertionError to the terminal letting us know the test failed
    assert b"Welcome" in response.data()   # This Assert tests if the byte (b) "Welcome" is in our response.data (this being all the bytesof data in the homepage file)


# we have to run this file with pytest in order to get a test report as the output when the script is run, EX pytest Mock_python_test.py