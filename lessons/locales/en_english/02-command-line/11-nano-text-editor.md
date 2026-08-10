# nano

## Lesson Content

Sooner or later you need to change a file rather than just read it. You could redirect output into it, but that is no good for editing one line in the middle of a config file. For that you need a text editor.

Linux has powerful editors, vim and emacs, and there is a whole section on them later. They are worth learning eventually, but they both take a while before you can do anything useful. <b>nano</b> takes about a minute, works everywhere, and is perfectly good for the editing you will actually do.

Open a file:

<pre>$ nano samples.tsv</pre>

If the file does not exist, nano starts with an empty buffer and creates it when you save. You are immediately able to type. There are no modes to worry about: the arrow keys move the cursor, Backspace deletes, typing inserts.

The important part is the two rows at the bottom of the screen. They list the commands, and they are always visible, which is why nano is easy to pick up. The <b>^</b> in those hints means the Control key, so ^O is Ctrl-O:

<ul>
<li>Ctrl-O - write out, that is, save. It shows the filename and you press Enter to confirm.</li>
<li>Ctrl-X - exit. If you have unsaved changes it asks whether to save first.</li>
<li>Ctrl-K - cut the current line.</li>
<li>Ctrl-U - paste the line you last cut.</li>
<li>Ctrl-W - where is, that is, search. Type your text and press Enter.</li>
<li>Ctrl-G - get help, a full list of commands.</li>
</ul>

Saving and quitting are the two you need on day one. Save with Ctrl-O and Enter, quit with Ctrl-X.

Two options are worth knowing. Config files often care about exact spacing, and an editor that converts your tabs into spaces can quietly break them, so many people disable that. And when you are editing something where line numbers matter, turn them on:

<pre>
$ nano -l samples.tsv     show line numbers
$ nano -w longlines.txt   do not wrap long lines
</pre>

A word of warning for files you do not own. If you open a system file without permission to write it, nano will happily let you type for ten minutes and only complain when you try to save. If the file belongs to root, open it with sudo from the start:

<pre>$ sudo nano /etc/hosts</pre>

## Exercise

<ol>
<li>Create a file with nano, type a few lines, and save it with Ctrl-O.</li>
<li>Exit with Ctrl-X and check the contents with cat.</li>
<li>Open it again, use Ctrl-W to search for a word, delete a line with Ctrl-K, then quit <i>without</i> saving and confirm the file is unchanged.</li>
</ol>

## Quiz Question

Which key combination saves the file in nano?

## Quiz Answer

Ctrl-O