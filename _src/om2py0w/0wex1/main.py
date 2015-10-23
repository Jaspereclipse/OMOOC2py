#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def main():
    dir = '/home/oski/OMOOC2py/_src/om2py0w/0wex1/Jaspers_Journal.md'
    f = open(dir,'a+')
    print f.read()
    headertime = "{0:*^50}"
    s = '##' + time.strftime("%c")
    now = headertime.format(s)
    Msg = ''
    while 1:
        tmp = raw_input()
        if tmp == 'q':
            break
        else:
            Msg += '\n\n' + tmp
    if len(Msg) > 0:
        f.write('\n\n' + now)
        f.write(Msg)
    f.close()

if __name__=="__main__":
    main()
