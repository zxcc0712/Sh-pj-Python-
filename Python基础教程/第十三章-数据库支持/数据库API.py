# 为解决Python中数据库模块存在的接口（API）不同的这个问题，人们一直同意开发一个标准数据库
# 13.1.1全局变量
# apilevel            使用的Python DB API版本
# threadsafety        模块的线程安全程度如何
# paramstyle          在SQL查询中使用哪种参数风格

# 13.1.2异常


#试验数据库，起步
import sqlite3
conn = sqlite3.connect('somedatabase.db')
# 从连接获得游标
curs = conn.cursor()
conn.commit()
conn.close()
