Same code for 32 , 33 , 34 , 35

C:/msys64/usr/bin/bash.exe -l
yacc -d expr.y      # generates y.tab.c and y.tab.h
flex expr.l         # generates lex.yy.c
gcc y.tab.c lex.yy.c -o calc -lfl   # compile everything
./calc              # run the calculator


//on terminal 
bison -d expr.y           # generates expr.tab.c and expr.tab.h
flex expr.l               # generates lex.yy.c
gcc expr.tab.c lex.yy.c -o calc.exe   # no -lfl needed on Windows
.\calc.exe                # run the calculator
