# cat

## Lesson Content

We’re almost done navigating files, but first let’s learn how to read a file. A simple command to use is the cat command, short for concatenate, it not only displays file contents but it can combine multiple files and show you the output of them. 

<pre>$ cat dogfile birdfile</pre>

Those two names are just examples. To try it for real, make yourself a file first:

<pre>
$ echo "the dog barks" > dogfile
$ echo "the bird sings" > birdfile
$ cat dogfile birdfile
</pre>

It’s not great for viewing large files and it’s only meant for short content. There are many other tools that we use to view larger text files that we’ll discuss in the next lesson.

## Exercise

Make a couple of small files as above and cat them, first one at a time and then both at once. Then try cat on a directory, such as cat /home, and note that it refuses: cat is for files, and the error message says so.

## Quiz Question

What's a good way to see the contents of a file?

## Quiz Answer

cat