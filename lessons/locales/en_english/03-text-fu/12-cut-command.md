# cut

## Lesson Content

The cut command extracts portions of each line of a file. It is what you reach for when your data is in columns and you only want some of them.

Let's use the sample table again:

<pre>
samples.tsv
sample1   control   12000
sample2   treated   9500
sample3   control   8000
</pre>

The columns here are separated by tabs, which is what cut expects by default. Pull out a field with <b>-f</b>:

<pre>$ cut -f 1 samples.tsv
sample1
sample2
sample3</pre>

You can ask for several, either as a list or as a range:

<pre>
$ cut -f 1,3 samples.tsv
sample1   12000
sample2   9500
sample3   8000

$ cut -f 2-3 samples.tsv
control   12000
treated   9500
control   8000
</pre>

Not every file uses tabs. For a comma separated file, tell cut what the delimiter is with <b>-d</b>:

<pre>
samples.csv
sample1,control,12000

$ cut -d "," -f 2 samples.csv
control
</pre>

Note the quotes around the delimiter. Some delimiters, such as a semicolon or a space, mean something to the shell, so quoting them is a good habit even when you could get away without it.

There is also <b>-c</b>, which cuts by character position rather than by field:

<pre>
$ cut -c 1-7 samples.tsv
sample1
sample2
sample3
</pre>

This is useful for fixed width data, where the columns line up by position rather than being separated by a delimiter. Spaces count as characters.

Two things to know before you rely on cut.

<b>It does not handle multiple spaces as one separator.</b> If your columns are lined up with a variable number of spaces rather than tabs, cut -d " " will produce empty fields, because it treats every single space as a separator. Tab separated data is the happy case.

<b>It cannot reorder columns.</b> cut -f 3,1 gives you fields 1 and 3 in that order, not 3 then 1. Output is always in file order.

Where cut really earns its place is in a pipeline. Pull out a column, then count what is in it:

<pre>$ cut -f 2 samples.tsv | sort | uniq -c</pre>

That is the frequency table pattern from the uniq lesson, applied to one column of a table, and it is probably the single most useful thing in this section.

## Exercise

<ol>
<li>Create samples.tsv with real tabs between the columns and pull out the first and third fields.</li>
<li>Make a comma separated version and extract the second field using -d.</li>
<li>Count how many samples are in each condition with cut, sort and uniq -c.</li>
</ol>

## Quiz Question

Which flag tells cut what character separates the fields?

## Quiz Answer

-d