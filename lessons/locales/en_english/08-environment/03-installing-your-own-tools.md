# Installing your own tools

## Lesson Content

The packages section later in this course covers apt and yum, the usual way software gets installed on Linux. Both need sudo. On a shared server you almost certainly do not have it, and you should not expect to get it.

That does not stop you installing anything. It just means installing into your own home directory rather than into the system, and the tool for that is <b>conda</b>.

<b>Conda</b> installs software as a normal user, needs no admin rights, and works out dependencies for you. Fetch the installer onto the server with wget, from the previous section, and run it:

<pre>
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
</pre>

The installer asks a few questions and offers to modify your ~/.bashrc so that conda is on your PATH in new shells. Say yes. Then open a new shell, or run source ~/.bashrc, and conda is available.

<b>Environments are the important idea.</b> An environment is a self-contained set of installed software. You can have several, they do not see each other, and you switch between them.

Here is the problem they solve. Say one tool you need was written years ago and only works with Python 3.8. Another is actively developed and needs Python 3.12. If everything is installed in one pile, these two requirements cannot both be satisfied, and installing the second tool quietly breaks the first. This is not a rare edge case, it is a normal Tuesday in bioinformatics, and it is worse than it sounds because the breakage often shows up as a confusing error in a tool you were not touching.

With environments, each project gets its own:

<pre>
$ conda create -n oldpipeline python=3.8
$ conda create -n myproject python=3.12
</pre>

Activate the one you want, and your PATH is rearranged so that environment's software comes first:

<pre>
$ conda activate myproject
(myproject) $ conda install -c bioconda samtools
(myproject) $ conda deactivate
$ </pre>

Notice the prompt. When an environment is active its name appears in front, which is a constant reminder of which set of tools you are using. When a command works for a colleague and not for you, "which environment are you in" is a very good first question. If a command is not found and you expected it to be, check with conda env list and conda activate the right one before assuming anything is broken.

The <b>-c bioconda</b> above says which channel to install from. Channels are collections of packages, and most bioinformatics software lives in bioconda rather than in the default channel. You will type it a lot.

A few habits worth forming early:

<ul>
<li>One environment per project, not one big environment for everything. They are cheap to make and painful to untangle.</li>
<li>Record what you used. conda env export &gt; environment.yml writes out the exact set of packages and versions, and conda env create -f environment.yml rebuilds it. This is what makes your analysis reproducible six months later, and it is the difference between a result you can defend and one you cannot.</li>
<li>Watch your disk. Environments are not small, home directories usually are. If your server has a scratch or project area, put your environments there and check where before you fill your home directory up, because a full home directory breaks things in confusing ways.</li>
</ul>

<b>Modules.</b> Some shared servers also have a module system, which exposes software the administrators have already installed. It is worth knowing it exists, since it costs nothing to check:

<pre>
$ module avail
$ module load samtools
$ module list
</pre>

Loading a module simply adjusts your PATH, which is why the previous lesson matters. The catch is that you get whichever versions the administrators chose, which may not be the ones your analysis needs, and you cannot record a module list as precisely as an environment file. Useful for common tools, not a substitute for managing your own environments.

<b>By hand.</b> Occasionally you just have a single program and want to run it. Put it in a bin directory in your home and add that to your PATH:

<pre>
$ mkdir -p ~/bin
$ cp mytool ~/bin/
$ chmod +x ~/bin/mytool
$ export PATH=$HOME/bin:$PATH
</pre>

Whichever route you take, the mechanism underneath is the same one from the previous lesson: something lands in a directory, and that directory goes on your PATH. When software mysteriously stops working, echo $PATH and type -a are almost always the fastest way to see what happened.

## Exercise

<ol>
<li>Install conda if it is not already there, and check it works with conda --version.</li>
<li>Create an environment with a specific Python version, activate it, and confirm your prompt changes and python --version matches what you asked for.</li>
<li>Run conda env export in that environment and look at the file it produces.</li>
<li>Deactivate, and check that python --version goes back to what it was.</li>
</ol>

## Quiz Question

Why would you put two tools in separate conda environments?

## Quiz Answer

because they need different versions of something, such as Python, and cannot both be satisfied in one environment