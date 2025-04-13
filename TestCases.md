# Test Cases for Network Pinger Application

This document outlines the test cases for the network pinger application, covering ping functionality, reporting features, and negative scenarios.

## Ping Tests

### Test case 1 - Scenario with 1 unreachable endpoint, min_successful_pings - 1, max_pings - 2, empty description
**Steps:**
1. Run the pinger with a config containing 1 unreachable endpoint, min_successful_pings - 1, max_pings - 2, empty description.

**Expected result:**
- Ping should be executed once.
- The 'description' field in the output for this endpoint should be empty.
- Max pings is equal to 2 in the output

**Execution result - failed on third expected result. Expected "NOT OK [0/2]", got "NOT OK [0/1]"**

---

### Test case 2 - Scenario with 1 unreachable 1 endpoint, min_successful_pings - 0, max_pings - 0
**Steps:**
1. Create a config containing one unreachable endpoint.
2. Set `min_successful_pings` to `0`.
3. Set `max_pings` to `0`.
4. Run the pinger

**Expected result:**
- The endpoint should be effectively ignored; no ping attempts should be made.

**Execution result - failed showing 'NOT OK'. Should have ignored endpoint**

---

### Test case 3 - Scenario with 1 unreachable endpoint, min_successful_pings - 0, max_pings - 1
**Steps:**
1. Create a config containing one unreachable IP endpoint.
2. Set `min_successful_pings` to `0`.
3. Set `max_pings` to `1`.
4. Run the pinger

**Expected result:**
- The status for this endpoint in the report should be 'ok' (indicating no minimum successful pings were required).

**Execution result - passed**

---

### Test case 4 - Scenario with 1 valid endpoint, min_successful_pings - 1, max_pings - 0
**Steps:**
1. Create a config containing one valid endpoint.
2. Set `min_successful_pings` to `1`.
3. Set `max_pings` to `0`.
4. Run the pinger

**Expected result:**
- The status for this endpoint in the report should NOT be 'ok' (as the minimum successful pings required cannot be met with a maximum of 0 attempts).

**Execution result - passed**

---

### Test case 5 - Scenario with 3 valid endpoints, min_successful_pings - 2, max_pings - 2
**Steps:**
1. Create a config containing three valid endpoints.
2. Set `min_successful_pings` to `2`.
3. Set `max_pings` to `2`.
4. Run the pinger
5. Print exit code after execution

**Expected result:**
- The application should exit with an exit code of 0 (success), assuming all endpoints are reachable.

**Execution result - failed. Expected to get "OK [2/2]", got "NOT OK [1/2]"**

---

### Test case 6 - Scenario with 1 valid endpoint, min_successful_pings - 2, max_pings - 3
**Steps:**
1. Create a config containing three valid endpoints.
2. Set `min_successful_pings` to `2`.
3. Set `max_pings` to `3`.
4. Run the pinger

**Expected result:**
- The application should execute ping exactly 2 times, not 3.

**Execution result - passed**

---

### Test case 7 - Scenario with 2 valid, 1 unreachable endpoints, min_successful_pings - 1, max_pings - 1
**Steps:**
1. Create a config containing two valid endpoints and one unreachable endpoint.
2. Set `min_successful_pings` to `1`.
3. Set `max_pings` to `1`.
4. Run the pinger
5. Check exit code is not zero

**Expected result:**
- The application should exit with a non-zero exit code (failure) because at least one endpoint is unreachable

**Execution result - passed**

---

### Test case 8 - Scenario with 2 valid endpoints and Ignore field true for one of them
**Steps:**
1. Create a config containing two valid endpoints.
2. For one of the endpoints, include the field `ignore: true`.
3. Run the pinger

**Expected result:**
- The output report should only contain an entry for the endpoint where `ignore` was set to `false` (or not present). The ignored endpoint should not be processed or included in the results.

**Execution result - failed. Ignored endpoint was pinged**

---

### Test case 9 - Scenario with Empty valid config
**Steps:**
1. Run the pinger providing configuration file with {}

**Expected result:**
- The application should display a user-friendly error message indicating that a configuration file is empty.

**Execution result - failed. No info that config is empty. Got - Starting availability check...**

---

### Test case 10 - Scenario with Empty endpoint list
**Steps:**
1. Create a configuration file.
2. Ensure the 'endpoints' field in the configuration file is an empty list (`[]`).
3. Run the pinger

**Expected result:**
- The application should display a user-friendly message indicating that the endpoints list is empty and no pings will be performed.

**Execution result - failed. No info that endpoints list is empty. Got - Starting availability check...**

---

### Test case 11 - Scenario with more than 10 valid endpoints
**Steps:**
1. Run the pinger with a configuration containing more than 10 valid endpoints.

**Expected result:**
- The application should attempt to ping all the listed endpoints (more than 10).
- There should be entries in the output for each of the provided endpoints.

**Execution result - failed. Only first 10 endpoints were pinged**

## Reporting Tests

### Test case 12 - Check that start_time less than end_time in the report
**Pre-condition:**Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
**Steps:**
1. Run the pinger with the pre-condition configuration.
2. Inspect the generated report.

**Expected result:**
- The 'start_time' value in the report should be chronologically earlier than the 'end_time' value.

**Execution result - failed. end_time is equal to start_time**

---

### Test case 13 - Check min/max pings equal to config values
**Pre-condition:** Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
**Steps:**
1. Run the pinger with the pre-condition configuration.
2. Inspect the 'min_successful_pings' and 'max_pings' values in the generated report.

**Expected result:**
- The 'min_successful_pings' value in the report should be 2.
- The 'max_pings' value should be 3, matching the configuration.

**Execution result - failed. min_successful_pings and max_pings are equal to 1 in the report**

---

### Test case 14 - Check number of entries equals number of config endpoints
**Pre-condition:** Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
**Steps:**
1. Run the pinger with the pre-condition configuration (3 endpoints).
2. Inspect the 'entries' array in the generated report.

**Expected result:**
- The 'entries' array in the report should contain 3 elements, corresponding to the three endpoints defined in the configuration.

**Execution result - passed**

---

### Test case 15 - Check entries are correct - total/successful pings
**Pre-condition:** Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
**Steps:**
1. Run the pinger with the pre-condition configuration.
2. Inspect the 'entries' for each endpoint in the report.

**Expected result:**
- For each valid endpoint, 'total_pings' should be 2, and 'successful_pings' should be 2 (if consistently reachable) or less (if there were any failures).
- For the invalid endpoint, 'total_pings' should be 3, and 'successful_pings' should be 0.

**Execution result - failed. Valid endpoints shows "total_pings":3 instead of 2**

## Negative Scenarios

### Test case 16 - Invalid IP - 1.1.1
**Steps:**
1. Run the pinger with a config containing the IP address "1.1.1".

**Expected result:**
- The application should display a validation error message.

**Execution result - failed. Output shows 'Checking availability of <nil> []..' instead of 'Provided ip address 1.1.1 is invalid'**

---

### Test case 17 - IPv6 address
**Steps:**
1. Run the pinger with a config containing a valid IPv6 address (e.g., `2001:4860:4860:0:0:0:0:8888`).

**Expected result:**
- There are no defined requirements. Confirm expected behavior with Product Owner

**Execution result - got NOT OK [0/2]**

---

### Test case 18 - Non-boolean to ignore report
**Steps:**
1. Run the pinger with a config containing a valid endpoint.
2. Set the 'ignore' field for this endpoint to a non-boolean value (e.g., `"yes"`, `1`).

**Expected result:**
- The application should print validation message that 'ignore' field type is incorrect.

**Execution result - failed. No validation of 'ignore' field**

---

### Test case 19 - Config with nonexistent path
**Steps:**
1. Run the pinger by specifying a configuration file path that does not exist.

**Expected result:**
- The application should display an error message indicating that the specified configuration file cannot be found.

**Execution result - failed. Got 'Starting availability check...' instead of validation error message**

---

### Test case 20 - Min - (-1), max - (-1)
**Steps:**
1. Set `min_successful_pings` set to `-1`.
2. Set `max_pings` set to `-1`.
3. Run the pinger

**Expected result:**
- The application should display an error message that those values can't be negative.

**Execution result - failed. Got NOT OK [0/-1] instead of validation error message**

---

### Test case 21 - Wrong data types - strings as min, max, random string as endpoint
**Steps:**
1. `min_successful_pings` set to a string (e.g., `"one"`).
2. `max_pings` set to a string (e.g., `"two"`).
3. 'endpoint' field as a string instead of an object (e.g., `"test"`).
4. Run the pinger

**Expected result:**
- The application should fail to parse the configuration due to incorrect data types and display an error message for each case.

**Execution result - failed. Got NOT OK [0/0] instead of validation error message**

---

### Test case 22 - Run app without specifying config file
**Steps:**
1. Attempt to execute the pinger application without providing any command-line argument for the configuration file path.

**Expected result:**
- The application should display a user-friendly message indicating how to provide the configuration file path (e.g., via a command-line argument).

**Execution result - passed. Got Usage: [path_to_json_file] [path_to_result_file]**
