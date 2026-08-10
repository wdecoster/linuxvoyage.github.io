# yum and apt

## Lesson Content

Ah, the Batmans of package management, these systems come with all the fixins to make package installation, removal and changes easier, including installing package dependencies. Two of the most popular management systems is <b>yum</b> and <b>apt</b>. Yum is exclusive to the Red Hat family and apt is exclusively to the Debian family.

<b>Install a package from a repository</b>

<pre>
Debian: $ sudo apt install package_name
RPM: $ sudo yum install package_name
</pre>

Note the sudo. Installing and removing software changes the whole system, not just your own files, so these commands need superuser access. Only the commands that just read information, like apt show, work without it.

<b>Remove a package</b>

<pre>
Debian: $ sudo apt remove package_name
RPM: $ sudo yum erase package_name
</pre>

<b>Updating packages for a repository</b>

It's always best practice to update your package repositories so they are up to date before you install and update a package. 

<pre>
Debian: sudo apt update; sudo apt upgrade
RPM: sudo yum update
</pre>

<b>Get information about an installed package</b>

<pre>
Debian: apt show package_name
RPM: yum info package_name
</pre>

## Exercise

Run through each of these package commands and see the output you receive.

## Quiz Question

What command is used to show package information on a Debian system?

## Quiz Answer

apt show
