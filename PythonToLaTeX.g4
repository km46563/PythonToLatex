grammar PythonToLaTeX;

// Parser Rules

start: expression EOF;

expression: l=expression op=ADD r=term #addOp
          | l=expression op=SUB r=term #subOp
          | term                #exprTerm
          ;

term: l=term op=MUL r=factor           #mulOp
    | l=term op=DIV r=factor           #divOp
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
