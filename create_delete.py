from pyqldb.driver.qldb_driver import QldbDriver
import os
from functions import qldb_func as qf

if __name__ == '__main__':
    print(f"Starting {os.path.basename(__file__)}")
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

    # Execute a scenario: create a table, insert a document, query the table, delete the document, query again. Log all results to stdout.

    # declare variables
    table_name = 'data_to_delete'
    document = {'name': 'elephant', 'age': 10}

    # create a table
    result = qldb_driver.execute_lambda(lambda executor: qf.create_table(qldb_driver, executor, table_name))

    # insert a document
    qldb_driver.execute_lambda(lambda executor: qf.insert_documents(executor, table_name, document, "name"))

    # query the table
    qldb_driver.execute_lambda(lambda executor: qf.read_documents(executor, table_name, document))

    # delete the document
    qldb_driver.execute_lambda(lambda executor: qf.delete_documents(executor, table_name, "age", 10))

    # query the table
    qldb_driver.execute_lambda(lambda executor: qf.read_documents(executor, table_name, document))
