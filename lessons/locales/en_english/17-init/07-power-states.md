# Power States

## Lesson Content

Hard to believe we haven't actually discussed ways to control your system state through the command line, but when talking about init, we not only talk about the modes that get us starting our system, but also the ones that stop our system.

To shutdown your system:

<pre>$ sudo shutdown -h now</pre>

This will halt the system (power it off), you must also specify a time when you want this to take place. You can add a time in minutes that will shutdown the system in that amount of time.

<pre>$ sudo shutdown -h +2</pre>

This will shutdown your system in two minutes. You can also restart with the shutdown command: 

<pre>$ sudo shutdown -r now</pre>

Or just use the reboot command:

<pre>$ sudo reboot</pre>

Init systems are one of the few corners of Linux where the disagreement was public and bad tempered. systemd won, and it does a great deal more than start services: logging, timers, device management and container plumbing all sit inside it, none of which these seven lessons touch. If you administer a machine of your own, <a href="https://wiki.archlinux.org/title/Systemd">ArchWiki's systemd page</a> is the practical reference, and <b>man systemd.service</b> is on the machine already.

## Exercise

What do you think is happening with init when you shutdown your machine?

## Quiz Question

What is the command to poweroff your system in 4 minutes?

## Quiz Answer

sudo shutdown -h +4