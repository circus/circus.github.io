#!/opt/local/bin/python

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
indexpara = '<p>TODO lorem ipsum</p>'
subpara = '<p>{4}</p>'
evidence = '''<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
{1}
</table>'''

c_table = '''
C1 & Structural mismatch          & 13 & 8 & ...
C2 & Interface contract mismatch  &  4 & 5 & ...
C3 & Behavioural contradiction    &  3 & 6 & ...
C4 & Requirement satisfaction gap &  7 & 1 & ...
C5 & Terminology divergence       &  3 & 3 & ...
C6 & Traceability disruption      &  7 & 6 & ...
C7 & Temporal skew                &  3 & 9 & ...
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
	if !os.path.exists(filename):
		return ''
	with open(filename, "r", encoding="utf-8") as f:
		return r.read()

old_content = safe_load('index')
new_content = c_pattern.replace('###TITLE###','').replace('###SUBTITLE###','').replace('###SUBPARA###',indexpara).replace('###EVIDENCE###', evidence)
par0 = par1 = ''
for line in c_table.split('\n'):
	columns = line.split(' & ')[:-1]
	par0 += ' & '.join(columns) + '\n'
for line in e_table.split('\n'):
	columns = line.split(' & ')[:-1]
	# TODO: hyperlinkify the case ID
	columns[1] = f'[{columns[1]}]@{columns[1].lower()}.html'
	columns[2] = f'{columns[2]}@{columns[2].lower()}.html'
	columns[3] = columns[3] if columns[3] == '—' else f'{columns[3]}@{columns[3].lower()}.html' 
	par1 += ' & '.join(columns) + '\n'
new_content = new_content.format(par0, par1)
if new_content == old_content:
	print('index.html ... preserved')
else:
	with open(filename, "w", encoding="utf-8") as f:
		f.write(new_content)
	print('index.html ... updated')

# print(c_list)
for c in c_list:
	old_content = safe_load(c.lower())
	new_content = c_pattern.replace('###TITLE###',title).replace('###SUBTITLE###',subtitle).replace('###SUBPARA###',subpara).replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = c
	for line in c_table.split('\n'):
		columns = line.split(' & ')
		if columns[0] == c:
			par3 = columns[1]
			par4 = columns[4]
		par0 += ' & '.join(columns[:-1]) + '\n'
	for line in e_table.split('\n'):
		columns = line.split(' & ')[:-1]
		# colour the rows
		if columns[2] == c:
			columns[0] = '¶ ' + columns[0]
		if columns[3] == c:
			columns[0] = '¶¶ ' + columns[0]
		# TODO: hyperlinkify the case ID
		columns[1] = f'[{columns[1]}]@{columns[1].lower()}.html'
		columns[2] = f'{columns[2]}@{columns[2].lower()}.html'
		columns[3] = columns[3] if columns[3] == '—' else f'{columns[3]}@{columns[3].lower()}.html' 
		par1 += ' & '.join(columns) + '\n'
	new_content = new_content.format(par0, par1)
	if new_content == old_content:
		print('index.html ... preserved')
	else:
		with open(filename, "w", encoding="utf-8") as f:
			f.write(new_content)
		print('index.html ... updated')
