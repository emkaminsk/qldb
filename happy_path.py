from pyqldb.driver.qldb_driver import QldbDriver
import os
from functions import qldb_func as qf

if __name__ == '__main__':
    print(f"Starting {os.path.basename(__file__)}")
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

    # Execute a happy path: create a table, insert a document, update one and query the table. Log all results to stdout.

    # declare variables
    table_name = 'Malgorzata'
    document = {'name': 'Olek', 'age': 20}
    updated_document = {'name': 'Olek', 'age': 21}

    # create a table
    result = qldb_driver.execute_lambda(lambda executor: qf.create_table(qldb_driver, executor, table_name))

    # insert a document
    qldb_driver.execute_lambda(lambda executor: qf.insert_documents(executor, table_name, document))

    # update a document
    qldb_driver.execute_lambda(lambda executor: qf.update_documents(executor, table_name, updated_document))

    # query the table
    qldb_driver.execute_lambda(lambda executor: qf.read_documents(executor, table_name, document))
