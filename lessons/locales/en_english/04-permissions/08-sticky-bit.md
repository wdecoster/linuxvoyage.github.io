# The Sticky Bit

## Lesson Content

One last special permission bit I want to talk about is the sticky bit. 

This permission bit, "sticks a file/directory" this means that only the owner or the root user can delete or modify the file. This is very useful for shared directories. Take a look at the example below:

<pre>$ ls -ld /tmp
drwxrwxrwt 6 root root 4096 Dec 15 11:45 /tmp
</pre>

You'll see a special permission bit at the end here <b>t</b>. Notice it sits where the execute bit for other users would normally be. It means that although anyone may create files in /tmp, you can only delete or rename a file in there if you own it. Without the sticky bit, write permission on a directory would let anybody remove anybody else's files from it, which on a shared directory like /tmp would be a disaster. 

<b>Modify sticky bit</b>

<pre>$ sudo chmod +t mydir

$ sudo chmod 1755 mydir</pre>

The numerical representation for the sticky bit is <b>1</b>

## Exercise

What other files and directories do you think have a sticky bit enabled? 

## Quiz Question

What symbol represents the sticky bit?

## Quiz Answer

t