grammar Expression;

program: statement+ EOF;

statement
    : TYPE IDENTIFIER ('=' expression)? ';'  #declareStmt
    | IDENTIFIER '=' expression ';'          #assignStmt
    | 'if' '(' expression ')' '{' block '}' ('else' '{' block '}')?  #ifStmt
    | 'while' '(' expression ')' '{' block '}'   #whileStmt
    | 'for' '(' forInit? ';' expression? ';' forUpdate? ')' '{' block '}'  #forStmt
    | 'function' IDENTIFIER '(' parameters? ')' '{' block 'return' expression';' '}'  #funcDefStmt
    | 'print' expression ';'                #printStmt
    | expression ';'                        #exprStmt
    | IDENTIFIER ('++' | '--') ';'          #incDecStmt
    | 'goto' IDENTIFIER ';'  #gotoStmt
    | IDENTIFIER ':' statement  #labeledStmt
    ;

forInit
    : TYPE? IDENTIFIER '=' expression
    | IDENTIFIER '=' expression
    ;

forUpdate
    : IDENTIFIER ('++' | '--')
    | IDENTIFIER '+=' expression
    | IDENTIFIER '=' expression
    ;

block: statement*;

parameters: param (',' param)*;
param: TYPE IDENTIFIER;

expression
    : NUMBER                                # numberExpr
    | BOOL                                  # boolExpr
    | STRING                                # stringExpr
    | IDENTIFIER                            # variableExpr
    | IDENTIFIER '(' arguments? ')'         # functionCallExpr
    | '(' expression ')'                    # parenExpr
    | expression op=('*'|'/') expression    # mulDivExpr
    | expression op=('+'|'-') expression    # addSubExpr
    | expression op=('=='|'!='|'<'|'>'|'<='|'>=') expression  # comparisonExpr
    | expression '&&' expression            # logicalAndExpr
    | expression '||' expression            # logicalOrExpr
    ;

arguments: expression (',' expression)*;

TYPE: 'int' | 'float' | 'bool' | 'string';
BOOL: 'false' | 'true';
NUMBER: [0-9]+ ('.' [0-9]+)?;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;

