import json
import os
import shutil

from huggingface_hub import hf_hub_download

# LIMIT-small and LIMIT-small-synonyms ship three jsonl files in MTEB format:
#   corpus.jsonl   {"_id", "title", "text"}          already BEIR
#   queries.jsonl  {"_id", "text"}                   already BEIR
#   qrels.jsonl    {"query-id", "corpus-id", "score"} needs BEIR tsv
#
# Corpus and queries are copied as-is. Qrels are rewritten to
# qrels/test.tsv, same as transfer_limit_data_to_beir_format.py.
#
# The synonyms set keeps the same ids and the same queries. Only the
# corpus text changes, so both datasets use this writer.
#
# Files are downloaded with huggingface_hub instead of datasets.load_dataset.
# The local datasets package (2.12) cannot parse this dataset card's
# multiple configs.

DATASETS = [
    ("orionweller/LIMIT-small", "limit_small"),
    ("orionweller/LIMIT-small-synonyms", "limit_small_synonyms"),
]


def download(repo_id, filename):
    return hf_hub_download(repo_id=repo_id, filename=filename, repo_type="dataset")


def write_qrels(qrels_jsonl_path, output_path):
    n = 0
    with open(qrels_jsonl_path, "r", encoding="utf-8") as f_in, \
         open(output_path, "w", encoding="utf-8") as f_out:
        # BEIR GenericDataLoader skips the first line as a header.
        f_out.write("query-id\tcorpus-id\tscore\n")
        for line in f_in:
            item = json.loads(line)
            f_out.write(f"{item['query-id']}\t{item['corpus-id']}\t{item['score']}\n")
            n += 1
    print(f"Saved {output_path}, total {n} lines")


def transfer_one(repo_id, folder_name, project_root):
    out_dir = os.path.join(project_root, folder_name)
    qrels_dir = os.path.join(out_dir, "qrels")
    os.makedirs(qrels_dir, exist_ok=True)

    corpus_src = download(repo_id, "corpus.jsonl")
    queries_src = download(repo_id, "queries.jsonl")
    qrels_src = download(repo_id, "qrels.jsonl")

    corpus_dst = os.path.join(out_dir, "corpus.jsonl")
    queries_dst = os.path.join(out_dir, "queries.jsonl")
    shutil.copyfile(corpus_src, corpus_dst)
    shutil.copyfile(queries_src, queries_dst)
    print(f"Saved {corpus_dst}")
    print(f"Saved {queries_dst}")

    write_qrels(qrels_src, os.path.join(qrels_dir, "test.tsv"))


def main():
    # Script lives in Code/. Dataset folders go to the repo root so they can be zipped directly.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    for repo_id, folder_name in DATASETS:
        print(f"Converting {repo_id} -> {folder_name}/")
        transfer_one(repo_id, folder_name, project_root)


if __name__ == "__main__":
    main()
