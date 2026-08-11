# Process Permissions

## Lesson Content

Let's segway into process permissions for a bit, some programs run as root even when you start them, the passwd command being the usual example. The next lesson covers the permission bit that makes this happen, but the effect is worth seeing first: That is true, however does that mean since you are temporarily root you can modify other user's passwords? Nope fortunately not!

This is because of the many UIDs that Linux implements. There are three UIDS associated with every process:

When you launch a process, it runs with the same permissions as the user or group that ran it, this is known as an <b>effective user ID</b>. This UID is used to grant access rights to a process. So naturally if Bob ran the touch command, the process would run as him and any files he created would be under his ownership.

There is another UID, called the <b>real user ID</b> this is the ID of the user that launched the process. These are used to track down who the user who launched the process is.

One last UID is the <b>saved user ID</b>, this allows a process to switch between the effective UID and real UID, vice versa. This is useful because we don't want our process to run with elevated privileges all the time, it's just good practice to use special privileges at specific times. 

Now let's piece these all together by looking at the passwd command once more. 

When running the passwd command, your effective UID is your user ID, let's say its 500 for now. Oh but wait, remember the passwd command has the SUID permission enabled. So when you run it, your effective UID is now 0 (0 is the UID of root). Now this program can access files as root.

Let's say you get a little taste of power and you want to modify Sally's password, Sally has a UID of 600. Well you'll be out of luck, fortunately the process also has your real UID in this case 500. It knows that your UID is 500 and therefore you can't modify the password of UID of 600. (This of course is always bypassed if you are a superuser on a machine and can control and change everything).

Since you ran passwd, it will start the process off using your real UID, and it will save the UID of the owner of the file (effective UID), so you can switch between the two. No need to modify all files with root access if it's not required. 

Most of the time the real UID and the effective UID are the same, but in such cases as the passwd command they will change.

## Exercise

We haven't discussed processes yet, but you can still see the evidence of this on disk. Look at the passwd program itself:

<pre>$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68208 Mar 23 16:45 /usr/bin/passwd</pre>

<ol>
<li>Note that the file is owned by <b>root</b>, not by you.</li>
<li>Note the <b>s</b> where the owner's execute bit would normally be. That is the setuid bit, and it is what makes the program run as root even when you start it.</li>
<li>Now compare it with an ordinary command, such as ls -l /bin/ls, which has a plain x in the same place and therefore runs as you.</li>
</ol>

Do not run passwd itself as an experiment. It changes your real login password on a real account, and on a shared server that is not something to try out of curiosity.

## Quiz Question

What UID decides what access to grant?

## Quiz Answer

effective
