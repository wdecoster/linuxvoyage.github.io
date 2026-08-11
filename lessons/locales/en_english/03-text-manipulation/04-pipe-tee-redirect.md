# pipe and tee

## Lesson Content

Let's get into some plumbing now, not really but kinda. Let's try a command: 

<pre>$ ls -la /etc</pre>

You should see a very long list of items, it's a little hard to read actually. Instead of redirecting this output to a file, wouldn't it be nice if we could just see the output in another command like less? Well we can!

<pre>$ ls -la /etc | less </pre>

The pipe operator |, represented by a vertical bar, allows us to get the stdout of a command and make that the stdin to another process. In this case, we took the stdout of ls -la /etc and then <i>piped</i> it to the less command. The pipe command is extremely useful and we will continue to use it for all eternity. 

One thing to be aware of: <b>a pipe carries stdout only</b>. Standard error is not piped, it goes straight to your screen as usual. So if a program reports its progress or its warnings on stderr, that text will not reach the next command, and it will not end up in a file if you redirect the far end of the pipeline. This surprises people regularly, because the pipeline looks like it worked while the interesting message went somewhere else.

If you do want the errors to travel through the pipe as well, send stderr to stdout first, using the 2>&1 you saw in the stderr lesson:

<pre>$ mycommand 2>&1 | less</pre>

Well what if I wanted to write the output of my command to two different streams? That's possible with the tee command: 

<pre>$ ls | tee peanuts.txt</pre>

You should see the output of ls on your screen and if you open up the peanuts.txt file you should see the same information!

## Exercise

Try the following commands: 
<pre>$ ls | tee peanuts.txt banan.txt</pre>

## Quiz Question

What key represents the pipe operator?

## Quiz Answer

|