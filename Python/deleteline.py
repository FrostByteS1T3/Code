#!/usr/bin/python
def deleteLine():
 fn = 'Passwords.txt'
 f = open(fn)
 output = []
 str="Test"
 for line in f:
   if not line.startswith(str):
    output.append(line)
 f.close()
 f = open(fn, 'w')
 f.writelines(output)
 f.close()
deleteLine()