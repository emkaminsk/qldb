# FUNCTIONS
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

# Function to insert a JSON document into a table with a uniqueness constraint.
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

# Delete documents        
def delete_documents(transaction_executor, table_name, key, value):
    transaction_executor.execute_statement(f"DELETE FROM {table_name} WHERE {key} = ?", value)
    print(f"Deleted document {key}={value}")    
