# -*- coding: utf-8 -*-
"""spacy_lemma.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SKBW5thNA_P-dVZmRBmVx2Bgo7_iCcMb
"""

import spacy

sp=spacy.load("en_core_web_sm")

doc=sp("arguing Dr. John roaming 60$ catlike Lipika ate programs 123 loving")

doc

for x in doc:
  print(x)

type(doc)

## lemmatization

for x in doc:
  print(x,":",x.lemma_,":",x.pos_)

for x in doc:
  print(x,":",x.lemma)

sp.pipe_names

sp.pipeline

### NER- NAMED ENTITY RECOGNIZATION

doc

str="Microsoft 60$ Bangalore 2023 Expectations LIVE News Updates: FM Sitharaman Likely to Increase Defence Allocation"

import spacy
nlp=spacy.load("en_core_web_sm")

doc=nlp(str)

doc[4]

doc[5:9]

doc

type(doc)

type(nlp)

for word in doc.ents:
  print(word.text,":",word.label_,":",spacy.explain(word.label_))

exm="Microsoft was fonded by Bill Gates on 1990 wheres Tesla Inc was invented by ElonMusk"

for entity in (nlp(exm)).ents:
  print(entity.text,"|",entity.label_)

nlp.pipe_labels['ner']

spacy.explain('GPE')

text="KIIT is the best University of India,Dr. John had donated 4500$ "

spacy.explain('ORG')

for entity in (nlp(text)).ents:
  print(entity.text,"|",entity.label_)

### Create a blank model of spacy and then Customize it as per your choice

model=spacy.blank("en")

model.pipe_names

nlp.pipe_names

model.add_pipe('ner','tagger',source=nlp)

model.pipe_names

## hugging face ner