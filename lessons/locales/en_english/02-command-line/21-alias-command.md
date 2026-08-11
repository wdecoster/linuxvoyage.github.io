# alias

## Lesson Content

Sometimes typing commands can get really repetitive, or if you need to type a long command many times, it’s best to have an alias you can use for that. To create an alias for a command you simply specify an alias name and set it to the command. 

<pre>$ alias foobar='ls -la'</pre>

Now instead of typing ls -la, you can type foobar and it will execute that command, pretty neat stuff. Keep in mind that an alias made this way only lasts for the current session. Close your terminal or log out of the server, and it is gone. To have it every time, open the following file with nano and put the alias line in it:

<pre>~/.bashrc</pre>

or similar files if you want to have it persist after reboot.

You can remove aliases with the unalias command: 

<pre>$ unalias foobar</pre>

## Exercise

Create a couple of aliases then remove them.

## Quiz Question

What command is used to make an alias?

## Quiz Answer

alias