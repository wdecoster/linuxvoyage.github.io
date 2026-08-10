# What is Linux

## Lesson Content

Before you connect to anything, it is worth a minute on what you are connecting to.

Strictly speaking, <b>Linux is a kernel</b>. The kernel is the part of an operating system that sits between the hardware and everything else: it decides which program gets the processor, hands out memory, and is the only thing that actually talks to the disk and the network. On its own a kernel is not much use to anybody.

What people call "Linux" in everyday speech is the kernel plus all the programs that come with it: a shell to type commands into, tools for copying and searching files, editors, compilers, network utilities. That whole bundle, packaged up and ready to install, is called a <b>distribution</b>. Ubuntu, Debian, Red Hat and Fedora are all distributions. They share the same kernel and most of the same tools, and differ mainly in how software is installed and how often things are updated.

For this course it does not much matter which one your server runs. Nearly everything here works identically on all of them, and the few places where they differ are called out when we get to them. There is a section on distributions later if you are curious.

<b>Why Linux is worth learning.</b> It runs most of the world's servers, and essentially all of the large machines used for scientific computing. If you need more memory or more processors than a laptop has, the machine you end up on will almost certainly be running Linux, and it will almost certainly have no graphical desktop. Which brings us to the important part.

<b>You will be typing commands, not clicking.</b> If your experience of computers is Windows or macOS, this is the real adjustment, more than anything technical. Instead of finding a program and clicking it, you type its name. Instead of dragging a file, you type a command to move it.

This feels slower for about a week, and then it does not, because typed commands have two properties that clicking does not. They can be <i>combined</i>, so the output of one becomes the input of the next. And they can be <i>repeated</i>, so a thing you worked out once can be saved and run again on a thousand files without you being there. Most of this course is really about those two ideas.

<b>How you will use it.</b> You are not going to install Linux on your own machine. You will connect over the network to a server that already runs it, using a program called ssh, and type into a window on your own laptop while the commands run on the server. That is what the next lesson covers.

## Exercise

No exercises for this lesson, but have your username and the address of your server to hand before you start the next one.

## Quiz Question

What is the difference between the Linux kernel and a Linux distribution?

## Quiz Answer

the kernel manages the hardware; a distribution is the kernel bundled with all the programs that make it usable