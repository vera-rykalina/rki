---
marp: true
paginate: true
author: Vera Rykalina
theme: default
size: 4:3
footer: Vera Rykalina | September 2022

---

# Subtyping Pipeline

## Comprehensive Guide

---
<!-- ![fg :25% w:30](Documentation/../images/github.svg)-->
# Repo 
### https://github.com/vera-rykalina/rki_subtyping

---

# Conda Version
Pipeline's version of conda `4.14.0`
```sh
$ conda --version
```
---

# Pipeline Directory
Locate to Pipeline directory:
```sh
$ cd ~/rki_subtyping/Pipeline
```

---
# Input Folders
Make sure you have 5 directories:

```sh
tree  -d
```

```sh
├── AllSeqsCO20
├── InputFasta
├── ManualRega
├── References
└── Scripts
```
---
# InputFasta Folder
Prodive this folder with files as listed (from NGS pipeline): 
```sh
InputFasta/
├── MS95_ENV_20.fasta
├── MS95_INT_20.fasta
└── MS95_PRRT_20.fasta
```
---


# Example of .fasta within InputFasta
```sh
>20-02955_ENV_20
GGAATTAGGCCAGTGGTGTCAACCCAACTATTGTTAAATGGCAGCCTAGCAGAAGAAGAT
GTGGTCATTAGATCTGAAAATTTCACAAACAATGCTAAAACCATAATAGTACAGCTTAAT
GAAACAGTAGTGATTAATTGTACAAGACCCGGCAACAATACAAGAAAAAGTATACATATA
GGACCAGGAAAAGCATGGTATGCAACAGGAGAGATAATAGGAGATATAAGACAAGCACAT
TGTAAACTTAATAAAACACAATGGGAAAAAACTTTAAAAAGGGTAGCTAGTAAATTAAGG
AAACAATCCAACCTTACAACAGTAATCTTTAAGAACTCCTCAGGGGGGGACCCAGAAATT
GTAATGCACAGTTTTAACTGTGGAGGGGAATTTTTCTATTGTAACACAACACAGTTGTTC
AATAGTATTTGGAATGACACTACTAATAGTACTGACACAAATGAAACTATCACACTCCCA
TGCAGAATAAAACAAATTATAAATAGATGGCAGGAAGCAGGAAGGG
```
---
# AllSeqCO20 Folder
Prodive this folder with .xlsx files as listed (from NGS pipeline): 
```sh
AllSeqsCO20/
├── MS95_Seqs_ENV_CO20_V5.xlsx
├── MS95_Seqs_INT_CO20_V5.xlsx
└── MS95_Seqs_PRRT_CO20_V5.xlsx
```

---
# Conda Info (can be skipped)
List available conda environments.
```sh
$ conda info --envs
# conda environments:
#
base                  *  /home/beast2/anaconda3
subtyping_pipeline       /home/beast2/anaconda3/envs/subtyping_pipeline
```
---
# Activate Environment
Activate `subtyping_pipeline` enviromnet.
```sh
$ conda activate subtyping_pipeline
```
Be sure you have change in prompt:

```sh
(subtyping_pipeline) beast2@Beast2:~/rki_sybtyping/Pipeline$
```

---
#### Processes Overview
```sh
[1b/f2f10a] process > mark_fasta (2)        [100%] 3 of 3, cached: 3 ✔
[73/a28f41] process > stanford (3)          [100%] 3 of 3, cached: 3 ✔
[e6/e4af1d] process > json_to_csv (3)       [100%] 3 of 3, cached: 3 ✔
[65/e0eb90] process > clean_rega (3)        [100%] 3 of 3, cached: 3 ✔
[97/70bbdd] process > comet (3)             [100%] 3 of 3, cached: 3 ✔
[62/e59285] process > join_prrt (1)         [100%] 1 of 1, cached: 1 ✔
[87/4d2fcf] process > join_env (1)          [100%] 1 of 1, cached: 1 ✔
[34/36991e] process > join_int (1)          [100%] 1 of 1, cached: 1 ✔
[a9/dd644a] process > get_tags (3)          [100%] 3 of 3, cached: 3 ✔
[8d/dad394] process > make_decision (1)     [100%] 1 of 1, cached: 1 ✔
[d8/983216] process > join_with_tags        [100%] 1 of 1, cached: 1 ✔
[e6/ceaa42] process > fasta_for_mafft (2)   [100%] 3 of 3, cached: 3 ✔
[f7/9e1ccf] process > prrt_concat_panel (1) [100%] 1 of 1, cached: 1 ✔
[a4/b7aaee] process > int_concat_panel (1)  [100%] 1 of 1, cached: 1 ✔
[54/89322b] process > env_concat_panel (1)  [100%] 1 of 1 ✔
[c0/786bcd] process > mafft (3)             [100%] 3 of 3, cached: 2 ✔
[68/72f0eb] process > iqtree (3)            [100%] 3 of 3 ✔
[3c/0fb71f] process > report                [100%] 1 of 1, cached: 1 ✔
[c5/462a18] process > countplot (1)         [100%] 1 of 1, cached: 1 ✔
```




