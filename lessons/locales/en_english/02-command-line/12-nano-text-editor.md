# nano

## Lesson Content

Sooner or later you need to change a file rather than just read it. You could redirect output into it, but that is no good for editing one line in the middle of a config file. For that you need a text editor.

You may hear people talk about vim and emacs, which are powerful and which both take a long while before you can do anything useful in them. You do not need either. Between <b>nano</b> here and VS Code from the first section, you have everything this course asks of you. nano takes about a minute to learn, is on essentially every machine you will meet, and is perfectly good for the editing you will actually do.

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

One option is worth knowing about early. When you are editing something where line numbers matter, such as fixing the line an error message pointed at, turn them on:

<pre>$ nano -l samples.tsv</pre>

A word about tabs, since this catches people out with files where spacing matters. nano leaves your tabs as tabs, which is what you want for a Makefile or a TSV. If you ever <i>do</i> want tabs turned into spaces, that is opt in, with <b>-E</b>.

A word of warning for files you do not own. If you open a file without permission to write it, nano will happily let you type for ten minutes and only complain when you try to save. Check that it is yours before you start, and on a shared server expect anything outside your home directory not to be.

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