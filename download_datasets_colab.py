# DMRA-NMF paper dataset preparation for Google Colab
# Run this whole file in a Colab cell with:
# exec(open("/content/download_datasets_colab.py").read())

import os, subprocess, urllib.request, tarfile, gzip, shutil, zipfile
from pathlib import Path

ROOT = Path("/content/DMRA_NMF_DATASETS")
ROOT.mkdir(exist_ok=True)

def sh(cmd):
    print("$", cmd)
    subprocess.run(cmd, shell=True, check=True)

def download(url, out):
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading:", url)
    urllib.request.urlretrieve(url, out)
    print("Saved:", out)

# ---------------- Cora ----------------
cora = ROOT/"Cora"
cora.mkdir(exist_ok=True)
if not (cora/"cora.content").exists():
    download("https://linqs-data.soe.ucsc.edu/public/lbc/cora.tgz", ROOT/"cora.tgz")
    with tarfile.open(ROOT/"cora.tgz","r:gz") as t:
        t.extractall(cora)
print("Cora prepared.")

# ---------------- Citeseer ----------------
cit = ROOT/"Citeseer"
cit.mkdir(exist_ok=True)
if not (cit/"citeseer.content").exists():
    download("https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz", ROOT/"citeseer.tgz")
    with tarfile.open(ROOT/"citeseer.tgz","r:gz") as t:
        t.extractall(cit)
print("Citeseer prepared.")

# ---------------- PubMed ----------------
pub = ROOT/"PubMed"
pub.mkdir(exist_ok=True)
if not (pub/"Pubmed-Diabetes.NODE.paper.tab").exists():
    download("https://linqs-data.soe.ucsc.edu/public/Pubmed-Diabetes.tgz", ROOT/"Pubmed-Diabetes.tgz")
    with tarfile.open(ROOT/"Pubmed-Diabetes.tgz","r:gz") as t:
        t.extractall(pub)
print("PubMed prepared.")

# ---------------- Email-Eu-core ----------------
email = ROOT/"Email"
email.mkdir(exist_ok=True)
if not (email/"email-Eu-core.txt").exists():
    download("https://snap.stanford.edu/data/email-Eu-core.txt.gz", email/"email-Eu-core.txt.gz")
    with gzip.open(email/"email-Eu-core.txt.gz","rb") as fin, open(email/"email-Eu-core.txt","wb") as fout:
        shutil.copyfileobj(fin,fout)
if not (email/"email-Eu-core-department-labels.txt").exists():
    download("https://snap.stanford.edu/data/email-Eu-core-department-labels.txt.gz",
             email/"email-Eu-core-department-labels.txt.gz")
    with gzip.open(email/"email-Eu-core-department-labels.txt.gz","rb") as fin, open(email/"email-Eu-core-department-labels.txt","wb") as fout:
        shutil.copyfileobj(fin,fout)
print("Email prepared.")

# ---------------- Dolphin ----------------
dol = ROOT/"Dolphin"
dol.mkdir(exist_ok=True)
if not (dol/"out.dolphins").exists():
    download("https://www-personal.umich.edu/~mejn/netdata/dolphins.zip", ROOT/"dolphins.zip")
    with zipfile.ZipFile(ROOT/"dolphins.zip") as z:
        z.extractall(dol)
print("Dolphin prepared.")

print("\nDownloaded public source datasets:")
for p in ROOT.rglob("*"):
    if p.is_file():
        print(p)

print("\nNOTE:")
print("Amazon-C, BZR, Cornell, Gene and Reality-call have multiple public versions.")
print("The paper's exact node/edge counts should be reproduced with the authors'")
print("DMRA-NMF preprocessing/code rather than silently substituting another version.")
print("Repository: https://github.com/sohrabi94/DMRA-NMF")
