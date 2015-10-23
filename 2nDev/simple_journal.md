# Simple journal

References:

[PEP 0263 -- Defining Python Source Code Encodings](https://www.python.org/dev/peps/pep-0263/)

##v-0.0

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