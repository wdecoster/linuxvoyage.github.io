# ssh keys

## Lesson Content

Typing your password every single time you connect gets old fast, and it gets worse once you start copying files back and forth. The better way is an ssh key pair.

A key pair is two matching files. The <b>private key</b> stays on your laptop and is yours alone. The <b>public key</b> is the half you hand out, and you put a copy on every server you want to log in to. The server uses the public key to check that you hold the matching private one. The private key never leaves your machine and is never sent to the server.

Make a pair with ssh-keygen:

<pre>$ ssh-keygen -t ed25519</pre>

It asks where to save the key, and the default (~/.ssh/id_ed25519) is fine. Then it asks for a passphrase. It is tempting to leave it empty, but a passphrase means that someone who copies your private key still cannot use it. Your system will usually remember the passphrase for you after the first use each session, so you are not typing it constantly.

You now have two files:

<pre>
~/.ssh/id_ed25519       your private key, keep it secret
~/.ssh/id_ed25519.pub   your public key, safe to share
</pre>

Copy the public half to the server:

<pre>$ ssh-copy-id pete@server.example.org</pre>

This asks for your password one last time, then appends your public key to a file on the server called ~/.ssh/authorized_keys. Any key listed in that file is allowed to log in as you.

Windows does not come with ssh-copy-id. You can do the same thing by hand from PowerShell, which is worth reading anyway, because it shows exactly what ssh-copy-id does:

<pre>$ type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh pete@server.example.org "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"</pre>

From now on:

<pre>$ ssh pete@server.example.org</pre>

goes straight in.

If it still asks for a password, the usual cause is permissions. ssh deliberately refuses to use keys if the files are readable by other people, and it tends to fail quietly rather than explain itself. On the server, ~/.ssh should be 700 and authorized_keys should be 600:

<pre>
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
</pre>

If you have several servers, or your username differs from machine to machine, you can write it all down once in ~/.ssh/config on your laptop:

<pre>
Host work
    HostName server.example.org
    User pete
</pre>

Now <b>ssh work</b> is enough. That short name works with scp and rsync too, and, as you will see in the next lesson, with VS Code.

## Exercise

<ol>
<li>Generate a key pair with ssh-keygen -t ed25519.</li>
<li>Copy the public half to your server with ssh-copy-id, then log in again and confirm you are not asked for your password.</li>
<li>Add a short Host entry to ~/.ssh/config and connect using just that name.</li>
</ol>

## Quiz Question

Which half of your key pair gets copied to the server?

## Quiz Answer

the public key