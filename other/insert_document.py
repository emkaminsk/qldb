from pyqldb.driver.qldb_driver import QldbDriver

def insert_document(transaction_executor, table_name, document):
    transaction_executor.execute_statement(f"INSERT INTO {table_name} ?", document)
    return 0
    
print("Starting insert_document.py")
qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

table_name = 'test_table'

result = insert_document(qldb_driver, table_name, {'name': 'John', 'age': 42})