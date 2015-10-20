# GitHub

## SSH key

Generate an SSH key for my Linux virtual machine

[Official Documentation](https://help.github.com/articles/generating-ssh-keys/)

###1. Check for SSH key

    $ ls -al ~/.ssh

I didn't have a key yet.

###2. Generate one

    $ ssh-keygen -t rsa -b 4096 -C "my_email@gmail.com"

Enter my password

###3. Add key to ssh-agent

    $ eval "($ssh-agent -s)"
    $ ssh-add ~/.ssh/id_rsa

An explanation of `ssh-agent` given by [wikipedia](https://en.wikipedia.org/wiki/Ssh-agent):

> `ssh-agent` creates a socket and then checks the connections from `ssh`. Everyone who is able to connect to this socket also has access to the `ssh-agent`. The permissions are set as in a usual Linux or Unix system. When the agent starts, it creates a new directory in `/tmp` with restrictive permissions. The socket is located in the folder.

###4. Add SSH key to GitHub account

    $ sudo cat ~/.ssh/id_rsa.pub

Then I copied into Github/setting/SSH/Add Key under my `Github` account.

###5. Test for connection

    $ ssh -T git@github.com

Note that I don't have to change the above code to run the test.
















    