from pyqldb.driver.qldb_driver import QldbDriver

def insert_documents(transaction_executor, table_name, arg_1):
    # Check if doc with GovId:TOYENC486FH exists
    # This is critical to make this transaction idempotent
    cursor = transaction_executor.execute_statement(f"SELECT * FROM {table_name} WHERE name = ?", 'John')
    # Check if there is any record in the cursor
    first_record = next(cursor, None)

    if first_record:
        # Record already exists, no need to insert
        pass
    else:
        transaction_executor.execute_statement(f"INSERT INTO {table_name} ?", arg_1)
    
print("Starting insert_document.py")
qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

table_name = 'docs_table'
doc_1 =  {'name': 'John', 'age': 42}

qldb_driver.execute_lambda(lambda executor: insert_documents(executor, table_name, doc_1))