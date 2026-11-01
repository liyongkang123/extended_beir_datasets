from datasets import load_dataset
import json
import os
import zipfile
import nltk
from nltk.tokenize import word_tokenize

def count_words_nltk(text):
    """Count words using NLTK tokenizer"""
    tokens = word_tokenize(text.lower())
    # Filter out punctuation, keep only alphanumeric tokens
    words = [token for token in tokens if token.isalnum()]
    return len(words)

def transfer_bright_corpus_to_beir(hf_dataset,output_corpus_path):
    # Iterate through data and write each item as a JSON line to output_corpus_path
    # Write to jsonl file
    length=[]
    if output_corpus_path is None:
        return
    with open(output_corpus_path, "w", encoding="utf-8") as f:
        for item in hf_dataset:
            new_json = {}
            new_json["_id"] = item["id"]
            new_json["text"] = item["content"] # Use 'content' field as text
            new_json['metadata']= { }
            new_json["title"] = item.get("title", "")
            length.append(count_words_nltk(new_json["text"]))
            f.write(json.dumps(new_json) + "\n")

    print(f"Saved to {output_corpus_path}, total {len(hf_dataset)} lines")
    print('corpus avg length:' ,sum(length)/len(length))

def transfer_bright_qrels_to_beir( hf_dataset, output_qrels_path ):
    if output_qrels_path is None:
        return

    with open(output_qrels_path, "w", encoding="utf-8") as f:
        # BEIR GenericDataLoader skips the first line as a header.
        f.write("query-id\tcorpus-id\tscore\n")
        for item in hf_dataset:
            query_id = item["id"]
            if 'long' in output_qrels_path:
                gold_ids = item["gold_ids_long"]
            else:
                gold_ids = item["gold_ids"]

            # Write one line for each relevant document
            for doc_id in gold_ids:
                # TREC qrels format: query_id 0 doc_id relevance_score
                # Using 1 as relevance score (indicating relevant)
                f.write(f"{query_id}\t{doc_id}\t1\n")

    print(f"Saved qrels to {output_qrels_path}, processed {len(hf_dataset)} queries")


def transfer_bright_queries_to_beir( hf_dataset, output_queries_path ):
    length = []
    with open(output_queries_path, "w", encoding="utf-8") as f:
        for item in hf_dataset:
            new_json = {}
            new_json["_id"] = item["id"]
            new_json["text"] = item["query"]
            length.append(count_words_nltk(new_json["text"]))
            # Create metadata with all fields except "id" and "query"
            new_json['metadata'] = {k: v for k, v in item.items() if k not in ["id", "query"]}

            f.write(json.dumps(new_json, ensure_ascii=False) + "\n")

    print(f"Saved to {output_queries_path}, total {len(hf_dataset)} lines")
    print('query avg length:' ,sum(length)/len(length))


def zip_beir_dataset(folder_path, zip_path):
    # Archive root is the dataset folder, e.g. biology/corpus.jsonl.
    # BEIR download_and_unzip extracts into out_dir and expects that folder name.
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.startswith("."):
                    continue
                full_path = os.path.join(dirpath, filename)
                arcname = os.path.relpath(full_path, os.path.dirname(folder_path))
                zf.write(full_path, arcname.replace(os.sep, "/"))
    print(f"Saved {zip_path}")


def main():
    # Write outside OneDrive. CloudStorage writes of the large jsonl files time out.
    project_root = os.path.expanduser("~/Downloads")

    task_list =["biology","earth_science","economics","psychology","robotics","stackoverflow","sustainable_living","leetcode","pony","aops","theoremqa_theorems","theoremqa_questions"]
    long_task_list = ["biology","earth_science","economics","psychology","robotics","stackoverflow","sustainable_living","pony"]
    for task in task_list:

        query_data = load_dataset('xlangai/BRIGHT', 'examples')[task]
        corpus = load_dataset('xlangai/bright', 'documents', )[task]

        '''Output paths'''
        task_dir = os.path.join(project_root, "bright_data", task)
        output_corpus_path = os.path.join(task_dir, "corpus.jsonl")
        output_queries_path = os.path.join(task_dir, "queries.jsonl")
        output_qrels_path = os.path.join(task_dir, "qrels", "test.tsv")
        zip_path = os.path.join(project_root, "bright_data", f"{task}.zip")


        if task in long_task_list:
            output_corpus_long_path = os.path.join(task_dir, "corpus_long.jsonl")
            corpus_long = load_dataset('xlangai/bright', 'long_documents', )[task]
            output_qrels_long_path = os.path.join(task_dir, "qrels", "test_long.tsv")
        else:
            output_corpus_long_path = None
            corpus_long = None
            output_qrels_long_path = None

        # Create necessary directories for output files
        os.makedirs(os.path.dirname(output_corpus_path), exist_ok=True)
        os.makedirs(os.path.dirname(output_qrels_path), exist_ok=True)

        # Transfer corpus data
        transfer_bright_corpus_to_beir( corpus, output_corpus_path )
        transfer_bright_corpus_to_beir( corpus_long, output_corpus_long_path )
        transfer_bright_queries_to_beir( query_data, output_queries_path )
        transfer_bright_qrels_to_beir( query_data, output_qrels_path )
        transfer_bright_qrels_to_beir( query_data, output_qrels_long_path )
        zip_beir_dataset(task_dir, zip_path)

        print(query_data)
        print(corpus)
        print('-------------------------')

if __name__ == "__main__":
    main()