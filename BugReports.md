## Bug Reports

### Bug #1: max_pings is displayed incorrectly in the output 

**Severity:** High

**Priority:** High

**Steps to Reproduce:**
1. Run the pinger with a config containing 1 unreachable endpoint, min_successful_pings - 1, max_pings - 2, empty description.

**Expected Results:**
Max pings is equal to 2 in the output

**Actual Results:**
Got "NOT OK [0/1]. Max pings was set to min_successful_pings

---

### Bug #2: min_successful_pings is displayed incorrectly in the output when min_successful_pings equal to max_pings

**Severity:** High

**Priority:** High

**Steps to Reproduce:**
1. Create a config containing one valid endpoint.
2. Set `min_successful_pings` to `2`.
3. Set `max_pings` to `2`.
4. Run the pinger

**Expected Results:**
Expected to get "OK [2/2]"

**Actual Results:**
Got "NOT OK [1/2]"

---

### Bug #3: Endpoints with 'ignore' field 'true' are still executed 

**Severity:** High

**Priority:** High

**Steps to Reproduce:**
1. Create a config containing two valid endpoints.
2. For one of the endpoints, include the field `ignore: true`.
3. Run the pinger

**Expected Results:**
The output report should only contain an entry for the endpoint where `ignore` was set to `false` (or not present). The ignored endpoint should not be processed or included in the results

**Actual Results:**
Ignored endpoint was pinged

---

### Bug #4: Only first 10 provided endpoints are pinged

**Severity:** Medium

**Priority:** High

**Steps to Reproduce:**
1. Run the pinger with a configuration containing more than 10 valid endpoints.

**Expected Results:**
- The application should attempt to ping all the listed endpoints (more than 10).
- There should be entries in the output for each of the provided endpoints.

**Actual Results:**
Only first 10 endpoints were pinged

---

### Bug #5: Non-zero exit code is returned in case of successful execution

**Severity:** Medium

**Priority:** Medium

**Steps to Reproduce:**
1. Create a config containing three valid endpoints.
2. Set `min_successful_pings` to `1`.
3. Set `max_pings` to `1`.
4. Run the pinger
5. Print exit code after execution

**Expected Results:**
- Exit code should be 0

**Actual Results:**
Exit code is 123. If Pinger is executed by another app that checks exit code - it can break that app execution.

---

### Bug #6: Endpoint is not ignored when min_successful_pings = 0, max_pings = 0

**Severity:** Low

**Priority:** Low

**Steps to Reproduce:**
1. Create a config containing one unreachable endpoint.
2. Set `min_successful_pings` to `0`.
3. Set `max_pings` to `0`.
4. Run the pinger

**Expected Results:**
- The endpoint should be effectively ignored; no ping attempts should be made

**Actual Results:**
Output shows 'NOT OK'

---

### Improvement #7: There is no validation if empty config is provided

**Severity:** Low

**Priority:** Low

**Steps to Reproduce:**
1. Run the pinger providing configuration file with {}

**Expected Results:**
- The application should display a user-friendly error message indicating that a configuration file is empty.

**Actual Results:**
Got - Starting availability check...

---

### Improvement #8: There is no validation if empty endpoint list is provided

**Severity:** Low

**Priority:** Low

**Steps to Reproduce:**
1. Create a configuration file.
2. Ensure the 'endpoints' field in the configuration file is an empty list (`[]`).
3. Run the pinger

**Expected Results:**
- The application should display a user-friendly message indicating that the endpoints list is empty and no pings will be performed

**Actual Results:**
Got - Starting availability check...

---

### Bug #9: end_time is equal to start_time in the report

**Severity:** Medium

**Priority:** High

**Steps to Reproduce:**
**Pre-condition:**Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
**Steps:**
1. Run the pinger with the pre-condition configuration.
2. Inspect the generated report.

**Expected Results:**
- The 'start_time' value in the report should be chronologically earlier than the 'end_time' value

**Actual Results:**
end_time is equal to start_time

---

### Bug #10: Generated report isn't valid json file

**Severity:** Medium

**Priority:** Critical

**Steps to Reproduce:**
**Pre-condition:**Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
1. Run the pinger with the pre-condition configuration.
2. Inspect the generated report.

**Expected Results:**
- Generated report is valid JSON that can be read by other app

**Actual Results:**
Json report misses '}' so it can break users applications that are parsing that report

---

### Bug #11: min/max pings in the report aren't equal to provided config values (hardcoded to 1 instead)

**Severity:** Medium

**Priority:** High

**Steps to Reproduce:**
**Pre-condition:**Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
1. Run the pinger with the pre-condition configuration.
2. Inspect the generated report.

**Expected Results:**
- The 'min_successful_pings' value in the report should be 2.
- The 'max_pings' value should be 3, matching the configuration.

**Actual Results:**
min_successful_pings and max_pings are hardcoded to 1 in the report

---

### Bug #12: total_pings is set to max_pings instead of executed pings in the report

**Severity:** Medium

**Priority:** Low

**Steps to Reproduce:**
**Pre-condition:**Create config with `min_successful_pings: 2`, `max_pings: 3`, 2 valid endpoints, and 1 unreachable endpoint.
1. Run the pinger with the pre-condition configuration.
2. Inspect the generated report.

**Expected Results:**
- For each valid endpoint, 'total_pings' should be 2, and 'successful_pings' should be 2

**Actual Results:**
Valid endpoints shows "total_pings":3 instead of 2

---

### Bug #13: Invalid IP address isn't validated

**Severity:** Medium

**Priority:** Medium

**Steps to Reproduce:**
1. Run the pinger with a config containing the IP address "1.1.1".

**Expected Results:**
- The application should display a validation error message.

**Actual Results:**
Output shows 'Checking availability of <nil> []..' instead of 'Provided ip address 1.1.1 is invalid'

---

### Bug #14: Input config isn't validated on wrong data types

**Severity:** Medium

**Priority:** Low

**Steps to Reproduce:**
1. min_successful_pings` set to a string `"one"`
2. `max_pings` set to a string `"two"`
3. 'endpoint' field as a string instead of an object  - `"test"`
4. Set the 'ignore' field for this endpoint to a non-boolean value `"yes"`
5. Run the pinger

**Expected Results:**
- The application should fail to parse the configuration due to incorrect data types and display an error message for each case.

**Actual Results:**
Got NOT OK [0/0] instead of validation error message

---

### Bug #15: Input config isn't validated on negative values for min_successful_pings and max_pings

**Severity:** Low

**Priority:** Low

**Steps to Reproduce:**
1. Set `min_successful_pings` set to `-1`.
2. Set `max_pings` set to `-1`.
3. Run the pinger

**Expected Results:**
- The application should display an error message that those values can't be negative

**Actual Results:**
Got NOT OK [0/-1] instead of validation error message

---

### Bug #16: Config with nonexistent path isn't validated

**Severity:** Low

**Priority:** Medium

**Steps to Reproduce:**
1. Run the pinger by specifying a configuration file path that does not exist.

**Expected Results:**
- The application should display an error message indicating that the specified configuration file cannot be found.

**Actual Results:**
 Got 'Starting availability check...' instead of validation error message

---