# screen sessions

## Lesson Content

Here is the problem this lesson solves. You ssh to the server, start something that takes three hours, and go home. Your laptop sleeps, the connection drops, and the job dies. Or the wifi hiccups for two seconds and takes your work with it.

<b>screen</b> fixes this by putting your shell somewhere that does not belong to your ssh connection. The session lives on the server. You attach to it, do some work, detach, close your laptop, come back tomorrow from a different machine and attach again. Everything is exactly where you left it, still running.

Start one:

<pre>$ screen -S alignment</pre>

The <b>-S</b> gives it a name, which you will thank yourself for later. The screen clears and you get a normal shell prompt. It looks like nothing happened, but you are now inside a session called alignment. Start your long job here as usual.

To leave it running and get back to your ordinary shell, press <b>Ctrl-A</b> then <b>d</b>:

<pre>
[detached from 12345.alignment]
$ </pre>

That is the one piece of screen you have to remember. Ctrl-A is screen's attention key: you press it, let go, and then press the actual command key. Ctrl-A then d means detach.

Now you can log out entirely. The job keeps running. When you come back:

<pre>
$ screen -ls
There is a screen on:
        12345.alignment	(10/08/2026 14:22:31)	(Detached)

$ screen -r alignment
</pre>

<b>screen -ls</b> lists your sessions and <b>screen -r</b> reattaches to one. With only one session, plain screen -r is enough.

When the work is genuinely done, exit the shell inside the session as normal, with exit or Ctrl-D. The session ends and disappears from screen -ls. Detaching leaves it running; exiting closes it.

A few more keys, all after Ctrl-A:

<ul>
<li>Ctrl-A then d - detach, leaving everything running</li>
<li>Ctrl-A then c - create another window inside the session</li>
<li>Ctrl-A then n - switch to the next window</li>
<li>Ctrl-A then " - list the windows and pick one</li>
<li>Ctrl-A then ? - show all the key bindings</li>
</ul>

Windows are handy once you are comfortable: one for the job that is running, one for poking around at the output, without opening a second ssh connection.

Compared with nohup from the last lesson, screen is the better tool for interactive work. nohup fires something off and you can only look at the log afterwards, while a screen session is a real terminal you can come back to, type in, and watch.

You may also hear about <b>tmux</b>, which does the same job with more features and a more modern feel. If your server has it and you like it, use it. screen is on essentially every machine you will ever meet and takes about three keystrokes to learn, which is why we start here.

One habit worth forming: get into screen <i>before</i> you start the long job, not after. Moving an already running command into a session afterwards is fiddly at best, and usually not possible at all.

## Exercise

<ol>
<li>Start a named session with screen -S test and run a command that prints something every few seconds.</li>
<li>Detach with Ctrl-A then d, log out of the server completely, then log back in and reattach with screen -r test.</li>
<li>List your sessions with screen -ls, then end the session properly with exit.</li>
</ol>

## Quiz Question

Which keys detach you from a screen session while leaving it running?

## Quiz Answer

Ctrl-A then d