# Interrupting commands

## Lesson Content

At some point, quite soon, you will run a command that does not stop. Maybe you left off a filename and it is sitting there waiting for input, maybe you asked it to search the entire filesystem, maybe it is just slower than you expected. The prompt does not come back and typing does nothing useful.

The way out is <b>Ctrl-C</b>.

<pre>
$ cat /etc/services
... pages and pages of text scrolling past ...
^C
$ </pre>

Ctrl-C sends the running program an interrupt signal, asking it to stop. Most programs take the hint and exit, and you get your prompt back. It is the single most useful key combination in the terminal, and it is worth pressing deliberately a few times now so it becomes automatic later.

Note that it interrupts the program, not the shell. You will not be logged out and you will not lose your session.

Some commands do not scroll at all, they simply sit there with the cursor blinking and no prompt, as though the terminal has died. Usually that means the command is waiting for you to type something at it. Ctrl-C gets you out of those too.

A close relative is <b>Ctrl-D</b>, which is not the same thing at all. Ctrl-D means end of input. If a command is waiting for you to type at it, Ctrl-D says there is nothing more coming, and it stops politely rather than being interrupted:

<pre>
$ cat > notes.txt
some text I am typing
^D
$ </pre>

Here cat was waiting for input, and Ctrl-D ended it cleanly and wrote the file. Ctrl-C would have interrupted it instead. At an empty shell prompt, Ctrl-D means "no more input for the shell", which logs you out, exactly like typing exit.

Then there is <b>Ctrl-Z</b>, which suspends the program rather than killing it:

<pre>
$ cat /etc/services
^Z
[1]+  Stopped                 cat /etc/services
$ </pre>

The program is still there, frozen, doing nothing. You get your prompt back and can carry on. To pick it up again:

<pre>
$ fg
</pre>

and it continues where it left off, as if nothing had happened. Ctrl-Z is how you get out of "I need my prompt for one second but I do not want to lose this". There is a whole section on Jobs and Processes later that does more with this.

Occasionally Ctrl-C does not work, because a program can choose to ignore the interrupt. If that happens, Ctrl-Z will usually still suspend it, and the Jobs and Processes section later covers how to get rid of it for good.

None of these will log you out or damage anything. They are the normal way to stop a command, and you will use Ctrl-C many times a day.

<ul>
<li>Ctrl-C - interrupt, stop the running command</li>
<li>Ctrl-D - end of input, or log out at an empty prompt</li>
<li>Ctrl-Z - suspend the running command, resume it with fg</li>
</ul>

## Exercise

<ol>
<li>Run cat /etc/services, watch it scroll, and stop it with Ctrl-C.</li>
<li>Run cat on its own with nothing after it. It will sit there waiting for you. Type a couple of lines, then press Ctrl-D and watch it finish.</li>
<li>Do the same again, but press Ctrl-C instead of Ctrl-D, and note that you get the prompt back either way.</li>
</ol>

## Quiz Question

Which key combination interrupts a running command?

## Quiz Answer

Ctrl-C