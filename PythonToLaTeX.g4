grammar PythonToLaTeX;

// Parser Rules

start: equation* EOF;

equation: stat  #equationStatic
		| l=equation op=(EQ|GREATER|LESSER|GREATEREQ|LESSEREQ|UNEQ) (r=equation)? #primaryEquation
		;

stat: expression #statExpression
	| '[' numerator=stat ']' florOp=(FRACTIONS|POWERS) '[' denominator=stat ']' (simplOp=(ADD|SUB|DIV|MUL) rest=stat)? #staticFloor
	| LPAREN stat RPAREN (simplOp=(ADD|SUB|DIV|MUL) rest=stat)?   #parenExpr
	;

expression: factor                           #exprFactor
		  | l=expression op=ADD r=expression #addOp
          | l=expression op=SUB r=expression #subOp
          | l=expression op=DIV r=expression #divOp
          | l=expression op=MUL r=expression #mulOp
          ;

factor: INT                     #number
      | ID                      #variable
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
GREATER: '>';
LESSER: '<';
GREATEREQ: '>=';
LESSEREQ: '<=';
UNEQ: '!=';

INT: ('0'..'9')+ ('.'('0'..'9')+)?;
ID: [a-zA-Z]+;
WS: [ \r\n\t]+ -> skip;
