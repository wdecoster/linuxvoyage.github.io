# sort

## Lesson Content

The sort command is useful for sorting lines. Let's use a small table of samples, with a sample name, a condition, and a count of reads, separated by tabs:

<pre>
samples.tsv
sample3   control   8000
sample1   control   12000
sample4   treated   45000
sample2   treated   9500
</pre>

By default sort works alphabetically on the whole line:

<pre>$ sort samples.tsv
sample1   control   12000
sample2   treated   9500
sample3   control   8000
sample4   treated   45000
</pre>

You can reverse it with -r:

<pre>$ sort -r samples.tsv
sample4   treated   45000
sample3   control   8000
sample2   treated   9500
sample1   control   12000
</pre>

Now the interesting part. Say you want the samples ordered by read count, which is the third column. Use <b>-k</b> to pick the column:

<pre>$ sort -k 3 samples.tsv
sample1   control   12000
sample3   control   8000
sample4   treated   45000
sample2   treated   9500
</pre>

That is not what you wanted. 12000 came before 8000, because sort compared the text character by character, and the character "1" sorts before "8". Alphabetical order and numerical order are not the same thing.

<b>-n</b> tells sort to read the field as a number:

<pre>$ sort -n -k 3 samples.tsv
sample3   control   8000
sample2   treated   9500
sample1   control   12000
sample4   treated   45000
</pre>

That is the one you wanted. Forgetting -n on numbers is an easy mistake to make and a hard one to notice, because the output still looks sorted.

Combine it with -r to get the largest first, which is the usual way to answer "what are the top few":

<pre>$ sort -nr -k 3 samples.tsv
sample4   treated   45000
sample1   control   12000
sample2   treated   9500
sample3   control   8000
</pre>

Two more that come up often: <b>-u</b> drops duplicate lines as it sorts, and <b>-h</b> understands human readable sizes such as 4K and 2G, which is what you want for sorting the output of du.

## Exercise

<ol>
<li>Create the samples.tsv file above and sort it on the third column, with and without -n, and compare.</li>
<li>Use sort -nr to put the largest count first.</li>
<li>Try du -h in a directory with some files, and sort it with sort -h.</li>
</ol>

## Quiz Question

What flag makes sort compare fields as numbers rather than as text?

## Quiz Answer

-n