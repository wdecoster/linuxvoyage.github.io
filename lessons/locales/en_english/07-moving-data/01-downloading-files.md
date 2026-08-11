# Downloading files

## Lesson Content

Often the data you need is not on your laptop at all, it is on a website somewhere, and you want it on the server. Downloading it to your laptop and then copying it up is a waste of time and of your own bandwidth. Far better to have the server fetch it directly.

There are two tools for this and almost every machine has at least one.

<b>wget</b> is the simpler of the two. Give it a URL and it saves the file, keeping its name:

<pre>$ wget https://example.org/data/reference.fa.gz</pre>

You get a progress bar, and when it finishes the file is in your current directory. Check where you are with pwd first, because that is where it will land.

<b>curl</b> does the same job but its defaults are all different, and each difference has bitten somebody. Out of the box it prints what it downloads to the screen rather than saving it. For a web page that means a screenful of HTML, and for a compressed genome a screenful of binary rubbish and a confused terminal. So you want <b>-O</b> to save it under its original name. But you want two more flags as well:

<pre>$ curl -fLO https://example.org/data/reference.fa.gz</pre>

<ul>
<li><b>-O</b> save to a file, named after the URL, instead of printing it.</li>
<li><b>-L</b> follow redirects. Without it, a URL that has moved gives you a tiny HTML "this has moved" page instead of your data. wget follows redirects on its own.</li>
<li><b>-f</b> fail properly. Without it, a 404 makes curl save the error page and report success, which is the worst of both worlds.</li>
</ul>

<b>-fLO</b> is worth learning as one word.

Use lowercase <b>-o</b> if you want to choose the name yourself:

<pre>$ curl -o hg38.fa.gz https://example.org/data/reference.fa.gz</pre>

If you ever run curl without either and your terminal fills with nonsense, that is what happened. Ctrl-C stops it, and the reset command will tidy up a terminal that has been left displaying garbage.

<b>Always look at what you got.</b> This is the habit that matters most. A plain <b>curl -O</b> against a URL that no longer exists writes the web server's error page to disk and exits as though nothing were wrong:

<pre>
$ curl -O https://example.org/data/gone.fa.gz
$ echo $?
0
$ ls -lh gone.fa.gz
-rw-r--r-- 1 pete pete 335 Aug 11 14:02 gone.fa.gz
</pre>

You now have a 335-byte file named like a genome, containing "404 Not Found", and a script that thinks the download worked. wget is better behaved here: on a 404 it writes nothing and exits non-zero. Either way, look:

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
9f2c81b1a4f8e6d70a3b5c19e7d84f26  reference.fa.gz
</pre>

Compare that string with the one published on the site. If they match, your copy is byte for byte the same. If they do not, download it again. This is worth doing for anything large or anything you are going to build results on.

One last thing: check where you are putting it. Home directories are usually small and reference data usually is not, so download into your project or scratch area rather than filling up your home directory.

## Exercise

<ol>
<li>Download a small real file with wget and check it, for example:
<pre>
$ wget https://www.gnu.org/licenses/gpl-3.0.txt
$ ls -lh gpl-3.0.txt
$ file gpl-3.0.txt
</pre></li>
<li>Fetch the same URL with curl under a different name, then compare: <b>curl -fLO</b> would overwrite what wget just saved, since curl replaces an existing file without a word, while wget writes gpl-3.0.txt.1 instead. Use <b>curl -fL -o gpl-curl.txt</b> and then <b>md5sum gpl-3.0.txt gpl-curl.txt</b>; the two hashes should match.</li>
<li>Try curl without -O on a web page and watch it print to the screen instead. Stop it with Ctrl-C if it is long.</li>
<li>Ask for a URL that does not exist, first with curl -O and then with curl -fO, and compare what each leaves behind and what echo $? reports.</li>
</ol>

## Quiz Question

Why does curl usually need the -O flag?

## Quiz Answer

without it curl prints the file to the screen instead of saving it