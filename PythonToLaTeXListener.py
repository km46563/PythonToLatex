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


    # Enter a parse tree produced by PythonToLaTeXParser#addOp.
    def enterAddOp(self, ctx:PythonToLaTeXParser.AddOpContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#addOp.
    def exitAddOp(self, ctx:PythonToLaTeXParser.AddOpContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#subOp.
    def enterSubOp(self, ctx:PythonToLaTeXParser.SubOpContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#subOp.
    def exitSubOp(self, ctx:PythonToLaTeXParser.SubOpContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#exprTerm.
    def enterExprTerm(self, ctx:PythonToLaTeXParser.ExprTermContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#exprTerm.
    def exitExprTerm(self, ctx:PythonToLaTeXParser.ExprTermContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#divOp.
    def enterDivOp(self, ctx:PythonToLaTeXParser.DivOpContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#divOp.
    def exitDivOp(self, ctx:PythonToLaTeXParser.DivOpContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#mulOp.
    def enterMulOp(self, ctx:PythonToLaTeXParser.MulOpContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#mulOp.
    def exitMulOp(self, ctx:PythonToLaTeXParser.MulOpContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#termFactor.
    def enterTermFactor(self, ctx:PythonToLaTeXParser.TermFactorContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#termFactor.
    def exitTermFactor(self, ctx:PythonToLaTeXParser.TermFactorContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#number.
    def enterNumber(self, ctx:PythonToLaTeXParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#number.
    def exitNumber(self, ctx:PythonToLaTeXParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#variable.
    def enterVariable(self, ctx:PythonToLaTeXParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#variable.
    def exitVariable(self, ctx:PythonToLaTeXParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonToLaTeXParser#parenExpr.
    def enterParenExpr(self, ctx:PythonToLaTeXParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PythonToLaTeXParser#parenExpr.
    def exitParenExpr(self, ctx:PythonToLaTeXParser.ParenExprContext):
        pass



del PythonToLaTeXParser