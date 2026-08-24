# Boot Process: Init

## Lesson Content

We've discussed init in previous lessons and know that it is the first process that gets started and it starts all the other essential services on our system. But how?

There are actually three major implementations of init in Linux: 

<b>System V init (sysv)</b>

This is the traditional init system. It sequentially starts and stops processes, based on startup scripts. The state of the machine is denoted by runlevels, each runlevel starts or stops a machine in a different way. 

<b>Upstart</b>

This is the init you'll find on older Ubuntu installations. Upstart uses the idea of jobs and events and works by starting jobs that performs certain actions in response to events. 

<b>Systemd</b>

This is the new standard for init, it is goal oriented. Basically you have a goal that you want to achieve and systemd tries to satisfy the goal's dependencies to complete the goal. 

We have an entire course on Init systems where we will dive into each of these systems in more detail.

Five lessons for a sequence that differs between machines in most of its details. Firmware and UEFI, GRUB's configuration, the initramfs, secure boot: each is a topic of its own, and you tend to meet them on the day a machine does not come back up. <a href="https://wiki.archlinux.org/title/Arch_boot_process">Arch's boot process page</a> is one of the clearest walkthroughs of the whole sequence, and most of it is not Arch specific.

## Exercise

No exercises for this lesson.

## Quiz Question

What is the newest standard for init?

## Quiz Answer

systemd