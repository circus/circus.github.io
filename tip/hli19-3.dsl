<html doctype>
	<head jquery title="Taxonomy of Inconsistency Patterns — HLI19-3" />
	<body>
		<credit/>
		<h1>
			<img src="tip.200.png" alt="TIP" title="TIP logo designed by Vadim Zaytsev"/>
			<a href="index.html"><u>T</u>axonomy of <u>I</u>nconsistency <u>P</u>atterns</a>
			in Multi-View Modelling
			<br><span class="red">Case</span> <code>HLI19-3</code>
		</h1>
		<dl><dt>Source</dt>
	<dd><a href="jongeling2019.html">Jongeling2019</a></dd>
<dt>Categories</dt>
	<dd><a href="c1.html">C1</a></dd>
<dt>Domain</dt>
	<dd>industrial MBSE (SysML/Simulink)</dd>
<dt>Views</dt>
	<dd>SysML block diagram</dd>
	<dd>Simulink model</dd>
<dt>Artefacts</dt>
	<dd>expected subsystem/block correspondence</dd>
<dt>Quotes</dt>
	<dd>"we could for example detect if the Simulink model is missing a subsystem that was expected in the SysML block diagram"</dd>
<dt>Summary</dt>
	<dd>A lower-level model omits a subsystem required by the higher-level architectural view.</dd>
	<dd>Cause: missing correspondence under a refinement relation.</dd>
	<dd>As a result, likely incompleteness or incorrect realisation of the higher-level design.</dd>
</dl>
<h2>Taxonomy Categories</h2>
		<clear/>
		<table center clrr>
			Code & Label & As primary & As secondary
¶ C1 & Structural mismatch@c1.html & 13 & 7
C2 & Interface contract mismatch@c2.html & 4 & 5
C3 & Behavioural contradiction@c3.html & 3 & 6
C4 & Requirement satisfaction gap@c4.html & 7 & 1
C5 & Terminology divergence@c5.html & 3 & 3
C6 & Traceability disruption@c6.html & 7 & 6
C7 & Temporal skew@c7.html & 3 & 9

		</table>
		<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
¶ HLI19-3@hli19-3.html & [Jongeling2019]@jongeling2019.html & C1@c1.html & —
RCM05-1@rcm05-1.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C2@c2.html
RCM05-5@rcm05-5.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C2@c2.html
RCM05-2@rcm05-2.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
RCM05-3@rcm05-3.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
RCM05-4@rcm05-4.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
RCM05-6@rcm05-6.html & [Wehrheim2005]@wehrheim2005.html & C1@c1.html & C3@c3.html
DHI19-3@dhi19-3.html & [Feldmann2019]@feldmann2019.html & C1@c1.html & C5@c5.html
FER94-2@fer94-2.html & [NuseibehKF1994]@nuseibehkf1994.html & C1@c1.html & C5@c5.html
DSS22-1@dss22-1.html & [JongelingFCCC2022]@jongelingfccc2022.html & C1@c1.html & C6@c6.html
IMM98-2@imm98-2.html & [GrundyHM1998]@grundyhm1998.html & C1@c1.html & C7@c7.html
HLI19-1@hli19-1.html & [Jongeling2019]@jongeling2019.html & C1@c1.html & C7@c7.html
ARC22-3@arc22-3.html & [JongelingCCC2022]@jongelingccc2022.html & C1@c1.html & C7@c7.html
DHI19-2@dhi19-2.html & [Feldmann2019]@feldmann2019.html & C2@c2.html & C1@c1.html
DHI19-4@dhi19-4.html & [Feldmann2019]@feldmann2019.html & C2@c2.html & C1@c1.html
IMM98-3@imm98-3.html & [GrundyHM1998]@grundyhm1998.html & C2@c2.html & C1@c1.html
HLI19-2@hli19-2.html & [Jongeling2019]@jongeling2019.html & C2@c2.html & C3@c3.html
BCM23-1@bcm23-1.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C1@c1.html
BCM23-2@bcm23-2.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C2@c2.html
BCM23-4@bcm23-4.html & [KrauterKRLS2023]@krauterkrls2023.html & C3@c3.html & C6@c6.html
FER94-1@fer94-1.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C1@c1.html
DHI19-5@dhi19-5.html & [Feldmann2019]@feldmann2019.html & C4@c4.html & C2@c2.html
FER94-3@fer94-3.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C2@c2.html
ABB09-1@abb09-1.html & [AbborsTL2009]@abborstl2009.html & C4@c4.html & C6@c6.html
FER94-4@fer94-4.html & [NuseibehKF1994]@nuseibehkf1994.html & C4@c4.html & C6@c6.html
MME21-1@mme21-1.html & [StunkelKRL2021]@stunkelkrl2021.html & C4@c4.html & C6@c6.html
ARC22-2@arc22-2.html & [JongelingCCC2022]@jongelingccc2022.html & C4@c4.html & C7@c7.html
DHI19-1@dhi19-1.html & [Feldmann2019]@feldmann2019.html & C5@c5.html & —
DSS22-3@dss22-3.html & [JongelingFCCC2022]@jongelingfccc2022.html & C5@c5.html & C1@c1.html
IMM98-1@imm98-1.html & [GrundyHM1998]@grundyhm1998.html & C5@c5.html & C7@c7.html
ATD11-1@atd11-1.html & [BuchgeherWeinreich2011]@buchgeherweinreich2011.html & C6@c6.html & —
BCM23-3@bcm23-3.html & [KrauterKRLS2023]@krauterkrls2023.html & C6@c6.html & C3@c3.html
MBT12-1@mbt12-1.html & [GeorgeFHKBA2012]@georgefhkba2012.html & C6@c6.html & C4@c4.html
ITC16-1@itc16-1.html & [DemuthKEM2016]@demuthkem2016.html & C6@c6.html & C7@c7.html
OAT18-1@oat18-1.html & [JavedMZ2018]@javedmz2018.html & C6@c6.html & C7@c7.html
ATM12-1@atm12-1.html & [MaderG2012]@maderg2012.html & C6@c6.html & C7@c7.html
CAE08-1@cae08-1.html & [MurtaHW2008]@murtahw2008.html & C6@c6.html & C7@c7.html
ARC22-1@arc22-1.html & [JongelingCCC2022]@jongelingccc2022.html & C7@c7.html & C1@c1.html
IMM98-4@imm98-4.html & [GrundyHM1998]@grundyhm1998.html & C7@c7.html & C5@c5.html
DSS22-2@dss22-2.html & [JongelingFCCC2022]@jongelingfccc2022.html & C7@c7.html & C6@c6.html

</table>
		<footer/>
	</body>
</html>
