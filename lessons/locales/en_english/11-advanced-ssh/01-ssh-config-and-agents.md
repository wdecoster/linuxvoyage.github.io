# ssh config and agents

## Lesson Content

This section is not needed to follow the course. It is here for when the basics start to chafe, which for most people is around the time they are typing the same long ssh command twenty times a day.

<b>The config file.</b> The keys lesson introduced ~/.ssh/config with a single hostname alias. It does considerably more, and every option you set there applies to ssh, scp and rsync alike.

Two things before you edit it. It lives on <b>your own machine</b>, not on the server, which is easy to forget once you spend most of your day logged in. Nothing you write in it can damage the server or your account there.

It can still stop <i>you</i> connecting, though, in two ways worth knowing. A typo anywhere makes ssh refuse to start at all, with a message naming the line. And a <b>Host *</b> block applies to every connection, including ones you thought were unaffected. If ssh starts behaving strangely and you suspect the config, this ignores it completely:

<pre>$ ssh -F /dev/null pete@server.example.org</pre>

<pre>
Host work
    HostName bigserver.university.example
    User pdecoster
    IdentityFile ~/.ssh/id_ed25519_work
    ServerAliveInterval 60
</pre>

<b>ServerAliveInterval</b> is the one people wish they had known about sooner. It sends a small packet every sixty seconds, which stops an idle connection being silently dropped by a firewall or a home router. If your sessions die whenever you make a cup of tea, this fixes it.

You can set defaults for everything with a <b>Host *</b> block, and patterns work too, so <b>Host *.university.example</b> covers a whole site. Put the wildcard block at the <i>bottom</i>: ssh takes the first value it finds for each setting, so anything more specific has to come first.

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

A <b>port</b> is just a numbered door on a machine, so that one computer can offer several services at once; a web server usually listens on one, and a notebook on another. Read the command as: take port 8888 on my machine, and connect it to port 8888 as seen from the server. With that running, opening http://localhost:8888 in your own browser reaches the notebook on the server. The connection lasts as long as the ssh session does.

If the port is already taken on your side, change the first number only:

<pre>$ ssh -L 9999:localhost:8888 work</pre>

and use http://localhost:9999 instead.

<b>Running a command without a shell.</b> You saw this in the first ssh lesson, and it becomes much more useful in combination with pipes, since the output arrives on your own machine:

<pre>
$ ssh work "ls /data/project" > listing.txt
$ ssh work "cat /data/results.tsv" | sort -k2 -n | head
</pre>

In both of those the redirect and the pipe are outside the quotes, so they happen on <i>your</i> machine, which is what you want: the file and the sorting end up locally.

Move something inside the quotes and it happens on the server instead. This matters in two cases. If the command contains a wildcard, unquoted it would be expanded by your own shell against your own files, which is almost never what you meant:

<pre>$ ssh work "wc -l /data/*.tsv"</pre>

And if you want the output to stay on the server rather than travel back to you, put the redirect inside as well:

<pre>$ ssh work "sort big.tsv > sorted.tsv"</pre>

Unquoted, that last one would drag the whole file across the network and write it on your laptop.

## Exercise

<ol>
<li>Add ServerAliveInterval to your Host block and see whether idle disconnections stop.</li>
<li>Check what your agent is holding with ssh-add -l.</li>
<li>If your site uses a gateway, set up ProxyJump and confirm scp works through it in one step.</li>
<li>Try forwarding with something you can start yourself. On the server run <b>python3 -m http.server 8888</b>, which serves the current directory. Then from your own machine run <b>ssh -L 8888:localhost:8888 work</b> and open http://localhost:8888 in your browser. Ctrl-C stops the server when you are done.</li>
</ol>

## Quiz Question

Which ssh config option keeps an idle connection from being dropped?

## Quiz Answer

ServerAliveInterval