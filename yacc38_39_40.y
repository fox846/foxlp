%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int yylex();
int yyerror(char *s);
%}

%union {
    float fval;
    char* str;
}

%token <fval> NUMBER
%token <str> STRING
%token <str> ID

%token SQRT STRLEN SIN COS POW LOG
%token ASSIGN LPAREN RPAREN COMMA

%left '+' '-'
%left '*' '/'

%type <fval> expr

%%

input:
    input stmt '\n'
  | stmt '\n'
;

stmt:
      ID ASSIGN expr   { printf("%s = %.2f\n", $1, $3); free($1); }
    | expr             { printf("Result = %.2f\n", $1); }
    | ID               { printf("Variable: %s\n", $1); free($1); }
;

expr:
      NUMBER                       { $$ = $1; }
    | expr '+' expr               { $$ = $1 + $3; }
    | expr '-' expr               { $$ = $1 - $3; }
    | expr '*' expr               { $$ = $1 * $3; }
    | expr '/' expr               { $$ = $1 / $3; }

    | SQRT LPAREN expr RPAREN     { $$ = sqrt($3); }
    | SIN LPAREN expr RPAREN      { $$ = sin($3); }
    | COS LPAREN expr RPAREN      { $$ = cos($3); }
    | LOG LPAREN expr RPAREN      { $$ = log($3); }
    | POW LPAREN expr COMMA expr RPAREN { $$ = pow($3, $5); }

    | STRLEN LPAREN STRING RPAREN {
                                    // Remove surrounding quotes
                                    int len = strlen($3) - 2;
                                    $$ = len;
                                    free($3);
                                  }
;

%%

int main() {
    printf("Enter expression like:\n");
    printf("u = sqrt(36)\nv = strlen(\"pune\")\np = pow(3,2) / log(24)\n> ");
    while (1) { // Allow multiple inputs
        printf("> ");
        yyparse();
    }
    return 0;
}

int yyerror(char *s) {
    printf("Parsing error: %s\n", s);
    return 0;
}