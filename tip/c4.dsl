<html doctype>
	<head jquery title="Taxonomy of Inconsistency Patterns - C4: Requirement satisfaction gap" />
	<body>
		<credit/>
		<h1>
			<img src="tip.200.png" alt="TIP" title="TIP logo designed by Vadim Zaytsev"/>
			<a href="index.html"><u>T</u>axonomy of <u>I</u>nconsistency <u>P</u>atterns</a>
			in Multi-View Modelling
			<br><span class="red">Category</span> <code>C4</code>: Requirement satisfaction gap
		</h1>
		<p>A requirement is not adequately realised, linked, tested, or accompanied by the artefacts needed to justify satisfaction.</p><p>C4 covers failures to justify that <em>requirements are satisfied or covered</em>. Some examples are classical viewpoint gaps, such as a required dependent view not being created, or a formal schema lacking its required associated description. Others arise later in the lifecycle, for instance when critical requirements are not traced through to tests, or when tests continue to execute but no longer cover the intended behaviour after model evolution.</p>
		<clear/>
		<table center clrr>
			Code & Label & As primary & As secondary
C1 & Structural mismatch@c1.html & 13 & 8
C2 & Interface contract mismatch@c2.html & 4 & 5
C3 & Behavioural contradiction@c3.html & 3 & 6
C4 & Requirement satisfaction gap & 7 & 1
C5 & Terminology divergence@c5.html & 3 & 3
C6 & Traceability disruption@c6.html & 7 & 6
C7 & Temporal skew@c7.html & 3 & 9

		</table>
		<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
J19-3@j19-3.html & [Jongeling2019]@jongeling2019.html & C1@c1.html & —
W05-1@w05-1.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C2@c2.html
W05-5@w05-5.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C2@c2.html
W05-2@w05-2.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
W05-3@w05-3.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
W05-4@w05-4.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
W05-6@w05-6.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
DHI-3@dhi-3.html & [Feldmann2019]@feldmann2019.html & C1@c1.html & C5@c5.html
N94-2@n94-2.html & [NuseibehKF1994]@nuseibehkf1994.html & C1@c1.html & C5@c5.html
JS22-1@js22-1.html & [JongelingFCCC2022]@jongelingfccc2022.html & C1@c1.html & C6@c6.html
G98-2@g98-2.html & [GrundyHM1998]@grundyhm1998.html & C1@c1.html & C7@c7.html
J19-1@j19-1.html & [Jongeling2019]@jongeling2019.html & C1@c1.html & C7@c7.html
J22-3@j22-3.html & [JongelingCCC2022]@jongelingccc2022.html & C1@c1.html & C7@c7.html
DHI-2@dhi-2.html & [Feldmann2019]@feldmann2019.html & C2@c2.html & C1@c1.html
DHI-4@dhi-4.html & [Feldmann2019]@feldmann2019.html & C2@c2.html & C1@c1.html
G98-3@g98-3.html & [GrundyHM1998]@grundyhm1998.html & C2@c2.html & C1@c1.html
J19-2@j19-2.html & [Jongeling2019]@jongeling2019.html & C2@c2.html & C3@c3.html
BC23-1@bc23-1.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C1@c1.html
BC23-2@bc23-2.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C2@c2.html
BC23-4@bc23-4.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C6@c6.html
¶ N94-1@n94-1.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C1@c1.html
¶ DHI-5@dhi-5.html & [Feldmann2019]@feldmann2019.html & C4@c4.html & C2@c2.html
¶ N94-3@n94-3.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C2@c2.html
¶ ABB09-1@abb09-1.html & [AbborsTL2009]@abborstl2009.html & C4@c4.html & C6@c6.html
¶ N94-4@n94-4.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C6@c6.html
¶ ST21-1@st21-1.html & [StunkelKRL2021]@stunkelkrl2021.html & C4@c4.html & C6@c6.html
¶ J22-2@j22-2.html & [JongelingCCC2022]@jongelingccc2022.html & C4@c4.html & C7@c7.html
DHI-1@dhi-1.html & [Feldmann2019]@feldmann2019.html & C5@c5.html & —
JS22-3@js22-3.html & [JongelingFCCC2022]@jongelingfccc2022.html & C5@c5.html & C1@c1.html
G98-1@g98-1.html & [GrundyHM1998]@grundyhm1998.html & C5@c5.html & C7@c7.html
BUC11-1@buc11-1.html & [BuchgeherWeinreich2011]@buchgeherweinreich2011.html & C6@c6.html & —
BC23-3@bc23-3.html & [KrauterKRLS2023]@krauterkrls2023.html & C6@c6.html & C3@c3.html
¶¶ GEO12-1@geo12-1.html & [GeorgeFHKBA2012]@georgefhkba2012.html & C6@c6.html & C4@c4.html
DEM16-1@dem16-1.html & [DemuthKEM2016]@demuthkem2016.html & C6@c6.html & C7@c7.html
OD18-1@od18-1.html & [JavedMZ2018]@javedmz2018.html & C6@c6.html & C7@c7.html
MG12-1@mg12-1.html & [MaderG2012]@maderg2012.html & C6@c6.html & C7@c7.html
MUR08-1@mur08-1.html & [MurtaHW2008]@murtahw2008.html & C6@c6.html & C7@c7.html
J22-1@j22-1.html & [JongelingCCC2022]@jongelingccc2022.html & C7@c7.html & C1@c1.html
G98-4@g98-4.html & [GrundyHM1998]@grundyhm1998.html & C7@c7.html & C5@c5.html
JS22-2@js22-2.html & [JongelingFCCC2022]@jongelingfccc2022.html & C7@c7.html & C6@c6.html

</table>
		<footer/>
	</body>
</html>
