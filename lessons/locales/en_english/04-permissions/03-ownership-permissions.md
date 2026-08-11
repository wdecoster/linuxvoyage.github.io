# Ownership Permissions

## Lesson Content

Before we go further, a word about <b>sudo</b>, which appears in the commands below.

Every system has one all-powerful account called <b>root</b>, also known as the superuser, which is allowed to do anything at all: read any file, change any permission, delete anything. Ordinary accounts, including yours, deliberately cannot. Putting <b>sudo</b> in front of a command means "run this one command as root".

On your own machine you would normally be allowed to do that. <b>On a shared server you almost certainly are not</b>, and that is deliberate rather than something being wrong with your account. If you try, you will get either a password prompt you cannot answer or a blunt message like:

<pre>pete is not in the sudoers file. This incident will be reported.</pre>

That sounds far more dramatic than it is. It means "you are not on the list", it writes a line to a log file, and nothing else happens. You are not in trouble and you have not broken anything.

So read the sudo examples below to understand what changing ownership does and who is allowed to do it, but expect not to be able to run them yourself. The permission bits in the previous lessons, which you change on your own files with chmod, are the part you will use every day.

In addition to modifying permissions on files, you can also modify the group and user ownership of the file as well. 

<b>Modify user ownership</b>

<pre>$ sudo chown patty myfile</pre>

This command will set the owner of myfile to patty.

<b>Modify group ownership</b>

<pre>$ sudo chgrp whales myfile</pre>

This command will set the group of myfile to whales.

<b>Modify both user and group ownership at the same time</b>
If you add a colon and groupname after the user you can set both the user and group at the same time.

<pre>$ sudo chown patty:whales myfile</pre> 

## Exercise

Modify the group and user of some test files. Afterwards take a look at the permissions with ls -l.

## Quiz Question

What command do you use to change user ownership?

## Quiz Answer

chown