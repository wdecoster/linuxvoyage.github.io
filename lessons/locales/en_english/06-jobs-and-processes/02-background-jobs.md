# Background jobs

## Lesson Content

A command normally holds your terminal until it finishes. That is fine for ls, and no good at all for something that takes an hour. You can put such a command in the background and carry on working.

Add an <b>&</b> to the end:

<pre>
$ ./align_reads.sh &
[1] 24601
$ </pre>

You get your prompt back straight away. The <b>[1]</b> is the job number, which the shell uses to keep track of it, and <b>24601</b> is the process id, which the whole system uses. The job number is the short one you will use most.

List what you have running with <b>jobs</b>:

<pre>
$ jobs
[1]-  Running                 ./align_reads.sh &
[2]+  Stopped                 wc -l enormous.fastq
</pre>

The <b>+</b> marks the most recent job, which is the one fg and bg act on if you do not name one, and <b>-</b> marks the one before it.

Move things between foreground and background with fg and bg, giving the job number with a % in front:

<pre>
$ fg %1     bring job 1 back to the foreground
$ bg %2     let the suspended job 2 continue, in the background
</pre>

So the full manoeuvre for "I started something long in the foreground by mistake" is: <b>Ctrl-Z</b> to suspend it, then <b>bg</b> to set it running again in the background. No need to start over.

There is a catch, and it is the important part of this lesson. A background job is still attached to your terminal. If your ssh connection drops, or you close the laptop, the job usually dies with it. Backgrounding solves "I want my prompt back", not "I want this to survive the night".

<b>nohup</b> is one answer. It detaches the command from the terminal so a hangup does not kill it:

<pre>
$ nohup ./align_reads.sh &
[1] 24601
$ nohup: ignoring input and appending output to 'nohup.out'
</pre>

Since there is no terminal to print to, the output goes into a file called nohup.out. Usually you want to choose where it goes yourself, using the redirection you already know:

<pre>$ nohup ./align_reads.sh > align.log 2>&1 &</pre>

That says: run it, send stdout to align.log, send stderr to the same place, and put the whole thing in the background. It is a mouthful, but it is a pattern you will use often enough to memorise.

nohup works, but you cannot get back to the job to see how it is doing, and you cannot type at it. For that there is a better tool, which is the next lesson. The job control lesson later in this section goes over jobs, fg and bg again in more detail.

## Exercise

<ol>
<li>Start a long running command with & and check it with jobs.</li>
<li>Start one in the foreground, suspend it with Ctrl-Z, and set it running again with bg.</li>
<li>Run something with nohup, redirect the output to a log file, then log out and back in and check the log.</li>
</ol>

## Quiz Question

What do you add to the end of a command to run it in the background?

## Quiz Answer

&