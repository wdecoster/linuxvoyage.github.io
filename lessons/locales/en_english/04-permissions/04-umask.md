# Umask

## Lesson Content

Every file that gets created comes with a default set of permissions. If you ever wanted to change that default set of permissions, you can do so with the umask command. This command takes the 3 bit permission set we see in numerical permissions. 

Instead of adding these permissions though, umask takes away these permissions. 

<pre>$ umask 021</pre>

In the above example, we are taking nothing away from the user, taking the write permission away from the group, and taking the execute permission away from everyone else.

Now, what is umask subtracting from? Not 777, as you might expect. The system starts from 666 for a new file and 777 for a new directory, and then removes the umask bits. Files start at 666 because it would be a bad idea to make every file you create executable.

So with the common default umask of 022:

<pre>
new file:      666 - 022 = 644  (rw-r--r--)
new directory: 777 - 022 = 755  (rwxr-xr-x)
</pre>

This is why a file you just made is not executable even though your umask leaves the user bits alone. If you want to run it as a program, you still have to add the execute bit yourself with chmod.

When you run the umask command it will give that default set of permissions on any new file you make. However, if you want it to persist you'll have to modify your startup file (.profile), but we'll discuss that in a later lesson.

## Exercise

<ol>
<li>Create a new file, then note it's permissions.</li>
<li>Modify the umask and then create another new file.</li>
<li>Check the permissions once more on the new file, what do you expect to see?</li>
<li>Make a new directory as well and compare its permissions to the new file's.</li>
</ol>

## Quiz Question

What command is used to change default file permissions?

## Quiz Answer

umask