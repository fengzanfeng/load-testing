from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

from com.wandoujia.hbase.load.test import HBaseLoadTest

cacheBlocks = grinder.getProperties().getBoolean("hbase.test.cacheblocks", True)
scanRowNum = grinder.getProperties().getInt("hbase.test.scan.rownum", 1)
putPercent = grinder.getProperties().getDouble("hbase.test.put.percent", 0.0)
scanPercent = grinder.getProperties().getDouble("hbase.test.scan.percent", 0.0)
threadNum = grinder.getProperties().getInt("grinder.threads", -1)
putThreadNum = int(round(threadNum * putPercent))
scanThreadNum = int(round(threadNum * scanPercent))
print "cacheBlocks: %s, scanRowNum: %d" % (cacheBlocks, scanRowNum)
print "total thread number: %d, put thread number: %d, scan thread number: %d" % (threadNum, putThreadNum, scanThreadNum)

hbaseLoadTest = HBaseLoadTest(cacheBlocks, scanRowNum)

def put():
    hbaseLoadTest.put()

def scan():
    hbaseLoadTest.scan()

hbasePutTest = Test(1, "HBase Put").wrap(put)
hbaseScanTest = Test(2, "HBase Scan").wrap(scan)

class TestRunner:
    def __init__(self):
        self.threadId = grinder.getThreadNumber()
        print "current thread id: %d" % (self.threadId)

    def __del__(self):
        hbaseLoadTest.close()

    def __call__(self):
        if self.threadId < putThreadNum:
            hbasePutTest()
        else:
            hbaseScanTest()
