<html doctype>
	<head jquery title="Taxonomy of Inconsistency Patterns — table1" />
	<body>
		<credit/>
		<h1>
			<img src="tip.200.png" alt="TIP" title="TIP logo designed by Vadim Zaytsev"/>
			<a href="index.html"><u>T</u>axonomy of <u>I</u>nconsistency <u>P</u>atterns</a>
			in Multi-View Modelling
			<br><span class="red">Artefact</span> <code>table1</code>
		</h1>
		<p>Download raw LaTeX: <a href="table1.tex">table1.tex</a></p>
<pre>\[kw1]begin[/]{[kw2]table[/]}[t]
\[kw1]caption[/]{Stabilised taxonomy of inconsistency patterns. Counts are based on the 40 core examples.}
\[kw1]label[/]{tab:taxonomy}
\[kw1]small[/]
\[kw1]begin[/]{[kw2]tabularx[/]}{\[kw1]linewidth[/]}{@{}l l c Y@{}}
\[kw1]toprule[/]
Code [kw2]&amp;[/] Label [kw2]&amp;[/] Count [kw2]&amp;[/] Definition [kw2]\\[/]
\[kw1]midrule[/]
\<a href="c1.html">CA</a> [kw2]&amp;[/] \CAtext [kw2]&amp;[/] 13 [kw2]&amp;[/] An expected correspondence, allocation, or refinement relation between views is missing, extra, or incompatible. [kw2]\\[/]
\<a href="c2.html">CB</a> [kw2]&amp;[/] \CBtext [kw2]&amp;[/] 4 [kw2]&amp;[/] Views disagree at a boundary on signatures, ports, parameter sets, types, units, directions, or equivalent exchanged values. [kw2]\\[/]
\<a href="c3.html">CC</a> [kw2]&amp;[/] \CCtext [kw2]&amp;[/] 3 [kw2]&amp;[/] Views admit conflicting protocols, orderings, pre/postconditions, state combinations, or jointly unsafe behaviour. [kw2]\\[/]
\<a href="c4.html">CD</a> [kw2]&amp;[/] \CDtext [kw2]&amp;[/] 7 [kw2]&amp;[/] A requirement is not adequately realised, linked, tested, or accompanied by the artefacts needed to justify satisfaction. [kw2]\\[/]
\<a href="c5.html">CE</a> [kw2]&amp;[/] \CEtext [kw2]&amp;[/] 3 [kw2]&amp;[/] Corresponding concepts are named differently, or the same label is used for non-equivalent concepts across views. [kw2]\\[/]
\<a href="c6.html">CF</a> [kw2]&amp;[/] \CFtext [kw2]&amp;[/] 7 [kw2]&amp;[/] Explicit cross-artefact links are missing, stale, ambiguous, incomplete, or insufficiently maintained for navigation or impact analysis. [kw2]\\[/]
\<a href="c7.html">CG</a> [kw2]&amp;[/] \CGtext [kw2]&amp;[/] 3 [kw2]&amp;[/] Views are individually plausible but inconsistent because they reflect different points in evolution, propagation, or branching history. [kw2]\\[/]
\[kw1]bottomrule[/]
\[kw1]end[/]{[kw2]tabularx[/]}
\[kw1]end[/]{[kw2]table[/]}</pre>
<clear/>
<h2>Taxonomy Categories</h2>
		<table center clrr>
			Code & Label & As primary & As secondary
C1 & Structural mismatch@c1.html & 13 & 7
C2 & Interface contract mismatch@c2.html & 4 & 5
C3 & Behavioural contradiction@c3.html & 3 & 6
C4 & Requirement satisfaction gap@c4.html & 7 & 1
C5 & Terminology divergence@c5.html & 3 & 3
C6 & Traceability disruption@c6.html & 7 & 6
C7 & Temporal skew@c7.html & 3 & 9

		</table>
		
		<footer/>
	</body>
</html>
