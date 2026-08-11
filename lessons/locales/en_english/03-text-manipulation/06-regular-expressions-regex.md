# regex (Regular Expressions)

## Lesson Content

Regular expressions are a powerful tool to do pattern based selection. It uses special notations similar to those we've encountered already such as the * wildcard. 

We'll go through a couple of the most common regular expressions, these are almost universal with any programming language.

We'll use this phrase as our test string. Make it into a file so you can actually try these:

<pre>
$ printf 'sally sells seashells\nby the seashore\n' > tongue.txt
</pre>

Each example below can be run as grep with the pattern in single quotes, like this:

<pre>
$ grep 'sea' tongue.txt
sally sells seashells 
by the seashore
</pre>

Quote the pattern. Several of the characters below mean something to the shell as well, and the quotes keep them safe until grep sees them.

<b>1. Beginning of a line with ^</b>

<pre>
<b>^</b>by
would match the line "by the seashore"
</pre>

<b>2. End of a line with $</b>

<pre>
seashore<b>$</b>
would match the line "by the seashore"
</pre>

<b>3. Matching any single character with .</b>

<pre>
b<b>.</b>
would match by
</pre>

<b>4. Bracket notation with [] and ()</b>

This can be a little tricky, brackets allow us to specify characters found within the bracket. 

<pre>
d<b>[iou]</b>g
would match: dig, dog, dug
</pre>

The previous anchor tag ^ when used in a bracket means anything except the characters within the bracket. 

<pre>
d<b>[^i]</b>g
would match: dog and dug but not dig
</pre>

Brackets can also use ranges to increase the amount of characters you want to use. 

<pre>
d<b>[a-c]</b>g
will match patterns like dag, dbg, and dcg
</pre>

Be careful though as brackets are case sensitive:

<pre>
d<b>[A-C]</b>g
will match dAg, dBg and dCg but not dag, dbg and dcg
</pre>

And those are some basic regular expressions. There is a great deal more: repetition with * + and ?, alternation with |, grouping with parentheses, and a frankly confusing split between "basic" and "extended" syntax, which is why grep -E sometimes behaves differently from plain grep.

This lesson is a starting point rather than a reference. Two places are worth knowing when you need more:

<ul>
<li><a href="https://regexone.com/">RegexOne</a> is a short interactive tutorial that takes about an hour and covers the rest of the syntax properly.</li>
<li><a href="https://regex101.com/">regex101</a> lets you paste a pattern and some text and watch it match, piece by piece, with an explanation of every character. Set the flavour to POSIX or PCRE depending on the tool you are using. For working out why a pattern does not do what you expected, nothing else comes close.</li>
</ul>

## Exercise

Try each pattern from this lesson against tongue.txt, in the form:

<pre>
$ grep '^by' tongue.txt
$ grep 'seashore$' tongue.txt
$ grep 'b.' tongue.txt
</pre>

The square brackets in this exercise's earlier wording were a placeholder meaning "put your own thing here". Do not type them, unless you mean the bracket notation from the lesson.

## Quiz Question

What regular expression would you use to match a single character?

## Quiz Answer

.