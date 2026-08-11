# Running many jobs

## Lesson Content

You know how to run a command on every file in a directory:

<pre>
for f in *.fastq
do
    mytool "$f" > "$(basename "$f" .fastq).out"
done
</pre>

That loop runs them <b>one after another</b>. With four samples, fine. With four hundred, each taking ten minutes, that is nearly three days of the server doing one thing at a time while fifteen of its sixteen processors sit idle.

The saving grace is that these jobs usually do not depend on each other. Sample 7 does not need sample 6 to finish first. Work like that is called <i>embarrassingly parallel</i>, and it is most of what bioinformatics does.

<b>GNU parallel</b> runs the same command on many inputs at once. In its simplest form it looks like a loop turned inside out:

<pre>$ parallel mytool {} ::: *.fastq</pre>

The <b>{}</b> is where each input gets substituted, and <b>:::</b> separates the command from the list of things to run it on. By default parallel uses one job per processor core. Say how many you want with <b>-j</b>:

<pre>$ parallel -j 4 mytool {} ::: *.fastq</pre>

It can also read its inputs from another command, which is how you feed it something more selective than a wildcard:

<pre>$ ls *.fastq | parallel -j 4 mytool {}</pre>

There are modifiers for building output names, and <b>{.}</b> is the one you will want most, since it gives the input with its extension removed:

<pre>$ parallel -j 4 'mytool {} > {.}.out' ::: *.fastq</pre>

Note the quotes. Without them the shell would apply the redirect once, to parallel itself, rather than inside each job.

Two things worth doing before you trust a parallel command. <b>--dry-run</b> prints what it would run without running any of it, which is the same "echo before you act" habit from the loops lesson:

<pre>$ parallel --dry-run mytool {} ::: *.fastq</pre>

And start with <b>-j 2</b> on a couple of files rather than -j 32 on all of them. Which brings us to the thing that will make you unpopular.

<b>Do not saturate a shared machine.</b> The login node of a shared server is for editing files and launching work, not for running it. Sixteen parallel jobs there will slow the machine down for everyone else on it, and administrators notice. Find out what your site expects: usually there is a job scheduler such as Slurm, and the parallel work belongs there rather than on the machine you ssh into. If you are on a server with no scheduler, agree with the other users what a reasonable -j is, and remember that memory usually runs out before cores do. Sixteen copies of a tool that each want 8 GB will need 128 GB.

If parallel is not installed, <b>xargs</b> is on every machine and does a cruder version of the same thing:

<pre>$ ls *.fastq | xargs -n 1 -P 4 mytool</pre>

<b>-P 4</b> is the number of jobs at once and <b>-n 1</b> means one input per invocation.

<b>When to stop hand-rolling this.</b> Everything above works well for one command over many files. Real analyses are rarely one command. They are five or six steps, each depending on the last, over hundreds of samples, and then something fails at step four on sample 231 at two in the morning.

At that point you want a <b>workflow manager</b>. The two common in bioinformatics are <a href="https://snakemake.readthedocs.io/">Snakemake</a>, which is Python-based, and <a href="https://www.nextflow.io/docs/latest/index.html">Nextflow</a>. Covering either properly is a course of its own, and this lesson does not try. What is worth knowing is what they buy you, so you can recognise when you have outgrown a shell script:

<ul>
<li>You describe the steps and what each needs, and the tool works out the order and what can run at the same time.</li>
<li><b>It resumes.</b> After a failure, rerunning does not redo the three days of work that already succeeded, only what is missing. This is the big one.</li>
<li>It submits to the cluster scheduler for you, so the same workflow runs on your laptop and on a cluster with one flag changed.</li>
<li>It can pin each step to a conda environment or container, so the analysis still runs the same way next year.</li>
<li>It keeps a record of what ran, which is what you need when a reviewer asks how a figure was produced.</li>
</ul>

A reasonable rule of thumb:

<ul>
<li>A handful of files, one command: a <b>for loop</b>.</li>
<li>Many files, one command, no dependencies between them: <b>parallel</b>.</li>
<li>Several steps that depend on each other, and you will run it more than once: a <b>workflow manager</b>.</li>
</ul>

Do not jump to the third one for a task the first one handles. But when you find yourself writing a shell script that checks whether each output already exists so it can skip it, you have started writing a bad workflow manager, and it is time to use a good one.

When you get there, both have good tutorials to start from: the <a href="https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html">Snakemake tutorial</a> and <a href="https://training.nextflow.io/">Nextflow training</a>. GNU parallel's own <a href="https://www.gnu.org/software/parallel/parallel_tutorial.html">tutorial</a> goes well beyond what is here too.

Whichever you use, start it inside a <b>screen</b> session, as covered in Jobs and Processes. Work at this scale outlives your connection.

## Exercise

<ol>
<li>Make a few files with touch, and use parallel --dry-run to see what a command over them would run.</li>
<li>Run something harmless over them with parallel -j 2, such as wc -l.</li>
<li>Try the same with xargs -P 2 and compare.</li>
<li>Find out whether your server has a job scheduler, and what it expects you to run on the login node.</li>
</ol>

## Quiz Question

When should you reach for a workflow manager instead of a shell loop?

## Quiz Answer

when the analysis has several steps that depend on each other and you need it to resume after a failure rather than start over