# Generated from Expression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#program.
    def visitProgram(self, ctx:ExpressionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#declareStmt.
    def visitDeclareStmt(self, ctx:ExpressionParser.DeclareStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#assignStmt.
    def visitAssignStmt(self, ctx:ExpressionParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#ifStmt.
    def visitIfStmt(self, ctx:ExpressionParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#whileStmt.
    def visitWhileStmt(self, ctx:ExpressionParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#forStmt.
    def visitForStmt(self, ctx:ExpressionParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#funcDefStmt.
    def visitFuncDefStmt(self, ctx:ExpressionParser.FuncDefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#printStmt.
    def visitPrintStmt(self, ctx:ExpressionParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#exprStmt.
    def visitExprStmt(self, ctx:ExpressionParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#incDecStmt.
    def visitIncDecStmt(self, ctx:ExpressionParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#gotoStmt.
    def visitGotoStmt(self, ctx:ExpressionParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#labeledStmt.
    def visitLabeledStmt(self, ctx:ExpressionParser.LabeledStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arrayPushStmt.
    def visitArrayPushStmt(self, ctx:ExpressionParser.ArrayPushStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arrayPopStmt.
    def visitArrayPopStmt(self, ctx:ExpressionParser.ArrayPopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:ExpressionParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#forInit.
    def visitForInit(self, ctx:ExpressionParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#forUpdate.
    def visitForUpdate(self, ctx:ExpressionParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#block.
    def visitBlock(self, ctx:ExpressionParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#parameters.
    def visitParameters(self, ctx:ExpressionParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#param.
    def visitParam(self, ctx:ExpressionParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ExpressionParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:ExpressionParser.LogicalAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#numberExpr.
    def visitNumberExpr(self, ctx:ExpressionParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:ExpressionParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#parenExpr.
    def visitParenExpr(self, ctx:ExpressionParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#stringExpr.
    def visitStringExpr(self, ctx:ExpressionParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:ExpressionParser.LogicalOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#variableExpr.
    def visitVariableExpr(self, ctx:ExpressionParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arrayLengthExpr.
    def visitArrayLengthExpr(self, ctx:ExpressionParser.ArrayLengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:ExpressionParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:ExpressionParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#boolExpr.
    def visitBoolExpr(self, ctx:ExpressionParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ExpressionParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#arguments.
    def visitArguments(self, ctx:ExpressionParser.ArgumentsContext):
        return self.visitChildren(ctx)



del ExpressionParser