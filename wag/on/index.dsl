<path css="../.."/>
<html doctype>
	<head title="WAGon (Rafael Dulfer, Vadim Zaytsev)" />
	<body>
		<credit first="Rafael Dulfer@dulfer.be">
		<h1>
			<a href="..">Weighted Attribute Grammars</a> Oriented Notation (WAGon)
		</h1>
		<hr/>
		<p>
			WAGon is a Library/Ecosystem/Proof-of-Concept for working with <a href="..">Weighted Attribute Grammars</a>.
		</p>
		<p>
			WAGon is designed for researchers and language designers experimenting with WAGs such that they do not have to waste time creating a DSL and parser and can start immediately experimenting with the format itself.
		</p>
		<p>
			You can read the <a href="http://purl.utwente.nl/essays/99790">master thesis</a> which explains more in detail what WAGon is, what WAGon's WAGs are, and why you should care.
		</p>
		<p>
			WAGon consists out of the following crates:
		</p>
		<ul>
			<li>
				<a href="parser.html"><code>wagon-parser</code></a>
				<ul><li>This crate is the main entrypoint for any language designer who wants to use WAGs.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-codegen"><code>wagon-codegen</code></a>
				<ul><li>Various methods that are generally useful for performing code generation when working with WAGon.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-lexer"><code>wagon-lexer</code></a>
				<ul><li>Lexer for the WAGon DSL.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-value"><code>wagon-value</code></a>
				<ul><li>Pseudo-dynamically typed values as defined by the WAGon DSL.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-utils"><code>wagon-utils</code></a>
				<ul><li>Utility methods used in the WAGon ecosystem.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-macros"><code>wagon-macros</code></a>
				<ul><li>Various build-time macros used in the WAGon ecosystem.</li></ul>
			</li>
			<li>
				<a href="https://github.com/Rafaeltheraven/wagon/tree/main/wagon-ident"><code>wagon-ident</code></a>
				<ul><li>Centralized location for attribute identifiers in WAGon.</li></ul>
			</li>
		</ul>
		<footer/>
	</body>
</html>
