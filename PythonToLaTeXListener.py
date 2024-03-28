# Generated from PythonToLaTeX.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonToLaTeXParser import PythonToLaTeXParser
else:
    from PythonToLaTeXParser import PythonToLaTeXParser

# This class defines a complete listener for a parse tree produced by PythonToLaTeXParser.
class PythonToLaTeXListener(ParseTreeListener):

    # Enter a parse tree produced by PythonToLaTeXParser#start.
    def enterStart(self, ctx:PythonToLaTeXParser.StartContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#start.
    def exitStart(self, ctx:PythonToLaTeXParser.StartContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#expression.
    def enterExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#expression.
    def exitExpression(self, ctx:PythonToLaTeXParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#add_expression.
    def enterAdd_expression(self, ctx:PythonToLaTeXParser.Add_expressionContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#add_expression.
    def exitAdd_expression(self, ctx:PythonToLaTeXParser.Add_expressionContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#mul_expression.
    def enterMul_expression(self, ctx:PythonToLaTeXParser.Mul_expressionContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#mul_expression.
    def exitMul_expression(self, ctx:PythonToLaTeXParser.Mul_expressionContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#atom_expression.
    def enterAtom_expression(self, ctx:PythonToLaTeXParser.Atom_expressionContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#atom_expression.
    def exitAtom_expression(self, ctx:PythonToLaTeXParser.Atom_expressionContext):
        pass



del PythonToLaTeXParser