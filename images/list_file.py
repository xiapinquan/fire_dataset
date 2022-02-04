#!/usr/bin/env python
# coding:utf-8

import os


def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    for root, subdirs, files in os.walk(dir):
        for name in files:
            for ext in exts:
                if (name.endswith(ext)):
                    name = os.path.join(rootdir, name)
                    file.write(name + "\n")
                    break
            if (not recursion):
                break


def Test():
    dir = os.getcwd()
    outfile = "binaries.txt"
    wildcard = ".jpg"
    file = open(outfile, "w")
    if not file:
        print("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir, file, wildcard, 1)

    file.close()


rootdir = os.getcwd()
print(rootdir)
Test()

f = open("binaries.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
print
line,

line = f.readline()  # 调用文件的 readline()方法
print
line
