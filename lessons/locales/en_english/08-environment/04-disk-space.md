# Disk space

## Lesson Content

Sequencing data is large, intermediate files are larger, and shared servers run out of space with great regularity. Running out is not a tidy failure either: jobs die partway through, files end up truncated, and on a full home directory even logging in can start misbehaving. Knowing two commands prevents most of it.

<b>df</b> shows how full each filesystem is. The <b>-h</b> flag makes the numbers human readable, which you always want:

<pre>
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   47G  1.2G  98% /
/dev/sdb1       9.1T  4.2T  4.5T  49% /data
</pre>

Each line is a separate pool of storage. The one to look at is the row whose "Mounted on" path your files are actually under. In the example above, the home directories are on a nearly full 50 GB disk while /data has terabytes free, and that is a very common arrangement: a small system disk and a big data volume. Writing a large output into your home directory when /data is right there is the usual way people run into trouble.

To ask about a particular place rather than reading the whole table:

<pre>$ df -h .</pre>

The dot means the directory you are standing in, so this answers "how much room is there where I am?".

<b>du</b> shows how much space things are taking up. On its own it walks every subdirectory and produces an unreadable wall of output, so it is almost always used with <b>-s</b> for summary and <b>-h</b> for human readable:

<pre>
$ du -sh
14G     .
</pre>

That is the total for the current directory. The genuinely useful form asks about everything in the current directory, one line each:

<pre>
$ du -sh *
2.1G    alignments
8.6G    raw_reads
1.2G    results
14M     scripts
</pre>

Now you can see where it went. When a directory has a lot in it, sort the answer, using the -h flag from the sort lesson, which understands G and M:

<pre>$ du -sh * | sort -h</pre>

The biggest offender ends up at the bottom, next to your prompt, which is exactly where you want it. This one line is the answer to "why is my quota full" nine times out of ten.

One catch: <b>*</b> does not match names beginning with a dot, so hidden directories are invisible to that command, and some of the largest things in your home directory are hidden. ~/.conda and ~/.cache are the usual culprits. If the numbers do not add up to what du -sh reports for the whole directory, that is why. Include them with:

<pre>$ du -sh -- .[!.]* * 2>/dev/null | sort -h</pre>

The 2>/dev/null is there because if a directory happens to have no hidden entries, the shell leaves the pattern unexpanded and du complains about a file literally called .[!.]* . Sending that grumble to /dev/null keeps the output clean.

A warning worth having: du on a large directory tree takes a while, because it really does look at everything. On a network filesystem it can take minutes. That is normal, and Ctrl-C stops it.

<b>Quotas.</b> On many shared servers you are not limited by the disk being full but by a quota, a per-user limit set by the administrators. If you get "Disk quota exceeded" while df cheerfully reports terabytes free, that is what has happened. Check yours with:

<pre>$ quota -s</pre>

If that command is not available or reports nothing, your site may use a different tool, and it is worth asking early rather than discovering the limit mid-analysis.

<b>Habits that keep you out of trouble:</b>

<ul>
<li>Find out where your big data is supposed to live — usually a project, scratch or data area, not your home directory — and work there from the start. Moving a terabyte afterwards is slow and dull.</li>
<li>Delete intermediate files once you no longer need them. Alignment pipelines in particular leave enormous ones behind.</li>
<li>Keep data compressed. Most bioinformatics tools read .gz files directly, so decompressing is usually unnecessary.</li>
<li>Check df -h before launching something large, not after it fails at 90% complete.</li>
<li>Remember that conda environments are not small, as the previous lesson mentioned. A few of them will quietly eat a home directory quota.</li>
</ul>

## Exercise

<ol>
<li>Run df -h and work out which line your home directory is on.</li>
<li>Run du -sh in your home directory to see the total.</li>
<li>Run du -sh * | sort -h and find your largest directory. Then run the version that includes hidden directories and see whether the answer changes, which in a home directory it usually does.</li>
<li>Check whether you have a quota, with quota -s.</li>
</ol>

## Quiz Question

Which command tells you how much space a directory is using?

## Quiz Answer

du