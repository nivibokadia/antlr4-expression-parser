grammar Expression;

program: statement+ EOF;

statement
    : TYPE? IDENTIFIER '=' expression ';'   #assignStmt
    | 'if' '(' expression ')' '{' block '}' ('else' '{' block '}')?  #ifStmt
    | 'while' '(' expression ')' '{' block '}'   #whileStmt
    | 'function' IDENTIFIER '(' parameters? ')' '{' block 'return' expression';' '}'  #funcDefStmt
    | 'print' expression ';'                #printStmt
    | expression ';'                        #exprStmt
    ;

block: statement*;

parameters: param (',' param)*;
param: TYPE IDENTIFIER;

expression
    : NUMBER                                # numberExpr
    | BOOL                                  # boolExpr
    | IDENTIFIER                            # variableExpr
    | IDENTIFIER '(' arguments? ')'         # functionCallExpr
    | '(' expression ')'                    # parenExpr
    | expression op=('*'|'/') expression    # mulDivExpr
    | expression op=('+'|'-') expression    # addSubExpr
    | expression op=('=='|'!='|'<'|'>'|'<='|'>=') expression  # comparisonExpr
    ;

arguments: expression (',' expression)*;

TYPE: 'int' | 'float' | 'bool';
BOOL: 'true' | 'false';
NUMBER: [0-9]+ ('.' [0-9]+)?;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;