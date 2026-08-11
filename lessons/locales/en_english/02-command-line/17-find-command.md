# find

## Lesson Content

With all these files we have on the system it can get a little hectic trying to find a specific one. Well there’s a command we can use for that, find! 

<pre>$ find /home -name puppies.jpg</pre>

With find you’ll have to specify the directory you’ll be searching it, what you’re searching for, in this case we are trying to find a file by the name of puppies.jpg. 

You can specify what type of file you are trying to find. 

<pre>$ find /home -type d -name MyFolder</pre>

You can see that I set the type of file I’m trying to find as (d) for directory and I’m still searching by the name of MyFolder. 

One cool thing to note is that find doesn’t stop at the directory you are searching, it will look inside any subdirectories that directory may have as well.

If you search somewhere broad, such as the whole system, expect a lot of lines like this mixed in with your results:

<pre>find: '/root': Permission denied</pre>

That is normal and it is not a mistake in your command. find walks into every directory it can see, and on a shared machine there are plenty you are not allowed to look inside. Your actual matches are in there among the complaints. The Text Manipulation section later shows how to send those messages somewhere else so they stop cluttering the output. For now, read past them, or search a directory you own:

<pre>$ find ~ -name "*.txt"</pre>

## Exercise

<ol>
<li>Search your home directory for files whose <i>name</i> contains net, using find ~ -name "*net*". Note the quotes, and note that this matches names rather than the text inside the files.</li>
</ol>

## Quiz Question

What option should I specify for find if I want to search by name?

## Quiz Answer

-name