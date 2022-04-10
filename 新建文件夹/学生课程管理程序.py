zhu = '''
  主菜单
1 学生管理
2 课程管理
3 排课
4 学生课表查询
5 教师课表查询'''
manu = '''
1,添加
2，删除
3，查询
'''
list1 = ['number', 'name', 'age']
list2 = ['2007040420', 'lihaiping', '21']
list3 = ['number', 'name', 'age']
list4 = ['2007040446', 'hanzhuohong', '20']
student1 = dict(zip(list1, list2))#字典存储学生信息
student2 = dict(zip(list3, list4))
students = [student1, student2]
from datetime import datetime
start1 = datetime(2022, 2, 27, 8, 00, 00)
end1 = datetime(2022, 2, 27, 9, 45, 00)
start2 = datetime(2022, 3, 8, 5, 00, 00)
end2 = datetime(2022, 3, 8, 6, 45, 00)
start3 = datetime(2022, 4, 1, 11, 00, 00)
end3 = datetime(2022, 4, 1, 12, 45, 00)
schedule = [{'course': 'Python', 'teacher': 'zhangjianhua', 'start': start1, 'end': end1},
            {'course': 'C', 'teacher': 'zhangjianhua', 'start': start2, 'end': end2},
            {'course': 'C++', 'teacher': 'zhangjianhua', 'start': start3, 'end': end3},
            {'course': 'java', 'teacher': 'liling', 'start': start3, 'end': end3},
            {'course': 'javascript', 'teacher': 'liling', 'start': start2, 'end': end2},
            {'course': '计网', 'teacher': 'fancaixia', 'start': start3, 'end': end3}]
schedule1 = {'course': 'Python', 'teacher': 'zhangjianhua', 'start': start1, 'end': end1}
schedule2 = {'course': 'java', 'teacher': 'liling', 'start': start3, 'end': end3}
schedule3 = {'course': '计网', 'teacher': 'fancaixia', 'start': start3, 'end': end3}
stable1 = {'student': '2007040420', 'schedules': [schedule1, schedule2]}#学生的选课信息
stable2 = {'student': '2007040446', 'schedules': [schedule1, schedule3]}
from prettytable import PrettyTable
table1 = PrettyTable(['学号', '姓名', '课程'])#学生课表
table2 = PrettyTable(['姓名', '所带课程'])#教师课表
table3 = PrettyTable(['学号', '姓名', '年龄'])#学生名单
table4 = PrettyTable(['课程名称', '代课老师', '开始时间', '结束时间'])#排课课表
table5 = PrettyTable(['学号', '姓名', '课程', '代课老师'])#学生课程管理
table5.add_row(['2007040420', 'lihaiping', 'Python', 'zhangjianhua'])
table5.add_row(['2007040420', 'lihaiping', 'java', 'liling'])
table5.add_row(['2007040446', 'hanzhuohong', 'Python', 'zhangjianhua'])
table5.add_row(['2007040446', 'hanzhuohong', '计网', 'fancaixia'])
table3.add_row(list2)
table3.add_row(list4)
d = []
while True:
 print(zhu)
 s = input('请输入选项：')
 sf = float(s)
 if sf == 1:#打印学生信息名单，并可修改
    print(manu)
    c = input('请输入选项:')
    cf = float(c)
    if cf == 1:
        d.append(input('请输入学号:'))
        d.append(input('请输入姓名:'))
        d.append(input('请输入年龄:'))
        table3.add_row(d)
        print(table3)
    elif cf == 2:
        table3.del_row(int(input('请输入要删除信息在表中的位置:')))
        print(table3)
    else:
        print(table3)
 elif sf == 2:#学生要上的课可选课
    print(manu)
    c = input('请输入选项:')
    cf = float(c)
    if cf == 1:
       course = input('请输入要添加课程:')
       num = input('请输入学号:')
       t = input('请输入代课老师:')
       s = input('请输入学生姓名:')
       e = [num, s, course, t]
       table5.add_row(e)
       print(table5)
    elif cf == 2:
       print(table5)
       table5.del_row(int(input('请输入要删除课程位置:')))
       print(table5)
    else:
        print(table5)
 elif sf == 3:#上课的时间
    print(manu)
    schedule = [{'course': 'Python', 'teacher': 'zhangjianhua', 'start': start1, 'end': end1},
    {'course': 'C', 'teacher': 'zhangjianhua', 'start': start2, 'end': end2},
    {'course': 'C++', 'teacher': 'zhangjianhua', 'start': start3, 'end': end3},
    {'course': 'java', 'teacher': 'liling', 'start': start3, 'end': end3},
    {'course': 'javascript', 'teacher': 'liling', 'start': start2, 'end': end2},
    {'course': '计网', 'teacher': 'fancaixia', 'start': start3, 'end': end3}]
    c = input('请输入选项:')
    cf = float(c)
    if cf == 1:
        name = input('请输入课程:')
        tname = input('请输入老师:')
        btime = input('请输入开始时间:')
        otime = input('请输入结束时间:')
        newschedule = {'course': name, 'teacher': tname, 'start': btime, 'end': otime}
        schedule.append(newschedule)
        for i in schedule:
            table4.add_row(i.values())
        print(table4)
    elif cf == 2:
        name = input('请输入要删除课程：')
        for i in schedule:
            if i['course'] == name:
                schedule.remove(i)
                print('已删除!')
                break
        else:
            print('课表中不存在此课程!!')
    else:
        for i in schedule:
            table4.add_row(i.values())
        print(table4)
        table4.clear_rows()
 elif sf == 4:
    a = input('请输入学号:')
    fa = float(a)
    if fa == 2007040420:
        table1.add_row(['2007040420', 'lihaiping', 'Python'])
        table1.add_row(['2007040420', 'lihaiping', 'java'])
        print(table1)
        table1.clear_rows()
    else:
        table1.add_row(['2007040446', 'hanzhuohong', 'Python'])
        table1.add_row(['2007040446', 'hanzhuohong', '计网'])
        print(table1)
        table1.clear_rows()
 elif sf == 5:
     b = input('请输入姓名:')
     if b == 'zhangjianhua':
         table2.add_row(['zhangjianhua', 'Python'])
         table2.add_row(['zhangjianhua', 'C'])
         table2.add_row(['zhangjianhua', 'C++'])
         print(table2)
         table2.clear_rows()
     elif b == 'liling':
         table2.add_row(['liling', 'java'])
         table2.add_row(['liling', 'javascript'])
         print(table2)
         table2.clear_rows()
     else:
         table2.add_row(['fancaixia', '计网'])
         print(table2)
         table2.clear_rows()
 else:
    print('输入错误!')