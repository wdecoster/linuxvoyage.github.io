# Interrupting commands

## Lesson Content

At some point, quite soon, you will run a command that does not stop. Maybe you left off a filename and it is sitting there waiting for input, maybe you asked it to search the entire filesystem, maybe it is just slower than you expected. The prompt does not come back and typing does nothing useful.

The way out is <b>Ctrl-C</b>.

<pre>
$ find / -name "*.fastq"
... pages and pages of output ...
^C
$ </pre>

Ctrl-C sends the running program an interrupt signal, asking it to stop. Most programs take the hint and exit, and you get your prompt back. It is the single most useful key combination in the terminal, and it is worth pressing deliberately a few times now so it becomes automatic later.

Note that it interrupts the program, not the shell. You will not be logged out and you will not lose your session.

A close relative is <b>Ctrl-D</b>, which is not the same thing at all. Ctrl-D means end of input. If a command is reading from the keyboard, Ctrl-D tells it there is nothing more coming:

<pre>
$ cat > notes.txt
some text I am typing
^D
$ </pre>

Here cat was waiting for input, and Ctrl-D ended it cleanly and wrote the file. Ctrl-C would have interrupted it instead. At an empty shell prompt, Ctrl-D means "no more input for the shell", which logs you out, exactly like typing exit.

Then there is <b>Ctrl-Z</b>, which suspends the program rather than killing it:

<pre>
$ wc -l enormous.fastq
^Z
[1]+  Stopped                 wc -l enormous.fastq
$ </pre>

The program is still there, frozen, doing nothing. You get your prompt back and can carry on. To pick it up again:

<pre>
$ fg
</pre>

and it continues in the foreground, as if nothing happened. Ctrl-Z is how you get out of "I need my prompt for one second but I do not want to lose this", and it leads directly into the next lesson on background jobs.

Occasionally Ctrl-C does not work, because a program can choose to ignore the interrupt. If that happens, Ctrl-Z to suspend it, then get rid of it properly with kill, which is covered a few lessons from now.

<ul>
<li>Ctrl-C - interrupt, stop the running command</li>
<li>Ctrl-D - end of input, or log out at an empty prompt</li>
<li>Ctrl-Z - suspend the running command, resume it with fg</li>
</ul>

## Exercise

<ol>
<li>Run find / -name "*.conf" and stop it with Ctrl-C.</li>
<li>Run cat with no arguments, type a couple of lines, and end it with Ctrl-D.</li>
<li>Run a slow command, suspend it with Ctrl-Z, run ls, then bring it back with fg.</li>
</ol>

## Quiz Question

Which key combination interrupts a running command?

## Quiz Answer

Ctrl-C