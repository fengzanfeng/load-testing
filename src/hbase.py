from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

from java.lang import String
from java.util import UUID
from org.apache.hadoop.hbase import HBaseConfiguration, HTableDescriptor, HColumnDescriptor, HConstants
from org.apache.hadoop.hbase.client import HBaseAdmin, HTable, Get, Put

conf = HBaseConfiguration()
tablename = "performance_test"
table = HTable(conf, tablename)

def put():
    row_key = UUID.randomUUID().toString()
    put_row = Put(row_key)
    put_row.add("c", "d", "value")
    table.put(put_row)

def get():
    get = Get("ff01c0cb-a14f-4c03-845f-fe45fa5b6323")
    get_row = table.get(get)
    data = String(get_row.value(), "UTF8")


test1 = Test(1, "HBase Put").wrap(put)
test2 = Test(2, "HBase Get").wrap(get)

class TestRunner:
    def __call__(self):
        test1()
        test2()
