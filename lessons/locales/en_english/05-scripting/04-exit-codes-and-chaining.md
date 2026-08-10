# Exit codes and chaining

## Lesson Content

Every command that finishes hands back a number saying whether it worked. You do not normally see it, but the shell keeps it in a special variable called <b>$?</b>.

<pre>
$ ls /home
pete
$ echo $?
0

$ ls /fake/directory
ls: cannot access '/fake/directory': No such file or directory
$ echo $?
2
</pre>

<b>Zero means success.</b> Anything other than zero means something went wrong. This is backwards from what most people expect, so it is worth saying twice: 0 is good. There is only one way to succeed, but many ways to fail, which is why the failure codes vary.

Because the shell can see this number, you can chain commands together based on it.

<b>&&</b> runs the next command only if the previous one succeeded:

<pre>$ mkdir results && cd results</pre>

If mkdir fails, the cd never happens. Compare that with using a semicolon, which just runs both regardless:

<pre>$ mkdir results ; cd results</pre>

That version tries to cd even when the directory was not created, and you end up somewhere you did not expect. When the second command depends on the first, use &&.

<b>||</b> is the opposite, and runs the next command only if the previous one <i>failed</i>:

<pre>$ cd /data/project || echo "could not find the project directory"</pre>

You will see this most often as a guard in scripts.

Inside a script you set your own exit code with <b>exit</b>:

<pre>
#!/bin/bash

if [ ! -f "$1" ]; then
    echo "no such file: $1"
    exit 1
fi

wc -l "$1"
</pre>

exit 1 stops the script and reports failure, so whoever runs it, or whatever pipeline calls it, can tell that it did not work. A script that fails silently with exit code 0 is a genuinely nasty thing to debug.

There is one trap worth knowing. In a pipeline, $? is the exit code of the <b>last</b> command only:

<pre>$ cat missing.fastq | wc -l
cat: missing.fastq: No such file or directory
0
$ echo $?
0</pre>

cat failed, but wc succeeded at counting nothing, so the pipeline reports success. This is the same theme as stderr not travelling through a pipe: a pipeline can look fine while something in the middle of it went wrong. When a script matters, check the pieces rather than trusting the end of the chain.

## Exercise

<ol>
<li>Run a command that works and one that fails, checking echo $? after each.</li>
<li>Compare mkdir somedir && cd somedir with mkdir somedir ; cd somedir when somedir already exists.</li>
<li>Add an exit 1 to a script and confirm the exit code with echo $? after running it.</li>
</ol>

## Quiz Question

What exit code does a command return when it succeeds?

## Quiz Answer

0