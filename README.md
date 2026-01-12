# Extended Beir Datasets
This `Extended Beir Datasets` is derived from the original BEIR dataset download link: [https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/)

On this basis, I have added new datasets (`msmarco_titled`, `trec_dl19`, `trec_dl20`, all datasets in `Bright`, `BrowseComp-Plus` ) and maintained the same format as the original, making it more convenient for evaluation.

**Dataprocess details can be found under the ``Code`` folder.**

## :beers: Available Datasets (Extended)
| Dataset                     | Website| BEIR-Name          | Public? | Type                             | Queries | Corpus | Rel D/Q | Down-load | md5 | Note|
|-----------------------------| -----|--------------------| ------- |----------------------------------|---------| ---------|---------| :----------: | :------:|:------:|
| MSMARCO Passage(with title) | [Homepage](https://microsoft.github.io/msmarco/)| ``msmarco_titled`` | ✅ | ``train``<br>``dev``<br>``test`` | 6,980   |  8.84M     | 1.1     | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/msmarco.zip) | ``444067daf65d982533ea17ebd59501e4`` | From [Tevatron](https://huggingface.co/datasets/Tevatron/msmarco-passage-corpus) |
| TREC-DL 19                  |  [Homepage](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2019)| ``trec_dl19``     | ✅ | ``test``                         | 43      |  8.84M | 95.4    | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/trec-covid.zip) | ``ce62140cb23feb9becf6270d0d1fe6d1`` |original, without passage title|
| TREC-DL 20                  | [Homepage](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020.html) | ``trec_dl20``       | ✅ | ``test``                         | 54      |  8.84M     | 66.8    | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/nfcorpus.zip) | ``a89dba18a62ef92f7d323ec890a0d38d`` |original, without passage title|
| Biology | None| ``biology`` | ✅ | ``test``     | 103 | 57,359| 3.6 |None| None| only passage retrieval|
| Earth Science | None| ``earth_science`` | ✅ | ``test``     | 116 | 121,249| 5.3 |None| None| only passage retrieval|
| Economics | None| ``economics`` | ✅ | ``test``     | 103 | 50,220| 8.0 |None| None| only passage retrieval|
| Psychology | None| ``psychology`` | ✅ | ``test``     | 101 | 52,835| 7.3 |None| None| only passage retrieval|
| Robotics | None| ``robotics`` | ✅ | ``test``     | 101 | 61,961| 5.5 |None| None| only passage retrieval|
| Stack Overflow | None| ``stack_overflow`` | ✅ | ``test``     | 117 | 107,081| 7.0 |None| None| only passage retrieval|
| Sustainable Living | None| ``sustainable_living`` | ✅ | ``test``     | 108 | 60,792| 5.6 |None| None| only passage retrieval|
| LeetCode | None| ``leetcode`` | ✅ | ``test``     | 142 | 413,932| 1.8 |None| None| only passage retrieval|
| Pony | None| ``pony`` | ✅ | ``test``     | 112 | 7,894| 22.5 |None| None| only passage retrieval|
| AoPS | None| ``aops`` | ✅ | ``test``     | 111 | 188,002| 4.7 |None| None| only passage retrieval|
| TheoremQA-Q | None| ``theoremqa_questions`` | ✅ | ``test``     | 194 | 188,002| 3.2 |None| None| only passage retrieval|
| TheoremQA-T | None| ``theoremqa_theorems`` | ✅ | ``test``     | 76 | 23,839| 2.0 |None| None| only passage retrieval|
|BrowseComp-Plus|None| ``browsecomp_plus``| ✅ | ``golds``,``evidence`` | 830 |100,195| 6.1 , 2.9 | None| None| only passage retrieval|


## :beers: Available Datasets (Original)

Command to generate md5hash using Terminal:  ``md5sum filename.zip``.

You can view all datasets available **[here](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/)** or on **[Hugging Face](https://huggingface.co/BeIR)**.

| Dataset   | Website| BEIR-Name | Public? | Type | Queries  | Corpus | Rel D/Q | Down-load | md5 |     Note      |
| -------- | -----| ---------| ------- | --------- | ----------- | ---------| ---------| :----------: | :------:|:-------------:|
| MSMARCO    | [Homepage](https://microsoft.github.io/msmarco/)| ``msmarco`` | ✅ | ``train``<br>``dev``<br>``test``|  6,980   |  8.84M     |    1.1 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/msmarco.zip) | ``444067daf65d982533ea17ebd59501e4`` | Without title |
| TREC-COVID |  [Homepage](https://ir.nist.gov/covidSubmit/index.html)| ``trec-covid``| ✅ | ``test``| 50|  171K| 493.5 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/trec-covid.zip) | ``ce62140cb23feb9becf6270d0d1fe6d1`` |
| NFCorpus   | [Homepage](https://www.cl.uni-heidelberg.de/statnlpgroup/nfcorpus/) | ``nfcorpus`` | ✅ |``train``<br>``dev``<br>``test``|  323     |  3.6K     |  38.2 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/nfcorpus.zip) | ``a89dba18a62ef92f7d323ec890a0d38d`` |
| BioASQ     | [Homepage](http://bioasq.org) | ``bioasq``| ❌ | ``train``<br>``test`` | 500 |  14.91M    |  4.7 | No | [How to Reproduce?](https://github.com/beir-cellar/beir/blob/main/examples/dataset#2-bioasq) |
| NQ         | [Homepage](https://ai.google.com/research/NaturalQuestions) | ``nq``| ✅ | ``train``<br>``test``| 3,452   |  2.68M  |  1.2 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/nq.zip) | ``d4d3d2e48787a744b6f6e691ff534307`` |
| HotpotQA   | [Homepage](https://hotpotqa.github.io) | ``hotpotqa``| ✅ |``train``<br>``dev``<br>``test``|  7,405   |  5.23M  |  2.0 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/hotpotqa.zip)  | ``f412724f78b0d91183a0e86805e16114`` |
| FiQA-2018  | [Homepage](https://sites.google.com/view/fiqa/) | ``fiqa`` | ✅ | ``train``<br>``dev``<br>``test``|  648     |  57K    |  2.6 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/fiqa.zip)  | ``17918ed23cd04fb15047f73e6c3bd9d9`` |
| Signal-1M(RT) | [Homepage](https://research.signal-ai.com/datasets/signal1m-tweetir.html)| ``signal1m`` | ❌ | ``test``| 97   |  2.86M  |  19.6 | No | [How to Reproduce?](https://github.com/beir-cellar/beir/blob/main/examples/dataset#4-signal-1m) |
| TREC-NEWS  | [Homepage](https://trec.nist.gov/data/news2019.html) | ``trec-news`` | ❌ | ``test``| 57    |  595K    |  19.6 | No | [How to Reproduce?](https://github.com/beir-cellar/beir/blob/main/examples/dataset#1-trec-news) |
| Robust04 | [Homepage](https://trec.nist.gov/data/robust/04.guidelines.html) | ``robust04``| ❌ | ``test``| 249  |  528K  |  69.9 |  No  |  [How to Reproduce?](https://github.com/beir-cellar/beir/blob/main/examples/dataset#3-robust04)  |
| ArguAna    | [Homepage](http://argumentation.bplaced.net/arguana/data) | ``arguana``| ✅ |``test`` | 1,406     |  8.67K    |  1.0 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/arguana.zip)  | ``8ad3e3c2a5867cdced806d6503f29b99`` |
| Touche-2020| [Homepage](https://webis.de/events/touche-20/shared-task-1.html) | ``webis-touche2020``| ✅ | ``test``| 49     |  382K    |  19.0 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/webis-touche2020.zip) | ``46f650ba5a527fc69e0a6521c5a23563`` |
| CQADupstack| [Homepage](http://nlp.cis.unimelb.edu.au/resources/cqadupstack/) | ``cqadupstack``| ✅ | ``test``| 13,145 |  457K  |  1.4 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/cqadupstack.zip) | ``4e41456d7df8ee7760a7f866133bda78`` |
| Quora| [Homepage](https://www.quora.com/q/quoradata/First-Quora-Dataset-Release-Question-Pairs) | ``quora``| ✅ | ``dev``<br>``test``| 10,000     |  523K    |  1.6 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/quora.zip) | ``18fb154900ba42a600f84b839c173167`` |
| DBPedia | [Homepage](https://github.com/iai-group/DBpedia-Entity/) | ``dbpedia-entity``| ✅ | ``dev``<br>``test``| 400    |  4.63M    |  38.2 | [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/dbpedia-entity.zip) | ``c2a39eb420a3164af735795df012ac2c`` |
| SCIDOCS| [Homepage](https://allenai.org/data/scidocs) | ``scidocs``| ✅ | ``test``| 1,000     |  25K    |  4.9 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scidocs.zip) | ``38121350fc3a4d2f48850f6aff52e4a9`` |
| FEVER | [Homepage](http://fever.ai) | ``fever``| ✅ | ``train``<br>``dev``<br>``test``|  6,666     |  5.42M    |  1.2|  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/fever.zip)  | ``5a818580227bfb4b35bb6fa46d9b6c03`` |
| Climate-FEVER| [Homepage](http://climatefever.ai) | ``climate-fever``| ✅ |``test``|  1,535     |  5.42M |  3.0 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/climate-fever.zip)  | ``8b66f0a9126c521bae2bde127b4dc99d`` |
| SciFact| [Homepage](https://github.com/allenai/scifact) | ``scifact``| ✅ | ``train``<br>``test``|  300     |  5K    |  1.1 |  [Link](https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip)  | ``5f7d1de60b170fc8027bb7898e2efca1`` |


## :beers:  How to use it:

The usage is exactly the same as when using the original BEIR datasets. Simply replace the download URL in the code with ours. The specific code is as follows:

```python
import os
from beir import LoggingHandler, util
from beir.datasets.data_loader import GenericDataLoader
import pathlib

dataset = "nfcorpus"  # All available datasets, please refer to the README file

#### Download nfcorpus.zip dataset and unzip the dataset
url = f"https://github.com/liyongkang123/extended_beir_datasets/releases/download/beir_v1.0/{dataset}.zip"
hf_home = os.getenv('HF_HOME')  # Using the Hugging Face cache path
if hf_home:
    out_dir = os.path.join(hf_home, "datasets")
else:
    out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
data_path = util.download_and_unzip(url, out_dir)

#### Provide the data path where nfcorpus has been downloaded and unzipped to the data loader
# The data folder would contain these files:
# (1) nfcorpus/corpus.jsonl  (format: jsonlines)
# (2) nfcorpus/queries.jsonl (format: jsonlines)
# (3) nfcorpus/qrels/test.tsv (format: tsv ("\t"))

corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="test")
```
Specifically, replace the download link with the following:
```python
url = f"https://github.com/liyongkang123/extended_beir_datasets/releases/download/beir_v1.0/{dataset}.zip"
```
