grammar MyLang;

// Parser rules

program: (functionDecl | varDecl | statement)* ;

functionDecl
    : ('async' 'function' | 'function') IDENTIFIER '(' paramList? ')' block
    ;

paramList
    : param (',' param)*
    ;

param
    : IDENTIFIER '[' type ']'
    ;

varDecl
    : ('const' | 'let') IDENTIFIER '[' type ']' '=' expression
    ;

block
    : '{' (statement | varDecl)* '}'
    ;

statement
    : varDecl
    | assignment
    | ifStatement
    | loop
    | functionCall
    | 'return' expression?
    | 'log' '(' expression ')'
    | 'await' functionCall
    ;

assignment
    : IDENTIFIER '=' expression
    | IDENTIFIER '++'
    | IDENTIFIER '--'
    ;

ifStatement
    : 'if' '(' expression ')' block ( 'else' 'if' '(' expression ')' block )* ( 'else' block )?
    ;

loop
    : 'for' '(' varDecl ';' expression ';' assignment ')' block
    | 'while' '(' expression ')' block
    ;

functionCall
    : IDENTIFIER '(' argumentList? ')'
    ;

argumentList
    : expression (',' expression)*
    ;

// Expression rules
expression
    : literal
    | IDENTIFIER
    | functionCall
    | '(' expression ')'
    | expression binaryOp expression
    | '-' expression
    | expression '[' expression ']' // array access
    | expression '.' IDENTIFIER '(' argumentList? ')' // method call
    | expression '.' IDENTIFIER // property access
    | array
    | object
    | IDENTIFIER '++'
    | IDENTIFIER '--'
    ;

binaryOp
    : '+' | '-' | '*' | '/' | '<' | '<=' | '>' | '>=' | '==' | '!='
    ;

// Lexer rules

IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

INT_LITERAL
    : [0-9]+
    ;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]*
    ;

STRING_LITERAL
    : '"' ( ~["\\] | '\\' . )* '"'
    | '\'' ( ~['\\] | '\\' . )* '\''
    ;

type
    : 'int' | 'float' | 'str' | 'bool' | 'any' | 'obj'
    ;

literal
    : INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | 'true'
    | 'false'
    ;

array
    : '[' (expression (',' expression)*)? ']'
    ;

object
    : '{' (objectField (',' objectField)*)? '}'
    ;

objectField
    : IDENTIFIER ':' expression
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;
