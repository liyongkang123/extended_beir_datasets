import logging
import os
import pathlib
import random
from time import time
import json
from beir import LoggingHandler, util
from beir.datasets.data_loader import GenericDataLoader


#### Just some code to print debug information to stdout
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    handlers=[LoggingHandler()],
)
#### /print debug information to stdout

dataset = "msmarco" #

#### Download nfcorpus.zip dataset and unzip the dataset
url = f"https://github.com/liyongkang123/extended_beir_datasets/releases/download/beir_v1.0/{dataset}.zip"
hf_home = os.getenv('HF_HOME')
if hf_home:
    out_dir = os.path.join(hf_home, "datasets")
else:
    out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
# out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
data_path = util.download_and_unzip(url, out_dir)
corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="dev")
print(len(corpus))
print(corpus['517'])


from datasets import load_dataset
#load Tevatron/msmarco-passage-corpus
tevatron_corpus = load_dataset('Tevatron/msmarco-passage-corpus')['train']
print(len(tevatron_corpus))

# transfer tevatron_corpus to json
tevatron_corpus_json ={}
for item in tevatron_corpus:
    tevatron_corpus_json[item['docid']] = {'text': item['text'].strip(), 'title': item['title'].strip()}
    # here I use .strip() because in tevatron_corpus, some texts have leading spaces (strange)

print('finish tevatron_corpus_json')

# Now we will check the corpus and replace the title with the one from tevatron_corpus_json
for id in corpus.keys():
    try:
        # Check and replace logic
        assert corpus[id]['title'] == ''
        assert corpus[id]['text'] == tevatron_corpus_json[id]['text']
        corpus[id]['title'] = tevatron_corpus_json[id]['title']
        # In `Tevatron`, all empty titles are set to '-', and I have kept this behavior here.
        # So sometimes you may see `corpus[id]['title'] = '-'`
        # if you want to remove the dash in the title. Please use the following datasets:   msmarco_titled_without_dash

    except KeyError:
        # If the id is not found in tevatron_corpus_json, print the id and the original text
        print(f"Id not found: {id}, Content: {corpus[id]['text']}")
    except AssertionError as e:
        # If the assertion fails, print the specific error message
        print(f"Assertion failed for id: {id}, Error: {e}")
        print('--------------------------------')
        print(corpus[id]['title'])
        print(tevatron_corpus_json[id]['title'])
        print('--------------------------------')
        print(corpus[id]['text'])
        print(tevatron_corpus_json[id]['text'])

# Save corpus to a JSONL file

output_dir = r'datasets/msmarco_titled/corpus_remove_title_.jsonl'

with open(output_dir, 'w', encoding='utf-8') as f:
    for _id, record in corpus.items():
        json_obj = {"_id": _id,
                    "text": record["text"],
                    "title": record["title"],
                    "metadata": {},  # Leave the metadata field empty in the target file
                    }
        f.write(json.dumps(json_obj, ensure_ascii=False) + "\n")

print(f"The updated corpus has been saved to: {output_dir}")

'''
All other files are consistent with MSMARCO.
'''