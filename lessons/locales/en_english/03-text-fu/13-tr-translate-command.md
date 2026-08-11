# tr (Translate)

## Lesson Content

One thing before we start: tr does not take a filename. It reads whatever you feed it, and if you do not feed it anything it reads your keyboard and sits there waiting. That is why the examples below type a line and get a line back. When you have finished typing, press <b>Ctrl-D</b> to end the input, or <b>Ctrl-C</b> to give up. Most of the time you will feed it from another command with a pipe instead:

<pre>$ echo hello | tr a-z A-Z
HELLO</pre>

The tr (translate) command allows you to translate a set of characters into another set of characters. Let's try an example of translating all lower case characters to uppercase characters. 

<pre>$ tr a-z A-Z
hello
HELLO</pre>

As you can see we made the ranges of a-z into A-Z and all text we type that is lowercase gets uppercased. 

## Exercise

Try the following command what happens? 

<pre>$ tr -d ello
hello</pre>

## Quiz Question

What command is used to translate characters?

## Quiz Answer

tr