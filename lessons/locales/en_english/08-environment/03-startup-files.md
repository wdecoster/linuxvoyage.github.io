# Startup files

## Lesson Content

Everything you set in a shell, a PATH addition, an exported variable, a umask, lasts only until you log out. A <b>startup file</b> is how you make it stick. It is an ordinary file in your home directory containing shell commands, and bash runs it for you every time a shell starts.

The complication, and it is the source of a great deal of confusion, is that there is more than one such file, and which one bash reads depends on <i>how</i> the shell was started. Nearly every "I put it in my bashrc and it did not work" is really this.

<b>Three kinds of shell.</b> Bash cares about two questions: did this shell come from logging in, and is a human typing at it.

<pre>
how it started                          what bash calls it     what it reads
ssh server                              login shell            ~/.bash_profile, or ~/.profile
bash, screen, a second terminal         interactive shell      ~/.bashrc
ssh server 'samtools --version'         non-interactive        in effect, nothing
</pre>

The first two are the ones that matter day to day. When you ssh in, you get a login shell, and it does <b>not</b> read ~/.bashrc. When you then start screen, or type bash, you get an interactive shell, and it reads ~/.bashrc and none of the others. So a change can easily work in one and not the other.

<b>A login shell reads exactly one of the three.</b> It looks for ~/.bash_profile, then ~/.bash_login, then ~/.profile, and runs the first one that exists. Not all of them, the first. This trips people up: a machine works fine with the ~/.profile it shipped with, someone creates a ~/.bash_profile to hold one line, and everything that was in ~/.profile silently stops happening.

<b>Why ~/.bashrc usually works anyway.</b> Debian and Ubuntu ship a ~/.profile that reads ~/.bashrc itself:

<pre>
# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
</pre>

That dot is the <b>source</b> command under its older name. It means the login shell ends up reading ~/.bashrc after all, which is why the advice "put it in ~/.bashrc" holds on these systems. Check it on your server with:

<pre>$ grep bashrc ~/.profile</pre>

If that finds nothing, your login shells are not reading ~/.bashrc, and things you put there will not be set when you ssh in.

The same stock ~/.profile ends with a piece you have already met:

<pre>
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
</pre>

So on Ubuntu you often do not have to add ~/bin to your PATH at all. Creating the directory is enough. Note the condition though: the test runs at login, so a directory you make now is picked up at your <i>next</i> login, not in the shell you are sitting in.

<b>The system's files run first.</b> Before any of yours, a login shell reads /etc/profile and an interactive one reads /etc/bash.bashrc. These belong to the administrators and you cannot change them, but they explain things you will notice: the shape of the default prompt, the colours ls uses, and on Ubuntu the "To run a command as administrator (user root), use sudo" message. Your own file runs afterwards, so anything you set in it wins.

<b>What goes in a startup file.</b> Four things, in practice.

<ul>
<li><b>PATH and other exported variables</b>, as in the previous lesson: <b>export PATH=$HOME/bin:$PATH</b>.</li>
<li><b>Aliases</b>, from the command line section. This is the file the alias lesson told you to put them in. The stock ~/.bashrc already defines a few of its own, such as <b>alias ll='ls -alF'</b>, and that is where ll comes from if you have ever wondered.</li>
<li><b>umask</b>, which is what the permissions section promised would be explained here. Put <b>umask 007</b> in your ~/.bashrc and every file you create afterwards is 660 rather than 644, so your group can write to your files and nobody outside it can read them. On a shared server with a group per project this is worth setting deliberately.</li>
<li><b>Blocks that installers add for you.</b> The next lesson installs conda, which offers to append a dozen lines to your ~/.bashrc so its tools are on your PATH in new shells. That block is doing exactly what this lesson describes, written for you rather than by you.</li>
</ul>

<b>Aliases and umask are inherited differently, and it matters.</b> A umask is a property of the process, so a script you run inherits it:

<pre>
$ umask 007
$ ./analyse.sh
$ ls -l results.txt
-rw-rw---- 1 pete pete 0 Aug 24 13:27 results.txt
</pre>

An alias is not. It is a shell convenience that is never passed on, so the same alias that works when you type it is a command not found inside a script:

<pre>
$ ll
total 16
drwxrwxr-x 2 pete pete 4096 Aug 24 13:27 ./
drwx------ 4 pete pete 4096 Aug 24 13:27 ../
-rwxrwxr-x 1 pete pete   15 Aug 24 13:27 myscript.sh*
-rw-rw-r-- 1 pete pete   13 Aug 24 13:27 notes.txt
$ ./myscript.sh
./myscript.sh: line 2: ll: command not found
</pre>

Write out the real command in scripts. An alias is for your fingers, not for anything that has to run somewhere else.

<b>Never print anything unconditionally.</b> Look at the first lines of the stock ~/.bashrc:

<pre>
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
</pre>

That says: if this shell has no human at it, stop reading this file now. It is there for a real reason. Bash reads ~/.bashrc when sshd runs a command on your behalf, and scp, rsync and sftp all work by running a command over ssh and speaking a protocol on that connection. Anything your ~/.bashrc prints goes into that conversation and corrupts it. The symptom is memorable: interactive ssh is completely fine, and scp fails with a protocol error that says nothing about your shell. So add your lines at the <b>end</b> of the file, below that check, and if you want a welcome banner, know what you are trading for it.

<b>Rereading a file you changed.</b> A startup file is read when the shell starts, so the shell you are in now has not seen your change. Either open a new one, or reread it in place:

<pre>$ source ~/.bashrc</pre>

<b>source</b> runs the file in your current shell, which is the whole point: a variable set by a separate shell would vanish when that shell exited. This is also why you cannot simply run the file. It has no execute permission and no shebang, and ./.bashrc only gets you a Permission denied.

<b>Do not lock yourself out.</b> A mistake in ~/.bashrc affects every new shell, including every new ssh login, so it is entirely possible to make yourself unable to log in comfortably. Two habits:

<ol>
<li>Keep your current session open while you test. Open a <i>second</i> connection to check the change, and only close the first once the second works.</li>
<li>If you do break it, a remote command usually still runs, because that path stops at the check above. From your own machine, <b>ssh server 'mv ~/.bashrc ~/.bashrc.broken'</b> will normally put you back to a working login.</li>
</ol>

## Exercise

<ol>
<li>List the startup files you actually have with ls -a ~ and see which of ~/.bashrc, ~/.profile and ~/.bash_profile exist.</li>
<li>Run grep bashrc ~/.profile and work out whether your login shells read ~/.bashrc.</li>
<li>Add an alias to the end of ~/.bashrc, run source ~/.bashrc, and check it works. Then put the same alias in a small script, run the script, and confirm it does not.</li>
<li>Add umask 007 to the end of ~/.bashrc, open a new shell, create a file, and compare its permissions to one you made before.</li>
</ol>

## Quiz Question

You add a line to ~/.bashrc, but it has no effect when you ssh in. Why not?

## Quiz Answer

An ssh login starts a login shell, which reads ~/.bash_profile or ~/.profile rather than ~/.bashrc. It only picks up ~/.bashrc if one of those files sources it, as the stock Ubuntu ~/.profile does.
