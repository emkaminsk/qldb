# qldb
Python sample code to run queries on AWS QLDB

To work with the examples:

- have your own ledger in AWS and collect credentials. Store your API Key and Secret as environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- install newest python,
- clone the repository, 
- create your own python environment (like venv) and activate it, 
- install dependencies in this environment
> pip install -r requirements.txt 

You can run the examples as many times as you want (they are idempotent). Modify the .py scripts in the root folder to set your ledger name and data examples.
