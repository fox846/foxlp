flex pos_lex.l
gcc lex.yy.c -o pos_lex -lfl
./pos_lex

%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Convert a string to lowercase
void to_lower(char *dest, const char *src) {
    int i = 0;
    while (src[i]) {
        dest[i] = tolower((unsigned char)src[i]);
        i++;
    }
    dest[i] = '\0';
}

// POS word lists
const char* pronouns[] = {"i", "you", "he", "she", "it", "we", "they", "itself", NULL};
const char* verbs[] = {"am", "are", "is", "was", "were", "be", "been", "being", "have", "has", "do", "does", "imagine", "went", "comes", NULL};
const char* nouns[] = {"generation", "one", "it", NULL};
const char* adjectives[] = {"intelligent", "wiser", "more", NULL};
const char* interjections[] = {"oops", NULL};
const char* determiners[] = {"the", "a", "an", NULL};
const char* conjunctions[] = {"and", "but", "or", "nor", "so", NULL};
const char* modals[] = {"can", "should", "would", "might", NULL};
const char* prepositions[] = {"to", "before", "after", NULL};

// Match a word with a category list
int match(const char* word, const char* list[]) {
    char lower[100];
    to_lower(lower, word);
    for (int i = 0; list[i]; i++) {
        if (strcmp(lower, list[i]) == 0)
            return 1;
    }
    return 0;
}
%}

%%

// Handle variations of "I'm" with smart apostrophes or grave accents
[Ii](['’`‛＇´‘])m {
    printf("Pronoun: I\n");
    printf("Verb: am\n");
}

[[:alpha:]]+ {
    if (match(yytext, interjections))    printf("Interjection: %s\n", yytext);
    else if (match(yytext, conjunctions)) printf("Conjunction: %s\n", yytext);
    else if (match(yytext, pronouns))    printf("Pronoun: %s\n", yytext);
    else if (match(yytext, verbs))       printf("Verb: %s\n", yytext);
    else if (match(yytext, nouns))       printf("Noun: %s\n", yytext);
    else if (match(yytext, adjectives))  printf("Adjective: %s\n", yytext);
    else if (match(yytext, determiners)) printf("Determiner: %s\n", yytext);
    else if (match(yytext, modals))      printf("Modal: %s\n", yytext);
    else if (match(yytext, prepositions)) printf("Preposition: %s\n", yytext);
    else                                 printf("Unknown Word: %s\n", yytext);
}

[.!?,]       { printf("Punctuation: %s\n", yytext); }
[ \t\n]+     { /* Ignore whitespace */ }
.            { printf("Unknown Symbol: %s\n", yytext); }

%%

int main() {
    printf("Enter a sentence (Ctrl+D to end input):\n");
    yylex();
    return 0;
}
