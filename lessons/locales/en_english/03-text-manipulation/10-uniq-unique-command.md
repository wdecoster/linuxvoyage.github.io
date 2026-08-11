# uniq (Unique)

## Lesson Content

The uniq (unique) command is another useful tool for parsing text. Say you pulled the condition column out of your sample table and ended up with a file full of repeats:

<pre>
conditions.txt
control
control
treated
treated
treated
untreated
</pre>

To collapse the repeats:

<pre>$ uniq conditions.txt
control
treated
untreated</pre>

Counting how often each one occurs is usually more useful, and that is <b>-c</b>:

<pre>$ uniq -c conditions.txt
      2 control
      3 treated
      1 untreated</pre>

<b>-u</b> keeps only the lines that appear exactly once:

<pre>$ uniq -u conditions.txt
untreated</pre>

and <b>-d</b> keeps only the ones that are repeated:

<pre>$ uniq -d conditions.txt
control
treated
</pre>

<b>Now the catch, and it is the thing to remember about uniq: it only compares each line with the one directly above it.</b> Duplicates that are not next to each other are invisible to it.

<pre>
conditions.txt
control
treated
control
treated
untreated
</pre>

<pre>$ uniq conditions.txt
control
treated
control
treated
untreated</pre>

Nothing was removed, because no two identical lines were adjacent. This catches people out constantly, and the symptom is a count that is quietly too high.

The fix is to sort first, so that identical lines end up together:

<pre>
$ sort conditions.txt | uniq
control
treated
untreated</pre>

<b>sort | uniq -c</b> is one of the most useful pairs in the whole shell. It answers "how many of each?" for anything you can get onto separate lines:

<pre>
$ sort conditions.txt | uniq -c
      2 control
      2 treated
      1 untreated</pre>

Add a numeric reverse sort on the end and you have a frequency table, most common first:

<pre>$ sort conditions.txt | uniq -c | sort -nr</pre>

That pipeline is worth memorising. You will use it on log files, on column output from cut, and on anything else where the question is "what is in here, and how much of it".

## Exercise

<ol>
<li>Create the second, unsorted version of conditions.txt and confirm that plain uniq misses the duplicates.</li>
<li>Fix it with sort, and get counts with sort file | uniq -c.</li>
<li>Build the full sort | uniq -c | sort -nr pipeline and check the most common value comes out on top.</li>
</ol>

## Quiz Question

Why does uniq usually need sort in front of it?

## Quiz Answer

uniq only removes duplicate lines that are next to each other