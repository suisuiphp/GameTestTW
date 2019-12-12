# _*_ coding: utf-8 _*_
from DBApi import DBApi
from unittest import TestCase
import sys



class rfelibDb(TestCase):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = 0.1
    ROBOT_LIBRARY_DOC_FORMAT = 'reST'
    def __init__(self):
        pass

    def listTablesInDb(self,db):
        '''
        获取数据库用户表属性信息
        :param db:dbtype,user/password@ip:port/databases
        :return:表名列表
        '''
        tables=[]
        str_sql="show tables"
        dbService=DBApi(db)
        list_table=dbService.listDataBySQL(str_sql)
        for table in list_table:
            tables.append(table[0])
        return tables

    def assertTablesInDb(self,db,tables):
        '''
        批量验证表是否在数据库中
        :param db:dbtype,user/password@ip:port/databases
        :param tables: 表名 str,多个表时，用“逗号（英文）”隔开
        :return: str_tables_exited str在数据库中存在的表，str_tables_missed str 数据库中不存在的表
        '''
        rs_mark = True
        #将需要验证的表名字符串转化为列表
        list_tables=tables.split(",")
        #print("list_tables=",list_tables)

        #获取数据库中的所有表名列表
        dbtables_list = self.listTablesInDb(db)

        #验证表是否存在数据库中
        tables_exited=[]
        table_missed=[]
        for tableName in list_tables:
            if tableName not in dbtables_list:
                table_missed.append(tableName)
            else:
                tables_exited.append(tableName)
        str_tables_exited=",".join(tables_exited)
        str_tables_missed=",".join(table_missed)
        if len(table_missed) > 0:
            rs_mark = False
            print("*ERROR* db:%s\n--------missed tables:%s" %(db,str_tables_missed))
            # self.fail("*ERROR* db:%s,missed tables:%s" %(db,str_tables_missed))
        else:
            print("*INFO* db:%s\n--------All tablenames marched!")
        return  str_tables_exited,str_tables_missed

    def listStructureByTablename(self,db,tablename):
        '''
       根据表名获取该表的表结构
       :param db:数据库信息，dbtype,user/password@ip:port/databases
       :param tablename:表名
       :return:表结构列表
       '''
        str_sql = "DESC %s" % tablename
        #str_sql = "select ordinal_position,colume_name,data_type from information_schema.'columns' where table_name ='%s' order by ordinal_position" % tablename
        #str_sql = "SELECT ORDINAL_POSITION,COLUME_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.'COLUMNS' WHERE TABLE_NAME ='%S' ORDER BY ORDINAL_POSITION" % tablename
        dbService = DBApi(db)
        tableStructure = dbService.listDataBySQL(str_sql)
        return tableStructure

    def assertTableStructureBetweenDb(self,referdb,targetdb,tables):
        '''
        批量比对表在两个数据库中的结构是否一致
        :param referdb:参照数据库，dbtype,user/password@ip:port/databases
        :param targetdb:目标数据库，dbtype,user/password@ip:port/databases
        :param tables: str
        :return:error_msg
        '''
        rs_mark = True
        error_msg = ["************************************************************************",
                     "referdb:" + referdb,
                     "targetdb:" + targetdb,
                     "tables:" +tables,
                     "************************************************************************\n",
                     "************************************************************************"]

        # 验证的表在目标数据库中是否存在
        str_tables_exited, str_tables_missed=self.assertTablesInDb(targetdb,tables)
        if len(str_tables_missed)>0:
            #print("targetDb:%s has no tables:%s" %(targetdb,str_tables_missed))
            # error_msg.append("目标数据库不存在以下表:'%s'" %(str_tables_missed))
            # error_msg.append("targetdb:%s\n--------missed tables:%s" % (targetdb,str_tables_missed))
            rs_mark = False
        # 验证存在于目标数据库中的表在参照数据库中是否存在
        str_tables_exited, str_tables_missed=self.assertTablesInDb(referdb,str_tables_exited)
        if len(str_tables_missed)>0:
            # print("referDb:%s has no tables:'%s'" % (referdb, str_tables_missed))
            # error_msg.append("参照数据库不存在以下表:'%s'" % (str_tables_missed))
            # error_msg.append("referdb:%s\n-------- missed tables::'%s'" % (referdb,str_tables_missed))
            rs_mark = False

        #验证表结构
        marched_tables=[]
        ummarched_tables=[]
        single_table_msg=[]

        if len(str_tables_exited)>0:
            list_tables = str_tables_exited.split(",")
            for tableName in list_tables:
                table_mark=True
                refer_attributes = self.listAttributeNameOfTable(referdb, tableName)
                target_attributes = self.listAttributeNameOfTable(targetdb, tableName)
                refer_structure_dict = self.listStructureByTablenameAsDict(referdb, tableName)
                target_structure_dict = self.listStructureByTablenameAsDict(targetdb, tableName)

                single_table_msg.append("\n*********%s*********" % (tableName))
                #验证字段个数
                if len(refer_attributes) != len(target_attributes):
                    single_table_msg.append("Attributes count not matched.\n referdb: %d.    targetdb:%d."
                                            % (len(refer_attributes), len(target_attributes)))
                    # single_table_msg.append("表： %s 字段个数不一致 !  参照数据库中字段: %d个, 目标数据库中字段: %d个"
                    #                         % (tableName, len(refer_attributes), len(target_attributes)))
                    # table_mark=False
                #获取目标表中新增字段
                attributes_add = []
                attributes_existed = []
                for attributename in target_attributes:
                    if attributename not in refer_attributes:
                        attributes_add.append(attributename)
                    else:
                        attributes_existed.append(attributename)
                if len(attributes_add)>0:

                    table_mark = False
                    single_table_msg.append("Attributes added:%s" %(",".join(attributes_add)))
                  # single_table_msg.append("新增字段为：%s" % (",".join(attributes_add)))
                #获取目标表中减少的字段
                attributes_del = []
                for attributename in refer_attributes:
                    if attributename not in target_attributes:
                        attributes_del.append(attributename)
                if len(attributes_del)>0:
                    table_mark = False
                    single_table_msg.append("Attributes deleted:%s" %(",".join(attributes_del)))
                    # single_table_msg.append("减少字段为：%s" % (",".join(attributes_del)))
                #获取目标表中修改字段信息：
                if len(attributes_existed)>0:
                    attributes_changed = []
                    attributes_changed_msg = []
                    for attributename in attributes_existed:
                        if refer_structure_dict[attributename] != target_structure_dict[attributename]:
                            attributes_changed.append(attributename)
                            attributes_changed_msg.append("attribute:%s , referdb:%s , targetdb:%s"
                                                          %(attributename,refer_structure_dict[attributename],target_structure_dict[attributename]))
                            # attributes_changed_msg.append("字段：%s 参照数据库：%s 目标数据库：%s"
                            #                               % (attributename, refer_structure_dict[attributename],
                            #                                  target_structure_dict[attributename]))
                    if len(attributes_changed) > 0:
                        table_mark = False
                        single_table_msg.append("Attributes changed:%s." %(",".join(attributes_changed)))
                        # single_table_msg.append("修改字段为：%s." % (",".join(attributes_changed)))
                        single_table_msg.append("\n".join(attributes_changed_msg))
                #判断表结构是否完全匹配
                if table_mark:
                    refer_structure=self.listStructureByTablename(referdb, tableName)
                    target_structure=self.listStructureByTablename(targetdb, tableName)
                    for i in range(0, len(target_structure)):
                        if target_structure[i] != refer_structure[i]:
                            table_mark=False
                            break
                #比对结果
                if table_mark:
                    single_table_msg.pop()
                    #single_table_msg.append("march!")
                    marched_tables.append(tableName)
                else:
                    ummarched_tables.append(tableName)

        if len(marched_tables) > 0:
            # error_msg.append("结构完全相同的表有：%s" %(",".join(marched_tables)))
            error_msg.append("Structure marched tables:%s" % (",".join(marched_tables)))
        if len(ummarched_tables) > 0:
            error_msg.append("Structure not marched tables:%s" % (",".join(ummarched_tables)))
            # error_msg.append("结构不同的表有：%s" % (",".join(ummarched_tables)))
            rs_mark = False

        error_msg.append("\n***************************details**************************************")
        error_msg.append("\n".join(single_table_msg))
        marched_tables_str=",".join(marched_tables)

        if not rs_mark:
            print("*ERROR* Structure not marched!")
            print("\n".join(error_msg))
            # self.fail("\n".join(error_msg))
        else:
            print("*INFO* Structure completely marched!")

        return marched_tables_str,"\n".join(error_msg)


    def join(self,list):
        '''
        将列表元素按逗号连接为字符串
        :param list:
        :return:
        '''
        return ",".join(list)

    def listStructureByTablenameAsDict(self,db,tablename):
        '''
       根据表名获取该表的表结构
       :param db:数据库信息
       :param tablename:表名
       :return:表结构字典，{字段名：字段信息}
       '''
        tableStructureAsDict={}
        str_sql = "DESC %s" % tablename
        dbService = DBApi(db)
        tableStructure = dbService.listDataBySQL(str_sql)
        for sturcture in tableStructure:
            tableStructureAsDict[sturcture[0]] = sturcture
        #print(tableStructureAsDict)
        return tableStructureAsDict

    def listAttributeNameOfTable(self,db,tablename):
        attributes = []
        str_sql = "DESC %s" % tablename
        dbService = DBApi(db)
        tableStructure = dbService.listDataBySQL(str_sql)
        for sturcture in tableStructure:
            attributes.append(sturcture[0])
        #print(attributes)
        return attributes

    def assertTabledataBetweenDb(self,referdb,targetdb,tables):
        '''
        比较两个数据库中的所有数据
        :param referdb: dbtype,user/password@ip:port/databases
        :param targetdb: dbtype,user/password@ip:port/databases
        :param tables: tablename or tablename1,tablename2,tablename3
        :return:
        示例：
        db:"mysql,root/123456@10.20.112.181:50016/pdw"
        tables:"BUSI_REALIZABLE_ASSET, BUSI_HOUSE_DETAIL"
        '''
        print("hell")
        msg=[]
        msg_single_tabledata=[]
        bool_db = True
        # 验证需要验证的表在数据库中是否存在,表结构是否一致
        marched_tables_str, msg_structure = self.assertTableStructureBetweenDb(referdb, targetdb,tables)
        if marched_tables_str != tables:
            bool_db=False
        msg.append(msg_structure)
        #验证表数据
        if len(marched_tables_str) > 0:
            msg.append("*****************************data detail*********************************")
            list_tables = marched_tables_str.split(",")
            data_marched_tables=[]
            data_unmarched_tables = []

            #断言数据
            for tableName in list_tables:
                msg_single_tabledata.append("\n*********%s*********" % (tableName))
                bool_table = True
                print("tablename:",tableName)
                str_sql = "SELECT * FROM %s" % tableName
                referdbService = DBApi(referdb)
                rs1 = referdbService.listDataBySQL(str_sql)
                targetdbService = DBApi(targetdb)
                rs2 = targetdbService.listDataBySQL(str_sql)
                if len(rs1) != len(rs2):
                    # print("数据条数不一致！参照数据库：%d条，目标数据库：%d条" %(len(rs1),len(rs2)))
                    msg_single_tabledata.append("Data count not marched！referdb：%d，targetdb：%d" %(len(rs1),len(rs2)))
                    bool_db = False
                    bool_table = False
                #获取目标表中新增数据信息：
                data_add=[]
                for row in range(0,len(rs2)):
                    if rs2[row] not in rs1:
                        data_add.append(rs2[row])

                if len(data_add)>0:
                    bool_db = False
                    bool_table = False
                    data_add_list=[]
                    for data in data_add:
                        data_add_list.append(str(data))
                    # msg_single_tabledata.append("data added：")
                    # msg_single_tabledata.append("\n".join(data_add_list))
                #获取目标表中减少的数据
                data_del = []
                for row in range(0, len(rs1)):
                    if rs1[row] not in rs2:
                        data_del.append(rs1[row])
                if len(data_del) > 0:
                    bool_db = False
                    bool_table = False
                    data_del_list = []
                    for data in data_del:
                        data_del_list.append(str(data))
                    # msg_single_tabledata.append("data deleted：")
                    # msg_single_tabledata.append("\n".join(data_del_list))
                #获取数据一致的表
                if bool_table:
                    data_marched_tables.append(tableName)
                else:
                    data_unmarched_tables.append(tableName)
            if bool_db:
                print("*INFO* DB data marched!")
            else:
                msg.append("DB data not marched")
                if len(data_marched_tables)>0:
                    msg.append("data marched tables：%s" %(",".join(data_marched_tables)))
                if len(data_unmarched_tables)>0:
                    msg.append("data not marched tables：%s" %(",".join(data_unmarched_tables)))
                    msg.append("***************************details**************************************")
                    # msg.append("\n".join(msg_single_tabledata))
                print("*ERROR* %s" %("\n".join(msg)))
        else:
            print("*ERROR* DB data not marched!")
            # msg.append("两个数据库中表结构不一致！")
        return "\n".join(msg)




    def assertTabledataBetweenDbByAttribute(self,referdb="mysql,root/123456@10.20.112.181:50016/pdw",
                                         targetdb="mysql,root/123456@10.20.112.181:50016/pdw",tables="",
                                         attribute="period",
                                         attr_value="201705"):
        '''
        根据table 的 att 字段 获取数据，比较在referdb 与targetdb 中的数据是否一致
        :param referdb:
        :param targetdb:
        :param attribute:
        :param attr_value:
        :return:
        '''
        # 验证表在数据库中是否存在
        str_tables_ref = self.assertTablesInDb(referdb, tables)
        if len(str_tables_ref) == 0:
            print("referanceDb:%s has no tables:%s" % (referdb, tables))
            return

        str_tables_target = self.assertTablesInDb(targetdb, str_tables_ref)
        if len(str_tables_target) == 0:
            print("targetDb:%s has no tables:%s" % (targetdb, str_tables_target))
            return
        #验证
        list_table = str_tables_target.split(",")
        bool_rs = True
        if len(list_table) > 0:
            for tableName in list_table:
                str_sql = "SELECT * FROM %s t WHERE t.%s = '%s'" % (tableName,attribute,attr_value)
                referdbService = DBApi(referdb)
                rs1 = referdbService.listDataBySQL(str_sql)
                targetdbService = DBApi(targetdb)
                rs2 = targetdbService.listDataBySQL(str_sql)
                if len(rs1) != len(rs2):
                    print("*ERROR* Table %-34s %s:%s miss marched! excepted:%d rows, actural:%d rows" %
                          (tableName,attribute,attr_value, len(rs1), len(rs2)))
                    bool_rs = False
                else:
                    sum_rows = len(rs1)
                    for row in range(sum_rows):
                        if rs1[row] not in rs2:
                            print("*ERROR* Table %s %s:%s miss marched!\nLine %d miss data:%s\n" %
                                  (tableName,attribute,attr_value, row, rs1[row]))
                            bool_rs = False
                    if bool_rs:
                        print("*INFO* table %s-34s %s:%s  rows:%-5d pass" % (tableName, attribute,attr_value,sum_rows))
        else:
            print("*ERROR* Empty tables!")
            bool_rs = False
        if not bool_rs:
            self.fail()

    def testFail(self):
        self.fail()




