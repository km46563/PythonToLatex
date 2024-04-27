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
        4,1,16,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,54,8,3,1,3,0,
        1,4,4,0,2,4,6,0,1,1,0,3,4,59,0,11,1,0,0,0,2,25,1,0,0,0,4,27,1,0,
        0,0,6,53,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,
        0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,
        1,0,0,0,16,17,5,1,0,0,17,18,3,2,1,0,18,19,5,2,0,0,19,20,7,0,0,0,
        20,21,5,1,0,0,21,22,3,2,1,0,22,23,5,2,0,0,23,26,1,0,0,0,24,26,3,
        4,2,0,25,16,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,6,2,-1,0,28,
        29,3,6,3,0,29,44,1,0,0,0,30,31,10,4,0,0,31,32,5,5,0,0,32,43,3,4,
        2,5,33,34,10,3,0,0,34,35,5,6,0,0,35,43,3,4,2,4,36,37,10,2,0,0,37,
        38,5,8,0,0,38,43,3,4,2,3,39,40,10,1,0,0,40,41,5,7,0,0,41,43,3,4,
        2,2,42,30,1,0,0,0,42,33,1,0,0,0,42,36,1,0,0,0,42,39,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,
        54,5,14,0,0,48,54,5,15,0,0,49,50,5,12,0,0,50,51,3,2,1,0,51,52,5,
        13,0,0,52,54,1,0,0,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,
        7,1,0,0,0,5,11,25,42,44,53
    ]

class PythonToLaTeXParser ( Parser ):

    grammarFileName = "PythonToLaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'//'", "'^'", "'+'", "'-'", 
                     "'*'", "'/'", "'='", "'.'", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FRACTIONS", 
                      "POWERS", "ADD", "SUB", "MUL", "DIV", "EQ", "COMMA", 
                      "SEMI", "LPAREN", "RPAREN", "INT", "ID", "WS" ]

    RULE_start = 0
    RULE_stat = 1
    RULE_expression = 2
    RULE_factor = 3

    ruleNames =  [ "start", "stat", "expression", "factor" ]

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
    INT=14
    ID=15
    WS=16

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.StatContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.StatContext,i)


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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53250) != 0):
                self.state = 8
                self.stat()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(PythonToLaTeXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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



    class EquationFloorContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.StatContext
            super().__init__(parser)
            self.numerator = None # StatContext
            self.op = None # Token
            self.denominator = None # StatContext
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquationFloor" ):
                listener.enterEquationFloor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquationFloor" ):
                listener.exitEquationFloor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquationFloor" ):
                return visitor.visitEquationFloor(self)
            else:
                return visitor.visitChildren(self)


    class ExprStaticContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatic" ):
                listener.enterExprStatic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatic" ):
                listener.exitExprStatic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatic" ):
                return visitor.visitExprStatic(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = PythonToLaTeXParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PythonToLaTeXParser.EquationFloorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(PythonToLaTeXParser.T__0)
                self.state = 17
                localctx.numerator = self.stat()
                self.state = 18
                self.match(PythonToLaTeXParser.T__1)
                self.state = 19
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.match(PythonToLaTeXParser.T__0)
                self.state = 21
                localctx.denominator = self.stat()
                self.state = 22
                self.match(PythonToLaTeXParser.T__1)
                pass
            elif token in [12, 14, 15]:
                localctx = PythonToLaTeXParser.ExprStaticContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.expression(0)
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


    class ExprTermContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTerm" ):
                listener.enterExprTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTerm" ):
                listener.exitExprTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprTerm" ):
                return visitor.visitExprTerm(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PythonToLaTeXParser.ExprTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 28
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PythonToLaTeXParser.AddOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.op = self.match(PythonToLaTeXParser.ADD)
                        self.state = 32
                        localctx.r = self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = PythonToLaTeXParser.SubOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        localctx.op = self.match(PythonToLaTeXParser.SUB)
                        self.state = 35
                        localctx.r = self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = PythonToLaTeXParser.DivOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        localctx.op = self.match(PythonToLaTeXParser.DIV)
                        self.state = 38
                        localctx.r = self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = PythonToLaTeXParser.MulOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 40
                        localctx.op = self.match(PythonToLaTeXParser.MUL)
                        self.state = 41
                        localctx.r = self.expression(2)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


    class ParenExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PythonToLaTeXParser.LPAREN, 0)
        def stat(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.StatContext,0)

        def RPAREN(self):
            return self.getToken(PythonToLaTeXParser.RPAREN, 0)

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



    def factor(self):

        localctx = PythonToLaTeXParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = PythonToLaTeXParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(PythonToLaTeXParser.INT)
                pass
            elif token in [15]:
                localctx = PythonToLaTeXParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(PythonToLaTeXParser.ID)
                pass
            elif token in [12]:
                localctx = PythonToLaTeXParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(PythonToLaTeXParser.LPAREN)
                self.state = 50
                self.stat()
                self.state = 51
                self.match(PythonToLaTeXParser.RPAREN)
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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




