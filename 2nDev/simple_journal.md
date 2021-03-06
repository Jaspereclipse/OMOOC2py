# Simple journal

References:

1. How to set **encoding**: [PEP 0263 -- Defining Python Source Code Encodings](https://www.python.org/dev/peps/pep-0263/)
2. Useful introduction to **string operations**: [string — Common string operations](https://docs.python.org/2/library/string.html)
3. Introduction to **file editing mode**: [stackoverflow: difference between modes a, a+, w, w+, and r+?](http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r)
4. **Date & Time** format: [strftime](http://strftime.org/)

5. Outstanding works by [wp-lai](https://wp-lai.gitbooks.io/learn-python/content/2nDev/diary.html)

6. **Color** setting in Ubuntu Terminal: [(1) Enable Colorful Terminal in Debian and Ubuntu](https://scottlinux.com/2013/07/08/enable-colorful-terminal-in-debian-and-ubuntu/)
(2) 
##V-0.0

###Basic realization

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def main():
    f = open('journal.txt','a+') #Create a file or append on it
    for line in f:
        print line #Print the previously written journals
    now = time.strftime("%c") #Add current data & time before start writing
    now += '\n'
    f.write(now)
    while 1:
        Msg = raw_input() 
        if Msg == 'q': #Waiting for user's input unless q(quit)
            break
        Msg += '\n'
        f.write(Msg)
    f.close() #Close the connection

if __name__=="__main__":
    main()
```

The question I have while implementing the code above is:

*Even if I did not set the encoding as `utf-8`, I got the right output anyway for Chinese input.*

I test something like this:
```python
import sys
print sys.getfilesystemencoding()
print sys.getdefaultencoding()
```
The former one returns `UTF-8`, while the latter returns `ascii`. Same results after I change the encoding.


##V-1.0

###Markdown format
This is inspired by [wp-lai](https://wp-lai.gitbooks.io/learn-python/content/2nDev/diary.html). I tried to reproduce what he has accomplished.









