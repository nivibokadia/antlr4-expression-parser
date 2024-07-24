// Generated from c:/Users/Nivi Bokadia/antlr/antlr4-expression-parser/Expression.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExpressionParser}.
 */
public interface ExpressionListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExpressionParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExpressionParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code declareStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterDeclareStmt(ExpressionParser.DeclareStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code declareStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitDeclareStmt(ExpressionParser.DeclareStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(ExpressionParser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(ExpressionParser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(ExpressionParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(ExpressionParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(ExpressionParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(ExpressionParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterForStmt(ExpressionParser.ForStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitForStmt(ExpressionParser.ForStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcDefStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterFuncDefStmt(ExpressionParser.FuncDefStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcDefStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitFuncDefStmt(ExpressionParser.FuncDefStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(ExpressionParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(ExpressionParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exprStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(ExpressionParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exprStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(ExpressionParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code incDecStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIncDecStmt(ExpressionParser.IncDecStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code incDecStmt}
	 * labeled alternative in {@link ExpressionParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIncDecStmt(ExpressionParser.IncDecStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(ExpressionParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(ExpressionParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(ExpressionParser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(ExpressionParser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ExpressionParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ExpressionParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(ExpressionParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(ExpressionParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(ExpressionParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(ExpressionParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by the {@code stringExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterStringExpr(ExpressionParser.StringExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code stringExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitStringExpr(ExpressionParser.StringExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalOrExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpr(ExpressionParser.LogicalOrExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalOrExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpr(ExpressionParser.LogicalOrExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variableExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterVariableExpr(ExpressionParser.VariableExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variableExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitVariableExpr(ExpressionParser.VariableExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addSubExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAddSubExpr(ExpressionParser.AddSubExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addSubExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAddSubExpr(ExpressionParser.AddSubExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalAndExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpr(ExpressionParser.LogicalAndExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalAndExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpr(ExpressionParser.LogicalAndExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numberExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNumberExpr(ExpressionParser.NumberExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numberExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNumberExpr(ExpressionParser.NumberExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionCallExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExpr(ExpressionParser.FunctionCallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionCallExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExpr(ExpressionParser.FunctionCallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterComparisonExpr(ExpressionParser.ComparisonExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitComparisonExpr(ExpressionParser.ComparisonExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code boolExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBoolExpr(ExpressionParser.BoolExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code boolExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBoolExpr(ExpressionParser.BoolExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mulDivExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMulDivExpr(ExpressionParser.MulDivExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mulDivExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMulDivExpr(ExpressionParser.MulDivExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(ExpressionParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link ExpressionParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(ExpressionParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExpressionParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(ExpressionParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExpressionParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(ExpressionParser.ArgumentsContext ctx);
}