'''
The raw data comes from

MSMARCO_BM25="msmarco_bm25_official.zip"
if [ ! -e data/$MSMARCO_BM25 ]; then
  wget -O data/${MSMARCO_BM25} https://huggingface.co/datasets/intfloat/simlm-msmarco/resolve/main/${MSMARCO_BM25}
  unzip data/${MSMARCO_BM25} -d data/
fi

we only need to transfer qrels and queries of TREC DL 2019 and 2020
'''

import os
qrels_path =r'msmarco_bm25_official\trec_dl2020_qrels.txt'
# Read the file and convert qrels to test.tsv

output_path =r'trec_dl20\qrels\test.tsv'
# Ensure the output directory exists

os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Convert the file

try:
    with open(qrels_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        # Write file header

        outfile.write("query-id\tcorpus-id\tscore\n")

        # Iterate through each line in the input file
        for line in infile:
            parts = line.strip().split("\t")
            if len(parts) == 4:
                query_id, _, corpus_id, score = parts  # Ignore the middle "Q0" field
                # Write to the target file
                outfile.write(f"{query_id}\t{corpus_id}\t{score}\n")
            else:
                print(f"Skipped line with incorrect format: {line.strip()}")

    print(f"Conversion complete! The output file has been saved to: {output_path}")
except Exception as e:
    print(f"Error occurred while processing the file: {e}")

import json
queries_path =r'msmarco_bm25_official\trec_dl2020_queries.tsv'
output_path =r'trec_dl20\queries.jsonl'
# Convert the queries in TSV format to JSON

# Ensure the output directory path exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Convert the file
try:
    with open(queries_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            parts = line.strip().split("\t")
            if len(parts) == 2:  # Ensure there are both query-id and text parts
                query_id, text = parts
                # Construct a JSON object
                json_obj = {
                    "_id": query_id,
                    "text": text,
                    "metadata": {}  # Leave the metadata field empty in the target file
                }
                # Write JSON line
                outfile.write(json.dumps(json_obj, ensure_ascii=False) + "\n")
            else:
                print(f"Skipped line with incorrect format: {line.strip()}")

    print(f"Conversion complete! The output file has been saved to: {output_path}")
except Exception as e:
    print(f"Error occurred while processing the file: {e}")