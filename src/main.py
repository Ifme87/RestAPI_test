import pytest
import requests

BASE_URL = "https://cat-fact.herokuapp.com"

# Test 1: retrieving a random cat fact

def test_get_random_cat_fact():
    #  1: Send a GET request to the random cat fact endpoint
    response = requests.get(f"{BASE_URL}/facts/random")

    #  2: Assert that the status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #  3: Assert that the response contains a valid cat fact
    data = response.json()
    assert "text" in data, "Response does not contain 'text' field"
    assert isinstance(data["text"], str), f"Expected 'text' to be a string, but got {type(data['text'])}"
    assert len(data["text"]) > 0, "The 'text' field is empty"
    assert "_id" in data, "Response does not contain '_id' field"
    assert isinstance(data["_id"], str), f"Expected '_id' to be a string, but got {type(data['_id'])}"

    print(f"Random Cat Fact: {data['text']}")


# Test 2: retrieving multiple cat facts with a limit

@pytest.mark.parametrize("amount", [20, 30, 50])
def test_get_multiple_cat_facts(amount):
    #  1: Send a GET request to the endpoint with a limit parameter
    response = requests.get(f"{BASE_URL}/facts/random", params={"amount": amount})

    #  2: Assert that the status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    #  3: Assert that the response contains the correct number of facts
    data = response.json()
    assert isinstance(data, list), f"Expected response to be a list, but got {type(data)}"
    assert len(data) == amount, f"Expected {amount} facts, but got {len(data)}"

    #  4: Validate the structure of each fact in the response
    for fact in data:
        assert "text" in fact, "Fact does not contain 'text' field"
        assert isinstance(fact["text"], str), f"Expected 'text' to be a string, but got {type(fact['text'])}"
        assert len(fact["text"]) > 0, "The 'text' field is empty"
        assert "_id" in fact, "Fact does not contain '_id' field"
        assert isinstance(fact["_id"], str), f"Expected '_id' to be a string, but got {type(fact['_id'])}"

    print(f"Received {len(data)} cat facts")

