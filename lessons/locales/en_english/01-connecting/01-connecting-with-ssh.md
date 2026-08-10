# Connecting with ssh

## Lesson Content

Most of the time you will not be sitting in front of the Linux machine you are using. The machine lives in a server room or a data centre somewhere, and you reach it over the network from your own laptop. The tool for that is <b>ssh</b>, the secure shell.

The basic form is your username on the server, an @, and the address of the server:

<pre>$ ssh pete@server.example.org</pre>

Your username on the server is not necessarily the same as the one on your laptop. If you leave off the username, ssh assumes you want to use the same name you are logged in as locally, which is often not what you want.

The first time you connect to a machine you will see something like this:

<pre>
The authenticity of host 'server.example.org' can't be established.
ED25519 key fingerprint is SHA256:4f9GhVpXqCnZ2mQ7bTsRk8eLwYd3JuNxA1oPvHiEgMc.
Are you sure you want to continue connecting (yes/no)?
</pre>

Your machine is telling you it has never seen this server before and cannot vouch for it. Type <b>yes</b> and the fingerprint gets saved in a file called ~/.ssh/known_hosts. From then on, ssh checks the server against that saved fingerprint and stays quiet.

If you ever connect again and ssh loudly warns you that the fingerprint has <i>changed</i>, do not just click past it. Usually it means the server was reinstalled, but it can also mean something is impersonating the server, so ask whoever runs it before continuing.

Once you are in, the shell prompt changes to show the server's hostname, which is your reminder that commands now run over there and not on your laptop:

<pre>pete@laptop:~$ ssh pete@server.example.org
pete@server:~$ </pre>

Everything you have learned about the shell works exactly the same way here. The difference is that the files you see belong to the server, not to your laptop. This trips up nearly everyone at least once: you go looking for a file you just downloaded and it is not there, because you downloaded it on the other machine.

To leave, use exit, or press <b>Ctrl-D</b>:

<pre>pete@server:~$ exit
pete@laptop:~$ </pre>

You can also run a single command on the server without staying there. ssh runs it, prints the output, and returns you to your own shell:

<pre>$ ssh pete@server.example.org ls /data/projects</pre>

One thing to know early: if your network drops, or you close your laptop, your ssh connection dies, and anything you were running in it usually dies too. That is a real problem when a job takes hours. We will fix it properly in the lesson on screen sessions.

## Exercise

<ol>
<li>Connect to your server with ssh.</li>
<li>Run hostname and pwd, and compare the output to the same commands in a local terminal.</li>
<li>Log out with Ctrl-D, then run a single command remotely without logging in, using ssh user@host hostname.</li>
</ol>

## Quiz Question

Which file stores the fingerprints of servers you have connected to before?

## Quiz Answer

~/.ssh/known_hosts