from pyqldb.driver.qldb_driver import QldbDriver
print("Starting test.py")
qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')

for table in qldb_driver.list_tables():
    print(table)