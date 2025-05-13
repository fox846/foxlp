%{
#include <stdio.h>
#include <stdlib.h>

// Declare yylex and yyerror to avoid warnings
int yylex();
int yyerror(char *s);
%}

%token VALID INVALID

%%
input:
    VALID     { printf("Valid Variable Name\n"); }
  | INVALID   { printf("Invalid Variable Name\n"); }
;
%%

int main() {
    printf("Enter variable name: ");
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("Parsing error: %s\n", s);
    return 0;
}
