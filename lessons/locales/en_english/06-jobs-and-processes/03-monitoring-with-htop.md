# Monitoring with htop

## Lesson Content

You have started a job. Is it actually doing anything? Is it using the memory you expected? Is somebody else already using the whole machine? <b>htop</b> answers all three, and it is the tool to reach for before any of the others in this section.

<pre>$ htop</pre>

If it is not installed, <b>top</b> is always there and shows the same information in a less friendly way. On a machine where you can install things, or inside a conda environment, htop is worth having.

The screen splits in two. Along the top are meters for the machine as a whole, and below is the list of running processes, refreshing every couple of seconds.

A word on <b>cores</b> first, since the whole display depends on it. A modern machine has several independent processors, called cores, and can genuinely run that many things at once. Sixteen cores means sixteen jobs at full speed. A program that uses only one is <i>single-threaded</i>, which most simple tools are; one that spreads itself over several is <i>multithreaded</i>. Find out how many your machine has with:

<pre>$ nproc</pre>

<b>The meters at the top.</b> One bar per core, then memory, then swap. The core bars tell you how busy the machine is: on a sixteen-core server, one full bar and fifteen empty ones means a single-threaded job, which is normal, and all sixteen full means either your parallel work or somebody else's. The memory bar is the one to watch most closely. When it fills and swap starts filling too, the machine is about to become extremely slow for everybody, because it has started shuffling memory out to disk.

<b>The process list.</b> The columns that matter:

<ul>
<li><b>USER</b> - who owns it. On a shared server most of what you see is not yours.</li>
<li><b>RES</b> - resident memory, the actual RAM this process is using right now. This is the memory number to trust.</li>
<li><b>VIRT</b> - virtual memory, which is usually an alarmingly large number and rarely means anything. Ignore it.</li>
<li><b>CPU%</b> - how much processor it is using. Note that 100% means one core fully busy, not the whole machine, so a well-behaved multithreaded tool can legitimately show 800%.</li>
<li><b>MEM%</b> - the same as RES, as a share of the machine's total.</li>
<li><b>TIME+</b> - how much processor time it has consumed since it started, which is not the same as how long ago you launched it.</li>
</ul>

<b>Making it useful.</b> The list is long and mostly other people's. A few keys fix that:

<ul>
<li><b>u</b> then your username - show only your own processes. This is the first thing to do.</li>
<li><b>F6</b> or <b>&gt;</b> - choose what to sort by. Sorting by RES or by CPU% puts the heavy things at the top.</li>
<li><b>F5</b> or <b>t</b> - tree view, which groups a process with the ones it started. Useful when a script has launched a tool and you want to see which is which.</li>
<li><b>F4</b> or <b>\</b> - filter the list by a piece of text, such as the name of your tool.</li>
<li><b>q</b> - quit. As ever, worth knowing before you go in.</li>
</ul>

<b>What you are looking for.</b> A few patterns are worth recognising:

If your job is at 100% CPU and its memory is steady, it is working normally. If it is at 0% CPU, it is waiting for something, usually reading or writing a file, and if it stays there the disk is your bottleneck rather than the processor. If RES is climbing steadily and never levels off, the job is consuming more and more memory, and on a shared machine it will eventually be killed, or take the machine down with it. Notice that early rather than at three in the morning.

<b>Killing something.</b> First, the reassurance: you can only kill your own processes. Selecting somebody else's and trying simply fails, which is the permissions system doing its job, so you cannot destroy a colleague's week by mistyping.

Select a process with the arrow keys and press <b>F9</b>, or <b>k</b> if your keyboard's function keys are taken by something else, which they usually are on a Mac. htop offers a list of signals; the default, SIGTERM, is the polite one that asks the program to stop and clean up. Only use SIGKILL if that does nothing, since it gives the program no chance to finish writing its output. The killing processes lesson later in this section covers what those signals actually are.

## Exercise

<ol>
<li>Run <b>yes > /dev/null</b> in one window. That keeps one core busy doing nothing useful, which is exactly what you want for this. Open a second window, either another ssh connection or another screen window, and start htop.</li>
<li>Press u and filter to your own processes, and find the yes command. It should be sitting at close to 100% CPU.</li>
<li>Sort by memory and by CPU, and see where it lands. Then go back to the first window and stop it with Ctrl-C.</li>
<li>Look at the core meters and work out how many cores your job is using.</li>
<li>Quit with q, then try top and compare.</li>
</ol>

## Quiz Question

Which memory column shows the RAM a process is actually using?

## Quiz Answer

RES