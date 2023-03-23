from pyqldb.driver.qldb_driver import QldbDriver

# FUNCTIONS
# Not idempotent
def create_table_once(transaction_executor, table_name):
    transaction_executor.execute_statement(f"CREATE TABLE {table_name}")
    return 0

# Create a table in the ledger.
def create_table(self, transaction_executor, table_name):
    # Check if the table already exists.
    tables = self.list_tables()
    if table_name in tables:
        print(f"Table '{table_name}' already exists!")
        return 2
    else:
        transaction_executor.execute_statement(f"CREATE TABLE {table_name}")
        return 0

# Function to insert a JSON document into a table.
def insert_document(transaction_executor, table_name, document):
    transaction_executor.execute_statement(f"INSERT INTO {table_name} ?", document)
    return 0

# Function to insert a JSON document into a table. Lambda version
def insert_documents(transaction_executor, table_name, document):
    # Check if doc with GovId:TOYENC486FH exists
    # This is critical to make this transaction idempotent
    value = document['name']
    cursor = transaction_executor.execute_statement(f"SELECT * FROM {table_name} WHERE name = ?", value)
    # Check if there is any record in the cursor
    first_record = next(cursor, None)

    if first_record:
        # Record already exists, no need to insert
        print(f"Record already exists: {first_record}")
        pass
    else:
        transaction_executor.execute_statement(f"INSERT INTO {table_name} ?", document)

# Function to update a document
def update_documents(transaction_executor, table_name, updated_document):
    transaction_executor.execute_statement(f"UPDATE {table_name} SET age = ?  WHERE name = ?", 
        updated_document['age'], updated_document['name'])
    print(f"Updated document {updated_document}")

# Query documents
def read_documents(transaction_executor, table_name, document):
    cursor = transaction_executor.execute_statement(f"SELECT * FROM {table_name}")
    fields = list(document.keys())
    print(' | '.join([str(field) for field in fields]))
    for doc in cursor:
        print(' | '.join([str(doc[str(field)]) for field in fields]))


if __name__ == '__main__':
    print("Starting happy.py")
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

    # Execute a happy path: create a table, insert a document, and query the table. Log all results to stdout.

    # declare variables
    table_name = 'docs_table'
    document = {'name': 'Minnie', 'age': 76}
    updated_document = {'name': 'Susan', 'age': 18}

    # create a table
    result = qldb_driver.execute_lambda(lambda executor: create_table(qldb_driver, executor, table_name))

    # insert a document
    qldb_driver.execute_lambda(lambda executor: insert_documents(executor, table_name, document))

    # update a document
    qldb_driver.execute_lambda(lambda executor: update_documents(executor, table_name, updated_document))

    # query the table
    qldb_driver.execute_lambda(lambda executor: read_documents(executor, table_name, document))
