## Mind the `[SEP]` Token Between Title and Text

When you cannot reproduce someone else's experimental results, it may be worth checking whether there is a `[SEP]` token between the *title* and *text*.

For **BERT-based models**, `[SEP]` is a very important special token.

---

### Background

In the past, when evaluating **BEIR** datasets, many of us (myself included) preferred to wrap our own model with the `DenseEncoderModel` class, which originates from the [`beir_utils.py`](https://github.com/facebookresearch/contriever/blob/main/src/beir_utils.py) code in **contriever**.

Typical usage looks like this:

```python
encoder = our own encoder
tokenizer = our own tokenizer
model = DRES(
    DenseEncoderModel(encoder, doc_encoder=encoder, tokenizer=tokenizer),
    batch_size=args.per_gpu_eval_batch_size
)
retriever = EvaluateRetrieval(model, score_function= score_function, k_values=[1, 5, 10, 50,100, 1000],) # "cos_sim"  or "dot" for dot-product
results = retriever.retrieve(corpus, queries)
```
### Difference in Corpus Processing

In [`DenseEncoderModel`](https://github.com/facebookresearch/contriever/blob/main/src/beir_utils.py), the BEIR corpus is processed as:
```python
"title" + " " + "text"
```
Therefore, the `[SEP]` token is not present. [Tevatron](https://github.com/texttron/tevatron/blob/main/src/tevatron/retriever/dataset.py) is also same as this.

Also, in the [`latest official BEIR code`](https://github.com/beir-cellar/beir/blob/main/beir/retrieval/models/util.py), the corpus is processed as:

```python
sep: str = " " (By default)
"title" + sep + "text"
```
(without `[SEP]` token).

However, some work like [`SimLM`](https://github.com/microsoft/unilm/blob/master/simlm/src/inference/encode_main.py) use the `[SEP]` token.
```python
batch_dict = tokenizer(examples['title'],
                       text_pair=examples['contents'],
                       max_length=args.p_max_len,
                       padding=PaddingStrategy.DO_NOT_PAD,
                       truncation=True)
```
Then here the BERT tokenizer will add the `[SEP]` token.


### Why It Matters

We found that the presence or absence of `[SEP]` can significantly affect evaluation results.
It is best to **keep it consistent with the way you processed data during training**.


### Example

When using the model `intfloat/simlm-base-msmarco-finetuned` to evaluate the `msmarco_titled` dataset:

With `[SEP]` (using BEIR’s latest code) → **MRR@10 = 41.1**

Without `[SEP]` (using `DenseEncoderModel` as above) → **MRR@10 = 35.53**

The difference is huge — pay attention!