#!/opt/local/bin/python

import os

c_pattern = '''
<html doctype>
	<head jquery title="Taxonomy of Inconsistency Patterns###TITLE###" />
	<body>
		<credit/>
		<h1>
			<img src="tip.200.png" alt="TIP" title="TIP logo designed by Vadim Zaytsev"/>
			<a href="index.html"><u>T</u>axonomy of <u>I</u>nconsistency <u>P</u>atterns</a>
			in Multi-View Modelling
			###SUBTITLE###
		</h1>
		###SUBPARA###
		<clear/>
		<table center clrr>
			Code & Label & As primary & As secondary
{0}
		</table>
		###EVIDENCE###
		<footer/>
	</body>
</html>
'''

title = ' - {2}: {3}'
subtitle = '<br><span class="red">Category</span> <code>{2}</code>: {3}'
indexpara = '''<p>
Multi-view modelling relies on consistency across heterogeneous views. Up until now, the literature
lacked a compact, example-backed taxonomy of the inconsistency patterns that we keep seeing across
practice and research prototypes. Existing surveys classify approaches and tools, but they do not
stabilise the recurring defect patterns themselves in a form that is directly useful for benchmarking,
evaluation, and tool-scope claims. This website presents a literature-based evidence map and a
seven-category <strong>taxonomy</strong> of inconsistency patterns in multi-view modelling.
</p><p>
We built a seed corpus of 31 papers from foundational and survey literature, then extracted and coded
46 inconsistency examples from 18 sources. After a stabilisation pass using explicit tie-break rules,
40 examples were retained as core evidence and 6 as support-only examples. The taxonomy provides a
concise vocabulary for describing consistency problems, a reusable evidence map for future research,
and a basis for more precise claims about what checking and repair approaches do and do not cover.</p>'''
subpara = '<p>{4}</p>'
evidence = '''<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
{1}
</table>'''

c_table = '''
C1 & Structural mismatch          & 13 & 8 & An expected correspondence, allocation, or refinement relation between views is missing, extra, or incompatible.
C2 & Interface contract mismatch  &  4 & 5 & Views disagree at a boundary on signatures, ports, parameter sets, types, units, directions, or equivalent exchanged values.
C3 & Behavioural contradiction    &  3 & 6 & Views admit conflicting protocols, orderings, pre/postconditions, state combinations, or jointly unsafe behaviour.
C4 & Requirement satisfaction gap &  7 & 1 & A requirement is not adequately realised, linked, tested, or accompanied by the artefacts needed to justify satisfaction.
C5 & Terminology divergence       &  3 & 3 & Corresponding concepts are named differently, or the same label is used for non-equivalent concepts across views.
C6 & Traceability disruption      &  7 & 6 & Explicit cross-artefact links are missing, stale, ambiguous, incomplete, or insufficiently maintained for navigation or impact analysis.
C7 & Temporal skew                &  3 & 9 & Views are individually plausible but inconsistent because they reflect different points in evolution, propagation, or branching history.
'''.strip()

e_table = '''
G98-2   & Grundy1998              & C1 & C7
J19-1   & Jongeling2019           & C1 & C7
J19-3   & Jongeling2019           & C1 & —
DHI-3   & Feldmann2019            & C1 & C5
J22-3   & Jongeling2022Reality    & C1 & C7
JS22-1  & Jongeling2022Structural & C1 & C6
N94-2   & Nuseibeh1994            & C1 & C5
W05-1   & Wehrheim2005            & C1 & C2
W05-2   & Wehrheim2005            & C1 & C3
W05-3   & Wehrheim2005            & C1 & C3
W05-4   & Wehrheim2005            & C1 & C3
W05-5   & Wehrheim2005            & C1 & C2
W05-6   & Wehrheim2005            & C1 & C3
G98-3   & Grundy1998              & C2 & C1
J19-2   & Jongeling2019           & C2 & C3
DHI-2   & Feldmann2019            & C2 & C1
DHI-4   & Feldmann2019            & C2 & C1
BC23-1  & Krauter2023             & C3 & C1
BC23-2  & Krauter2023             & C3 & C2
BC23-4  & Krauter2023             & C3 & C6
DHI-5   & Feldmann2019            & C4 & C2
J22-2   & Jongeling2022Reality    & C4 & C7
ST21-1  & Stunkel2021             & C4 & C6
ABB09-1 & Abbors2009              & C4 & C6
N94-1   & Nuseibeh1994            & C4 & C1
N94-3   & Nuseibeh1994            & C4 & C2
N94-4   & Nuseibeh1994            & C4 & C6
G98-1   & Grundy1998              & C5 & C7
DHI-1   & Feldmann2019            & C5 & —
JS22-3  & Jongeling2022Structural & C5 & C1
MG12-1  & Mader2012               & C6 & C7
BC23-3  & Krauter2023             & C6 & C3
OD18-1  & Javed2018               & C6 & C7
DEM16-1 & Demuth2016              & C6 & C7
BUC11-1 & Buchgeher2011           & C6 & —
GEO12-1 & George2012              & C6 & C4
MUR08-1 & Murta2008               & C6 & C7
G98-4   & Grundy1998              & C7 & C5
J22-1   & Jongeling2022Reality    & C7 & C1
JS22-2  & Jongeling2022Structural & C7 & C6
'''.strip()

c_list = [line.strip().split(' ')[0] for line in c_table.split('\n')]

def safe_load(filename):
	if not filename.endswith('.dsl'):
		filename += '.dsl'
	if not os.path.exists(filename):
		return ''
	with open(filename, "r", encoding="utf-8") as f:
		return f.read()

filename = 'index.dsl'
old_content = safe_load(filename)
new_content = c_pattern.replace('###TITLE###','').replace('###SUBTITLE###','').replace('###SUBPARA###',indexpara).replace('###EVIDENCE###', evidence)
par0 = par1 = ''
for line in c_table.split('\n'):
	columns = [word.strip() for word in line.split(' & ')][:-1]
	columns[1] = f'{columns[1]}@{columns[0].lower()}.html'
	par0 += ' & '.join(columns) + '\n'
for line in e_table.split('\n'):
	columns = [word.strip() for word in line.split(' & ')]
	# TODO: hyperlinkify the case ID
	columns[1] = f'[{columns[1]}]@{columns[1].lower()}.html'
	columns[2] = f'{columns[2]}@{columns[2].lower()}.html'
	if columns[3] != '—':
		columns[3] = f'{columns[3]}@{columns[3].lower()}.html'
	par1 += ' & '.join(columns) + '\n'
new_content = new_content.format(par0, par1)
if new_content == old_content:
	print(filename, '... preserved')
else:
	with open(filename, "w", encoding="utf-8") as f:
		f.write(new_content)
	print(filename, '... updated')

# print(c_list)
for c in c_list:
	filename = c.lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern.replace('###TITLE###',title).replace('###SUBTITLE###',subtitle).replace('###SUBPARA###',subpara).replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = c
	for line in c_table.split('\n'):
		columns = [word.strip() for word in line.split(' & ')]
		if columns[0] == c:
			par3 = columns[1]
			par4 = columns[4]
		else:
			columns[1] = f'{columns[1]}@{columns[0].lower()}.html'
		par0 += ' & '.join(columns[:-1]) + '\n'
	for line in e_table.split('\n'):
		columns = [word.strip() for word in line.split(' & ')]
		# colour the rows
		if columns[2] == c:
			columns[0] = '¶ ' + columns[0]
		if columns[3] == c:
			columns[0] = '¶¶ ' + columns[0]
		# TODO: hyperlinkify the case ID
		columns[1] = f'[{columns[1]}]@{columns[1].lower()}.html'
		columns[2] = f'{columns[2]}@{columns[2].lower()}.html'
		if columns[3] != '—':
			columns[3] = f'{columns[3]}@{columns[3].lower()}.html'
		par1 += ' & '.join(columns) + '\n'
	new_content = new_content.format(par0, par1, par2, par3, par4)
	if new_content == old_content:
		print(filename, '... preserved')
	else:
		with open(filename, "w", encoding="utf-8") as f:
			f.write(new_content)
		print(filename, '... updated')
