# Generated from MyLang.g4 by ANTLR 4.13.1
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
        4,1,48,247,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,5,0,40,8,0,10,
        0,12,0,43,9,0,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,3,1,53,8,1,1,1,
        1,1,1,1,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,82,8,5,10,5,
        12,5,85,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,95,8,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,114,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,128,
        8,8,10,8,12,8,131,9,8,1,8,1,8,3,8,135,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,153,8,9,1,10,1,10,
        1,10,1,10,1,10,3,10,160,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,176,8,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,187,8,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,198,8,10,10,10,12,10,201,9,10,1,11,
        1,11,1,12,1,12,1,12,5,12,208,8,12,10,12,12,12,211,9,12,1,13,1,13,
        1,13,1,13,5,13,217,8,13,10,13,12,13,220,9,13,3,13,222,8,13,1,13,
        1,13,1,14,1,14,1,14,1,14,5,14,230,8,14,10,14,12,14,233,9,14,3,14,
        235,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,
        0,1,20,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,
        0,8,9,1,0,24,33,1,0,35,40,2,0,41,42,44,46,268,0,41,1,0,0,0,2,47,
        1,0,0,0,4,57,1,0,0,0,6,65,1,0,0,0,8,70,1,0,0,0,10,78,1,0,0,0,12,
        104,1,0,0,0,14,113,1,0,0,0,16,115,1,0,0,0,18,152,1,0,0,0,20,175,
        1,0,0,0,22,202,1,0,0,0,24,204,1,0,0,0,26,212,1,0,0,0,28,225,1,0,
        0,0,30,238,1,0,0,0,32,242,1,0,0,0,34,244,1,0,0,0,36,40,3,2,1,0,37,
        40,3,8,4,0,38,40,3,12,6,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,
        0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,41,
        1,0,0,0,44,45,5,1,0,0,45,48,5,2,0,0,46,48,5,2,0,0,47,44,1,0,0,0,
        47,46,1,0,0,0,48,49,1,0,0,0,49,50,5,43,0,0,50,52,5,3,0,0,51,53,3,
        4,2,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,4,0,0,55,
        56,3,10,5,0,56,3,1,0,0,0,57,62,3,6,3,0,58,59,5,5,0,0,59,61,3,6,3,
        0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,5,1,
        0,0,0,64,62,1,0,0,0,65,66,5,43,0,0,66,67,5,6,0,0,67,68,3,32,16,0,
        68,69,5,7,0,0,69,7,1,0,0,0,70,71,7,0,0,0,71,72,5,43,0,0,72,73,5,
        6,0,0,73,74,3,32,16,0,74,75,5,7,0,0,75,76,5,10,0,0,76,77,3,20,10,
        0,77,9,1,0,0,0,78,83,5,11,0,0,79,82,3,12,6,0,80,82,3,8,4,0,81,79,
        1,0,0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,
        84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,12,0,0,87,11,1,0,0,0,88,105,
        3,8,4,0,89,105,3,14,7,0,90,105,3,16,8,0,91,105,3,18,9,0,92,94,5,
        13,0,0,93,95,3,20,10,0,94,93,1,0,0,0,94,95,1,0,0,0,95,105,1,0,0,
        0,96,97,5,14,0,0,97,98,5,3,0,0,98,99,3,20,10,0,99,100,5,4,0,0,100,
        105,1,0,0,0,101,102,5,15,0,0,102,105,3,20,10,0,103,105,3,20,10,0,
        104,88,1,0,0,0,104,89,1,0,0,0,104,90,1,0,0,0,104,91,1,0,0,0,104,
        92,1,0,0,0,104,96,1,0,0,0,104,101,1,0,0,0,104,103,1,0,0,0,105,13,
        1,0,0,0,106,107,5,43,0,0,107,108,5,10,0,0,108,114,3,20,10,0,109,
        110,5,43,0,0,110,114,5,16,0,0,111,112,5,43,0,0,112,114,5,17,0,0,
        113,106,1,0,0,0,113,109,1,0,0,0,113,111,1,0,0,0,114,15,1,0,0,0,115,
        116,5,18,0,0,116,117,5,3,0,0,117,118,3,20,10,0,118,119,5,4,0,0,119,
        129,3,10,5,0,120,121,5,19,0,0,121,122,5,18,0,0,122,123,5,3,0,0,123,
        124,3,20,10,0,124,125,5,4,0,0,125,126,3,10,5,0,126,128,1,0,0,0,127,
        120,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,
        134,1,0,0,0,131,129,1,0,0,0,132,133,5,19,0,0,133,135,3,10,5,0,134,
        132,1,0,0,0,134,135,1,0,0,0,135,17,1,0,0,0,136,137,5,20,0,0,137,
        138,5,3,0,0,138,139,3,8,4,0,139,140,5,21,0,0,140,141,3,20,10,0,141,
        142,5,21,0,0,142,143,3,14,7,0,143,144,5,4,0,0,144,145,3,10,5,0,145,
        153,1,0,0,0,146,147,5,22,0,0,147,148,5,3,0,0,148,149,3,20,10,0,149,
        150,5,4,0,0,150,151,3,10,5,0,151,153,1,0,0,0,152,136,1,0,0,0,152,
        146,1,0,0,0,153,19,1,0,0,0,154,155,6,10,-1,0,155,176,3,34,17,0,156,
        157,5,43,0,0,157,159,5,3,0,0,158,160,3,24,12,0,159,158,1,0,0,0,159,
        160,1,0,0,0,160,161,1,0,0,0,161,176,5,4,0,0,162,176,5,43,0,0,163,
        164,5,3,0,0,164,165,3,20,10,0,165,166,5,4,0,0,166,176,1,0,0,0,167,
        168,5,24,0,0,168,176,3,20,10,6,169,176,3,26,13,0,170,176,3,28,14,
        0,171,172,5,43,0,0,172,176,5,16,0,0,173,174,5,43,0,0,174,176,5,17,
        0,0,175,154,1,0,0,0,175,156,1,0,0,0,175,162,1,0,0,0,175,163,1,0,
        0,0,175,167,1,0,0,0,175,169,1,0,0,0,175,170,1,0,0,0,175,171,1,0,
        0,0,175,173,1,0,0,0,176,199,1,0,0,0,177,178,10,7,0,0,178,179,3,22,
        11,0,179,180,3,20,10,8,180,198,1,0,0,0,181,182,10,11,0,0,182,183,
        5,23,0,0,183,184,5,43,0,0,184,186,5,3,0,0,185,187,3,24,12,0,186,
        185,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,198,5,4,0,0,189,
        190,10,10,0,0,190,191,5,23,0,0,191,198,5,43,0,0,192,193,10,5,0,0,
        193,194,5,6,0,0,194,195,3,20,10,0,195,196,5,7,0,0,196,198,1,0,0,
        0,197,177,1,0,0,0,197,181,1,0,0,0,197,189,1,0,0,0,197,192,1,0,0,
        0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,21,1,0,0,0,
        201,199,1,0,0,0,202,203,7,1,0,0,203,23,1,0,0,0,204,209,3,20,10,0,
        205,206,5,5,0,0,206,208,3,20,10,0,207,205,1,0,0,0,208,211,1,0,0,
        0,209,207,1,0,0,0,209,210,1,0,0,0,210,25,1,0,0,0,211,209,1,0,0,0,
        212,221,5,6,0,0,213,218,3,20,10,0,214,215,5,5,0,0,215,217,3,20,10,
        0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,
        0,219,222,1,0,0,0,220,218,1,0,0,0,221,213,1,0,0,0,221,222,1,0,0,
        0,222,223,1,0,0,0,223,224,5,7,0,0,224,27,1,0,0,0,225,234,5,11,0,
        0,226,231,3,30,15,0,227,228,5,5,0,0,228,230,3,30,15,0,229,227,1,
        0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,235,1,
        0,0,0,233,231,1,0,0,0,234,226,1,0,0,0,234,235,1,0,0,0,235,236,1,
        0,0,0,236,237,5,12,0,0,237,29,1,0,0,0,238,239,5,43,0,0,239,240,5,
        34,0,0,240,241,3,20,10,0,241,31,1,0,0,0,242,243,7,2,0,0,243,33,1,
        0,0,0,244,245,7,3,0,0,245,35,1,0,0,0,23,39,41,47,52,62,81,83,94,
        104,113,129,134,152,159,175,186,197,199,209,218,221,231,234
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'async'", "'function'", "'('", "')'", 
                     "','", "'['", "']'", "'const'", "'let'", "'='", "'{'", 
                     "'}'", "'return'", "'log'", "'await'", "'++'", "'--'", 
                     "'if'", "'else'", "'for'", "';'", "'while'", "'.'", 
                     "'-'", "'+'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "':'", "'int'", "'float'", "'str'", 
                     "'bool'", "'any'", "'obj'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_paramList = 2
    RULE_param = 3
    RULE_varDecl = 4
    RULE_block = 5
    RULE_statement = 6
    RULE_assignment = 7
    RULE_ifStatement = 8
    RULE_loop = 9
    RULE_expression = 10
    RULE_binaryOp = 11
    RULE_argumentList = 12
    RULE_array = 13
    RULE_object = 14
    RULE_objectField = 15
    RULE_type = 16
    RULE_literal = 17

    ruleNames =  [ "program", "functionDecl", "paramList", "param", "varDecl", 
                   "block", "statement", "assignment", "ifStatement", "loop", 
                   "expression", "binaryOp", "argumentList", "array", "object", 
                   "objectField", "type", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    IDENTIFIER=43
    INT_LITERAL=44
    FLOAT_LITERAL=45
    STRING_LITERAL=46
    WS=47
    COMMENT=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(MyLangParser.FunctionDeclContext,i)


        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(MyLangParser.VarDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 138538487442254) != 0):
                self.state = 39
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 37
                    self.varDecl()
                    pass

                elif la_ == 3:
                    self.state = 38
                    self.statement()
                    pass


                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MyLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = MyLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 44
                self.match(MyLangParser.T__0)
                self.state = 45
                self.match(MyLangParser.T__1)
                pass
            elif token in [2]:
                self.state = 46
                self.match(MyLangParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self.match(MyLangParser.IDENTIFIER)
            self.state = 50
            self.match(MyLangParser.T__2)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 51
                self.paramList()


            self.state = 54
            self.match(MyLangParser.T__3)
            self.state = 55
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ParamContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = MyLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.param()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 58
                self.match(MyLangParser.T__4)
                self.state = 59
                self.param()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MyLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MyLangParser.IDENTIFIER)
            self.state = 66
            self.match(MyLangParser.T__5)
            self.state = 67
            self.type_()
            self.state = 68
            self.match(MyLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = MyLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 71
            self.match(MyLangParser.IDENTIFIER)
            self.state = 72
            self.match(MyLangParser.T__5)
            self.state = 73
            self.type_()
            self.state = 74
            self.match(MyLangParser.T__6)
            self.state = 75
            self.match(MyLangParser.T__9)
            self.state = 76
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(MyLangParser.VarDeclContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MyLangParser.T__10)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 138538487442248) != 0):
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 79
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 80
                    self.varDecl()
                    pass


                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(MyLangParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MyLangParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfStatementContext,0)


        def loop(self):
            return self.getTypedRuleContext(MyLangParser.LoopContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.loop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(MyLangParser.T__12)
                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.expression(0)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.match(MyLangParser.T__13)
                self.state = 97
                self.match(MyLangParser.T__2)
                self.state = 98
                self.expression(0)
                self.state = 99
                self.match(MyLangParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 101
                self.match(MyLangParser.T__14)
                self.state = 102
                self.expression(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 103
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(MyLangParser.IDENTIFIER)
                self.state = 107
                self.match(MyLangParser.T__9)
                self.state = 108
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(MyLangParser.IDENTIFIER)
                self.state = 110
                self.match(MyLangParser.T__15)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.match(MyLangParser.IDENTIFIER)
                self.state = 112
                self.match(MyLangParser.T__16)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MyLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(MyLangParser.T__17)
            self.state = 116
            self.match(MyLangParser.T__2)
            self.state = 117
            self.expression(0)
            self.state = 118
            self.match(MyLangParser.T__3)
            self.state = 119
            self.block()
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.match(MyLangParser.T__18)
                    self.state = 121
                    self.match(MyLangParser.T__17)
                    self.state = 122
                    self.match(MyLangParser.T__2)
                    self.state = 123
                    self.expression(0)
                    self.state = 124
                    self.match(MyLangParser.T__3)
                    self.state = 125
                    self.block() 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 132
                self.match(MyLangParser.T__18)
                self.state = 133
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MyLangParser.VarDeclContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)




    def loop(self):

        localctx = MyLangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(MyLangParser.T__19)
                self.state = 137
                self.match(MyLangParser.T__2)
                self.state = 138
                self.varDecl()
                self.state = 139
                self.match(MyLangParser.T__20)
                self.state = 140
                self.expression(0)
                self.state = 141
                self.match(MyLangParser.T__20)
                self.state = 142
                self.assignment()
                self.state = 143
                self.match(MyLangParser.T__3)
                self.state = 144
                self.block()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MyLangParser.T__21)
                self.state = 147
                self.match(MyLangParser.T__2)
                self.state = 148
                self.expression(0)
                self.state = 149
                self.match(MyLangParser.T__3)
                self.state = 150
                self.block()
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

        def literal(self):
            return self.getTypedRuleContext(MyLangParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MyLangParser.ArgumentListContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def array(self):
            return self.getTypedRuleContext(MyLangParser.ArrayContext,0)


        def object_(self):
            return self.getTypedRuleContext(MyLangParser.ObjectContext,0)


        def binaryOp(self):
            return self.getTypedRuleContext(MyLangParser.BinaryOpContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 155
                self.literal()
                pass

            elif la_ == 2:
                self.state = 156
                self.match(MyLangParser.IDENTIFIER)
                self.state = 157
                self.match(MyLangParser.T__2)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 138538481879112) != 0):
                    self.state = 158
                    self.argumentList()


                self.state = 161
                self.match(MyLangParser.T__3)
                pass

            elif la_ == 3:
                self.state = 162
                self.match(MyLangParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.state = 163
                self.match(MyLangParser.T__2)
                self.state = 164
                self.expression(0)
                self.state = 165
                self.match(MyLangParser.T__3)
                pass

            elif la_ == 5:
                self.state = 167
                self.match(MyLangParser.T__23)
                self.state = 168
                self.expression(6)
                pass

            elif la_ == 6:
                self.state = 169
                self.array()
                pass

            elif la_ == 7:
                self.state = 170
                self.object_()
                pass

            elif la_ == 8:
                self.state = 171
                self.match(MyLangParser.IDENTIFIER)
                self.state = 172
                self.match(MyLangParser.T__15)
                pass

            elif la_ == 9:
                self.state = 173
                self.match(MyLangParser.IDENTIFIER)
                self.state = 174
                self.match(MyLangParser.T__16)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 197
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 178
                        self.binaryOp()
                        self.state = 179
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 182
                        self.match(MyLangParser.T__22)
                        self.state = 183
                        self.match(MyLangParser.IDENTIFIER)
                        self.state = 184
                        self.match(MyLangParser.T__2)
                        self.state = 186
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 138538481879112) != 0):
                            self.state = 185
                            self.argumentList()


                        self.state = 188
                        self.match(MyLangParser.T__3)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 190
                        self.match(MyLangParser.T__22)
                        self.state = 191
                        self.match(MyLangParser.IDENTIFIER)
                        pass

                    elif la_ == 4:
                        localctx = MyLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 193
                        self.match(MyLangParser.T__5)
                        self.state = 194
                        self.expression(0)
                        self.state = 195
                        self.match(MyLangParser.T__6)
                        pass

             
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)




    def binaryOp(self):

        localctx = MyLangParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17163091968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = MyLangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expression(0)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 205
                self.match(MyLangParser.T__4)
                self.state = 206
                self.expression(0)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = MyLangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MyLangParser.T__5)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 138538481879112) != 0):
                self.state = 213
                self.expression(0)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 214
                    self.match(MyLangParser.T__4)
                    self.state = 215
                    self.expression(0)
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 223
            self.match(MyLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ObjectFieldContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ObjectFieldContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)




    def object_(self):

        localctx = MyLangParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MyLangParser.T__10)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 226
                self.objectField()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 227
                    self.match(MyLangParser.T__4)
                    self.state = 228
                    self.objectField()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 236
            self.match(MyLangParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyLangParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_objectField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectField" ):
                listener.enterObjectField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectField" ):
                listener.exitObjectField(self)




    def objectField(self):

        localctx = MyLangParser.ObjectFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_objectField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MyLangParser.IDENTIFIER)
            self.state = 239
            self.match(MyLangParser.T__33)
            self.state = 240
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = MyLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(MyLangParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MyLangParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MyLangParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = MyLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129742372077568) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




