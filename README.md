# RestAPI_test

## API Tests Description

| **Test Name**                | **Steps**                                                                                                                                                                                        |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `test_get_random_cat_fact`    | **Step 1**: The test sends a `GET` request to the `/facts/random` endpoint to fetch a random cat fact. <br> **Step 2**: It checks whether the status code of the response is `200`. <br> **Step 3**: It validates that the response body contains a `text` field with a string representing the cat fact and an `_id` field that serves as the unique identifier. |
| `test_get_multiple_cat_facts` | **Step 1**: The test sends a `GET` request to `/facts` with the `limit` query parameter to fetch multiple cat facts. This test is parameterized to test with limits of `5`, `10`, and `15`. <br> **Step 2**: It checks whether the status code is `200`. <br> **Step 3**: It ensures that the response is a list and contains exactly the number of facts specified by the `limit`. <br> **Step 4**: The test validates that each fact in the response has the required fields (`text` and `_id`), and that `text` is a non-empty string. |
