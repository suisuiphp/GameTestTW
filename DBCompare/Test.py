# encoding:utf-8
from TXTFile import TXTFile
from rfelibDb import rfelibDb
#from robot.api import logger

class Test(rfelibDb):
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # ROBOT_LIBRARY_VERSION = 0.1
    # ROBOT_LIBRARY_DOC_FORMAT = 'reST'
    def __init__(self):
        self.referdb="mysql,root/6tfc^YHN@10.0.127.14:3306/sodap"
        self.targetdb="mysql,root/6tfc^YHN@10.0.127.14:3306/sodap_dev"
        self.fileService=TXTFile()

    def tableCompare(self):
        print("********************数据库表名对比**********************")
        msg=["***************REPORT***************","referdb:"+self.referdb,"targetdb:"+self.targetdb,"************************************"]
        #获取目标数据库中的表
        tablesInTargetb = self.listTablesInDb(self.targetdb)
        if len(tablesInTargetb) == 0:
            msg.append("No tables in targetdb:%s" % (self.targetdb))
            self.fileService.fileWrite("report.txt","w","\n".join(msg))
            exit()
        #对比目标数据库
        str_tables_exited, str_tables_missed = self.assertTablesInDb(self.referdb, ",".join(tablesInTargetb))
        if len(str_tables_missed.split(",")) > 0:
            msg.append("This tables:'%s' missed in referdb" %(str_tables_missed))
        else:
            msg.append("Tables in targetdb marched tables in referdb!")
        msg.append("************************************")
        self.fileService.fileWrite("report.txt","w","\n".join(msg))

    def tableStructureCmpare(self):
        print("********************数据库表结构对比**********************")
        msg=["***********************************REPORT***************************************************",
             "***********************************数据库表结构对比******************************************",
             "referdb:"+self.referdb,"targetdb:"+self.targetdb,
             "********************************************************************************************\n"]
        tablesInTargetdb = self.listTablesInDb(self.targetdb)
        marched_tables_str, msg_structure=self.assertTableStructureBetweenDb(self.referdb,self.targetdb,",".join(tablesInTargetdb))
        #marched_tables_str, msg_structure = self.assertTableStructureBetweenDb(self.referdb, self.targetdb,"balances")
        msg.append(msg_structure)
        self.fileService.fileWrite("report_test2.txt","w","\n".join(msg))
        return marched_tables_str
    def tableDataCompare(self):
        print("********************数据库表数据对比**********************")
        msg=["***********************************REPORT***************************************************",
             "***********************************数据库表数据对比******************************************",
             "referdb:"+self.referdb,"targetdb:"+self.targetdb,
             "********************************************************************************************\n"]
        tablesInTargetdb = self.listTablesInDb(self.targetdb)
        msg_data = self.assertTabledataBetweenDb(self.referdb,self.targetdb,",".join(tablesInTargetdb))
        msg.append(msg_data)
        print("msg=",msg)
        self.fileService.fileWrite("report_test3.txt", "w", "\n".join(msg))

if __name__=="__main__":

    test=Test()
    #test.tableCompare()
    #test.tableStructureCmpare()
    #test.tableDataCompare()
    # test.assertTableStructureBetweenDb("mysql,root/6tfc^YHN@10.0.127.14:3306/zhuoyan","mysql,root/6tfc^YHN@10.0.127.14:3306/zhuoyan","balances")
    tables=test.listTablesInDb("mysql,root/6tfc^YHN@10.0.127.14:3306/zhuoyan_test")
    test.assertTabledataBetweenDb("mysql,root/6tfc^YHN@10.0.127.14:3306/zhuoyan","mysql,root/6tfc^YHN@10.0.127.14:3306/zhuoyan_test",",".join(tables))






