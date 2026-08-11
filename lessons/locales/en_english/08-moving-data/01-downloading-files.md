# Downloading files

## Lesson Content

Often the data you need is not on your laptop at all, it is on a website somewhere, and you want it on the server. Downloading it to your laptop and then copying it up is a waste of time and of your own bandwidth. Far better to have the server fetch it directly.

There are two tools for this and almost every machine has at least one.

<b>wget</b> is the simpler of the two. Give it a URL and it saves the file, keeping its name:

<pre>$ wget https://example.org/data/reference.fa.gz</pre>

You get a progress bar, and when it finishes the file is in your current directory. Check where you are with pwd first, because that is where it will land.

<b>curl</b> does the same job but behaves differently by default: it prints what it downloads to the screen rather than saving it. For a web page that means a screenful of HTML, and for a compressed genome it means a screenful of binary rubbish and a confused terminal. You almost always want <b>-O</b>, which saves it under its original name:

<pre>$ curl -O https://example.org/data/reference.fa.gz</pre>

Use lowercase <b>-o</b> if you want to choose the name yourself:

<pre>$ curl -o hg38.fa.gz https://example.org/data/reference.fa.gz</pre>

If you ever run curl without either and your terminal fills with nonsense, that is what happened. Ctrl-C stops it, and the reset command will tidy up a terminal that has been left displaying garbage.

<b>Always look at what you got.</b> A download that fails often still leaves a file behind, and it is easy to spend an hour wondering why a tool cannot read your reference before noticing it is four kilobytes of HTML saying "404 Not Found":

<pre>
$ ls -lh reference.fa.gz
$ file reference.fa.gz
</pre>

ls -lh shows the size in human readable units, and file tells you what it actually is. If file says "gzip compressed data" you are fine. If it says "HTML document" you downloaded an error page.

<b>Interrupted downloads.</b> Large files and long downloads do not mix well with a connection that might drop. Both tools can pick up where they left off rather than starting again:

<pre>
$ wget -c https://example.org/data/big.tar.gz
$ curl -C - -O https://example.org/data/big.tar.gz
</pre>

If a download will take hours, start it inside a screen session as covered in the Jobs and Processes section, so it survives you closing your laptop.

<b>Checksums.</b> Serious data sources publish a checksum next to the file, something like an md5 or sha256 value. It is a fingerprint of the contents, and it lets you prove your copy arrived intact:

<pre>
$ md5sum reference.fa.gz
d41d8cd98f00b204e9800998ecf8427e  reference.fa.gz
</pre>

Compare that string with the one published on the site. If they match, your copy is byte for byte the same. If they do not, download it again. This is worth doing for anything large or anything you are going to build results on.

One last thing: check where you are putting it. Home directories are usually small and reference data usually is not, so download into your project or scratch area rather than filling up your home directory.

## Exercise

<ol>
<li>Download something small with wget, then run ls -lh and file on it.</li>
<li>Download the same thing with curl -O and confirm you get the same file.</li>
<li>Try curl without -O on a web page and watch it print to the screen instead. Stop it with Ctrl-C if it is long.</li>
</ol>

## Quiz Question

Why does curl usually need the -O flag?

## Quiz Answer

without it curl prints the file to the screen instead of saving it