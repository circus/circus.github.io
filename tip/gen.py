#!/opt/local/bin/python

import os

def split3(text, one, two, include=True):
	first, second = text.split(one, 1)
	second, third = second.split(two, 1)
	return (first, one+second, two+third) if include else (first, second, third)

def latexify(c):
	if c in ('—', '–', ''):
		return c.replace('–', '---').replace('–', '--')
	letter = chr(ord('A') + int(c[-1]) - 1)
	return f'\\C{letter}'
	return f'\\<a href="{c.lower()}.html">C{letter}</a>'

def beautify_latex(lines):
	for kw in ('begin', 'end', 'caption', 'label', 'small', 'toprule', 'bottomrule', 'midrule', 'linewidth', 'usepackage', 'newcolumntype', 'newcommand', 'textcolor', 'xspace', 'raggedright', 'arraybackslash', 'cite', 'cline'):
		for i in range(len(lines)):
			if lines[i].find('\\' + kw) > -1:
				lines[i] = lines[i].replace(kw, f'[kw1]{kw}[/]')
	for kw in ('table',  'tabular', 'tabularx', 'purple'):
		for i in range(len(lines)):
			if lines[i].find('{' + kw + '}') > -1:
				lines[i] = lines[i].replace(kw, f'[kw2]{kw}[/]')
	for i in range(len(lines)):
		lines[i] = lines[i].replace('&', f'[kw2]&amp;[/]')
		if lines[i].endswith('\\\\'):
			lines[i] = lines[i][:-2] + '[kw2]\\\\[/]'
	return lines

def safe_load(filename):
	if filename.find('.') < -1:
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

def hyperlinkify(x):
	return x.strip()\
		.replace('SysML', '<a href="https://sysml.org/" title="System Modelling Language">SysML</a>')\
		.replace('UML', '<a href="https://www.omg.org/uml/" title="Unified Modelling Language">UML</a>')\
		.replace('Simulink', '<a href="https://en.wikipedia.org/wiki/Simulink">Simulink</a>')\
		.replace('MATLAB', '<a href="https://en.wikipedia.org/wiki/MATLAB">MATLAB</a>')\
		.replace('ABS', '<a href="https://en.wikipedia.org/wiki/Anti-lock_braking_system" title="anti-lock braking system">ABS</a>')\
		.replace('Git', '<a href="https://git-scm.com/">Git</a>')

def add_pair(t,d):
	c = ' class="red"' if t == 'Quotes' else ''
	result = f'<dt>{t}</dt>\n'
	for dd in d.split('//'):
		result += f'\t<dd{c}>{hyperlinkify(dd)}</dd>\n'
	return result

def hyperlink_map_no_highlight():
	text = ''
	for line in e_table:
		columns = line[:4]
		columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		text += join(columns)
	return text

def hyperlink_map_with_highlight(value, index1, index2=-1):
	text = ''
	for line in e_table:
		columns = line[:4]
		if columns[index1] == value:
			columns[0] = '¶ ' + hyper_value(columns[0])
		elif index2 >= 0 and columns[index2] == value:
			columns[0] = '¶¶ ' + hyper_value(columns[0])
		else:
			columns[0] = hyper_value(columns[0])
		columns[1] = hyper_bracketed_value(columns[1])
		columns[2] = hyper_value(columns[2])
		if columns[3] != '—':
			columns[3] = hyper_value(columns[3])
		text += join(columns)
	return text

def hyperlink_cats_no_highlight():
	text = ''
	for line in c_table:
		columns = line[:]
		columns[1] = hyper_other_value(columns[1], columns[0])
		text += join_flip(columns)
	return text

def process_index():
	filename = 'index.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###','')\
		.replace('###SUBTITLE###','')\
		.replace('###SUBPARA###',indexpara)\
		.replace('###EVIDENCE###', evidence)
	par0 = hyperlink_cats_no_highlight()
	par1 = hyperlink_map_no_highlight()
	maybe_update(new_content.format(par0, par1), old_content, filename)

def process_category(c):
	filename = c.lower() + '.dsl'
	old_content = safe_load(filename)
	new_content = c_pattern\
		.replace('###TITLE###',title_double)\
		.replace('###SUBTITLE###',subtitle_cat)\
		.replace('###SUBPARA###',sub_para)\
		.replace('###EVIDENCE###', evidence)
	par0 = par3 = par4 = ''
	par1 = hyperlink_map_with_highlight(c, 2, 3)
	par2 = c
	for line in c_table:
		columns = line[:]
		if columns[0] == c:
			par3 += columns[1]
			par4 += columns[2] + '</p><p>' + columns[3]
		else:
			columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
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
	par0 = ''
	par1 = hyperlink_map_with_highlight(case[0], 0)
	par2 = case[0]
	for line in c_table:
		columns = line[:]
		if columns[0] == case[2]:
			columns[0] = '¶ ' + columns[0]
		if columns[0] == case[3]:
			columns[0] = '¶¶ ' + columns[0]
		columns[1] = hyper_other_value(columns[1], columns[0])
		par0 += join_flip(columns)
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
		.replace('###TITLE###',title_single)\
		.replace('###SUBTITLE###',subtitle_source)\
		.replace('###SUBPARA###',sub_bib)\
		.replace('###EVIDENCE###', evidence)
	par0 = hyperlink_cats_no_highlight()
	par1 = hyperlink_map_with_highlight(key, 1)
	par2 = key
	par3 = par4 = ''
	for line in bibitems[key]:
		line2add = line
		if line.find('http') > -1:
			before, link, after = split3(line, 'http', '"')
			line2add = f'{before}<a href="{link.replace('\\_','_')}">{link}</a>{after}'
		elif line.find('doi =') > -1:
			before, doi, after = split3(line, '{', '}', include=False)
			line2add = f'{before}{{<a href="https://doi.org/{doi}">{doi}</a>}}{after}'
		elif line.find('{{') > -1 and line.find('}}') > -1:
			line2add = line.replace('{{', '{').replace('}}', '}')
		elif line.startswith('@'):
			before, kw, after = split3(line, '@', '{')
			line2add = f'{before}[kw1]{kw}[/]{after}'
		# beautification
		if line.find(' = ') > -1:
			key, val = line2add.split(' = ')
			key = key.strip()
			if key == 'author':
				val = val.replace(' and ', ' [kw2]and[/] ')
			line2add = f'  [kw2]{key}[/] = {val}'
		par4 += line2add
	maybe_update(new_content.format(par0, par1, par2, par3, par4), old_content, filename)

def process_latex(lines, filename):
	# print(lines),
	tex_filename = filename + '.tex'
	html_filename = filename + '.dsl'
	old_tex_content = safe_load(tex_filename)
	old_html_content = safe_load(html_filename)
	new_tex_content = '\n'.join(lines) + '\n'
	new_html_content = c_pattern\
		.replace('###TITLE###',title_single)\
		.replace('###SUBTITLE###',artefact_source)\
		.replace('###SUBPARA###',sub_tex)\
		.replace('###EVIDENCE###', '')
	par0 = hyperlink_cats_no_highlight()
	par1 = hyperlink_map_no_highlight()
	par2 = filename
	par3 = '\n'.join(beautify_latex(lines))
	maybe_update(new_tex_content, old_tex_content, tex_filename)
	maybe_update(new_html_content.format(par0, par1, par2, par3), old_html_content, html_filename)

def cap(s):
	return ' '.join([word[0].upper() + word[1:] for word in s.split(' ')])

def table1_line(cat, count, desc):
	letter = chr(ord('A') + int(cat[1]) - 1)
	return f'\\C{letter} & \\C{letter}text & {count} & {desc} \\\\'
	return f'\\<a href="{cat.lower()}.html">C{letter}</a> & \\C{letter}text & {count} & {desc} \\\\'

def table2_line(x):
	return f'{x[0]}~\\cite{{{x[1]}}} & {latexify(x[2])} & {latexify(x[3])}'
	return f'{x[0]}~\\cite{{<a href="{x[1].lower()}.html">{x[1]}</a>}} & {latexify(x[2])} & {latexify(x[3])}'

c_pattern = '''<html doctype>
	<head title="Taxonomy of Inconsistency Patterns###TITLE###" />
	<body>
		<credit/>
		<h1 logo="tip.200.png" alt="TIP" hover="TIP logo designed by Vadim Zaytsev">
			<a href="index.html"><u>T</u>axonomy of <u>I</u>nconsistency <u>P</u>atterns</a>
			in Multi-View Modelling
			###SUBTITLE###
		</h1>
		###SUBPARA###
		<table center clrr>
			Code & Label & As primary & As secondary
{0}
		</table>
		###EVIDENCE###
		<footer/>
	</body>
</html>
'''

title_double = ' — {2}: {3}'
title_single = ' — {2}'
subtitle_cat = '<br><span class="red">Category</span> <code>{2}</code>: {3}'
subtitle_case = '<br><span class="red">Case</span> <code>{2}</code>'
subtitle_source = '<br><span class="red">Source</span> <code>{2}</code>'
artefact_source = '<br><span class="red">Artefact</span> <code>{2}</code>'
indexpara = '''<p>
Multi-view modelling relies on consistency across heterogeneous views. Up until now, the literature
lacked a compact, example-backed taxonomy of the inconsistency patterns that we keep seeing across
practice and research prototypes. Existing surveys classify approaches and tools, but they do not
stabilise the recurring defect patterns themselves in a form that is directly useful for benchmarking,
evaluation, and tool-scope claims. This webpage presents a literature-based evidence map and a
seven-category <strong>taxonomy</strong> of inconsistency patterns in multi-view modelling.
</p><p>
We built a seed corpus from foundational and survey literature, then extracted
and coded 46 inconsistency examples from 18 sources. After a stabilisation
pass using explicit tie-break rules, <strong>40</strong> examples were
retained from <strong>17</strong> sources as core evidence. The taxonomy
provides a concise vocabulary for describing consistency problems, a reusable
evidence map for future research, and a basis for more precise claims about
what checking and repair approaches do and do not cover.
</p><p>
Feel free to browse specifics hyperlinked below or bulk download
the BibTeX collection <a href="sources.bib">sources.bib</a> or LaTeX files
<a href="macros.html">macros.tex</a>, <a href="table1.html">table1.tex</a>, and
<a href="table2.html">table2.tex</a>.
</p><p>
Raw data is available as <a href="cat.data">cat.data</a> and <a href="evidence.data">evidence.data</a>.
The format is “newline-separated values” which is like CSV but values within each record are “vertically” separated with newlines; with double newlines separating records.
</p>'''
sub_para = '<p>{4}</p>\n\t\t<clear/>'
main_table_title = '\n<clear/>\n<h2>Taxonomy Categories</h2>'
sub_list = '<dl>{3}</dl>' + main_table_title
sub_bib = '<p>{3}</p>\n<pre>{4}</pre>' + main_table_title
sub_tex = '<p>Download raw LaTeX: <a href="{2}.tex">{2}.tex</a></p>\n<pre>{3}</pre>' + main_table_title
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

# Generate the generic macros file (used by all the tables)
latex = []
latex.append('\\usepackage{tabularx}')
latex.append('\\newcolumntype{Y}{>{\\raggedright\\arraybackslash}X}')
latex.append('')
for cat in all_cats:
	letter = chr(ord('A') + int(cat[1]) - 1)
	latex.append(f'\\newcommand{{\\C{letter}}}{{\\textcolor{{purple}}{{\\textbf{{{cat}}}}}\\xspace}}')
	for cat_rec in c_table:
		if cat_rec[0] == cat:
			latex.append(f'\\newcommand{{\\C{letter}text}}{{{cat_rec[1]}\\xspace}}')
			latex.append(f'\\newcommand{{\\C{letter}textU}}{{{cap(cat_rec[1])}\\xspace}}')
			latex.append(f'\\newcommand{{\\C{letter}textL}}{{{cat_rec[1].lower()}\\xspace}}')
process_latex(latex, 'macros')

# Generate the first table (with just the taxonomy and basic statistics/descriptions)
latex = []
latex.append('\\begin{table}[t]')
latex.append(f'\\caption{{Stabilised taxonomy of inconsistency patterns. Counts are based on the {len(e_table)} core examples.}}')
latex.append('\\label{tab:taxonomy}')
latex.append('\\small')
latex.append('\\begin{tabularx}{\\linewidth}{@{}l l c Y@{}}')
latex.append('\\toprule')
latex.append('Code & Label & Count & Definition \\\\')
latex.append('\\midrule')
for cat in all_cats:
	letter = chr(ord('A') + int(cat[1]) - 1)
	for cat_rec in c_table:
		if cat == cat_rec[0]:
			latex.append(table1_line(cat, cat_rec[4], cat_rec[2]))
latex.append('\\bottomrule')
latex.append('\\end{tabularx}')
latex.append('\\end{table}')
process_latex(latex, 'table1')

latex = []
latex.append('\\begin{table}[t]')
latex.append('\\caption{All cases with their IDs, primary and possibly secondary categories.}')
latex.append('\\label{tab:allcats}')
latex.append('\\small')
latex.append('\\begin{tabular}{lrr|lrr|lrr}')
latex.append('\\toprule')
last = ''
full_groups = []
for line in e_table:
	if line[2] != last:
		full_groups.append([])
		last = line[2]
	full_groups[-1].append(line[:4])
# print(full_groups)
groups = [len(g) for g in full_groups]
# groups = [int(x[-2]) for x in c_table] # same thing
# print(groups)
pivot = min(sum(groups) // 3, max(groups))
# print(pivot)
division = []
while len(division) != 3:
	division = [[]]
	for member in groups:
		# if sum([len(d) for d in division[-1]]) + member > pivot:
		if sum(division[-1]) + member > pivot:
			division.append([])
		division[-1].append(member)
	pivot += 1
	# print('Possibly', division)
# print('Definitely', division)
col1 = []
limit1 = sum(division[0])
limit2 = sum(division[1]) + limit1
limit3 = sum(division[2]) + limit2
for i in range(0, limit1):
	col1.append(table2_line(e_table[i]))
col2 = []
for i in range(limit1, limit2):
	col2.append(table2_line(e_table[i]))
col3 = []
for i in range(limit2, limit3):
	col3.append(table2_line(e_table[i]))
last1 = col1[0].split('&')[1]
last2 = col2[0].split('&')[1]
last3 = col3[0].split('&')[1]
sep = ''
for i in range(0, max(len(col1), len(col2), len(col3))):
	if i < len(col1):
		if col1[i].split('&')[1] != last1:
			sep = '\\cline{1-3}'
			last1 = col1[i].split('&')[1]
		latex.append(col1[i] + ' & ')
	else:
		latex.append('&&&')
	if i < len(col2):
		if col2[i].split('&')[1] != last2:
			sep = '\\cline{4-6}'
			last2 = col2[i].split('&')[1]
		latex.append('\t' + col2[i] + ' & ')
	else:
		latex.append('&&&')
	if i < len(col3):
		if col3[i].split('&')[1] != last3:
			sep = '\\cline{7-9}'
			last3 = col3[i].split('&')[1]
		latex.append('\t\t' + col3[i] + ' \\\\\n')
	else:
		latex.append('&& ')
	if sep:
		latex.insert(-3,sep)
		sep = ''
latex[-1] += ' \\\\'
latex.append(f'\\bottomrule')
latex.append('\\end{tabular}')
latex.append('\\end{table}')
process_latex(latex, 'table2')
