# coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='luhan777',
        charset='utf8',
        db='homework'
    )
    cur=conn.cursor()
    with open('/home/oem/Documents/shuwa/MySQL上课文件/作业/university/department.txt','r')as document:#打开文件
        for line in document.readlines():#读取，对每一行进行操作
            line = line.strip('\n')#去掉换行符
            dept_name=line.split(' ')[0]#调用split方法，对每一行以字符串间的空格进行分割
            building=line.split(' ')[1]
            budget=int(line.split(' ')[2])#budget是整数，强制进行字符串转换
            cur.execute("insert into department(dept_name,building,budget)VALUES (%s,%s,%s)",(dept_name,building,budget))
            conn.commit()#插入数据
    with open('/home/oem/Documents/shuwa/MySQL上课文件/作业/university/student.txt','r')as student:#与上面同理
        for line in student.readlines():
            line = line.strip('\n')
            ID=int(line.split(' ')[0])
            name=line.split(' ')[1]
            sex=line.split(' ')[2]
            age=int(line.split(' ')[3])
            emotion_state=line.split(' ')[4]
            dept_name=line.split(' ')[5]
            cur.execute("insert into student(ID,name,sex,age,emotion_state,dept_name)VALUES (%s,%s,%s,%s,%s,%s)",
                        (ID,name,sex,age,emotion_state,dept_name))
            conn.commit()
    with open('/home/oem/Documents/shuwa/MySQL上课文件/作业/university/exam.txt','r')as exam:#与上面同理
        for line in exam.readlines():
            line = line.strip('\n')
            line=line.split(' ')
            student_ID=int(line.split(' ')[0])
            exam_name=line.split(' ')[1]
            grade=int(line.split(' ')[2])
            cur.execute("insert into exam(student_ID,exam_name,grade)VALUES (%s,%s,%s)",
                        (student_ID,exam_name,grade))
            conn.commit()
    cur.close()#关闭游标
    conn.close()#断开连接
