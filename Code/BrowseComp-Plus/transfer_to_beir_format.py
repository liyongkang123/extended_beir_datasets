import json
import os
from datasets import load_dataset

def parse_line(line: str):
    s = line.strip()
    if not s or s.startswith("#"):
        return None
    parts = s.split()
    # allow qid Q0 docid rel / qid docid rel / qid docid
    if len(parts) >= 4:
        qid, mid, docid, rel = parts[0], parts[1], parts[2], parts[3]
        if mid.upper() == "Q0":
            return str(qid), str(docid), str(rel)
        else:
            return str(qid), str(docid), str(rel)
    elif len(parts) == 3:
        qid, docid, rel = parts
        return str(qid), str(docid), str(rel)
    elif len(parts) == 2:
        qid, docid = parts
        return str(qid), str(docid), "1"
    return None

def transfer_qrels():
    # Ensure output directory exists
    output_dir = 'browsecomp_plus/qrels'
    os.makedirs(output_dir, exist_ok=True)

    # Define all qrels files that need to be processed
    qrels_files = [
        ('topics-qrels/qrel_evidence.txt', 'browsecomp_plus/qrels/evidence.tsv'),
        ('topics-qrels/qrel_golds.txt', 'browsecomp_plus/qrels/golds.tsv'),
    ]

    for qrels_input_path, qrels_output_path in qrels_files:
        total_in = total_out = 0
        with open(qrels_input_path, "r", encoding="utf-8") as fin, open(qrels_output_path, "w", encoding="utf-8") as fout:
            # Write header
            fout.write("query-id\tcorpus-id\tscore\n")
            for line in fin:
                parsed = parse_line(line)
                if not parsed:
                    continue
                qid, docid, rel = parsed
                fout.write(f"{qid}\t{docid}\t{rel}\n")
                total_in += 1
                total_out += 1
        print(f"Finished: Read {total_in} lines, wrote {total_out} lines to {qrels_output_path}")

def transfer_corpus():
    data= load_dataset("Tevatron/browsecomp-plus-corpus",split="train" )
    output_corpus_path = 'browsecomp_plus/corpus.jsonl'
    output_dir = 'browsecomp_plus'
    os.makedirs(output_dir, exist_ok=True)
    # Iterate through data and write one json per line to output_corpus_path
    # Write to jsonl file
    with open(output_corpus_path, "w", encoding="utf-8") as f:
        for item in data:
            new_json = {}
            new_json["_id"] = item["docid"]
            new_json["text"] = item["text"]
            new_json["title"] = item.get("title", "")
            new_json['metadata']={'url': item.get('url', '')}
            # Write to file
            f.write(json.dumps(new_json, ensure_ascii=False) + "\n")

    print(f"Saved to {output_corpus_path}, total {len(data)} lines")

def transfer_queries():
    data_path = "data/browsecomp_plus_decrypted.jsonl"
    output_queries_path = "browsecomp_plus/queries.jsonl"

    output_dir = 'browsecomp_plus'
    os.makedirs(output_dir, exist_ok=True)

    ds = load_dataset("json", data_files=data_path, split="train")  # Single file can also use 'train'
    print(ds)
    with open(output_queries_path, "w", encoding="utf-8") as f:
        for item in ds:
            new_json = {}
            new_json["_id"] = item["query_id"]
            new_json["text"] = item["query"]
            new_json['metadata']={ }
            # Write to file
            f.write(json.dumps(new_json, ensure_ascii=False) + "\n")

    print(f"Saved to {output_queries_path}, total {len(ds)} lines")

if __name__ == "__main__":
    # Prepare the decrypt dataset before running the following function
    transfer_queries()
    transfer_corpus()
    transfer_qrels()