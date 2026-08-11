# awk

## Lesson Content

cut pulls out columns. <b>awk</b> pulls out columns, and also does arithmetic on them, filters rows by a condition, and adds things up. It is where you go when cut is not quite enough, which happens quickly with real data.

awk splits every line into fields and names them <b>$1</b>, <b>$2</b> and so on, with <b>$0</b> meaning the whole line. The program goes in single quotes, in curly braces:

<pre>
samples.tsv
sample1   control   12000
sample2   treated   9500
sample3   control   8000
</pre>

<pre>
$ awk '{print $1}' samples.tsv
sample1
sample2
sample3
</pre>

Print several fields, in whatever order you like, which is the thing cut cannot do:

<pre>
$ awk '{print $3, $1}' samples.tsv
12000 sample1
9500 sample2
8000 sample3
</pre>

The comma puts a space between them. Note that these dollar signs are awk's field numbers, not shell variables. That is exactly why the program is in single quotes: it stops the shell trying to expand $1 before awk ever sees it.

<b>Whitespace is handled sensibly.</b> Unlike cut, awk treats any run of spaces or tabs as one separator, so it works on data lined up with spaces. For anything else, <b>-F</b> sets the separator:

<pre>$ awk -F "," '{print $2}' samples.csv</pre>

<b>Filtering.</b> Put a condition before the braces and only matching lines are processed:

<pre>
$ awk '$3 > 10000 {print $1}' samples.tsv
sample1
</pre>

Read it as: for lines where field 3 is greater than 10000, print field 1. Conditions can be numeric comparisons or regular expressions, and with no braces at all awk prints the whole matching line, which makes it a grep that understands columns:

<pre>
$ awk '$2 == "control"' samples.tsv
sample1   control   12000
sample3   control   8000
</pre>

<b>Arithmetic and totals.</b> awk keeps variables between lines, so you can accumulate. <b>END</b> runs once, after the last line:

<pre>
$ awk '{sum += $3} END {print sum}' samples.tsv
29500
</pre>

<b>NR</b> is the current line number and <b>NF</b> is the number of fields on this line. Both are more useful than they look:

<pre>
$ awk 'NR > 1' data.tsv              skip the header line
$ awk '{print NF}' data.tsv          how many columns does each row have?
$ awk 'NF != 3' data.tsv             show rows that do not have three columns
</pre>

That last one is a small gift. Malformed rows in a large file are miserable to find by eye, and this pulls them straight out.

awk is a complete programming language and this is a fraction of it. But the handful above covers most of what people actually use it for day to day, and between grep, sed and awk you can do a great deal to a text file without ever opening it.

## Exercise

<ol>
<li>Create samples.tsv and print the second and first columns, in that order.</li>
<li>Filter for rows where the third column is above some threshold.</li>
<li>Sum the third column with the END pattern.</li>
<li>Use NF to check every row has the number of columns you expect.</li>
</ol>

## Quiz Question

In awk, what does $0 refer to?

## Quiz Answer

the whole line