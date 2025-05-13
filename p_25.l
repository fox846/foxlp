%{
#include <stdio.h>
%}

%option caseless

%%
"every"|"the"|"that"|"this"|"an"|"a"                                      { printf("<DETERMINER: %s>\n", yytext); }
"generation"|"one"|"it"                                                   { printf("<NOUN: %s>\n", yytext); }
"imagines"|"is"|"be"|"went"|"comes"|"went"|"went"|"went"|"went"|"went"   { printf("<VERB: %s>\n", yytext); }
"more"|"less"|"most"|"least"|"wiser"|"intelligent"                        { printf("<ADJECTIVE: %s>\n", yytext); }
"before"|"after"                                                          { printf("<ADVERB: %s>\n", yytext); }
"and"|"but"|"or"                                                          { printf("<CONJUNCTION: %s>\n", yytext); }
"than"|"to"                                                               { printf("<PREPOSITION: %s>\n", yytext); }
"itself"|"himself"|"herself"                                             { printf("<PRONOUN: %s>\n", yytext); }
","|"."                                                                   { printf("<PUNCTUATION: %s>\n", yytext); }
[ \t\n]+                                                                  { /* ignore whitespace */ }
.                                                                         { printf("<UNKNOWN: %s>\n", yytext); }
%%

int main() {
    printf("Enter a sentence:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
