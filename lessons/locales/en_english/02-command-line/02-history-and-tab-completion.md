# Tab completion and history

## Lesson Content

Before we go any further, two features that will save you more typing than everything else in this course put together. They come this early on purpose: there is no point learning to type long paths by hand when the shell will do it for you.

<b>Tab completion.</b> Start typing the beginning of a command, a file or a directory, press the <b>Tab</b> key, and the shell fills in the rest.

<pre>$ cd Doc<b>[Tab]</b>
$ cd Documents/</pre>

If what you typed is enough to identify one thing, it completes it. If several things match, nothing appears to happen, and pressing Tab a second time lists the candidates so you can type another letter or two and try again.

This is not just about saving keystrokes. A completed name is a name that exists and is spelled correctly, so a great many "No such file or directory" errors simply never happen. Get into the habit now: type a few characters, press Tab, and only type the whole thing out when Tab refuses.

<b>Command history.</b> The shell remembers what you have already run. The up arrow walks back through it, and the down arrow forwards again, so repeating your last command is one keystroke.

To see the whole list:

<pre>$ history</pre>

Want to run the previous command again without typing it? Use !!. If you typed cat file1 and want to run it again, you can just go !! and it will run the last command you ran.

The most useful one is <b>Ctrl-R</b>, reverse search. Press it and start typing any part of a command you ran earlier, and the shell finds the most recent match. Press Ctrl-R again to step back through older matches, and press Enter to run the one you want. Once you have a few hundred commands behind you, this is much faster than scrolling with the arrow keys.

Our terminal is getting a little cluttered no? Let’s do a little cleanup, use the clear command to clear up your display.

<pre>$ clear</pre>

There that looks better doesn’t it?

## Exercise

<ol>
<li>Type the first two or three letters of a directory in your home and complete it with Tab.</li>
<li>Press Tab twice on something ambiguous, like just c, and look at the list of candidates.</li>
<li>Run a few commands, then find one of them again with Ctrl-R instead of the arrow keys.</li>
</ol>

## Quiz Question

Which key completes a partly typed command or filename?

## Quiz Answer

Tab