# sed (Stream Editor)

## Lesson Content

grep finds lines. <b>sed</b> changes them. It reads its input a line at a time, applies an instruction to each one, and prints the result, which makes it the tool for "replace this with that in a whole file" without opening an editor.

The instruction you will use ninety per cent of the time is <b>s</b>, for substitute:

<pre>$ sed 's/chr1/chromosome1/' variants.txt</pre>

Read it as: <b>s</b>ubstitute, then the thing to look for, then what to replace it with, separated by slashes. Every line that contains chr1 comes out with chromosome1 instead.

Two things to know immediately.

<b>It does not change the file.</b> sed prints the modified text to standard output and leaves your file exactly as it was. That is a feature, not a limitation: you get to look at the result before committing to it. To keep it, redirect to a new file, which you already know how to do:

<pre>$ sed 's/chr1/chromosome1/' variants.txt > renamed.txt</pre>

Never redirect onto the file you are reading. <b>sed 's/a/b/' file.txt &gt; file.txt</b> empties the file before sed gets to read it, and your data is gone.

<b>It replaces the first match on each line only.</b> Add a <b>g</b> on the end, for global, to get all of them:

<pre>
$ echo "one two one two" | sed 's/one/1/'
1 two one two

$ echo "one two one two" | sed 's/one/1/g'
1 two 1 two
</pre>

<b>The slash is not sacred.</b> Whatever character comes after the s is the separator, so when your text contains slashes, pick something else and avoid a thicket of backslashes:

<pre>$ sed 's|/home/pete|/data/pete|' paths.txt</pre>

<b>It takes regular expressions</b>, the ones from the regex lesson, which is where it gets its power:

<pre>
$ sed 's/^chr//' variants.txt          strip a leading chr from every line
$ sed 's/[0-9]//g' messy.txt           remove every digit
</pre>

A few other instructions worth knowing:

<pre>
$ sed -n '5p' file.txt        print only line 5 (-n means print nothing else)
$ sed -n '10,20p' file.txt    print lines 10 to 20
$ sed '1d' file.txt           delete the first line, useful for dropping a header
$ sed '/^#/d' file.txt        delete every line starting with #, dropping comments
</pre>

That last pair are genuinely useful on data files, where a header or comment lines get in the way of everything downstream.

Finally, <b>-i</b> edits the file in place, changing it for real:

<pre>$ sed -i 's/chr1/chromosome1/g' variants.txt</pre>

Treat that with respect. There is no undo, and if your pattern was wrong you have now quietly damaged your data. Run it without -i first, look at the output, and only then add the flag. If the file matters, <b>-i.bak</b> keeps the original as variants.txt.bak, which costs nothing. Note there is no space after -i, unlike most flags you have met:

<pre>$ sed -i.bak 's/chr1/chromosome1/g' variants.txt</pre>

## Exercise

<ol>
<li>Make a small file with a few repeated words and substitute one of them, with and without the g flag.</li>
<li>Use sed -n with a line range to print just the middle of the file.</li>
<li>Delete the first line with 1d and check the original file is untouched.</li>
<li>Redirect a substitution into a new file, then compare the two with less.</li>
</ol>

## Quiz Question

What does the g at the end of s/old/new/g do?

## Quiz Answer

replaces every match on the line rather than only the first