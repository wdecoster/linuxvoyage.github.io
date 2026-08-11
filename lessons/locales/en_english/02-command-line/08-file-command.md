# file

## Lesson Content

In the previous lesson we learned about touch, let’s go back to that for a bit. Did you notice that the filename didn’t conform to standard naming like you’ve probably seen with other operating systems like Windows? Normally you would expect a file called banana.jpeg and expect a JPEG picture file. 

In Linux, filenames aren’t required to represent the contents of the file. You can create a file called funny.gif that isn’t actually a GIF. 

To find out what kind of file a file is, you can use the file command. It will show you a description of the file’s contents.

<pre>$ file banana.jpg</pre>

Try it on things that actually exist on your machine. The answers are more interesting than you might expect:

<pre>
$ file /etc/services
/etc/services: ASCII text

$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, dynamically linked

$ file /home
/home: directory
</pre>

Do not worry about the detail in the middle answer. The point is that file looked inside and worked out what the thing is, without trusting its name.

## Exercise

Run the file command on a few different directories and files and note the output.

## Quiz Question

What command can you use to find the file type of a file?

## Quiz Answer

file