# PATH and export

## Lesson Content

In the previous lesson you saw that $PATH is the list of directories the shell searches when you type a command name. It is worth understanding properly, because "I installed it but the shell says command not found" is something you will hit again and again.

<pre>
$ echo $PATH
/usr/local/bin:/usr/bin:/bin
</pre>

When you type samtools, the shell looks in /usr/local/bin, then /usr/bin, then /bin, and runs the first match it finds. If it looks in all of them and finds nothing, you get command not found. The directory you are currently standing in is <b>not</b> on that list, which is why running your own script needs the ./ prefix.

Two commands tell you what is going on. <b>which</b> shows you which one the shell would actually run:

<pre>
$ which samtools
/usr/local/bin/samtools
</pre>

and <b>type -a</b> shows <i>all</i> the matches, in search order, which is how you diagnose the case where you have two versions installed and are getting the wrong one:

<pre>
$ type -a python
python is /home/pete/miniconda3/bin/python
python is /usr/bin/python
</pre>

The first line wins. Order matters: earlier directories in PATH shadow later ones.

To add a directory, assign a new value that includes the old one:

<pre>$ PATH=$HOME/bin:$PATH</pre>

Read that carefully. It puts $HOME/bin at the front, then a colon, then everything that was already there. Keeping the old $PATH is the whole trick. If you write PATH=$HOME/bin and forget the rest, you have just thrown away every directory the system needs, and almost nothing will work until you open a new shell.

Putting your directory first means yours wins over the system version. Putting it last, PATH=$PATH:$HOME/bin, means the system version wins. Choose deliberately.

Now, the <b>export</b> part. A plain assignment only affects your current shell. Programs you start do not see it:

<pre>
$ MYVAR=hello
$ bash -c 'echo $MYVAR'

$ export MYVAR=hello
$ bash -c 'echo $MYVAR'
hello
</pre>

export marks a variable to be passed on to any program the shell starts. Since PATH needs to be seen by everything, it is always exported:

<pre>$ export PATH=$HOME/bin:$PATH</pre>

There is still one thing missing. Everything above lasts only until you log out. To make it permanent, put the line in the file bash reads when it starts, which is <b>~/.bashrc</b>:

<pre>$ nano ~/.bashrc</pre>

and add at the end:

<pre>export PATH=$HOME/bin:$PATH</pre>

The file is only read when a shell starts, so your current shell will not notice. Either open a new one, or reread it now:

<pre>$ source ~/.bashrc</pre>

<b>source</b> runs the file in your current shell rather than in a new one, which is exactly what you want here. Running it as ./.bashrc would start a separate shell, set the variable there, and then throw it away.

A word of caution: a mistake in ~/.bashrc affects every new shell you open, including new ssh logins, and it is possible to break your own access. Keep an existing session open while you test changes, so you have a way back in.

## Exercise

<ol>
<li>Print your PATH and count the directories in it.</li>
<li>Run type -a on a command you use, such as python, and see whether there is more than one.</li>
<li>Make a bin directory in your home, put a small script in it, add it to your PATH in ~/.bashrc, run source ~/.bashrc, and confirm you can run the script by name from anywhere.</li>
</ol>

## Quiz Question

Which command makes a variable visible to programs that the shell starts?

## Quiz Answer

export