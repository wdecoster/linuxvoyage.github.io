# head

## Lesson Content

Let's say we have a very long file. A good one to practise on is /etc/services, which every Linux machine has and every user can read. Go ahead and cat it, and you should see pages upon pages of text go past. (If it is still scrolling, Ctrl-C stops it.) What if I just wanted to see the first couple of lines? Well we can do that with the head command, by default the head command will show you the first 10 lines in a file.

<pre>$ head /etc/services</pre>

You can also modify the line count to whatever you choose, let's say I wanted to see the first 15 lines instead. 

<pre>$ head -n 15 /etc/services</pre>

The -n flag stands for number of lines. 

## Exercise

What does the following command do and why? 

<pre>$ head -c 15 /etc/services</pre>

## Quiz Question

What flag would you use to change the number of lines you want to view for the head command?

## Quiz Answer

-n