# Generated from Expression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#program.
    def enterProgram(self, ctx:ExpressionParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExpressionParser#program.
    def exitProgram(self, ctx:ExpressionParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExpressionParser#declareStmt.
    def enterDeclareStmt(self, ctx:ExpressionParser.DeclareStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#declareStmt.
    def exitDeclareStmt(self, ctx:ExpressionParser.DeclareStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#assignStmt.
    def enterAssignStmt(self, ctx:ExpressionParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#assignStmt.
    def exitAssignStmt(self, ctx:ExpressionParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#ifStmt.
    def enterIfStmt(self, ctx:ExpressionParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#ifStmt.
    def exitIfStmt(self, ctx:ExpressionParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#whileStmt.
    def enterWhileStmt(self, ctx:ExpressionParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#whileStmt.
    def exitWhileStmt(self, ctx:ExpressionParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#forStmt.
    def enterForStmt(self, ctx:ExpressionParser.ForStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#forStmt.
    def exitForStmt(self, ctx:ExpressionParser.ForStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#funcDefStmt.
    def enterFuncDefStmt(self, ctx:ExpressionParser.FuncDefStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#funcDefStmt.
    def exitFuncDefStmt(self, ctx:ExpressionParser.FuncDefStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#printStmt.
    def enterPrintStmt(self, ctx:ExpressionParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#printStmt.
    def exitPrintStmt(self, ctx:ExpressionParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#exprStmt.
    def enterExprStmt(self, ctx:ExpressionParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#exprStmt.
    def exitExprStmt(self, ctx:ExpressionParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#incDecStmt.
    def enterIncDecStmt(self, ctx:ExpressionParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#incDecStmt.
    def exitIncDecStmt(self, ctx:ExpressionParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#gotoStmt.
    def enterGotoStmt(self, ctx:ExpressionParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#gotoStmt.
    def exitGotoStmt(self, ctx:ExpressionParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#labeledStmt.
    def enterLabeledStmt(self, ctx:ExpressionParser.LabeledStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#labeledStmt.
    def exitLabeledStmt(self, ctx:ExpressionParser.LabeledStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arrayPushStmt.
    def enterArrayPushStmt(self, ctx:ExpressionParser.ArrayPushStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arrayPushStmt.
    def exitArrayPushStmt(self, ctx:ExpressionParser.ArrayPushStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arrayPopStmt.
    def enterArrayPopStmt(self, ctx:ExpressionParser.ArrayPopStmtContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arrayPopStmt.
    def exitArrayPopStmt(self, ctx:ExpressionParser.ArrayPopStmtContext):
        pass


    # Enter a parse tree produced by ExpressionParser#printArguments.
    def enterPrintArguments(self, ctx:ExpressionParser.PrintArgumentsContext):
        pass

    # Exit a parse tree produced by ExpressionParser#printArguments.
    def exitPrintArguments(self, ctx:ExpressionParser.PrintArgumentsContext):
        pass


    # Enter a parse tree produced by ExpressionParser#printArg.
    def enterPrintArg(self, ctx:ExpressionParser.PrintArgContext):
        pass

    # Exit a parse tree produced by ExpressionParser#printArg.
    def exitPrintArg(self, ctx:ExpressionParser.PrintArgContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:ExpressionParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:ExpressionParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by ExpressionParser#forInit.
    def enterForInit(self, ctx:ExpressionParser.ForInitContext):
        pass

    # Exit a parse tree produced by ExpressionParser#forInit.
    def exitForInit(self, ctx:ExpressionParser.ForInitContext):
        pass


    # Enter a parse tree produced by ExpressionParser#forUpdate.
    def enterForUpdate(self, ctx:ExpressionParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by ExpressionParser#forUpdate.
    def exitForUpdate(self, ctx:ExpressionParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by ExpressionParser#block.
    def enterBlock(self, ctx:ExpressionParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpressionParser#block.
    def exitBlock(self, ctx:ExpressionParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpressionParser#parameters.
    def enterParameters(self, ctx:ExpressionParser.ParametersContext):
        pass

    # Exit a parse tree produced by ExpressionParser#parameters.
    def exitParameters(self, ctx:ExpressionParser.ParametersContext):
        pass


    # Enter a parse tree produced by ExpressionParser#param.
    def enterParam(self, ctx:ExpressionParser.ParamContext):
        pass

    # Exit a parse tree produced by ExpressionParser#param.
    def exitParam(self, ctx:ExpressionParser.ParamContext):
        pass


    # Enter a parse tree produced by ExpressionParser#addSubExpr.
    def enterAddSubExpr(self, ctx:ExpressionParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#addSubExpr.
    def exitAddSubExpr(self, ctx:ExpressionParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:ExpressionParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:ExpressionParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#numberExpr.
    def enterNumberExpr(self, ctx:ExpressionParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#numberExpr.
    def exitNumberExpr(self, ctx:ExpressionParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:ExpressionParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:ExpressionParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#parenExpr.
    def enterParenExpr(self, ctx:ExpressionParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#parenExpr.
    def exitParenExpr(self, ctx:ExpressionParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#stringExpr.
    def enterStringExpr(self, ctx:ExpressionParser.StringExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#stringExpr.
    def exitStringExpr(self, ctx:ExpressionParser.StringExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:ExpressionParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:ExpressionParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#variableExpr.
    def enterVariableExpr(self, ctx:ExpressionParser.VariableExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#variableExpr.
    def exitVariableExpr(self, ctx:ExpressionParser.VariableExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arrayLengthExpr.
    def enterArrayLengthExpr(self, ctx:ExpressionParser.ArrayLengthExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arrayLengthExpr.
    def exitArrayLengthExpr(self, ctx:ExpressionParser.ArrayLengthExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:ExpressionParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:ExpressionParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:ExpressionParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:ExpressionParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#boolExpr.
    def enterBoolExpr(self, ctx:ExpressionParser.BoolExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#boolExpr.
    def exitBoolExpr(self, ctx:ExpressionParser.BoolExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:ExpressionParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ExpressionParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:ExpressionParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ExpressionParser#arguments.
    def enterArguments(self, ctx:ExpressionParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ExpressionParser#arguments.
    def exitArguments(self, ctx:ExpressionParser.ArgumentsContext):
        pass



del ExpressionParser