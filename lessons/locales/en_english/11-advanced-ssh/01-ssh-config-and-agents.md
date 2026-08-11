# ssh config and agents

## Lesson Content

This section is not needed to follow the course. It is here for when the basics start to chafe, which for most people is around the time they are typing the same long ssh command twenty times a day.

<b>The config file.</b> The keys lesson introduced ~/.ssh/config with a single hostname alias. It does considerably more, and every option you set there applies to ssh, scp and rsync alike:

<pre>
Host work
    HostName bigserver.university.example
    User pdecoster
    IdentityFile ~/.ssh/id_ed25519_work
    ServerAliveInterval 60
</pre>

<b>ServerAliveInterval</b> is the one people wish they had known about sooner. It sends a small packet every sixty seconds, which stops an idle connection being silently dropped by a firewall or a home router. If your sessions die whenever you make a cup of tea, this fixes it.

You can set defaults for everything with a <b>Host *</b> block at the bottom of the file, and patterns work too, so <b>Host *.university.example</b> covers a whole site.

<b>The agent.</b> If you gave your key a passphrase, and you should have, you would otherwise type it on every connection. <b>ssh-agent</b> holds the unlocked key in memory for the rest of your session:

<pre>
$ eval "$(ssh-agent)"
$ ssh-add ~/.ssh/id_ed25519
</pre>

Most desktop systems start an agent for you at login, so often you only need ssh-add, or nothing at all. Check what it is holding with <b>ssh-add -l</b>.

<b>Jump hosts.</b> Many institutions do not expose their servers to the internet directly. You reach a gateway machine first, and only from there can you reach anything else. Doing that by hand means logging in twice, and it breaks scp entirely. <b>ProxyJump</b> makes it one step:

<pre>
Host work
    HostName internal.university.example
    User pdecoster
    ProxyJump gateway.university.example
</pre>

Now <b>ssh work</b> goes through the gateway on its own, and so do scp and rsync. This is also what makes VS Code's Remote-SSH work against a machine behind a gateway, which is otherwise one of the things that defeats it.

<b>Port forwarding.</b> Sometimes a program on the server offers a web interface — a Jupyter notebook, an RStudio server, a genome browser — that is only reachable from the server itself. Forwarding brings it to your own machine:

<pre>$ ssh -L 8888:localhost:8888 work</pre>

Read it as: take port 8888 on my machine, and connect it to port 8888 as seen from the server. With that running, opening http://localhost:8888 in your own browser reaches the notebook on the server. The connection lasts as long as the ssh session does.

If the port is already taken on your side, change the first number only:

<pre>$ ssh -L 9999:localhost:8888 work</pre>

and use http://localhost:9999 instead.

<b>Running a command without a shell.</b> You saw this in the first ssh lesson, and it becomes much more useful in combination with pipes, since the output arrives on your own machine:

<pre>
$ ssh work "ls /data/project" > listing.txt
$ ssh work "cat /data/results.tsv" | sort -k2 -n | head
</pre>

The quotes matter. Without them the redirect or the pipe would be applied on your own machine rather than passed to the server, which is the same distinction as in the quoting lesson.

## Exercise

<ol>
<li>Add ServerAliveInterval to your Host block and see whether idle disconnections stop.</li>
<li>Check what your agent is holding with ssh-add -l.</li>
<li>If your site uses a gateway, set up ProxyJump and confirm scp works through it in one step.</li>
<li>Forward a port for something running on the server and reach it from your own browser.</li>
</ol>

## Quiz Question

Which ssh config option keeps an idle connection from being dropped?

## Quiz Answer

ServerAliveInterval