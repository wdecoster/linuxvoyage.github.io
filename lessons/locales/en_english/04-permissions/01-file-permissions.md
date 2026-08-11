# File Permissions

## Lesson Content

As we learned previously, files have different permissions or file modes. Let's look at an example:

<pre>$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
</pre>

There are four parts to a file's permissions. The first part is the filetype, which is denoted by the first character in the permissions, in our case since we are looking at a directory it shows <b>d</b> for the filetype. Most commonly you will see a <b>-</b> for a regular file. 

The next three parts of the file mode are the actual permissions. The permissions are grouped into 3 bits each. The first 3 bits are user permissions, then group permissions and then other permissions. I've added the pipe to make it easier to differentiate.

<pre>d | rwx | r-x | r-x </pre>

The first group is often called the user permissions, but be careful with that word: it means the <b>owner</b> of the file, not you. Reading rwx in the first group tells you what the owner may do. If you are not the owner, the group or other bits are the ones that apply to you.

Each character represent a different permission: 
<ul>
<li>r: readable</li>
<li>w: writable</li>
<li>x: executable, meaning you can run it as a program</li>
<li>-: not permitted</li>
</ul>

On a <b>directory</b> the three mean slightly different things, which is worth knowing now because it explains most confusing permission errors:
<ul>
<li>r: you can list what is in it, with ls</li>
<li>w: you can add and remove entries in it</li>
<li>x: you can enter it and reach things inside, with cd</li>
</ul>

So x on a directory does not mean the directory is a program. A directory with r but no x will let you see the names inside and nothing else.

So in the above example, we see that the owner, pete, has read, write and execute permissions on it. The group penguins has read and execute permissions. And finally, the other users (everyone else) has read and execute permissions. 

## Exercise

Use the ls -l command on multiple files and recite their permissions, user and group. 

## Quiz Question

What permission bit is used for executable? 

## Quiz Answer

x