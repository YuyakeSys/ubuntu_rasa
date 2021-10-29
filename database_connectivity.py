# -*- codeing = utf-8 -*-
# @Time ： 2021/10/24 22:09
# @Author : Meng Zhouyang/Chester
# @File : database_connectivity.py
# @Software: PyCharm
import pymysql


def DataUpdate(account, plan):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='rasa_plan_data',
        charset='utf8'
    )

    cursor = db.cursor()
    check_sql = 'select * from accoun_plan'
    sql = "update account_plan set plan_info = %s where account= %s"
    try:
        cursor.execute(sql, [account, plan])
        db.commit()

        print("plan updated")
    except Exception as e:
        db.rollback()
    cursor.close()
    db.close()

def DataSearch(game):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='rasa_plan_data',
        charset='utf8'
    )

    cursor = db.cursor()
    sql= "select * from game where name= %s"
    try:
        cursor.execute(sql, game)
        db.commit()
    except Exception as e:
        db.rollback()
    cursor.close()
    db.close()
    return cursor.fetchone()[1]
