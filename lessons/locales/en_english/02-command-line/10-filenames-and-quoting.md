# Filenames and quoting

## Lesson Content

The shell splits whatever you type into words, using spaces as the separator. That is how it knows that in <b>cp reads.fastq backup/</b> there is a command and two arguments. It is also the source of one of the most common beginner frustrations.

Suppose someone hands you a file called <b>sample 1.fastq</b>, with a space in the name. Try to look at it:

<pre>$ cat sample 1.fastq
cat: sample: No such file or directory
cat: 1.fastq: No such file or directory</pre>

The shell split the name in half and handed cat two arguments instead of one. cat did what it was told. To keep the name in one piece, put quotes around it:

<pre>$ cat "sample 1.fastq"</pre>

Or escape the space with a backslash, which means "treat the next character literally":

<pre>$ cat sample\ 1.fastq</pre>

Both work. Quotes are easier to read, so prefer them.

Spaces are not the only characters with a meaning of their own. You have already met <b>*</b>, <b>?</b> and <b>></b>, and there are others such as <b>$</b>, <b>&</b>, <b>|</b>, <b>(</b> and <b>)</b>. If a filename contains any of these, it needs quoting too.

<b>Single quotes and double quotes are not the same.</b> Inside double quotes, the shell still expands things that start with a $. Inside single quotes, nothing is expanded at all:

<pre>
$ echo "my home is $HOME"
my home is /home/pete

$ echo 'my home is $HOME'
my home is $HOME
</pre>

The rule of thumb: use double quotes when you want a variable filled in, and single quotes when you want the text exactly as written.

Tab completion, from the previous lesson, is your friend here. If you start typing <b>sam</b> and press Tab, the shell fills in the rest and escapes any awkward characters correctly, so you do not have to think about it.

The best fix, though, is to avoid the problem when you are the one naming things. Stick to letters, digits, dots, dashes and underscores:

<pre>
avoid:   my reads (copy).fastq
prefer:  my_reads_copy.fastq
</pre>

One last trap. A leading dash makes a filename look like an option:

<pre>$ rm -file
rm: invalid option -- 'l'</pre>

Quoting does not help, because the problem is not word splitting, it is that rm reads it as flags. Point at the file with a path instead:

<pre>$ rm ./-file</pre>

## Exercise

<ol>
<li>Create a file whose name contains a space, using touch and quotes.</li>
<li>Look at it with cat, first without quotes to see the error, then with quotes.</li>
<li>Compare the output of echo "$HOME" and echo '$HOME'.</li>
</ol>

## Quiz Question

Which quotes stop the shell from expanding a variable like $HOME?

## Quiz Answer

single quotes