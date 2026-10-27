import json
import os

# The original data comes from https://github.com/google-deepmind/limit/tree/main/data/limit
# the corpus.jsonl and queries.jsonl are same format as beir, so we keep them.

# transfer qrels.jsonl to trec format

qrels_data_path = "Code/data/qrels.jsonl"
output_qrels_path = "Code/data/limit/qrels/test.tsv"

# Create necessary directories for output files
os.makedirs(os.path.dirname(output_qrels_path), exist_ok=True)

with open(qrels_data_path, "r", encoding="utf-8") as f_in, \
     open(output_qrels_path, "w", encoding="utf-8") as f_out:
    
    # BEIR qrels header: query-id\tcorpus-id\tscore
    f_out.write("query-id\tcorpus-id\tscore\n")
    
    for line in f_in:
        item = json.loads(line)
        query_id = item["query-id"]
        corpus_id = item["corpus-id"]
        score = item["score"]
        
        # Write to TSV format
        f_out.write(f"{query_id}\t{corpus_id}\t{score}\n")

print(f"Saved qrels to {output_qrels_path}")

