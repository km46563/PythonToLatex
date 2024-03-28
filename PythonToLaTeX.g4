grammar PythonToLaTeX;

// Parser Rules

start: expression EOF;

expression: add_expression;

add_expression: mul_expression (('+' | '-') mul_expression)*;

mul_expression: atom_expression (('*' | '/') atom_expression)*;

atom_expression: '(' expression ')' | INT | ID;


// Lexer Rules

EQ: '=';
COMMA: '.';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';

INT: ('0'..'9')+ ('.'('0'..'9')+)?;
ID: [a-zA-Z]+;
WS: [ \r\n\t]+ -> skip;
