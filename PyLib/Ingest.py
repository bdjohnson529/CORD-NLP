import os
import json
import logging


#####
# Loading functions
#####
def convertJSONtoTXT(json_dir, txt_dir):
	# read in json filenames
	filenames = os.listdir(json_dir)
	filepaths = [json_dir + "\\" + x for x in filenames]

	for filePath in filepaths:
		f = open(filePath)
		json_data = json.load(f)

		abstract_str = ""
		for paragraph in json_data['abstract']:
		    abstract_str += paragraph.get('text')

		paper_id = json_data.get('paper_id')
		out_filepath = txt_dir + "\\" + paper_id + ".txt"

		with open(out_filepath, "w", encoding="utf-8") as outf:
			outf.write(abstract_str)

	return True