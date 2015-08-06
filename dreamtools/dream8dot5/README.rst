Overview
===========


:Title: DREAM 8.5 - Rheumatoid Arthritis Responder Challenge
:Nickname: D8dotC1
:Summary: Participants were provided with genetics and transcriptomics information of the 1000 Genomes Project (www.1000genomes.org), as well as cytotoxicity measures derived from compound exposure to over a hundred toxic agents using the 1000 genomes lymphoblastoid cell lines and tasked with solving two related subchallenges.
:SubChallenges: sc1, sc2
:Synapse page: https://www.synapse.org/#!Synapse:syn1734172/wiki/

.. contents::

This directory contains tools for scoring of the two sub challenges of Rheumatoid Arthritis Responder DREAM Challenge. 
 


Subchallenge 1
-----------

**Challenge description:** Predict treatment response as measured by the change in disease activity score (DAS28) in response to anti-TNF therapy. 
The template for scoring is provided within this synapse https://www.synapse.org/#!Synapse:syn1917708 page. 

For further information on the subchallenge and on the submission format go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/55909 

For details on the scoring metrics go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/60497.


Subchallenge 2
-----------

**Challenge description:** Identify poor responders as defined by EULAR criteria for non-response (~20%% of the study population). 


Scoring
---------

From the dreamtools package, you can score a submission from the D8dot5C1 first sub challenge as follows:

::

  from dreamtools import D9dot5C1
  s = D9dot5C1()

  filename = s.download_template('sc1')
  df2 = s.score(filename, 'sc1')
  print(df1)

  filename = s.download_template('sc2')
  df2 = s.score(filename, 'sc2')
  print(df2)

Examples of submission files can be found in the source code (e.g., data/test_sc1.csv)



