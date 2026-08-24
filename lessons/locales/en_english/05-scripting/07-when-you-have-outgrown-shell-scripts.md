# When you have outgrown shell scripts

## Lesson Content

Everything in the previous lesson works well for one command over many files. Real analyses are rarely one command. They are five or six steps, each depending on the last, over hundreds of samples, and then something fails at step four on sample 231 at two in the morning.

At that point you want a <b>workflow manager</b>. The two common in bioinformatics are <a href="https://snakemake.readthedocs.io/">Snakemake</a>, which is Python-based, and <a href="https://www.nextflow.io/docs/latest/index.html">Nextflow</a>. Covering either properly is a course of its own, and this lesson does not try. What is worth knowing is what they buy you, so you can recognise when you have outgrown a shell script:

<ul>
<li>You describe the steps and what each needs, and the tool works out the order and what can run at the same time.</li>
<li><b>It resumes.</b> After a failure, rerunning does not redo the three days of work that already succeeded, only what is missing. This is the big one.</li>
<li>It submits to the cluster scheduler for you, so the same workflow runs on your laptop and on a cluster with one flag changed.</li>
<li>It can pin each step to an exact set of installed software, so the analysis still runs the same way next year. The Your Environment section later covers how that software gets installed.</li>
<li>It keeps a record of what ran, which is what you need when a reviewer asks how a figure was produced.</li>
</ul>

<b>A word on containers</b>, since you will see them alongside all of this. A <b>container</b> is a packaged copy of a program together with everything it needs to run, so that it behaves the same on your laptop, on the server and on a colleague's cluster. Docker is the name you will have heard; on shared servers you will more often meet <a href="https://apptainer.org/">Apptainer</a>, formerly Singularity, because it does not require the administrative rights that Docker does. Workflow managers can run each step inside one, which is the strongest form of that fourth point above. You do not need containers to get started, and this course does not use them, but when a tool's documentation offers you a container as the installation route, that is what it is offering.

A reasonable rule of thumb:

<ul>
<li>A handful of files, one command: a <b>for loop</b>.</li>
<li>Many files, one command, no dependencies between them: <b>parallel</b>.</li>
<li>Several steps that depend on each other, and you will run it more than once: a <b>workflow manager</b>.</li>
</ul>

Do not jump to the third one for a task the first one handles. But when you find yourself writing a shell script that checks whether each output already exists so it can skip it, you have started writing a bad workflow manager, and it is time to use a good one.

When you get there, both have good tutorials to start from: the <a href="https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html">Snakemake tutorial</a> and <a href="https://training.nextflow.io/">Nextflow training</a>. GNU parallel's own <a href="https://www.gnu.org/software/parallel/parallel_tutorial.html">tutorial</a> goes well beyond what the previous lesson covered too.

None of this is something to adopt today. It is here so that the day your shell script becomes unmanageable, you recognise what is happening and know the name of the thing that solves it.

## Exercise

<ol>
<li>Take an analysis you have run more than once, or one from your project, and write down its steps and which step needs which. That list is essentially what you would hand a workflow manager.</li>
<li>Go through the five points above and count how many your current approach gives you. Resuming after a failure is usually the one that is missing.</li>
<li>Check whether either tool is already on your server with <b>which snakemake nextflow</b>.</li>
</ol>

## Quiz Question

When should you reach for a workflow manager instead of a shell loop?

## Quiz Answer

when the analysis has several steps that depend on each other and you need it to resume after a failure rather than start over
