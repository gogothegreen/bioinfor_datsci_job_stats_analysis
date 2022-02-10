#!/usr/bin/env python
import os

def get_counts(job_file):
    lang_counts = {}
    with open(job_file) as file:
        for line in file:
            line = line.rstrip()
            line = line.strip()
            langs = line.split(',')
            langs.pop(0) # first element is company name
            for lang in langs:
                # converting first letter to upper case to ensure uniform names
                if lang[0].isalpha():
                    lang = lang[:1].upper() + lang[1:]
                if lang in lang_counts:
                    lang_counts[lang] += 1
                else:
                    lang_counts[lang] = 1
    return(lang_counts)


def write_file(out_file, lang_counts):
    with open(out_file, "w") as f:
        f.write("language,counts\n")
        for lang,val in lang_counts.items():
            f.write("{},{}\n".format(lang,val))

def write_list(out_file, lang_counts):
    with open(out_file, "w") as f:
        f.write("languages\n")
        for lang in lang_counts:
            f.write("{}\n".format(lang))

datascience_job_file = "data/datascience_job_skills.txt"
datascience_out_file = os.path.splitext(datascience_job_file)[0] + "_counts.txt"
bioinformatics_job_file = "data/bioinformatics_job_skills.txt"
bioinformatics_out_file = os.path.splitext(bioinformatics_job_file)[0] + "_counts.txt"

bioinformatics_lang_counts = get_counts(bioinformatics_job_file)
datascience_lang_counts = get_counts(datascience_job_file)

# creating a combined plot
combi_lang_counts = {}
combi_lang_counts["Datascience"] = {}
combi_lang_counts["Bioinformatics"] = {}
for lang in bioinformatics_lang_counts:
    combi_lang_counts["Bioinformatics"][lang] = bioinformatics_lang_counts[lang]
    if lang in datascience_lang_counts:
        combi_lang_counts["Datascience"][lang] = datascience_lang_counts[lang]
    else:
        combi_lang_counts["Datascience"][lang] = 0

write_file(bioinformatics_out_file, bioinformatics_lang_counts)
write_file(datascience_out_file, datascience_lang_counts)

# going through the datascience dictionary so that no langs are missed
for lang in datascience_lang_counts:
    if lang not in combi_lang_counts["Bioinformatics"]:
        combi_lang_counts["Datascience"][lang] = datascience_lang_counts[lang]
        combi_lang_counts["Bioinformatics"][lang] = 0

# printing the combined values
combined_out_file = "data/combined_job_skills_counts.txt"
with open(combined_out_file, "w") as f:
    f.write("language,group,counts\n")
    for group,langval in combi_lang_counts.items():
        for lang,val in combi_lang_counts[group].items():
            f.write("{},{},{}\n".format(lang,group,val))

# writing just the bioinfo & datascience skills
datascience_skills_file = "data/datascience_skills.txt"
bioinformatics_skills_file = "data/bioinformatics_skills.txt"
write_list(datascience_skills_file, datascience_lang_counts)
write_list(bioinformatics_skills_file, bioinformatics_lang_counts)