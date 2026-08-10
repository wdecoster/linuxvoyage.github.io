# Shell variables

## Lesson Content

You have already used a variable without making one: $HOME, which the shell fills in with the path to your home directory. You can make your own just as easily.

<pre>$ ref=/data/reference/hg38.fa</pre>

Note that there are <b>no spaces around the =</b>. This is the single most common mistake when starting out, because it looks so much like other languages. With spaces, the shell reads ref as a command name:

<pre>$ ref = /data/reference/hg38.fa
ref: command not found</pre>

To use the value, put a $ in front of the name:

<pre>
$ echo $ref
/data/reference/hg38.fa

$ ls -l $ref
</pre>

Variables are just text substitution. The shell replaces $ref with the value before the command runs, exactly like it does with wildcards.

<b>Quote your variables.</b> If a value contains a space, an unquoted variable gets split into several arguments, the same problem you saw with filenames:

<pre>
$ dir="my project"
$ ls $dir       looks for two directories, "my" and "project"
$ ls "$dir"     looks for one directory named "my project"
</pre>

Get into the habit of writing "$dir" with quotes. It costs nothing and saves a lot of confusion later.

Sometimes you need to make clear where the name ends. Curly braces do that:

<pre>
$ sample=patient1
$ echo $sample_reads.fastq
.fastq

$ echo ${sample}_reads.fastq
patient1_reads.fastq
</pre>

The first one lost the sample name entirely, because the shell looked for a variable called sample_reads, which does not exist, and put nothing in its place. Only the literal .fastq survived. An undefined variable quietly becomes empty rather than raising an error, which is worth remembering when a command behaves strangely.

You can also capture the output of a command into a variable, by putting it in $( ):

<pre>
$ today=$(date +%Y-%m-%d)
$ echo $today
2026-08-10

$ count=$(wc -l < samples.tsv)
$ echo "there are $count samples"
</pre>

This is enormously useful, and it is how you build filenames that include a date, a sample name, or a count.

Finally, a variable you set like this exists only in your current shell. It is not passed to programs you run, and it disappears when you log out. Making it stick is what the export command is for, and we come back to that in the section on your environment.

## Exercise

<ol>
<li>Set a variable to a directory you use often and cd into it using the variable.</li>
<li>Set a variable containing a space, then run ls on it with and without quotes and compare the errors.</li>
<li>Use $(date +%Y-%m-%d) to build a filename that includes today's date, and create it with touch.</li>
</ol>

## Quiz Question

What is wrong with the assignment: name = pete

## Quiz Answer

there must be no spaces around the =