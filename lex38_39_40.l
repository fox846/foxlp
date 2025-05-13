%{
#include "y.tab.h"
#include <stdlib.h>
#include <string.h>
%}

%%
"sqrt"                    { return SQRT; }
"strlen"                  { return STRLEN; }
"sin"                     { return SIN; }
"cos"                     { return COS; }
"pow"                     { return POW; }
"log"                     { return LOG; }
\"[^\"]*\"                { yylval.str = strdup(yytext); return STRING; } // Match string literals
[a-zA-Z_][a-zA-Z0-9_]*    { yylval.str = strdup(yytext); return ID; }
[0-9]+(\.[0-9]+)?         { yylval.fval = atof(yytext); return NUMBER; }
"="                       { return ASSIGN; }
"("                       { return LPAREN; }
")"                       { return RPAREN; }
","                       { return COMMA; }
[ \t]+                    { /* Ignore whitespace */ }
\n                        { return '\n'; }
.                         { return yytext[0]; }
%%

int yywrap() {
    return 1;
}