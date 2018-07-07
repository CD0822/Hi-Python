#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename: ex3_login_page.py
# History: July 4,2018 - [Dan Chen] created
# This file is written to achieve register or login function.
# 1.输入第3次密码错误，用户被锁定
# 2.将被锁定账户写入ex3_lock.txt
# 3.将被锁定账户从ex3_login.txt中删除


import re

file1 = open('.\ex3_login.txt','r')
file2 = open('.\ex3_lock.txt','r')
login_data = re.split('[:|\n]',file1.read())
lock_data = re.split('\n',file2.read())
file1.close()
file2.close()
count = 1
while count<=3:      
    input_usrname = input("please input usr name>>>>")
    if input_usrname in login_data:
        index = login_data.index(input_usrname)
        input_pwd = input("please input your password>>>>")
        if input_pwd == login_data[index+1]:
            exit("welcome %s back!" %input_usrname)
        elif count == 3:
            #将此用户从ex3_login.txt中删除
            with open('.\ex3_login.txt','r') as file1:
                lines = file1.readlines()
            with open('.\ex3_login.txt','w') as file1_w:
                for line in lines:
                    if input_usrname in line:
                        continue
                    file1_w.write(line)
            #将次用户名写入ex3_lock.txt
            file2 = open('.\ex3_lock.txt','a')
            file2.write('\n%s:%s' %(input_usrname,login_data[index+1]))
            file2.close()
            exit("sorry %s, you have failed 3 times, and your id is locked!" %input_usrname)
        else:
            print("wrong password! please try again!")        
    elif input_usrname in lock_data:
        exit("sorry %s, your id has been locked!" %input_usrname)
#    else:
#        print("%s is not registerd, please try again!" %input_usrname)
 #       count -= 1
    count += 1
