%{
#include "y.tab.h"
#include <string.h>
%}

%%

[A-Za-z]+   { yylval.str = strdup(yytext); return WORD; }
.|\n        { /* Ignore all other characters */ }

%%

int yywrap() {
    return 1;
}
