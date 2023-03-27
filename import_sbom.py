import json
import os
from pyqldb.driver.qldb_driver import QldbDriver
from functions import qldb_func as qf

if __name__ == '__main__':
    print(f"Starting {os.path.basename(__file__)}")
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')


    # declare variables
    table_name = 'SBOM'
    filename = 'composer.cdx'

    with open(filename, "r") as f:
      document = json.load(f)
    document = json.dumps(document)
    document = json.loads(document)

    # create a table
    result = qldb_driver.execute_lambda(lambda executor: qf.create_table(qldb_driver, executor, table_name))

    # insert a document
    qldb_driver.execute_lambda(lambda executor: qf.insert_documents(executor, table_name, document, "bomFormat"))

    # query the table
    qldb_driver.execute_lambda(lambda executor: qf.post_query(executor, f"Select count(*) from {table_name}"))

    '''
    document_new = {
   "a": 1,
   "b": "2",
   "c": [ 1, 2, 3]
}

    # insert a document
    qldb_driver.execute_lambda(lambda executor: qf.insert_documents(executor, table_name, document_new, "a"))
    '''
