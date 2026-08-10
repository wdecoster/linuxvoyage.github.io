# Loops over files

## Lesson Content

The real reason to learn scripting is this one: doing the same thing to a hundred files without typing a hundred commands.

The for loop walks through a list, putting each item into a variable in turn:

<pre>
for sample in patient1 patient2 patient3
do
    echo "processing $sample"
done
</pre>

Read it as: for each thing in this list, call it sample, and run the commands between do and done. You can type this straight at the prompt, and the shell will keep prompting until you finish with done.

The list can be a wildcard, which is where it gets useful:

<pre>
for f in *.fastq
do
    echo "$f has $(wc -l < "$f") lines"
done
</pre>

Remember that the shell expands *.fastq into the list of matching filenames before the loop starts, so the loop simply walks a list of names.

A very common pattern is turning input names into output names. Say you want a .txt report next to every .fastq. The problem is stripping the old extension, and <b>basename</b> does that:

<pre>
for f in *.fastq
do
    name=$(basename "$f" .fastq)
    wc -l "$f" > "${name}_count.txt"
done
</pre>

basename "$f" .fastq takes sample1.fastq and gives back sample1, so ${name}_count.txt becomes sample1_count.txt. The curly braces matter here, exactly as in the variables lesson.

Two habits will save you a lot of grief.

<b>Quote the variable.</b> "$f" and not $f. The moment one file in the directory has a space in its name, an unquoted loop starts doing things to files you did not mean.

<b>Echo before you act.</b> When the loop body deletes, moves or overwrites, run it once with echo in front of the real command so it prints what it <i>would</i> do:

<pre>
for f in *.fastq
do
    echo rm "$f"
done
</pre>

Read the output, convince yourself it is right, then take the echo away. This takes five seconds and has saved a great many people from deleting a directory they cared about.

If the list is in a file rather than on disk, a while loop reads it a line at a time:

<pre>
while read sample
do
    echo "processing $sample"
done < samples.txt
</pre>

The <b>&lt; samples.txt</b> at the end is the stdin redirection you already know, feeding the file into the loop.

## Exercise

<ol>
<li>Make a few files with touch, then write a loop that echoes each filename.</li>
<li>Change it to print the line count of each file alongside its name.</li>
<li>Write a loop that would rename each .txt file to .bak, using echo first to check it before running it for real.</li>
</ol>

## Quiz Question

Which keywords open and close the body of a for loop?

## Quiz Answer

do and done