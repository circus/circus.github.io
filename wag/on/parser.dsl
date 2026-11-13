<path css="../.."/>
<html doctype>
	<head title="WAGon (Rafael Dulfer, Vadim Zaytsev)" />
	<body>
		<credit first="Rafael Dulfer@dulfer.be">
		<h1>
			<a href="..">Weighted Attribute Grammars</a> Oriented Notation
			(<a href="index.html">WAGon</a>)
		</h1>
		<hr/>
		<h2>
			<a href="index.html">WAGon</a> <a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-parser">Parser</a>
		</h2>
		<p>
			A library for parsing the WAGon DSL. This crate provides a struct that, given a String with the DSL as input, either returns a full AST representing the input file, or a proper error. The error can be handled as needed, the AST can function as the basis for any code generation or analysis that one wants to do.
		</p>
		<p>
			Additionally, this crate includes a very simple checker which does the following things:
		</p>
		<ul>
			<li>Check whether any rule has duplicate attributes in their declaration (i.e. <code>S&lt;*a, *a> -&rt; ...;</code>).</li>
			<li>Check whether alternate definitions of the same nonterminal have different attributes in their declarations (i.e. <code>S&lt;*a&rt; -&rt; ...; S&lt;*b, *c&rt; -&rt; ...;</code>).</li>
			<li>Merge multiple rules for the same nonterminal into a single rule with alternatives.</li>
			<li>Factor our EBNF operators.</li>
		</ul>
		<h3>Example</h3>
		<pre>
use wagon_parser::parse_and_check;
&nbsp;
let input_grammar = ...;
let wag = parse_and_check(input_grammar);
assert!(wag.is_ok());</pre>
		<p>
			This crate also defines the AST for a fully parsed WAGon WAG. It's structure mirrors that of the formal DSL.
		</p>
		<footer/>
	</body>
</html>
