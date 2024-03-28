grammar PythonToLaTeX;

// Parser Rules

start: expression EOF;

expression: expression '+' term #addOp
          | expression '-' term #subOp
          | term                #exprTerm
          ;

term: term '*' factor           #mulOp
    | term '/' factor           #divOp
    | factor                    #termFactor
    ;

factor: INT                     #number
      | ID                      #variable
      | '(' expression ')'      #parenExpr
      ;

// Lexer Rules

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
EQ: '=';
COMMA: '.';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';

INT: ('0'..'9')+ ('.'('0'..'9')+)?;
ID: [a-zA-Z]+;
WS: [ \r\n\t]+ -> skip;
