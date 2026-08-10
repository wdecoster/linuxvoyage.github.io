# Installing your own tools

## Lesson Content

The packages section of this course covers apt and yum, and both of them need sudo. On a shared server you almost certainly do not have it, and you should not expect to get it. That does not stop you installing software, it just means installing it into your own home directory instead of into the system.

There are three routes you will meet.

<b>Modules.</b> Many shared servers already have a lot of software installed, hidden until you ask for it, managed by a tool called module or Lmod. This is always worth checking first, because it is free and the versions are maintained for you:

<pre>
$ module avail            what is available
$ module load samtools    add it to your environment
$ module list             what you have loaded
$ module unload samtools
</pre>

What module load actually does is adjust your PATH, which is why the previous lesson matters. Loaded modules last for the current session only, so if you need one every time, put the load line in your ~/.bashrc.

<b>Conda.</b> When the software you need is not already there, conda is the usual answer. It installs into your home directory, needs no admin rights, and handles dependencies. Miniconda or its faster relatives are installed by downloading an installer and running it:

<pre>
$ bash Miniconda3-latest-Linux-x86_64.sh
</pre>

The installer offers to modify your ~/.bashrc so that conda is on your PATH in new shells. The important idea is the environment: rather than one big pile of software, you make a separate environment per project, so that a tool needing an old version of Python cannot break another one that needs a new version.

<pre>
$ conda create -n myproject python=3.12
$ conda activate myproject
$ conda install -c bioconda samtools
$ conda deactivate
</pre>

When an environment is active your prompt usually shows its name, which is a useful reminder of which set of tools you are currently using. If a command works for a colleague and not for you, "which environment are you in" is a good first question.

<b>By hand.</b> Sometimes you just have a program, and you want it available. Put it in a bin directory in your home and add that to your PATH, as in the previous lesson:

<pre>
$ mkdir -p ~/bin
$ cp mytool ~/bin/
$ chmod +x ~/bin/mytool
$ export PATH=$HOME/bin:$PATH
</pre>

Whichever route you take, the underlying mechanism is the same: something ends up in a directory, and that directory ends up on your PATH. Modules and conda are convenient ways of doing that bookkeeping for you. When something mysteriously stops working, echo $PATH and type -a are almost always the fastest way to see what happened.

A note on where things go. Your home directory is often small, and quota limits are easy to hit once you have several conda environments, which are not small. Servers usually provide a larger scratch or project area. Find out where yours is before you fill up your home directory, because a full home directory tends to break things in confusing ways.

## Exercise

<ol>
<li>Check whether your server has modules, with module avail.</li>
<li>If conda is available, create an environment, activate it, and check that your prompt changes.</li>
<li>Run which and type -a on a tool before and after loading it, and see the PATH change take effect.</li>
</ol>

## Quiz Question

Why can you not usually use apt or yum to install software on a shared server?

## Quiz Answer

they need sudo, which you do not have