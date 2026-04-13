<html doctype>
	<head title="BibSLEIGH (Vadim Zaytsev)" />
	<body>
		<credit/>
		<h1 logo="bibsleigh.png" alt="BibSLEIGH" title="BibSLEIGH logo designed by Vadim Zaytsev">
			BibSLEIGH: Bibliography of Software Language Engineering in Generated Hypertext
		</h1>
		<p>
			This project started as a beautification frontend for <a href="https://dblp.org/">DBLP</a>, because DBLP-supplied BibTeX was/is suffering from a number of problems (to name a few: abbreviation of journal names, unnecessary timestamp, biburl, and bibsource tags, convoluted booktitles with long locations that contribute nothing, and eventually dysfunctional DOIs or URLs). It quickly became obvious that some of the problems are inherent to the BibTeX format itself, some are peculiar for DBLP (and thus prone to the changes in their internal policies), and some simply stem from my personal interest in some conferences and the lack thereof in others.
		</p>
		<p>
			BibSLEIGH has accumulated 150+k papers, all possibly related to some topic that can potentially be considered a part of software language engineering, but often only marginally so (the actual “body of knowledge” of SLE is much smaller), but has <span class="hl">not been properly updated</span> in the past couple of years (since about 2020) due to the lack of time to be dedicated to this. It is still a great tool to find related work, though. BibSLEIGH sits firmly between websites like DBLP, <a href="https://scholar.google.com/">GScholar</a>, <a href="https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/">WoS</a>, <a href="https://www.scopus.com/sources">Scopus</a> or by now defunct <a href="https://www.microsoft.com/en-us/research/project/academic/">Microsoft Academic</a> that simply dump millions of papers on you (and do it in a dynamic way, meaning eventual downtime and horrible performance on good days), and AI hallucinators like <a href="https://scite.ai/">Scite_</a>, <a href="https://www.sourcely.net/">Sourcely</a>, <a href="https://consensus.app/">Consensus</a> or <a href="https://www.connectedpapers.com/">ConnectedPapers</a>, which make a soulless effort in stitching things together but ultimately also don’t care.
		</p>
		<p>
			I believe there is a lot of value in recovering and preserving bibliographical data from old and obscure venues, and there’s a lot of research possible on research communities and publications, and I hope to return to it at some point in the future.
		</p>
		<h2>Resources</h2>
		<ul>
			<li>Vadim Zaytsev, <em><a href="https://grammarware.net/writes/#BibSATToSE2017">BibSLEIGH: Bibliography of Software (Language) Engineering in Generated Hypertext</a></em>, SATToSE 2015, CEUR 1820:54–64.</li>
			<li><a class="red" href="https://github.com/slebok/bibsleigh"><code>https://github.com/slebok/bibsleigh</code></a> — dataset/corpus</li>
			<li><a class="red" href="https://github.com/bibtex/bibsleigh"><code>https://github.com/bibtex/bibsleigh</code></a> — toolkit(s) that turn the dataset into the website</li>
			<li><a class="red" href="https://bibtex.github.io"><code>https://bibtex.github.io</code></a> — functioning frontend</li>
		</ul>
		<footer/>
	</body>
</html>
