flex pos_lex.l
gcc lex.yy.c -o pos_lex -lfl
./pos_lex

%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int is_keyword(char* str) {
    char* keywords[] = {"int", "float", "char", "void", "return", "if", "else", "for", "while", "break", "continue", NULL};
    for (int i = 0; keywords[i]; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}


int is_identifier(char* str) {
    if (isalpha(str[0]) || str[0] == '_') {
        for (int i = 1; str[i] != '\0'; i++) {
            if (!isalnum(str[i]) && str[i] != '_')
                return 0;
        }
        return 1;
    }
    return 0;
}
%}

%%

"int"|"float"|"char"|"void"|"return"|"if"|"else"|"for"|"while"|"break"|"continue" {
    printf("Keyword: %s\n", yytext);
}


[A-Za-z_][A-Za-z0-9_]* {
    if (is_keyword(yytext)) {
        printf("Keyword: %s\n", yytext);
    } else {
        printf("Identifier: %s\n", yytext);
    }
}


[0-9]+ {
    printf("Integer: %s\n", yytext);
}


"=" {
    printf("Assignment Operator: =\n");
}


"+"|"-"|"*"|"/" {
    printf("Arithmetic Operator: %s\n", yytext);
}


"{"|"}"|"("|")"|";" {
    printf("Punctuation: %s\n", yytext);
}


[ \t\n]+ {
    // Ignore whitespace
}


. {
    printf("Unknown Symbol: %s\n", yytext);
}

%%

int main() {
    printf("Enter C code (Ctrl+D to end input):\n");
    yylex();
    return 0;
}