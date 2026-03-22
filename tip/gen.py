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
		print(filename, '... preserved')
	else:
		with open(filename, "w", encoding="utf-8") as f:
			f.write(new_content)
		print(filename, '... updated')

def hyper_value(value):
	return f'{value}@{value.lower()}.html'
def hyper_bracketed_value(value):
	return f'[{value}]@{value.lower()}.html'
def hyper_other_value(value1, value2):
	return f'{value1}@{value2.lower()}.html'

def join(columns):
	return ' & '.join(columns) + '\n'

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
		columns = line[:4]
		columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join(columns)
	for line in e_table:
		columns = line[:4]
		# TODO: hyperlinkify the case ID
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
		.replace('###TITLE###',title_cat)\
		.replace('###SUBTITLE###',subtitle_cat)\
		.replace('###SUBPARA###',subpara_cat)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = c
	for line in c_table:
		columns = line[:]
		if columns[0] == c:
			par3 = columns[1]
			par4 = columns[4]
			if len(columns) > 5:
				par4 += '</p><p>' + columns[5]
		else:
			columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join(columns[:4])
	for line in e_table:
		columns = line[:4]
		# colour the rows
		if columns[2] == c:
			columns[0] = '¶ ' + columns[0]
		if columns[3] == c:
			columns[0] = '¶¶ ' + columns[0]
		# TODO: hyperlinkify the case ID
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	maybe_update(new_content.format(par0, par1, par2, par3, par4), old_content, filename)

def process_case(case):
	return
	filename = case.lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###',title_case)\
		.replace('###SUBTITLE###',subtitle_case)\
		.replace('###SUBPARA###',subpara)\
		.replace('###EVIDENCE###', evidence)
	par0 = par1 = par3 = par4 = ''
	par2 = c
	for line in c_table:
		columns = line[:]
		if columns[0] == c:
			par3 = columns[1]
			par4 = columns[4]
			if len(columns) > 5:
				par4 += '</p><p>' + columns[5]
		else:
			columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join(columns[:4])
	for line in e_table:
		columns = line[:4]
		# colour the rows
		if columns[2] == c:
			columns[0] = '¶ ' + columns[0]
		if columns[3] == c:
			columns[0] = '¶¶ ' + columns[0]
		# TODO: hyperlinkify the case ID
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		par1 += join(columns)
	maybe_update(new_content.format(par0, par1, par2, par3, par4), old_content, filename)

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

title_cat = ' - {2}: {3}'
title_case = ' — {2}'
subtitle_cat = '<br><span class="red">Category</span> <code>{2}</code>: {3}'
subtitle_case = '<br><span class="red">Case</span> <code>{2}</code>'
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
subpara_cat = '<p>{4}</p>'
subpara_case = '<p>{3}</p>'
evidence = '''<h2>Evidence Map</h2>
<table center llcc>
Case ID & Source & Primary & Secondary
{1}
</table>'''

c_table = load_data('cat.data')[1:]
e_table = load_data('evidence.data')[1:]

process_index()
for line in c_table:
	process_category(line[0])
for line in e_table:
	process_case(line)
