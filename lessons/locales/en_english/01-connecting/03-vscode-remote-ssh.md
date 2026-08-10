# VS Code over ssh

## Lesson Content

Editing files in a terminal editor is a skill worth having, but for day to day work most people are happier with a real editor window. Visual Studio Code can open a folder <i>on the server</i> and let you edit it as if it were local, while everything still runs remotely.

Install the <b>Remote - SSH</b> extension in VS Code, then open the command palette with <b>Ctrl-Shift-P</b> (<b>Cmd-Shift-P</b> on a Mac) and pick "Remote-SSH: Connect to Host". Type the same thing you would type after ssh:

<pre>pete@server.example.org</pre>

If you set up an ~/.ssh/config entry in the previous lesson, the short name shows up in the list, which is the easiest route. Set up your keys first: VS Code reconnects frequently, and doing that with password prompts is miserable.

Once connected, the bottom left corner of the window shows the server name. That indicator matters. It tells you where "File, Open Folder" will look, and where the built in terminal is running. Open a terminal with <b>Ctrl-`</b> and you get a shell on the server, in the same window as your files.

For a walkthrough of the setup, this video covers it well:

<pre>https://www.youtube.com/watch?v=B-s71n0dHUk</pre>

A few things worth knowing before you rely on it.

VS Code is not magic, and it is not a replacement for knowing the shell. When you connect, it installs and runs a small server process in your home directory on the remote machine. That process uses real memory and CPU on the login node. Some sites are strict about this, and a few forbid it outright, so check what your local rules are before leaving several windows connected overnight.

It also does not always work. Compute nodes behind a job scheduler, hosts you can only reach through a jump box, and locked down firewalls will all defeat it in ways that plain ssh handles fine. Files owned by root cannot be saved from the editor either, because the remote process runs as you.

So the honest summary is: use VS Code because it is comfortable, and learn nano as well, because sooner or later you will be on a machine where VS Code is not an option and you still need to change one line in a config file.

## Exercise

<ol>
<li>Install the Remote - SSH extension and connect to your server.</li>
<li>Open your home directory on the server and confirm the bottom left corner shows the server name.</li>
<li>Open the built in terminal and run hostname, to check it is running remotely and not on your laptop.</li>
</ol>

## Quiz Question

Where does the Remote - SSH server process actually run, on your laptop or on the remote machine?

## Quiz Answer

on the remote machine