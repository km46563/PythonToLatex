# Generated from PythonToLaTeX.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,5,1,
        27,8,1,10,1,12,1,30,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,42,8,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,3,2,51,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,68,8,3,10,3,
        12,3,71,9,3,1,4,1,4,3,4,75,8,4,1,4,0,2,2,6,5,0,2,4,6,8,0,3,2,0,9,
        9,14,18,1,0,3,4,1,0,5,8,83,0,13,1,0,0,0,2,18,1,0,0,0,4,50,1,0,0,
        0,6,52,1,0,0,0,8,74,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,
        0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,
        17,5,0,0,1,17,1,1,0,0,0,18,19,6,1,-1,0,19,20,3,4,2,0,20,28,1,0,0,
        0,21,22,10,1,0,0,22,24,7,0,0,0,23,25,3,2,1,0,24,23,1,0,0,0,24,25,
        1,0,0,0,25,27,1,0,0,0,26,21,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,
        28,29,1,0,0,0,29,3,1,0,0,0,30,28,1,0,0,0,31,51,3,6,3,0,32,33,5,1,
        0,0,33,34,3,4,2,0,34,35,5,2,0,0,35,36,7,1,0,0,36,37,5,1,0,0,37,38,
        3,4,2,0,38,41,5,2,0,0,39,40,7,2,0,0,40,42,3,4,2,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,51,1,0,0,0,43,44,5,12,0,0,44,45,3,4,2,0,45,48,5,
        13,0,0,46,47,7,2,0,0,47,49,3,4,2,0,48,46,1,0,0,0,48,49,1,0,0,0,49,
        51,1,0,0,0,50,31,1,0,0,0,50,32,1,0,0,0,50,43,1,0,0,0,51,5,1,0,0,
        0,52,53,6,3,-1,0,53,54,3,8,4,0,54,69,1,0,0,0,55,56,10,4,0,0,56,57,
        5,5,0,0,57,68,3,6,3,5,58,59,10,3,0,0,59,60,5,6,0,0,60,68,3,6,3,4,
        61,62,10,2,0,0,62,63,5,8,0,0,63,68,3,6,3,3,64,65,10,1,0,0,65,66,
        5,7,0,0,66,68,3,6,3,2,67,55,1,0,0,0,67,58,1,0,0,0,67,61,1,0,0,0,
        67,64,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,7,1,0,
        0,0,71,69,1,0,0,0,72,75,5,19,0,0,73,75,5,20,0,0,74,72,1,0,0,0,74,
        73,1,0,0,0,75,9,1,0,0,0,9,13,24,28,41,48,50,67,69,74
    ]

class PythonToLaTeXParser ( Parser ):

    grammarFileName = "PythonToLaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'//'", "'^'", "'+'", "'-'", 
                     "'*'", "'/'", "'='", "'.'", "';'", "'('", "')'", "'>'", 
                     "'<'", "'>='", "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FRACTIONS", 
                      "POWERS", "ADD", "SUB", "MUL", "DIV", "EQ", "COMMA", 
                      "SEMI", "LPAREN", "RPAREN", "GREATER", "LESSER", "GREATEREQ", 
                      "LESSEREQ", "UNEQ", "INT", "ID", "WS" ]

    RULE_start = 0
    RULE_equation = 1
    RULE_stat = 2
    RULE_expression = 3
    RULE_factor = 4

    ruleNames =  [ "start", "equation", "stat", "expression", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    FRACTIONS=3
    POWERS=4
    ADD=5
    SUB=6
    MUL=7
    DIV=8
    EQ=9
    COMMA=10
    SEMI=11
    LPAREN=12
    RPAREN=13
    GREATER=14
    LESSER=15
    GREATEREQ=16
    LESSEREQ=17
    UNEQ=18
    INT=19
    ID=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonToLaTeXParser.EOF, 0)

        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.EquationContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.EquationContext,i)


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = PythonToLaTeXParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1576962) != 0):
                self.state = 10
                self.equation(0)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(PythonToLaTeXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EquationStaticContext(EquationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.EquationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.StatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquationStatic" ):
                listener.enterEquationStatic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquationStatic" ):
                listener.exitEquationStatic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquationStatic" ):
                return visitor.visitEquationStatic(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryEquationContext(EquationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.EquationContext
            super().__init__(parser)
            self.l = None # EquationContext
            self.op = None # Token
            self.r = None # EquationContext
            self.copyFrom(ctx)

        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.EquationContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.EquationContext,i)

        def EQ(self):
            return self.getToken(PythonToLaTeXParser.EQ, 0)
        def GREATER(self):
            return self.getToken(PythonToLaTeXParser.GREATER, 0)
        def LESSER(self):
            return self.getToken(PythonToLaTeXParser.LESSER, 0)
        def GREATEREQ(self):
            return self.getToken(PythonToLaTeXParser.GREATEREQ, 0)
        def LESSEREQ(self):
            return self.getToken(PythonToLaTeXParser.LESSEREQ, 0)
        def UNEQ(self):
            return self.getToken(PythonToLaTeXParser.UNEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryEquation" ):
                listener.enterPrimaryEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryEquation" ):
                listener.exitPrimaryEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryEquation" ):
                return visitor.visitPrimaryEquation(self)
            else:
                return visitor.visitChildren(self)



    def equation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.EquationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_equation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PythonToLaTeXParser.EquationStaticContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 19
            self.stat()
            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonToLaTeXParser.PrimaryEquationContext(self, PythonToLaTeXParser.EquationContext(self, _parentctx, _parentState))
                    localctx.l = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equation)
                    self.state = 21
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 22
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 508416) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 23
                        localctx.r = self.equation(0)

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatExpressionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatExpression" ):
                listener.enterStatExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatExpression" ):
                listener.exitStatExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatExpression" ):
                return visitor.visitStatExpression(self)
            else:
                return visitor.visitChildren(self)


    class StaticFloorContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.StatContext
            super().__init__(parser)
            self.numerator = None # StatContext
            self.florOp = None # Token
            self.denominator = None # StatContext
            self.simplOp = None # Token
            self.rest = None # StatContext
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.StatContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.StatContext,i)

        def FRACTIONS(self):
            return self.getToken(PythonToLaTeXParser.FRACTIONS, 0)
        def POWERS(self):
            return self.getToken(PythonToLaTeXParser.POWERS, 0)
        def ADD(self):
            return self.getToken(PythonToLaTeXParser.ADD, 0)
        def SUB(self):
            return self.getToken(PythonToLaTeXParser.SUB, 0)
        def DIV(self):
            return self.getToken(PythonToLaTeXParser.DIV, 0)
        def MUL(self):
            return self.getToken(PythonToLaTeXParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticFloor" ):
                listener.enterStaticFloor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticFloor" ):
                listener.exitStaticFloor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticFloor" ):
                return visitor.visitStaticFloor(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.StatContext
            super().__init__(parser)
            self.simplOp = None # Token
            self.rest = None # StatContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PythonToLaTeXParser.LPAREN, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.StatContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.StatContext,i)

        def RPAREN(self):
            return self.getToken(PythonToLaTeXParser.RPAREN, 0)
        def ADD(self):
            return self.getToken(PythonToLaTeXParser.ADD, 0)
        def SUB(self):
            return self.getToken(PythonToLaTeXParser.SUB, 0)
        def DIV(self):
            return self.getToken(PythonToLaTeXParser.DIV, 0)
        def MUL(self):
            return self.getToken(PythonToLaTeXParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = PythonToLaTeXParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20]:
                localctx = PythonToLaTeXParser.StatExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.expression(0)
                pass
            elif token in [1]:
                localctx = PythonToLaTeXParser.StaticFloorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(PythonToLaTeXParser.T__0)
                self.state = 33
                localctx.numerator = self.stat()
                self.state = 34
                self.match(PythonToLaTeXParser.T__1)
                self.state = 35
                localctx.florOp = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.florOp = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.match(PythonToLaTeXParser.T__0)
                self.state = 37
                localctx.denominator = self.stat()
                self.state = 38
                self.match(PythonToLaTeXParser.T__1)
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 39
                    localctx.simplOp = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                        localctx.simplOp = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 40
                    localctx.rest = self.stat()


                pass
            elif token in [12]:
                localctx = PythonToLaTeXParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(PythonToLaTeXParser.LPAREN)
                self.state = 44
                self.stat()
                self.state = 45
                self.match(PythonToLaTeXParser.RPAREN)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 46
                    localctx.simplOp = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                        localctx.simplOp = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 47
                    localctx.rest = self.stat()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(PythonToLaTeXParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivOp" ):
                listener.enterDivOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivOp" ):
                listener.exitDivOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivOp" ):
                return visitor.visitDivOp(self)
            else:
                return visitor.visitChildren(self)


    class MulOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(PythonToLaTeXParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOp" ):
                listener.enterMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOp" ):
                listener.exitMulOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)


    class ExprFactorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFactor" ):
                listener.enterExprFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFactor" ):
                listener.exitExprFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFactor" ):
                return visitor.visitExprFactor(self)
            else:
                return visitor.visitChildren(self)


    class AddOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(PythonToLaTeXParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)


    class SubOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(PythonToLaTeXParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubOp" ):
                listener.enterSubOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubOp" ):
                listener.exitSubOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubOp" ):
                return visitor.visitSubOp(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PythonToLaTeXParser.ExprFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 53
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = PythonToLaTeXParser.AddOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 56
                        localctx.op = self.match(PythonToLaTeXParser.ADD)
                        self.state = 57
                        localctx.r = self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = PythonToLaTeXParser.SubOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        localctx.op = self.match(PythonToLaTeXParser.SUB)
                        self.state = 60
                        localctx.r = self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = PythonToLaTeXParser.DivOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        localctx.op = self.match(PythonToLaTeXParser.DIV)
                        self.state = 63
                        localctx.r = self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = PythonToLaTeXParser.MulOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 65
                        localctx.op = self.match(PythonToLaTeXParser.MUL)
                        self.state = 66
                        localctx.r = self.expression(2)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PythonToLaTeXParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PythonToLaTeXParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = PythonToLaTeXParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = PythonToLaTeXParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(PythonToLaTeXParser.INT)
                pass
            elif token in [20]:
                localctx = PythonToLaTeXParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(PythonToLaTeXParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.equation_sempred
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def equation_sempred(self, localctx:EquationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




