#!/opt/local/bin/python

import os

def safe_load(filename):
	if not filename.endswith('.dsl'):
		filename += '.dsl'
	if not os.path.exists(filename):
		return ''
	with open(filename, "r", encoding="utf-8") as f:
		return f.read()

def load_data(filename):
	result = []
	record = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.strip()
			if not line:
				if record:
					result.append(record)
					record = []
			else:
				record.append(line)
	if record:
		result.append(record)
	return result

def maybe_update(new_content, old_content, filename):
	if new_content == old_content:
		# print(filename, '... preserved')
		pass
	else:
		with open(filename, "w", encoding="utf-8") as f:
			f.write(new_content)
		print(filename, '... updated')

def hyper_value(value):
	if value.startswith('¶ '):
		value = value.split('¶ ')[-1]
		return f'¶ {value}@{value.lower()}.html'
	else:
		return f'{value}@{value.lower()}.html'
def hyper_bracketed_value(value):
	return f'[{value}]@{value.lower()}.html'
def hyper_other_value(value1, value2):
	if value2.startswith('¶'):
		value2 = value2.replace('¶','').strip()
	return f'{value1}@{value2.lower()}.html'
def hyper_html_value(value):
	return f'<a href="{value.lower()}.html">{value}</a>'

def join_flip(columns):
	return join((columns[0], columns[1], columns[4], columns[5]))

def join(columns):
	return ' & '.join(columns) + '\n'

def add_pair(t,d):
	result = f'<dt>{t}</dt>\n'
	for dd in d.split('//'):
		result += f'\t<dd>{dd.strip()}</dd>\n'
	return result

def process_index():
	filename = 'index.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###','')\
		.replace('###SUBTITLE###','')\
		.replace('###SUBPARA###',indexpara)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = ''
	for line in c_table:
		columns = line[:]
		columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
	for line in e_table:
		columns = line[:4]
		columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	maybe_update(new_content.format(par0, par1), old_content, filename)

def process_category(c):
	filename = c.lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###',title_double)\
		.replace('###SUBTITLE###',subtitle_cat)\
		.replace('###SUBPARA###',sub_para)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = c
	for line in c_table:
		columns = line[:]
		if columns[0] == c:
			par3 = columns[1]
			par4 = columns[2] + '</p><p>' + columns[3]
		else:
			columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
	for line in e_table:
		columns = line[:4]
		# colour the rows
		if columns[2] == c:
			columns[0] = '¶ ' + hyper_value(columns[0])
		elif columns[3] == c:
			columns[0] = '¶¶ ' + hyper_value(columns[0])
		else:
			columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	maybe_update(new_content.format(par0, par1, par2, par3, par4), old_content, filename)

def process_case(case):
	# print(case)
	filename = case[0].lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###',title_single)\
		.replace('###SUBTITLE###',subtitle_case)\
		.replace('###SUBPARA###',sub_list)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = ''
	par2 = case[0]
	for line in c_table:
		columns = line[:]
		if columns[0] == case[2]:
			columns[0] = '¶ ' + columns[0]
		if columns[0] == case[3]:
			columns[0] = '¶¶ ' + columns[0]
		columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
	for line in e_table:
		columns = line[:4]
		if columns[0] == case[0]:
			columns[0] = '¶ ' + hyper_value(columns[0])
		else:
			columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	# fill in the "form"
	par3 = add_pair('Source', hyper_html_value(case[1]))
	cats = hyper_html_value(case[2])
	if case[3] != '—':
		cats += f' (primary); {hyper_html_value(case[3])} (secondary)'
	par3 += add_pair('Categories', cats)
	if len(case)>4:
		par3 += add_pair('Domain', case[4])
	if len(case)>5:
		par3 += add_pair('Views', case[5])
	if len(case)>6:
		par3 += add_pair('Artefacts', case[6])
	if len(case)>7:
		par3 += add_pair('Quotes', case[7])
	if len(case)>8:
		par3 += add_pair('Summary', case[8])
	# ...
	maybe_update(new_content.format(par0, par1, par2, par3), old_content, filename)

def process_source(key):
	filename = key.lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###',title_double)\
		.replace('###SUBTITLE###',subtitle_source)\
		.replace('###SUBPARA###',sub_bib)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = key
	for line in bibitems[key]:
		if line.find('http') > -1:
			before, after = line.split('http')
			link, after = after.split('"')
			link = 'http' + link
			par4 += before + f'<a href="{link}">{link}</a>"' + after
		elif line.find('doi =') > -1:
			before, after = line.split('{')
			doi, after = after.split('}')
			par4 += before + f'{{<a href="https://doi.org/{doi}">{doi}</a>}}' + after
		else:
			par4 += line
	for line in c_table:
		columns = line[:]
		columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
	for line in e_table:
		columns = line[:4]
		# colour the rows
		if columns[1] == key:
			columns[0] = '¶ ' + hyper_value(columns[0])
		else:
			columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	maybe_update(new_content.format(par0, par1, par2, par3, par4), old_content, filename)

def cap(s):
	return ' '.join([word[0].upper() + word[1:] for word in s.split(' ')])

c_pattern = '''<html doctype>
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

title_double = ' - {2}: {3}'
title_single = ' — {2}'
subtitle_cat = '<br><span class="red">Category</span> <code>{2}</code>: {3}'
subtitle_case = '<br><span class="red">Case</span> <code>{2}</code>'
subtitle_source = '<br><span class="red">Source</span> <code>{2}</code>'
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
sub_para = '<p>{4}</p>'
sub_list = '<dl>{3}</dl>\n<h2>Taxonomy Categories</h2>'
sub_bib = '<p>{3}</p>\n<pre>{4}</pre>\n<h2>Taxonomy Categories</h2>'
evidence = '''<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
{1}
</table>'''

c_table = load_data('cat.data')[1:]
e_table = load_data('evidence.data')[1:]

all_cats = [line[0] for line in c_table]
primary = {c:len([1 for record in e_table if record[2]==c]) for c in all_cats}
secondary = {c:len([1 for record in e_table if record[3]==c]) for c in all_cats}
for cat in c_table:
	cat.append(str(primary[cat[0]]))
	cat.append(str(secondary[cat[0]]))

process_index()
for line in c_table:
	process_category(line[0])
for line in e_table:
	process_case(line)

# all the sources from BibTeX
bibitems = {}
with open('sources.bib', "r", encoding="utf-8") as f:
	for line in f.readlines():
		if not line.strip():
			continue
		if line.startswith('@'):
			key = line.split('{')[-1].split(',')[0]
			bibitems[key] = [line]
		else:
			bibitems[key].append(line)
for key in bibitems.keys():
	process_source(key)

with open('macros.tex', "w", encoding="utf-8") as f:
	f.write('\\usepackage{tabularx}\n')
	f.write('\\newcolumntype{Y}{>{\\raggedright\\arraybackslash}X}\n\n')
	for cat in all_cats:
		letter = chr(ord('A') + int(cat[1]) - 1)
		f.write(f'\\newcommand{{\\C{letter}}}{{\\textcolor{{purple}}{{\\textbf{{{cat}}}}}\\xspace}}\n')
		for cat_rec in c_table:
			if cat_rec[0] == cat:
				f.write(f'\\newcommand{{\\C{letter}text}}{{{cat_rec[1]}\\xspace}}\n')
				f.write(f'\\newcommand{{\\C{letter}textU}}{{{cap(cat_rec[1])}\\xspace}}\n')
				f.write(f'\\newcommand{{\\C{letter}textL}}{{{cat_rec[1].lower()}\\xspace}}\n')
