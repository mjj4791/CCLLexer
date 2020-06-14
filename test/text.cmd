pygmentize -l ccl -x -f html -O full,style=default,linenos=1 -o output/default_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=default,linenos=1 -o output/default_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=colorful,linenos=1 -o output/colorful_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=colorful,linenos=1 -o output/colorful_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=monokai -o output/monokai_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=monokai -o output/monokai_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=perldoc,linenos=1 -o output/perldoc_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=perldoc,linenos=1 -o output/perldoc_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=native -o output/native_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=native -o output/native_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=lovelace,linenos=1 -o output/lovelace_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=lovelace,linenos=1 -o output/lovelace_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=solarized-dark -o output/solarized-dark_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=solarized-dark -o output/solarized-dark_inc.html ./hello_world.inc

pygmentize -l ccl -x -f html -O full,style=solarized-light,linenos=1 -o output/solarized-light_prg.html ./hello_world.prg
pygmentize -l ccl -x -f html -O full,style=solarized-light,linenos=1 -o output/solarized-light_inc.html ./hello_world.inc

pause