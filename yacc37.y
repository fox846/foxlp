%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Declare yylex and yyerror to avoid warnings
int yylex();
int yyerror(char *s);
%}

%union {
    char* str;
}

%token <str> WORD

%%

input:
    WORD    {
                char *word = $1;
                for (int i = 0; word[i] != '\0'; i++) {
                    if (islower(word[i]))
                        word[i] = toupper(word[i]);
                    else if (isupper(word[i]))
                        word[i] = tolower(word[i]);
                }
                printf("Converted: %s\n", word);
                free(word);
            }
;

%%

int main() {
    printf("Enter a word to convert case: ");
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("Parsing error: %s\n", s);
    return 0;
}
