# Generated from PythonToLaTeX.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonToLaTeXParser import PythonToLaTeXParser
else:
    from PythonToLaTeXParser import PythonToLaTeXParser

# This class defines a complete generic visitor for a parse tree produced by PythonToLaTeXParser.

class PythonToLaTeXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonToLaTeXParser#start.
    def visitStart(self, ctx:PythonToLaTeXParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#equationFloor.
    def visitEquationFloor(self, ctx:PythonToLaTeXParser.EquationFloorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#exprStatic.
    def visitExprStatic(self, ctx:PythonToLaTeXParser.ExprStaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#divOp.
    def visitDivOp(self, ctx:PythonToLaTeXParser.DivOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#mulOp.
    def visitMulOp(self, ctx:PythonToLaTeXParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#addOp.
    def visitAddOp(self, ctx:PythonToLaTeXParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#subOp.
    def visitSubOp(self, ctx:PythonToLaTeXParser.SubOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#exprTerm.
    def visitExprTerm(self, ctx:PythonToLaTeXParser.ExprTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#number.
    def visitNumber(self, ctx:PythonToLaTeXParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#variable.
    def visitVariable(self, ctx:PythonToLaTeXParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonToLaTeXParser#parenExpr.
    def visitParenExpr(self, ctx:PythonToLaTeXParser.ParenExprContext):
        return self.visitChildren(ctx)



del PythonToLaTeXParser