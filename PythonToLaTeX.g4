grammar PythonToLaTeX;

// Parser Rules

start: stat* EOF;

stat: '[' numerator=stat ']' op=(FRACTIONS|POWERS) '[' denominator=stat ']' #equationFloor
	| expression #exprStatic
	;

expression: factor                           #exprTerm
		  | l=expression op=ADD r=expression #addOp
          | l=expression op=SUB r=expression #subOp
          | l=expression op=DIV r=expression #divOp
          | l=expression op=MUL r=expression #mulOp
          ;


factor: INT                     #number
      | ID                      #variable
      | LPAREN stat RPAREN      #parenExpr
      ;

// Lexer Rules

FRACTIONS: '//';
POWERS: '^';
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
