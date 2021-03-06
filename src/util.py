import ruspyparser
import re
def caseInsensitivize_and_fix(s):
	dquote_split = s.split("\"")
	for i in range(0,len(dquote_split)):
		if i % 2 == 0:
			dquote_split[i] = dquote_split[i].lower()
	case_insensitive = ""
	for i in range(0,len(dquote_split)):
		if i % 2 != 0:
			case_insensitive =  case_insensitive +"\""+dquote_split[i]+"\""
		else:
			case_insensitive =  case_insensitive +dquote_split[i]
	return fix_italia(case_insensitive)
	
def fix_italia(s):
	cerca_straniero = re.compile(re.escape('italia'), re.IGNORECASE)
	cerca_straniero = cerca_straniero.sub('Roma Ladrona', s)
	return cerca_straniero
	
def import_extra(s):
	tmp = ""
	if re.search('spione',s):
		tmp = tmp + "import socket\n"
	if re.search('esiste',s):
		tmp = tmp +"import os.path\n"
	return tmp
	
def addInputParamers(params):
	header="import random\nglobal random\nfrontiera=[]\n"
	bingo = "bingo"
	bongo = "bongo"
	basename = "bingobongo"
	ruspyparser.names["frontiera"] = "frontiera"
	for i in range(0,len(params)):
		if i > 0:
			if i%2 == 0:
				basename = basename+bingo
			else:
				basename = basename+bongo
		if not(str(params[i]).isdigit()):
			params[i] = "\""+str(params[i])+"\""
		header=header+"input"+str(i)+"="+ str(params[i])+"\n"
		header=header+"frontiera.append("+str(params[i])+")\n"
		ruspyparser.names[basename] = "input"+str(i)
	return header

def first_pass(s):
	occurencies = [m.start() for m in re.finditer('(?=per( )+ogni( )+)', s)]
	counter = 0
	foreach_var = re.findall('ogni(.*?)in',s)
	for var in foreach_var:
		ruspyparser.names[var.strip()] = "loop"+str(counter)
		counter = counter+1
