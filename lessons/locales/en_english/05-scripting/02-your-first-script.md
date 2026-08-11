# Your first script

## Lesson Content

Once you have typed the same three commands for the fourth time, it is time to put them in a file. A shell script is nothing more exotic than that: a list of commands, saved, so you can run them again without retyping.

Open a new file with nano:

<pre>$ nano count_reads.sh</pre>

and put this in it:

<pre>
#!/bin/bash

echo "counting reads"
wc -l reads.fastq
echo "done"
</pre>

The .sh ending is only a convention to help humans. What actually matters is the first line.

<b>#!/bin/bash</b> is called the shebang. Those first two characters tell the kernel that this file is not a program itself, it is a script, and the rest of the line says which interpreter should run it. Without it the system has to guess, and you may get a different shell than the one you wrote for.

Everywhere else, a # starts a comment and the rest of the line is ignored. Use them.

Now try to run it:

<pre>$ ./count_reads.sh
bash: ./count_reads.sh: Permission denied</pre>

This is the payoff of the permissions section. New files are not executable, because it would be a bad idea if they were. Add the execute bit:

<pre>
$ chmod +x count_reads.sh
$ ./count_reads.sh
counting reads
...
done
</pre>

Why <b>./</b> in front? Because when you type a bare command name, the shell only looks for it in a fixed list of system directories, and the directory you are standing in is deliberately not one of them. Writing ./count_reads.sh says "the file right here", rather than asking the shell to go looking. That list is called $PATH, and the section on your environment covers how to change it.

A script that always counts the same file is not very useful. You can pass arguments to it, and inside the script they arrive as $1, $2 and so on:

<pre>
#!/bin/bash

# $1 is the first thing typed after the script name
echo "counting reads in $1"
wc -l "$1"
</pre>

<pre>
$ ./count_reads.sh sample1.fastq
counting reads in sample1.fastq
4000 sample1.fastq
</pre>

Note the quotes around "$1". If someone hands your script a filename with a space in it, unquoted $1 falls apart in exactly the way you saw earlier.

A couple of other useful ones: <b>$0</b> is the name of the script itself, and <b>$#</b> is how many arguments were given. That lets you catch the case where somebody forgets to pass one. The syntax below is covered properly in the conditionals lesson shortly, so read it as "if fewer than one argument was given, complain and stop" and do not worry about the brackets yet:

<pre>
#!/bin/bash

if [ $# -lt 1 ]; then
    echo "usage: $0 FASTQ_FILE"
    exit 1
fi

wc -l "$1"
</pre>

## Exercise

<ol>
<li>Write a script that prints a message and runs pwd and ls.</li>
<li>Try to run it, get the Permission denied error, then fix it with chmod +x.</li>
<li>Change it to take a directory as $1 and list that directory instead.</li>
</ol>

## Quiz Question

What do you call the #!/bin/bash line at the top of a script?

## Quiz Answer

the shebang