# CCLLexer
CCL Lexer for pygments

The CCL Lexer allows you to parse CCL code (Cerner Command Language) with pygments / pygmentize and produce good looking exports of yout code. The lexer will register itself for the CCL language and the file extensions (.ccl, .inc, .prg)

To use this lexer
* install the pythong code/package
* run pygments on ccl code
    * pygmentize -l ccl -x -f html -O full,style=monokai -o output/monokai_inc.html ./hello_world.inc
* view the output generated

# Examples
Below are some example outputs, based on a dummy CCL script and some of the styles supported by pygments:

Default:\
![Default](https://github.com/mjj4791/CCLLexer/blob/master/img/default.png)

Monokai:\
![Monokai](https://github.com/mjj4791/CCLLexer/blob/master/img/monokai.png)

Native:\
![Native](https://github.com/mjj4791/CCLLexer/blob/master/img/native.png)

Perldoc:\
![Native](https://github.com/mjj4791/CCLLexer/blob/master/img/perldoc.png)

Solarized:\
![solarized-dark](https://github.com/mjj4791/CCLLexer/blob/master/img/solarized-dark.png)
![solarized-light](https://github.com/mjj4791/CCLLexer/blob/master/img/solarized-light.png)


