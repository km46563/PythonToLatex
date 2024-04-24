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
        4,1,13,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,
        9,3,1,3,0,3,2,4,6,4,0,2,4,6,0,0,59,0,8,1,0,0,0,2,11,1,0,0,0,4,25,
        1,0,0,0,6,46,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,
        6,1,-1,0,12,13,3,4,2,0,13,22,1,0,0,0,14,15,10,3,0,0,15,16,5,1,0,
        0,16,21,3,4,2,0,17,18,10,2,0,0,18,19,5,2,0,0,19,21,3,4,2,0,20,14,
        1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,
        23,3,1,0,0,0,24,22,1,0,0,0,25,26,6,2,-1,0,26,27,3,6,3,0,27,36,1,
        0,0,0,28,29,10,3,0,0,29,30,5,3,0,0,30,35,3,6,3,0,31,32,10,2,0,0,
        32,33,5,4,0,0,33,35,3,6,3,0,34,28,1,0,0,0,34,31,1,0,0,0,35,38,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,1,0,0,0,39,
        40,6,3,-1,0,40,47,5,11,0,0,41,47,5,12,0,0,42,43,5,9,0,0,43,44,3,
        2,1,0,44,45,5,10,0,0,45,47,1,0,0,0,46,39,1,0,0,0,46,41,1,0,0,0,46,
        42,1,0,0,0,47,53,1,0,0,0,48,49,10,1,0,0,49,50,5,5,0,0,50,52,3,6,
        3,2,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,7,
        1,0,0,0,55,53,1,0,0,0,6,20,22,34,36,46,53
    ]

class PythonToLaTeXParser ( Parser ):

    grammarFileName = "PythonToLaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'**'", "'='", 
                     "'.'", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "POW", "EQ", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "INT", "ID", 
                      "WS" ]

    RULE_start = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "start", "expression", "term", "factor" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    POW=5
    EQ=6
    COMMA=7
    SEMI=8
    LPAREN=9
    RPAREN=10
    INT=11
    ID=12
    WS=13

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

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(PythonToLaTeXParser.EOF, 0)

        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PythonToLaTeXParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expression(0)
            self.state = 9
            self.match(PythonToLaTeXParser.EOF)
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


    class AddOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # TermContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)

        def ADD(self):
            return self.getToken(PythonToLaTeXParser.ADD, 0)
        def term(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)


    class SubOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.l = None # ExpressionContext
            self.op = None # Token
            self.r = None # TermContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)

        def SUB(self):
            return self.getToken(PythonToLaTeXParser.SUB, 0)
        def term(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubOp" ):
                listener.enterSubOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubOp" ):
                listener.exitSubOp(self)


    class ExprTermContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTerm" ):
                listener.enterExprTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTerm" ):
                listener.exitExprTerm(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PythonToLaTeXParser.ExprTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = PythonToLaTeXParser.AddOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        localctx.op = self.match(PythonToLaTeXParser.ADD)
                        self.state = 16
                        localctx.r = self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = PythonToLaTeXParser.SubOpContext(self, PythonToLaTeXParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        localctx.op = self.match(PythonToLaTeXParser.SUB)
                        self.state = 19
                        localctx.r = self.term(0)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivOpContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.TermContext
            super().__init__(parser)
            self.l = None # TermContext
            self.op = None # Token
            self.r = None # FactorContext
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.TermContext,0)

        def DIV(self):
            return self.getToken(PythonToLaTeXParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivOp" ):
                listener.enterDivOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivOp" ):
                listener.exitDivOp(self)


    class MulOpContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.TermContext
            super().__init__(parser)
            self.l = None # TermContext
            self.op = None # Token
            self.r = None # FactorContext
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.TermContext,0)

        def MUL(self):
            return self.getToken(PythonToLaTeXParser.MUL, 0)
        def factor(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOp" ):
                listener.enterMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOp" ):
                listener.exitMulOp(self)


    class TermFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermFactor" ):
                listener.enterTermFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermFactor" ):
                listener.exitTermFactor(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PythonToLaTeXParser.TermFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PythonToLaTeXParser.MulOpContext(self, PythonToLaTeXParser.TermContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        localctx.op = self.match(PythonToLaTeXParser.MUL)
                        self.state = 30
                        localctx.r = self.factor(0)
                        pass

                    elif la_ == 2:
                        localctx = PythonToLaTeXParser.DivOpContext(self, PythonToLaTeXParser.TermContext(self, _parentctx, _parentState))
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        localctx.op = self.match(PythonToLaTeXParser.DIV)
                        self.state = 33
                        localctx.r = self.factor(0)
                        pass

             
                self.state = 38
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


    class PowOpContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.FactorContext
            super().__init__(parser)
            self.l = None # FactorContext
            self.op = None # Token
            self.r = None # FactorContext
            self.copyFrom(ctx)

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.FactorContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.FactorContext,i)

        def POW(self):
            return self.getToken(PythonToLaTeXParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowOp" ):
                listener.enterPowOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowOp" ):
                listener.exitPowOp(self)


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


    class ParenExprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonToLaTeXParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PythonToLaTeXParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(PythonToLaTeXParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonToLaTeXParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = PythonToLaTeXParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 40
                self.match(PythonToLaTeXParser.INT)
                pass
            elif token in [12]:
                localctx = PythonToLaTeXParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(PythonToLaTeXParser.ID)
                pass
            elif token in [9]:
                localctx = PythonToLaTeXParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(PythonToLaTeXParser.LPAREN)
                self.state = 43
                self.expression(0)
                self.state = 44
                self.match(PythonToLaTeXParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonToLaTeXParser.PowOpContext(self, PythonToLaTeXParser.FactorContext(self, _parentctx, _parentState))
                    localctx.l = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 48
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 49
                    localctx.op = self.match(PythonToLaTeXParser.POW)
                    self.state = 50
                    localctx.r = self.factor(2) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        self._predicates[2] = self.term_sempred
        self._predicates[3] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




