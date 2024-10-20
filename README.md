# RestAPI_test

Requierments:

- Python 3.11.10

Install required packages:

```
run pip install requests pytest
```
Run tests locally in CMD:
```
pytest src/main.py
```

## API Tests Description

| **Test Name**                | **Steps**                                                                                                                                                                                                                                           | **Validation Used & Reason**                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `test_get_random_cat_fact`    | **Step 1**: The test sends a `GET` request to the `/facts/random` endpoint to fetch a random cat fact. <br> **Step 2**: It checks whether the status code of the response is `200`. <br> **Step 3**: It validates that the response body contains a `text` field with a string representing the cat fact and an `_id` field that serves as the unique identifier.               | **Validation**: <br> - The **status code** `200` is validated to ensure that the API request was successful. <br> - The **presence of the `text` and `_id` fields** is validated because they are expected parts of the response. <br> - The `text` must be a non-empty string to confirm that a valid cat fact is returned. <br> **Reason**: These validations ensure the response meets the API contract. |
| `test_get_multiple_cat_facts` | **Step 1**: The test sends a `GET` request to `/facts` with the `limit` query parameter to fetch multiple cat facts. This test is parameterized to test with limits of `5`, `10`, and `15`. <br> **Step 2**: It checks whether the status code is `200`. <br> **Step 3**: It ensures that the response is a list and contains exactly the number of facts specified by the `limit`. <br> **Step 4**: The test validates that each fact in the response has the required fields (`text` and `_id`), and that `text` is a non-empty string. | **Validation**: <br> - The **status code** `200` confirms a successful API response. <br> - The **response length** matches the `limit` parameter to ensure the correct number of facts is returned. <br> - Each fact is checked for **non-empty `text` and valid `_id`** to confirm the data integrity of each fact. <br> **Reason**: These validations ensure the API behaves correctly when handling different request limits.  |
