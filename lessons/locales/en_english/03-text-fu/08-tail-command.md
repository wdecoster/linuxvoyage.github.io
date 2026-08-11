# tail

## Lesson Content

Similar to the head command, the tail command lets you see the last 10 lines of a file by default.

<pre>$ tail /etc/services</pre>

Along with head you can change the number of lines you want to see.

<pre>$ tail -n 10 /etc/services</pre>

Another great option you can use is the -f (follow) flag, this will follow the file as it grows. Give it a try and see what happens. 

<pre>$ tail -f mylogfile.txt</pre> 

If the file is one that something is still writing to, such as the log of a job you have running, tail -f shows you each new line as it arrives. Note that tail -f does not stop on its own: it sits there waiting for more, which is the point. Press Ctrl-C when you have seen enough.

On many systems you can watch this happen with a system log, such as /var/log/syslog, though on a shared server you will often not have permission to read those.

## Exercise

Look at the man page of tail and read some of the other commands we didn't discuss. 

<pre>$ man tail</pre>

## Quiz Question

What is the flag used to follow a file in tail?

## Quiz Answer

-f