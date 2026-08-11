# Conditionals

## Lesson Content

A script that does the same thing no matter what is only half useful. Usually you want it to check something first: does the input file actually exist, did the previous step work, is this sample already done.

That is what <b>if</b> is for:

<pre>
if [ -f reads.fastq ]
then
    echo "found it"
fi
</pre>

Read it as: if this test passes, run the commands between then and fi. <b>fi</b> is if backwards, which is the shell's idea of a joke, and it marks the end of the block.

You will also see it written on one line, which is what you get inside scripts most often. The semicolons stand in for the line breaks:

<pre>if [ -f reads.fastq ]; then echo "found it"; fi</pre>

<b>The square brackets are a command.</b> This is the part that makes everything else make sense. <b>[</b> is not punctuation, it is a command, another name for <b>test</b>. It runs, it looks at what you gave it, and it exits 0 if the condition holds and non-zero if it does not. if then branches on that exit code, exactly the one from the previous lesson.

Two consequences follow immediately, and between them they account for most of the errors beginners hit:

<b>The spaces are compulsory.</b> Since [ is a command name, it needs a space after it, the same as any other command. And ] is an argument, so it needs a space before it. Writing <b>[-f reads.fastq]</b> gets you "command not found", because you have asked the shell to run a program called [-f.

<b>Anything can be the condition</b>, not just brackets. if will branch on any command's exit code:

<pre>
if grep -q "chr1" variants.vcf
then
    echo "chromosome 1 is in there"
fi
</pre>

No brackets at all. grep -q searches quietly and exits 0 if it found something, and that is all if needs.

<b>The tests you will actually use.</b> For files:

<ul>
<li>-f file - exists and is a regular file</li>
<li>-d file - exists and is a directory</li>
<li>-e file - exists, whatever kind of thing it is</li>
<li>-s file - exists and is not empty, which is the one you want after a download</li>
</ul>

For numbers, spelled out rather than symbols:

<ul>
<li>-eq equal, -ne not equal</li>
<li>-lt less than, -le less than or equal</li>
<li>-gt greater than, -ge greater than or equal</li>
</ul>

For text, using the symbols instead:

<ul>
<li>= equal, != not equal</li>
<li>-z string - the string is empty</li>
<li>-n string - the string is not empty</li>
</ul>

Note that numbers use -lt while text uses =. Mixing them up is a rite of passage:

<pre>
$ [ 10 -gt 9 ] && echo yes        # yes, 10 is greater than 9
$ [ "10" = "9" ] && echo yes      # nothing, they are different strings
</pre>

And do not reach for &gt; and &lt; to compare text inside single brackets. They are still the shell's redirection operators there, so <b>[ "10" &gt; "9" ]</b> does not compare anything at all: it tests whether "10" is a non-empty string, which it is, and quietly creates a file called 9 in your current directory. If a file called 9 already existed, it has just been emptied. If you ever need to compare text in sort order, that is what the double brackets at the end of this lesson are for.

<b>Reverse a test with !</b>, which is much more useful than testing the positive case, because most checks in scripts are "stop if something is wrong":

<pre>
if [ ! -f "$1" ]
then
    echo "no such file: $1"
    exit 1
fi
</pre>

That is the guard you saw in the exit codes lesson, and now you can read every piece of it: if not a regular file named whatever was passed as the first argument, complain and exit with a failure code.

<b>Quote your variables in tests.</b> If $1 is empty and unquoted, the shell removes it entirely and test sees <b>[ ! -f ]</b>. That is no longer a file test at all: it asks whether the string "-f" is empty, which it is not, so the whole thing comes out false. Your guard does not fire, nothing is printed, and the script carries on without the argument it needed. "$1" with quotes stays one empty argument and the test does what you meant.

<b>else and elif</b> do what you would expect:

<pre>
if [ -s results.txt ]
then
    echo "we have results"
elif [ -f results.txt ]
then
    echo "the file is there but it is empty"
else
    echo "nothing ran yet"
fi
</pre>

One last thing you will see in other people's scripts. Bash also has <b>[[ ]]</b>, a double-bracket version with fewer traps. Inside it, &gt; and &lt; really are comparisons rather than redirects, so the earlier example behaves the way you would first have guessed:

<pre>$ [[ "10" > "9" ]] && echo yes      # nothing: as text, "1" sorts before "9"</pre>

It also does not need variables quoted. It works well and many people use it, but it is a bash extension rather than something every shell has, so this course sticks to single brackets.

## Exercise

<ol>
<li>Write a script that takes a filename and prints whether it exists, using -f.</li>
<li>Add an else branch for the missing case, and make the missing case exit 1.</li>
<li>Run it on a real file and a made-up one, checking echo $? after each.</li>
<li>Deliberately write [-f file] with no spaces and read the error you get.</li>
</ol>

## Quiz Question

Why do you need a space after the opening square bracket in a test?

## Quiz Answer

because [ is a command, not punctuation, and a command name must be followed by a space