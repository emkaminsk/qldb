from pyqldb.driver.qldb_driver import QldbDriver
import os
from functions import qldb_func as qf
from functions import digest as dg
from boto3 import client

def get_digest_result(name):
    """
    Get the digest of a ledger's journal.
    :type name: str
    :param name: Name of the ledger to operate on.
    :rtype: dict
    :return: The digest in a 256-bit hash value and a block address.
    """
    qldb_driver = QldbDriver(ledger_name='mkwest2ledger', region_name='eu-west-2')
    result = qldb_driver.get_ledger_digest()
    print('Success. LedgerDigest: {}.'.format(dg.digest_response_to_string(result)))
    return result


if __name__ == '__main__':
    print(f"Starting {os.path.basename(__file__)}")
    ledger_name='mkwest2ledger'
    region_name='eu-west-2'

#    qldb_client = client(ledger_name)
    
    try:
        get_digest_result(ledger_name)
    except Exception as e:
        raise e
