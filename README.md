# pinger_tests

### Pre-setup
Pinger binary is built locally

### Tests SetUp (Linux/MacOS)
1. Create virtual environment - `python3 -m venv venv`
2. Activate virtual env - `source venv/bin/activate`
3. Install dependencies - `pip install -r requirements.txt`
4. Set Pinger binary path - `export PINGER_BINARY=/path/to/Pinger`
5. Run tests with - `pytest -s --html=report.html`


### Notes

Most of the tests will fail because Pinger generates invalid json report. 
Fix line 87 of main.go file to - `os.WriteFile(os.Args[2], b, 0644)` and delete "bytes" from import.
Re-build Pinger binary after it. 
