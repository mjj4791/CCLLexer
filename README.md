# CCLLexer
CCL Lexer for pygments

The CCL Lexer allows you to parse CCL code (Cernaer Command Language) with pygments / pygmentize and produce good looking exports of yout code. The lexer will register itself for the CCL language and the file extensions (.ccl, .inc, .prg)

To use this lexer
* install the pythong code/package
* run pygments on ccl code
    * pygmentize -l ccl -x -f html -O full,style=monokai -o output/monokai_inc.html ./hello_world.inc
* view the output generated