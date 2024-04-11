# Generated from MyLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:MyLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MyLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:MyLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MyLangParser#paramList.
    def enterParamList(self, ctx:MyLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by MyLangParser#paramList.
    def exitParamList(self, ctx:MyLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by MyLangParser#param.
    def enterParam(self, ctx:MyLangParser.ParamContext):
        pass

    # Exit a parse tree produced by MyLangParser#param.
    def exitParam(self, ctx:MyLangParser.ParamContext):
        pass


    # Enter a parse tree produced by MyLangParser#varDecl.
    def enterVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MyLangParser#varDecl.
    def exitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#assignment.
    def enterAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLangParser#assignment.
    def exitAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifStatement.
    def enterIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifStatement.
    def exitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#loop.
    def enterLoop(self, ctx:MyLangParser.LoopContext):
        pass

    # Exit a parse tree produced by MyLangParser#loop.
    def exitLoop(self, ctx:MyLangParser.LoopContext):
        pass


    # Enter a parse tree produced by MyLangParser#expression.
    def enterExpression(self, ctx:MyLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLangParser#expression.
    def exitExpression(self, ctx:MyLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyLangParser#binaryOp.
    def enterBinaryOp(self, ctx:MyLangParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by MyLangParser#binaryOp.
    def exitBinaryOp(self, ctx:MyLangParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by MyLangParser#argumentList.
    def enterArgumentList(self, ctx:MyLangParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MyLangParser#argumentList.
    def exitArgumentList(self, ctx:MyLangParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MyLangParser#array.
    def enterArray(self, ctx:MyLangParser.ArrayContext):
        pass

    # Exit a parse tree produced by MyLangParser#array.
    def exitArray(self, ctx:MyLangParser.ArrayContext):
        pass


    # Enter a parse tree produced by MyLangParser#object.
    def enterObject(self, ctx:MyLangParser.ObjectContext):
        pass

    # Exit a parse tree produced by MyLangParser#object.
    def exitObject(self, ctx:MyLangParser.ObjectContext):
        pass


    # Enter a parse tree produced by MyLangParser#objectField.
    def enterObjectField(self, ctx:MyLangParser.ObjectFieldContext):
        pass

    # Exit a parse tree produced by MyLangParser#objectField.
    def exitObjectField(self, ctx:MyLangParser.ObjectFieldContext):
        pass


    # Enter a parse tree produced by MyLangParser#type.
    def enterType(self, ctx:MyLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLangParser#type.
    def exitType(self, ctx:MyLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLangParser#literal.
    def enterLiteral(self, ctx:MyLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by MyLangParser#literal.
    def exitLiteral(self, ctx:MyLangParser.LiteralContext):
        pass



del MyLangParser