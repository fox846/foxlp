%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+\.[0-9]+     { yylval.fval = atof(yytext); return FLOAT; }
[0-9]+             { yylval.fval = atof(yytext); return FLOAT; }
[ \t]+             ;   // ignore whitespace
\n                 { return '\n'; }
.                  { return yytext[0]; }

%%
