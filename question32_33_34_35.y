%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char* s);
%}

%union {
    float fval;
}

%token <fval> FLOAT
%type <fval> expr

%left '+' '-'
%left '*' '/'

%%

input:
      input expr '\n'    { printf("Result = %.2f\n", $2); }
    | /* empty */
    ;

expr:
      expr '+' expr      { $$ = $1 + $3; }
    | expr '-' expr      { $$ = $1 - $3; }
    | expr '*' expr      { $$ = $1 * $3; }
    | expr '/' expr      { $$ = $1 / $3; }
    | '(' expr ')'       { $$ = $2; }
    | FLOAT              { $$ = $1; }
    ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter an arithmetic expression:\n");
    return yyparse();
}