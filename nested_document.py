from pyqldb.driver.qldb_driver import QldbDriver
import os
from functions import qldb_func as qf

if __name__ == '__main__':
    print(f"Starting {os.path.basename(__file__)}")
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

    # Execute a happy path: create a table, insert a document, and query the table. Log all results to stdout.

    # declare variables
    table_name = 'nested_docs_table'
    document = {'name': 'Susan', 
                'age': 16, 
                'interests': ['plants', 'potatoes'], 
                'movies': {'action': 'Everything Everywhere', 'comedy': 'Monty Python'}
    }

    # create a table
    result = qldb_driver.execute_lambda(lambda executor: qf.create_table(qldb_driver, executor, table_name))

    # insert a document
    qldb_driver.execute_lambda(lambda executor: qf.insert_documents(executor, table_name, document, "name"))

    # query the table
    qldb_driver.execute_lambda(lambda executor: qf.read_documents(executor, table_name, document))
