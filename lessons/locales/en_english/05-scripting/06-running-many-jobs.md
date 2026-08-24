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

<pre>$ parallel -j 4 mytool {} ::: *.fastq</pre>

The <b>{}</b> is where each input gets substituted, and <b>:::</b> separates the command from the list of things to run it on. <b>-j</b> is how many to run at once.

Do not leave -j out. Without it parallel helps itself to one job per processor core, which on a shared machine means taking the entire thing, and there is a whole section on that below.

It can also read its inputs from another command, which is how you feed it something more selective than a wildcard:

<pre>$ ls *.fastq | parallel -j 4 mytool {}</pre>

There are modifiers for building output names, and <b>{.}</b> is the one you will want most, since it gives the input with its extension removed:

<pre>$ parallel -j 4 'mytool {} > {.}.out' ::: *.fastq</pre>

Note the quotes. Without them the shell would apply the redirect once, to parallel itself, rather than inside each job.

Two things worth doing before you trust a parallel command. <b>--dry-run</b> prints what it would run without running any of it, which is the same "echo before you act" habit from the loops lesson:

<pre>$ parallel --dry-run mytool {} ::: *.fastq</pre>

And start with <b>-j 2</b> on a couple of files rather than -j 32 on all of them. Which brings us to the thing that will make you unpopular.

<b>Do not saturate a shared machine.</b> You are not the only person on the server. Take every core with -j 32 and everyone else's work crawls, including the interactive session of whoever is trying to work out why the machine got slow.

On a server without a job scheduler, which is the situation for most of this course, there is nothing stopping you doing this, so the restraint has to come from you. In practice:

<pre>$ nproc</pre>

That tells you how many cores the machine has. <b>-j 4 is almost always polite</b> and is a good default until you know the machine better. Never use all of the cores nproc reports.

And remember that <b>memory runs out before cores do</b>: sixteen copies of a tool that each want 8 GB need 128 GB, and when that is not there the machine starts swapping and becomes unusable for everybody. The next section, Jobs and Processes, covers a tool called htop that shows you what the machine is doing before you add to it.

Larger shared systems solve this with a <b>job scheduler</b>, most commonly <a href="https://slurm.schedmd.com/quickstart.html">Slurm</a>. Instead of running work yourself, you describe what it needs and submit it to a queue, and the scheduler decides when and where it runs so that the machine is shared fairly. You do not need it here, but you will meet it the moment you move to a cluster, and it is worth knowing the word.

If parallel is not installed, <b>xargs</b> is on every machine and does a cruder version of the same thing:

<pre>$ ls *.fastq | xargs -n 1 -P 4 mytool</pre>

<b>-P 4</b> is the number of jobs at once and <b>-n 1</b> means one input per invocation.

This is as far as one command over many files will take you, and for a great deal of work that is far enough. When it stops being enough, the next lesson is about what to reach for instead.

One last thing before you set any of this going. Work at this scale takes longer than your connection will stay up, so it needs to survive you closing your laptop. The next section covers <b>screen</b>, which is how you do that; until you have read it, do not start a long run and walk away.

## Exercise

<ol>
<li>Make a few files with touch, and use parallel --dry-run to see what a command over them would run.</li>
<li>Run something harmless over them with parallel -j 2, such as wc -l.</li>
<li>Try the same with xargs -n 1 -P 2 and compare. The -n 1 matters: without it xargs hands every file to a single invocation and the -P has nothing to do.</li>
<li>Run nproc to see how many cores your machine has.</li>
<li>Check whether your server has a scheduler with <b>which sbatch qsub</b>. If neither exists, as on the machine used for this course, you are sharing the machine directly and the etiquette above is all there is.</li>
</ol>

## Quiz Question

Why should you always pass -j when you run parallel on a shared machine?

## Quiz Answer

Without it parallel runs one job per processor core, which takes the whole machine and slows everyone else on it to a crawl.
