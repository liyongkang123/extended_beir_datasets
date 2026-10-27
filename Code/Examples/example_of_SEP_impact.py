
import torch
from transformers import AutoModel, AutoTokenizer, BatchEncoding, PreTrainedTokenizerFast,set_seed
from transformers.modeling_outputs import BaseModelOutput
import gzip
import json
from datasets import load_dataset
from datasets import Dataset
from typing import Dict, List, Any

set_seed(2025)

def l2_normalize(x: torch.Tensor):
    return torch.nn.functional.normalize(x, p=2, dim=-1)

def encode_query(tokenizer: PreTrainedTokenizerFast, query: str) -> BatchEncoding:
    return tokenizer(query,
                     max_length=32,
                     padding=True,
                     truncation=True,
                     return_tensors='pt')

def encode_passage_with_sep(tokenizer: PreTrainedTokenizerFast, passage: str, title: str = '-') -> BatchEncoding:
    return tokenizer(title,
                     text_pair=passage,
                     max_length=144,
                     padding=True,
                     truncation=True,
                     return_tensors='pt')

def encode_passage_without_sep(tokenizer: PreTrainedTokenizerFast, passage: str, title: str = '') -> BatchEncoding:
    passage = title +" "+passage if title else passage
    return tokenizer(passage,
                     max_length=144,
                     padding=True,
                     truncation=True,
                     return_tensors='pt')


tokenizer = AutoTokenizer.from_pretrained('intfloat/simlm-base-msmarco-finetuned')
model = AutoModel.from_pretrained('intfloat/simlm-base-msmarco-finetuned')
model.eval()

#load Tevatron/msmarco-passage-corpus
dataset = load_dataset('Tevatron/msmarco-passage-corpus')['train']

queries = load_dataset('Tevatron/msmarco-passage')['dev']

query_id_to_text={}
for item in queries:
    query_id_to_text[item['query_id']] = item['query']

query_batch_dict = encode_query(tokenizer, query_id_to_text['29612'])
outputs: BaseModelOutput = model(**query_batch_dict, return_dict=True)
query_embedding = l2_normalize(outputs.last_hidden_state[0, 0, :])

psg1 =  dataset[7725922]['text']
title1 = dataset[7725922]['title']
print('docid ',dataset[7725922]['docid'])
print('title ',title1)
print('psg1 ',psg1)
psg1_batch_dict = encode_passage_with_sep(tokenizer, psg1, title1)
outputs: BaseModelOutput = model(**psg1_batch_dict, return_dict=True)
psg1_embedding = l2_normalize(outputs.last_hidden_state[0, 0, :])

psg2_batch_dict = encode_passage_without_sep(tokenizer, psg1, title1)
outputs: BaseModelOutput = model(**psg2_batch_dict, return_dict=True)
psg2_embedding = l2_normalize(outputs.last_hidden_state[0, 0, :])

# Higher cosine similarity means they are more relevant
print(query_embedding.dot(psg1_embedding) )
print(query_embedding.dot(psg2_embedding) )

'''Example 1 '''
# query_id = '300674'
# docid= 7067032
# tensor(0.8795, grad_fn=<DotBackward0>) with_sep
# tensor(0.8993, grad_fn=<DotBackward0>) without_sep

# docid= 7067029
# tensor(0.8809, grad_fn=<DotBackward0>)with_sep
# tensor(0.8905, grad_fn=<DotBackward0>) without_sep

'''Example 2 '''
# query_id = '29612'
# docid= 7725922
# tensor(0.8729, grad_fn=<DotBackward0>) with_sep
# tensor(0.7853, grad_fn=<DotBackward0>) without_sep very big difference