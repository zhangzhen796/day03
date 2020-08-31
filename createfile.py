#!/usr/local/bin/python3
import string
import subprocess
import sys


def check_file(path):
    stat = subprocess.run('ls %s' %path,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if stat.returncode == 0:
        return 1
    else:
        return 0
def write_file(path):
    with open(path,'w') as f:
        while True:
            txt = input('请输入内容(一次一行),直接回车退出: ')
            if txt == "":
                break
            f.writelines(txt+"\n")

if __name__ == '__main__':
    while True:
        file = input("请输入文件名以及路径，直接回车退出")
        if file == '':
            print("bye bye")
            break
        if check_file(file) == 1:
            print("文件已经存在,请重新输入")
            continue
        else:
            write_file(file)
