# Other languages and programs

## Lesson Content

Everything you have written so far has been a shell script: a list of commands in a file, run by bash. The shell is very good at one particular job, which is gluing other programs together — take these files, run that tool on each one, feed the output into the next thing. It is not good at arithmetic, statistics, or anything with much structure to it.

For that you use a real programming language, and in bioinformatics that usually means <b>Python</b> or <b>R</b>. You may also meet <b>Perl</b>, which is older and less fashionable but still underneath a lot of working bioinformatics software.

A rough division of labour: R for statistics and plots, Python for general programming and data wrangling, and the shell for orchestrating the tools that do the heavy lifting. Plenty of people argue about the boundaries. The useful thing to know is that they are all just programs on the server, and everything you have learned about paths, PATH, permissions and redirection applies to all of them equally.

<b>Interactive versus a script.</b> This is the distinction worth being clear about, because it confuses people for a long time.

Run a language with no file and you get an <i>interactive</i> session, a prompt of its own where you type one line at a time and see the result immediately:

<pre>
$ python3
Python 3.12.3
>>> 2 + 2
4
>>> exit()
$ </pre>

R does the same thing if you type R, and RStudio is a comfortable graphical wrapper around exactly that: a place to poke at your data, try something, look at a plot, adjust it. Note that the <b>&gt;&gt;&gt;</b> above is Python's prompt, not the shell's <b>$</b>. Beginners regularly type shell commands like ls at a Python prompt and get an error, or type python code at the shell and get command not found. If you are confused about why something will not run, look at the prompt and ask which program you are actually talking to. Ctrl-D gets you out of most of them and back to the shell.

Interactive work is excellent for exploring and hopeless for remembering. Nobody can reconstruct what you did last Tuesday from an interactive session. So once you know what you want, you put the same lines in a file and run it as a <i>script</i>:

<pre>
$ python3 analysis.py
$ Rscript analysis.R
</pre>

Now it is repeatable, it can go in version control, a colleague can run it, and you can run it over a hundred samples from a shell loop without sitting there. That progression — try it interactively, then write it down as a script — is how most analysis actually gets built.

You can give these scripts a shebang exactly like your bash scripts, and then run them by name:

<pre>
#!/usr/bin/env python3

print("hello")
</pre>

<pre>
$ chmod +x analysis.py
$ ./analysis.py
</pre>

The <b>#!/usr/bin/env python3</b> form is worth preferring over writing out a full path such as /usr/bin/python3, because it finds whichever python3 the shell would find if you typed it yourself. Once you start installing your own software, in the Your Environment section, that matters: it means your script uses your python rather than the system's.

<b>Compiled programs.</b> Python, R, Perl and bash are all <i>interpreted</i>: another program reads your file and does what it says, every time you run it. Languages like <b>C</b>, <b>C++</b> and <b>Rust</b> work differently. They are <i>compiled</i>: a compiler translates the source code once, ahead of time, into a file of machine instructions that the processor runs directly.

That file is a <b>binary</b>, and it is what most of the commands you have been using actually are. ls, grep and sort are compiled C programs. The file command, from the command line section, will tell you:

<pre>
$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, dynamically linked
</pre>

"ELF executable" means a compiled binary. Compare it with a script, where file reports the shebang instead.

The practical consequences for you:

<ul>
<li>Compiled programs are typically much faster, which is why aligners and variant callers are written in C or C++ rather than Python.</li>
<li>You cannot read one. Opening a binary with cat or nano gives you rubbish and may leave your terminal in a mess (run reset if that happens). A script is just text, so you can always read it and see what it does.</li>
<li>A binary is built for a particular kind of machine. A binary compiled for Linux on x86 will not run on your Mac, whereas the same Python script runs anywhere that has Python.</li>
<li>Some software is distributed as source code rather than as a ready-made binary, and has to be compiled before you can run it. That is a job, and it is exactly the pain that package managers spare you by shipping things already built.</li>
</ul>

None of this changes how you run them. Whether a command is a shell script, a Python script or a compiled binary, you type its name, it needs the execute bit set, and it has to be somewhere on your PATH. That is the whole point of the design: from the outside, they all look the same.

## Exercise

<ol>
<li>Start python3 with no arguments, do some arithmetic, then leave with Ctrl-D. Notice the prompt changing.</li>
<li>Put the same line in a file, run it with python3 yourfile.py, then add a shebang, chmod +x it, and run it as ./yourfile.py.</li>
<li>Run file on your script and on /bin/grep, and compare what it says about each.</li>
</ol>

## Quiz Question

What is the difference between an interpreted script and a compiled binary?

## Quiz Answer

a script is text that another program reads and executes each time; a binary was translated once by a compiler into machine instructions the processor runs directly