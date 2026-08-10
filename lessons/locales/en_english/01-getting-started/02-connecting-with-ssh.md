# Connecting with ssh

## Lesson Content

Most of the time you will not be sitting in front of the Linux machine you are using. The machine lives in a server room or a data centre somewhere, and you reach it over the network from your own laptop. The tool for that is <b>ssh</b>, the secure shell.

<b>Where do you type this?</b> You need a program on your own machine that accepts typed commands. Every operating system has one, it is just not somewhere you would have stumbled across it.

<b>On a Mac</b>, the program is called Terminal. Press <b>Cmd-Space</b> to open Spotlight, type <i>terminal</i>, and press Enter. You can also find it under Applications, then Utilities. A window opens with a prompt ending in <b>%</b> or <b>$</b>, waiting for you to type. Drag it to your dock, you will want it again.

<b>On Windows</b>, use PowerShell. Press the <b>Windows key</b>, type <i>powershell</i>, and press Enter. A blue window opens with a prompt ending in <b>&gt;</b>. Windows 10 and 11 include ssh already, so you can type the command below straight into it. Do not use the old Command Prompt (cmd.exe), and you do not need to install PuTTY.

<b>On Linux</b>, open your terminal application, usually called Terminal or Konsole. On many desktops <b>Ctrl-Alt-T</b> opens one directly.

If none of that works on your machine, the Remote - SSH extension in VS Code, two lessons from now, will do the connecting for you without a terminal at all.

This is the only part of the whole course where what you are running on your own machine matters. Once you are connected, everything happens on the server, and it makes no difference at all what you connected from.

The basic form is your username on the server, an @, and the address of the server:

<pre>$ ssh pete@server.example.org</pre>

Your username on the server is not necessarily the same as the one on your laptop. If you leave off the username, ssh assumes you want to use the same name you are logged in as locally, which is often not what you want.

The first time you connect to a machine you will see something like this:

<pre>
The authenticity of host 'server.example.org' can't be established.
ED25519 key fingerprint is SHA256:4f9GhVpXqCnZ2mQ7bTsRk8eLwYd3JuNxA1oPvHiEgMc.
Are you sure you want to continue connecting (yes/no)?
</pre>

Your machine is telling you it has never seen this server before and cannot vouch for it. The fingerprint is a short hash of the server's public key, shown so you can compare it against what the server's administrator told you. Type <b>yes</b> and ssh saves the server's key in a file called ~/.ssh/known_hosts. From then on, ssh checks the server against that saved key and stays quiet.

If you ever connect again and ssh loudly warns you that the fingerprint has <i>changed</i>, do not just click past it. Usually it means the server was reinstalled, but it can also mean something is impersonating the server, so ask whoever runs it before continuing.

Once you are in, you get a prompt just like the one on your own machine. The next section covers what to do at that prompt; for now the thing to notice is that it usually shows the server's hostname, which is your reminder that commands run over there and not on your laptop:

<pre>pete@laptop:~$ ssh pete@server.example.org
pete@server:~$ </pre>

Everything in the rest of this course works exactly the same way here as it would on a machine in front of you. The difference is that the files you see belong to the server, not to your laptop. This trips up nearly everyone at least once: you go looking for a file you just downloaded and it is not there, because you downloaded it on the other machine.

To leave, use exit, or press <b>Ctrl-D</b>:

<pre>pete@server:~$ exit
pete@laptop:~$ </pre>

You can also run a single command on the server without staying there. ssh runs it, prints the output, and returns you to your own shell:

<pre>$ ssh pete@server.example.org ls /data/projects</pre>

One thing to know early: if your network drops, or you close your laptop, your ssh connection dies, and anything you were running in it usually dies too. That is a real problem when a job takes hours. We will fix it properly in the lesson on screen sessions.

## Exercise

<ol>
<li>Connect to your server with ssh.</li>
<li>Run hostname and whoami. Both describe the server, not the machine in front of you: the name is the server's name, and the user is your account there.</li>
<li>Log out with Ctrl-D, then run a single command remotely without logging in, using ssh user@host hostname. Notice you get the same name back without ever seeing a prompt on the server.</li>
</ol>

## Quiz Question

Which file stores the keys of servers you have connected to before?

## Quiz Answer

~/.ssh/known_hosts