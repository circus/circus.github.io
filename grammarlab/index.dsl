<html doctype>
	<head title="GrammarLab (Vadim Zaytsev)" />
	<body>
		<credit first="Tijs van der Storm@https://homepages.cwi.nl/~storm/" first="Jurgen Vinju@https://homepages.cwi.nl/~jurgenv/" first="Paul Klint@https://homepages.cwi.nl/~paulk/"/>
		<h1 logo="grammarlab.200.png" alt="GrammarLab" title="GrammarLab logo designed by Vadim Zaytsev">
			GrammarLab: Foundations for a Grammar Laboratory
		</h1>
		<p style="font-weight: bold; font-size: larger;">
			• <a href="#main">Organisation</a>
			<!-- • <a href="#next">Future</a> -->
			• <a href="#events">Activities</a>
			• <a href="#tech">Technicalities</a>
			• <a href="#papers">Publications</a>
			•
		</p>
		<hr/>
		<h2><a id="main"></a>Organisation</h2>
		<ul>
			<li><a href="https://web.archive.org/web/20140904030412/http://www.cwi.nl/grammarlab-foundations-grammar-laboratory">GrammarLab</a> was an NWO-sponsored project in 2010–2013.
			Its webpage has long since perished, but according to the Way Back Machine, its description sounded like this:
<blockquote>
	<p><em>
		The shape of chemical compounds is governed by principles of molecular structure which can be understood using valence bond theory. The acquired understanding can be used to manipulate chemical compounds toobtain useful products such as plastics. Similarly, the internal shape of software is governed by the principles of source code structure which can be made insightful by the theory of grammars. This has enabled the creation of useful products such as compilers.
	</em></p>
	<p><em>
		Grammars for programming languages are complex: two grammar rules can generate an exponential number of source code structures.  Programming languages have hundreds of grammar rules. In the context of compiler construction—one language, one grammar, one compiler—this complexity is barely manageable. In the context of IDE construction,refactoring, and reverse engineering it is multiplied by the number of different languages, dialects, versions, embeddings and grammar usecases.
	</em></p>
	<p><em>
The theory of grammars does not provide insight in this complexity. It fails to provide answers to common engineering questions such as:
	</em></p>
	<ul>
		<li><em>How to efficiently construct grammars?</em></li>
		<li><em>How to assess the quality of grammars?</em></li>
		<li><em>When an erroneous structure is detected, how to relate this  effect to its grammatical cause?</em></li>
	</ul>
	<p><em>
		These common engineering questions imply that grammars are software,thus requiring well-founded engineering principles and practices. The domain and theory of grammarware engineering is underdeveloped. This research contributes to this field by developing the scientific framework and tools for understanding, creating, versioning, analyzing, testing, debugging, visualizing, and maintaining grammars.
	</em></p>
</blockquote>
		</li>
			<li>GrammarLab was designed and implemented by the <a href="http://www.cwi.nl/research-groups/Software-Analysis-and-Transformation">SWAT</a> team at <a href="http://www.cwi.nl/">CWI</a>.</li>
			<li>The lead developer of GrammarLab was <a href="http://grammarware.github.io">Vadim Zaytsev</a>.</li>
			<li>Other members of the GrammarLab project were <a href="http://homepages.cwi.nl/~paulk/">Paul Klint</a>, <a href="http://jurgen.vinju.org/">Jurgen Vinju</a> and <a href="http://homepages.cwi.nl/~storm/">Tijs van der Storm</a>.</li>
		</ul>
		<h2><a id="events"></a>Activities</h2>
		<ul>
			<li>A half-day tutorial about GrammarLab was given at <a href="http://models2013.lcc.uma.es">MoDELS 2013</a> in Miami: if you missed it, you can still have a look at <a href="http://grammarware.net/talks/index.html#Tutorial2013">the slides</a>.</li>
			<li>Each of the <a href="#papers">papers</a> published about GrammarLab, except for journal ones, had their corresponding <a href="http://grammarware.net/talks/index.html">talks with slides</a> available.</li>
			<li>A number of <a href="https://event.cwi.nl/pem/">PEM Colloquium</a> presentations concerned GrammarLab or research fragments that later became its components:
				<ul>
					<li><em><a href="http://grammarware.net/talks/index.html#PEM2010PHD">Recovery, Convergence and Documentation of Languages</a></em>, December 2010.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#SEM2011GI">Grammar Investigation</a></em>, February 2011.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#SEM2011SLE">Cheating on the Undecidability of Language Equivalence</a></em>, April 2011.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#SEM2011GR">Toward an Engineering Discipline for Grammar Recovery</a></em>, August 2011.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#SEM2012BX">Bidirectional Transformations and Grammarware</a></em>, February 2012.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#Tolerance2012">Tolerance in Grammarware</a></em>, May 2012.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#Negotiated-PEM2013">Negotiated Transformations</a></em>, January 2013.</li>
					<li><em><a href="http://grammarware.net/talks/index.html#GrammarLab2013">Modeling Software Structures with GrammarLab</a></em>, May 2013.</li>
				</ul>
			</li>
		</ul>
		<h2><a id="tech"></a>Technicalities</h2>
		<ul>
			<li>You can inspect the <a href="http://github.com/cwi-swat/grammarlab">git repo</a> of GrammarLab.</li>
			<li>Some of the experimental code that ended up deployed at GrammarLab, comes from a sibling project <a href="http://slps.github.io/">SLPS</a>.</li>
			<li>GrammarLab <code>GGrammar</code> ADT is based on <a href="http://github.com/grammarware/slps/wiki/BGF">BGF</a>, a BNF-like Grammar Format.</li>
			<li>GrammarLab grammar transformation engine is based on <a href="http://github.com/grammarware/slps/wiki/XBGF">XBGF</a>, an operator suite for transforming grammars.</li>
			<li>GrammarLab grammar mutation module SLEIR is a systematic intentional generalisation of XBGF.</li>
			<li><a href="http://slps.github.io/zoo/">Grammar Zoo</a> was being extended and maintained with the help of GrammarLab.</li>
		</ul>
		<h2><a id="papers"></a>Publications</h2>
		<ul>
			<li>Brian A. Malloy, James F. Power, <em><a href="https://onlinelibrary.wiley.com/doi/10.1002/spe.2665">Grammar engineering for multiple front-ends for Python</a></em>, SP&amp;E, 2018. <doired>10.1002/spe.2665</doired>
			<li>Brian Malloy, James Power, <em><a href="http://2016.splashcon.org/event/parsing2016-deriving-grammar-transformations-for-developing-and-maintaining-multiple-parser-versions">Deriving Grammar Transformations for Developing and Maintaining Multiple Parser Versions</a></em>, Parsing @ SLE, 2016.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#XSLT-to-Rascal2016">Evolution of Metaprograms: XSLT as a Metaprogramming Language</a></em>, META @ SPLASH, 2016.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#XSLT-to-Rascal2015">Evolution of Metaprograms, or How to Transform XSLT to Rascal</a></em>, SATToSE, 2015.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Zoo2015">Grammar Zoo: A Repository of Experimental Grammarware</a></em>, SCP EST5, 2015. <doired>10.1016/j.scico.2014.07.010</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Maturity2014">Grammar Maturity Model</a></em>, ME @ MoDELS, 2014.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Negotiated2014">Negotiated Grammar Evolution</a></em>, JOT, 2014. <doired>10.5381/jot.2014.13.3.a1</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#SLEIR2014">Software Language Engineering by Intentional Rewriting</a></em>, SQM @ CSMR-WCRE, EC-EASST, 2014. <doired>10.14279/tuj.eceasst.0.903</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Semiparsing2014">Formal Foundations for Semi-parsing</a></em>, ERA @ CSMR-WCRE, 2014. <doired>10.1109/CSMR-WCRE.2014.6747184</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Pending2013">Pending Evolution of Grammars</a></em>, XM @ MoDELS, 2013. <ceurred>1089/4.pdf</ceurred></li>
			<li>Ralf Lämmel, Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Renarration2013">Language Support for Megamodel Renarration</a></em>, XM @ MoDELS, 2013. <ceurred>1089/5.pdf</ceurred></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Micropatterns2013">Micropatterns in Grammars</a></em>, SLE, 2013. <doired>10.1007/978-3-319-02654-1_7</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Guided2013">Guided Grammar Convergence</a></em>, SLE poster paper, 2013. <doired>10.48550/arXiv.1503.08476</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Conjunctive-SATToSE2013">Modelling Robustness with Conjunctive Grammars</a></em>, SATToSE, 2013.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Grammar-Hammer2012">The Grammar Hammer of 2012</a></em>, CoRR 1212.4446, 2012. <doired>10.48550/arXiv.1212.4446</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Negotiated2012">Negotiated Grammar Transformation</a></em>, XM @ MoDELS, 2012. <doired>10.1145/2467307.2467313</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Renarration2012">Renarrating Linguistic Architecture: A Case Study</a></em>, MPM @ MoDELS, 2012. <doired>10.1145/2508443.2508454</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Guided2012">Guided Grammar Convergence. Full Case Study Report. Generated by converge::Guided</a></em>, CoRR 1207.6541, 2012. <doired>10.6084/m9.figshare.93551</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#NPGR2012">Notation-Parametric Grammar Recovery</a></em>, LDTA @ ETAPS, 2012. <doired>10.1145/2427048.2427057</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#BNF-WAS-HERE2012">BNF WAS HERE: What Have We Done About the Unnecessary Diversity of Notation for Syntactic Definitions</a></em>, PL @ SAC, 2012. <doired>10.1145/2245276.2232090</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#Metasyntactically2012">Language Evolution, Metasyntactically</a></em>, BX @ ETAPS, EC-EASST, 2012. <doired>10.14279/tuj.eceasst.49.708</doired></li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#WikiMigration2011">Wiki Migration</a></em>, Wikimania, 2011.</li>
			<li>Vadim Zaytsev, <em><a href="http://grammarware.net/writes/index.html#MediaWiki2011">MediaWiki Grammar Recovery</a></em>, CoRR 1107.4661, 2011. <doired>10.48550/arXiv.1107.4661</doired></li>
			<li>Paul Klint, Ralf Lämmel, Chris Verhoef, <em><a href="http://www.cs.vu.nl/grammarware/agenda/">Toward an Engineering Discipline for Grammarware</a></em>, ACM ToSEM, 2005.</li>
		</ul>
		<footer/>
	</body>
</html>
