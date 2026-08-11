# ls (List Directories)

## Lesson Content

Now that we know how to move around the system, how do we figure out what is available to us? Right now it’s like we are moving around in the dark. Well, we can use the wonderful ls command to list directory contents. The ls command will list directories and files in the current directory by default, however you can specify which path you want to list the directories of.

<pre>$ ls
$ ls /home/pete</pre>

ls is a quite useful tool, it also shows you detailed information about the files and directories you are looking at.

Also note that not all files in a directory will be visible. Filenames that start with . are hidden, you can view them however with the ls command and pass the -a flag to it (a for all). 

<pre>$ ls -a</pre>

There is also one more useful ls flag, -l for long, which shows a detailed list of files in a long format. 

<pre>$ ls -l</pre>

<pre>pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos</pre>

That is a lot at once, so here is what each part is, reading a line from left to right:

<pre>
drwxr-x---  7  pete  penguingroup  4096  Nov 20 16:37  Desktop
    |       |    |        |          |        |          |
    |       |    |        |          |        |          `- name
    |       |    |        |          |        `- last changed
    |       |    |        |          `- size in bytes
    |       |    |        `- which group it belongs to
    |       |    `- who owns it
    |       `- number of links (ignore this for now)
    `- type and permissions
</pre>

Two of those need a word now and a proper explanation later.

The first column is the one you will come to care about. The very first character is the <b>type</b>: <b>d</b> for a directory and <b>-</b> for an ordinary file. The nine characters after it are the <b>permissions</b>, saying who is allowed to read, write and run this thing. There is a whole section on them later; for now, just notice that directories start with d.

The <b>size</b> is in bytes, which gets hard to read once files are large. Add <b>-h</b> for human readable and you get 4.0K and 1.2G instead:

<pre>$ ls -lh</pre>

You will also see a line at the very top saying something like <b>total 80</b>. That is the amount of disk space used by the listed items, in blocks, and it is safe to ignore. The same goes for the number of links column, which almost never matters in day to day work.

Commands have things called flags (or arguments or options, whatever you want to call it) to add more functionality. See how we added -a and -l, well you can add them both together with -la. The order of the flags determines which order it goes in, most of the time this doesn’t really matter so you can also do ls -al and it would still work.

<pre>$ ls -la</pre>

## Exercise

Run ls with different flags and see the output you receive.

## Quiz Question

What command would you use to see hidden files?

## Quiz Answer

ls -a