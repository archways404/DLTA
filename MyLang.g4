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
    | 'return' expression?
    | 'log' '(' expression ')'
    | 'await' expression
    | expression // Allow expression as a statement for cases like myArray.push(6)
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

// Expression rules
expression
    : literal
    | IDENTIFIER '(' argumentList? ')' // Function call
    | expression '.' IDENTIFIER '(' argumentList? ')' // Method call
    | expression '.' IDENTIFIER // Property access
    | IDENTIFIER // Variable
    | '(' expression ')' // Grouped expression
    | expression binaryOp expression // Binary operation
    | '-' expression // Unary operation
    | expression '[' expression ']' // Array access
    | array
    | object
    | IDENTIFIER '++' // Increment
    | IDENTIFIER '--' // Decrement
    ;

binaryOp
    : '+' | '-' | '*' | '/' | '<' | '<=' | '>' | '>=' | '==' | '!='
    ;

argumentList
    : expression (',' expression)*
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

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;
