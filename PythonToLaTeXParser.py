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
        4,1,12,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,5,2,19,8,2,10,2,12,2,22,9,2,1,3,1,3,1,3,5,3,27,
        8,3,10,3,12,3,30,9,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,38,8,4,1,4,0,0,
        5,0,2,4,6,8,0,2,1,0,1,2,1,0,3,4,38,0,10,1,0,0,0,2,13,1,0,0,0,4,15,
        1,0,0,0,6,23,1,0,0,0,8,37,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,
        1,1,0,0,0,13,14,3,4,2,0,14,3,1,0,0,0,15,20,3,6,3,0,16,17,7,0,0,0,
        17,19,3,6,3,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,
        0,0,0,21,5,1,0,0,0,22,20,1,0,0,0,23,28,3,8,4,0,24,25,7,1,0,0,25,
        27,3,8,4,0,26,24,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,
        0,29,7,1,0,0,0,30,28,1,0,0,0,31,32,5,8,0,0,32,33,3,2,1,0,33,34,5,
        9,0,0,34,38,1,0,0,0,35,38,5,10,0,0,36,38,5,11,0,0,37,31,1,0,0,0,
        37,35,1,0,0,0,37,36,1,0,0,0,38,9,1,0,0,0,3,20,28,37
    ]

class PythonToLaTeXParser ( Parser ):

    grammarFileName = "PythonToLaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'.'", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "INT", "ID", "WS" ]

    RULE_start = 0
    RULE_expression = 1
    RULE_add_expression = 2
    RULE_mul_expression = 3
    RULE_atom_expression = 4

    ruleNames =  [ "start", "expression", "add_expression", "mul_expression", 
                   "atom_expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    EQ=5
    COMMA=6
    SEMI=7
    LPAREN=8
    RPAREN=9
    INT=10
    ID=11
    WS=12

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
            self.state = 10
            self.expression()
            self.state = 11
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

        def add_expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.Add_expressionContext,0)


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PythonToLaTeXParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.add_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.Mul_expressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.Mul_expressionContext,i)


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_add_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_expression" ):
                listener.enterAdd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_expression" ):
                listener.exitAdd_expression(self)




    def add_expression(self):

        localctx = PythonToLaTeXParser.Add_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_add_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.mul_expression()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 16
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self.mul_expression()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonToLaTeXParser.Atom_expressionContext)
            else:
                return self.getTypedRuleContext(PythonToLaTeXParser.Atom_expressionContext,i)


        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_mul_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_expression" ):
                listener.enterMul_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_expression" ):
                listener.exitMul_expression(self)




    def mul_expression(self):

        localctx = PythonToLaTeXParser.Mul_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mul_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.atom_expression()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                self.atom_expression()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(PythonToLaTeXParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PythonToLaTeXParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PythonToLaTeXParser.RPAREN, 0)

        def INT(self):
            return self.getToken(PythonToLaTeXParser.INT, 0)

        def ID(self):
            return self.getToken(PythonToLaTeXParser.ID, 0)

        def getRuleIndex(self):
            return PythonToLaTeXParser.RULE_atom_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_expression" ):
                listener.enterAtom_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_expression" ):
                listener.exitAtom_expression(self)




    def atom_expression(self):

        localctx = PythonToLaTeXParser.Atom_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom_expression)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(PythonToLaTeXParser.LPAREN)
                self.state = 32
                self.expression()
                self.state = 33
                self.match(PythonToLaTeXParser.RPAREN)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(PythonToLaTeXParser.INT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
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





