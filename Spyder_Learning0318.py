# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:13:27 2018

@author: ecupl
"""
 

import os
os.chdir(r"D:/mywork/test")

#if __name__ == "__main__"用法
#当调用了包时，名称对方的__name__是包的名称，这里是"test0318.py",
#而本地的__name__名称是"main"，所以没法读取调用包中判定条件下的程序
import test0318
print(__name__)
print('引用cs')
test0318.cs()
print('程序结束！')


#创建多进程
import os
#查看当前单进程
def run_proc(name):
    print("Now process %s is %s"%(name,os.getpid()))
run_proc('single')

#设计多进程
from multiprocessing import Process
if __name__ == '__main__':
    print("Now %s process is %s"%("parent",os.getpid()))
    for i in range(5):
        p = Process(target=run_proc, args=("child",))
        print("Process %s will strat"%i)
        p.start()
        print(p.is_alive())
    p.join()
    
    

