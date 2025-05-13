%{
#include "y.tab.h"
%}

%%
[a-z][a-zA-Z0-9_]*   { return VALID; }
.*                   { return INVALID; }
%%
int yywrap() {
    return 1;
}


