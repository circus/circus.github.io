<html doctype>
	<head jquery title="Dr. Vadim Zaytsev — Weighted Attribute Grammars" />
	<body>
		<credit last="others" />
		<h1 logo="engage.png" alt="Engage!" hover="the “Engage!” gesture from Star Trek">
			Engage!
		</h1>
		<clear/>
		<hr/>
		<p>
			<a name="Engage"></a>
			<strong><a href="https://github.com/grammarware/engage">Engage!</a></strong>
			(2019–2021)
			is an event-based parser generator.
			As far as I know, this is the only event-based parser <em>generator</em> in existence (please <a href="mailto:vadim@grammarware.net">tell me</a> if I'm wrong, would be glad to hear of similar projects), even though event-based parsers like <a href="https://en.wikipedia.org/wiki/Simple_API_for_XML">SAX</a> or <a href="https://github.com/yongjhih/RxParse">RxParse</a> are not really rarities. It was designed and developed as an experiment and published at the <a href="https://2019.splashcon.org/home/rebls-2019">REBLS</a> workshop at SPLASH 2019. The <a href="https://grammarware.net/writes/index.html#Event-Based2019">PDF of the paper</a> is freely available, it contains a more detailed and precise description of the idea, some implementation details and empirical comparison of parsers. The code of <em>Engage!</em> got improved a bit further due to a successful research project of <a href="http://essay.utwente.nl/85677/">Frank Groeneveld</a>.
		</p>
		<h2>Example spec <ared>https://github.com/grammarware/engage/blob/master/AB/spec/appbuilder.eng</ared></h2>
		<pre>
[kw1]namespace[/] AB

[kw1]types[/]
    ABProgram;
    Decl;
    ClearStmt, ConverseStmt, HandlerStmt, IfStmt, MapStmt, OverlayStmt, PrintStmt, ReturnStmt [kw1]<:[/] Stmt;
    Integer, String, Decimal [kw1]<:[/] Type;
    Var, Lit                 [kw1]<:[/] Expr;

[kw1]tokens[/]
  [kw2]' '[/], [kw2]'\r'[/], [kw2]'\n'[/] :: [kw1]skip[/]
  [kw2]';'[/], [kw2]'('[/], [kw2]')'[/] :: [kw1]mark[/]
  [kw2]'dcl'[/], [kw2]'enddcl'[/], [kw2]'integer'[/], [kw2]'char'[/], [kw2]'dec'[/], [kw2]'clear'[/], [kw2]'converse'[/], [kw2]'handler'[/],
  [kw2]'if'[/], [kw2]'endif'[/], [kw2]'map'[/], [kw2]'to'[/], [kw2]'overlay'[/], [kw2]'print'[/], [kw2]'return'[/] :: [kw1]word[/]
  [kw1]number[/] :: Num
  [kw1]string[/] :: Id

[kw1]handlers[/]
    EOF                 -> [kw1]push[/] ABProgram(data,code)
                           [kw1]while[/] code := [kw1]pop[/] Stmt,
                                 data := [kw1]pop[/] Decl
    Num                 -> [kw1]push[/] Lit([kw1]this[/])
    Id                  -> [kw1]push[/] Var([kw1]this[/])

    [kw2]'dcl'[/]               -> [kw1]lift[/] DCL
    [kw2]'enddcl'[/]            -> [kw1]drop[/] DCL
    [kw2]';'[/] [kw1]upon[/] DCL        -> [kw1]push[/] Decl(v,t)
                           [kw1]where[/] t := [kw1]pop[/] Type,
                                 v := [kw1]pop[/] Var
    [kw2]'integer'[/] [kw1]upon[/] DCL  -> [kw1]push[/] Integer
    [kw2]'char'[/]    [kw1]upon[/] DCL  -> [kw1]push[/] String(n)
                           [kw1]where[/] x := [kw1]await[/] (Lit [kw1]upon[/] BRACKET) [kw1]with[/] CHAR,
                                 n := [kw1]tear[/] x
    [kw2]'dec'[/]     [kw1]upon[/] DCL  -> [kw1]push[/] Decimal(n)
                           [kw1]where[/] x := [kw1]await[/] (Lit [kw1]upon[/] BRACKET) [kw1]with[/] DEC,
                                 n := [kw1]tear[/] x
    [kw2]'('[/] [kw1]upon[/] CHAR       -> [kw1]lift[/] BRACKET
    [kw2]'('[/] [kw1]upon[/] DEC        -> [kw1]lift[/] BRACKET
    [kw2]'('[/] [kw1]upon[/] HANDLER    -> [kw1]lift[/] BRACKET
    [kw2]')'[/]                 -> [kw1]drop[/] BRACKET

    [kw2]'clear'[/]             -> [kw1]push[/] ClearStmt(view)
                           [kw1]where[/] view := [kw1]await[/] Var
    [kw2]'converse'[/]          -> [kw1]push[/] ConverseStmt(win)
                           [kw1]where[/] win := [kw1]await[/] Var [kw1]with[/] CONVERSE
    [kw2]'handler'[/]           -> [kw1]push[/] HandlerStmt(obj,proc)
                           [kw1]where[/] obj  := [kw1]await[/] Var,
                                 proc := [kw1]await[/] (Var [kw1]upon[/] BRACKET) [kw1]with[/] HANDLER
    [kw2]'if'[/]                -> [kw1]push[/] IfStmt(cond,branch)
                           [kw1]where[/] cond   := [kw1]await[/] Expr [kw1]with[/] IF,
                                 branch := [kw1]await*[/] Stmt
    [kw2]'endif'[/]             -> [kw1]trim[/] Stmt*
    [kw2]'map'[/]               -> [kw1]push[/] MapStmt(source,target)
                           [kw1]where[/] source := [kw1]await[/] Expr [kw1]with[/] MAP,
                                 target := [kw1]await[/] Var [kw1]with[/] MAP
    [kw2]'overlay'[/]           -> [kw1]push[/] OverlayStmt(source,target)
                           [kw1]where[/] source := [kw1]await[/] Expr [kw1]with[/] OVERLAY,
                                 target := [kw1]await[/] Var [kw1]with[/] OVERLAY
    [kw2]'print'[/]             -> [kw1]push[/] PrintStmt(message)
                           [kw1]where[/] message := [kw1]await[/] Expr
    [kw2]'return'[/]            -> [kw1]push[/] ReturnStmt
		</pre>
		<clear/>
		<footer/>
	</body>
</html>
