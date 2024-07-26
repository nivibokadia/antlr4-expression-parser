grammar Expression;

program: statement+ EOF;

statement
    : TYPE IDENTIFIER ('=' (expression | arrayInitializer))? ';'  #declareStmt
    | IDENTIFIER '=' expression ';'          #assignStmt
    | 'if' '(' expression ')' '{' block '}' ('else' '{' block '}')?  #ifStmt
    | 'while' '(' expression ')' '{' block '}'   #whileStmt
    | 'for' '(' forInit? ';' expression? ';' forUpdate? ')' '{' block '}'  #forStmt
    | TYPE 'function' IDENTIFIER '(' parameters? ')' '{' block 'return' expression';' '}'  #funcDefStmt
    | 'print' '('? printArguments ')'? ';'    #printStmt
    | expression ';'                        #exprStmt
    | IDENTIFIER ('++' | '--') ';'          #incDecStmt
    | 'goto' IDENTIFIER ';'                 #gotoStmt
    | IDENTIFIER ':' statement              #labeledStmt
    | IDENTIFIER '.push' '(' expression ')' ';'  #arrayPushStmt
    | IDENTIFIER '.pop' '(' ')' ';'              #arrayPopStmt
    ;

printArguments
    : printArg (',' printArg)*
    ;

printArg
    : expression
    | STRING
    ;

arrayInitializer
    : '[' (expression (',' expression)*)? ']'
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
    | IDENTIFIER '[' expression ']'         # arrayAccessExpr
    | IDENTIFIER '.length'                  # arrayLengthExpr
    ;

arguments: expression (',' expression)*;

TYPE: 'int' | 'float' | 'bool' | 'string' | 'int[]' | 'float[]' | 'bool[]' | 'string[]';
BOOL: 'false' | 'true';
NUMBER: [0-9]+ ('.' [0-9]+)?;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;