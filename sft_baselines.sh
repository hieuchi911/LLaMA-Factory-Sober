export WANDB_API_KEY="8b07b9ebb0f0b08e31878929ec6324fdc098f376"
export WANDB_PROJECT="i_am_sober"

python jsonl_to_json.py

FORCE_TORCHRUN=1 llamafactory-cli train examples/train_full/llama3_full_sft_ds3_baselines.yaml