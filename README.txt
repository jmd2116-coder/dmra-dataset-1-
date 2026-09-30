DMRA-NMF PAPER DATASET PACKAGE
================================

Based on:
Community Detection via Deep Motif-Regularized Asymmetric Nonnegative Matrix Factorization
Sohrabi et al., Engineering Applications of Artificial Intelligence (2026).

The paper evaluates 10 real-world networks:
Amazon-C, BZR, Citeseer, Cornell, Cora, Dolphin, Email, Gene, PubMed, Reality-call.

IMPORTANT
---------
This package does NOT pretend that public downloads are identical to the paper's
preprocessed inputs. The paper's table gives the following target statistics:

Amazon-C   13,752 nodes, 245,861 edges, 10 communities
BZR        14,479 nodes, 15,535 edges, 10 communities
Citeseer    3,312 nodes,   4,732 edges,  6 communities
Cornell       195 nodes,     301 edges,  5 communities
Cora        2,708 nodes,   5,429 edges,  7 communities
Dolphin        62 nodes,     159 edges,  2 communities
Email       1,005 nodes,  25,571 edges, 42 communities
Gene        1,103 nodes,   1,672 edges,  2 communities
PubMed     19,717 nodes,  44,324 edges,  3 communities
Reality-call 6,809 nodes, 7,697 edges,  3 communities

The authors state that their MATLAB source code, preprocessing functions,
parameter configurations, and supplementary material are publicly available
in their DMRA-NMF GitHub repository:
https://github.com/sohrabi94/DMRA-NMF

The included Colab script downloads public source datasets where stable public
URLs are known. It then lets you compare the resulting graph statistics against
the paper's target table. For an exact reproduction, use the authors'
preprocessing code.

PUBLIC SOURCES USED/REFERENCED
------------------------------
Cora/Citeseer:
https://linqs-data.soe.ucsc.edu/public/lbc/cora.tgz
https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz

PubMed:
https://linqs-data.soe.ucsc.edu/public/Pubmed-Diabetes.tgz

Email-Eu-core:
https://snap.stanford.edu/data/email-Eu-core.txt.gz
https://snap.stanford.edu/data/email-Eu-core-department-labels.txt.gz

Dolphins:
https://www-personal.umich.edu/~mejn/netdata/dolphins.zip

Network Repository:
https://networkrepository.com/gene.php
https://networkrepository.com/BZR.php
https://networkrepository.com/reality-call.php

Paper repository:
https://github.com/sohrabi94/DMRA-NMF

HOW TO USE IN GOOGLE COLAB
--------------------------
1. Upload/run download_datasets_colab.py in Colab.
2. It creates /content/DMRA_NMF_DATASETS.
3. Run the final verification cell in that script.
4. For your project, Cora, Citeseer, Dolphin, and Email are the easiest
   starting datasets.
