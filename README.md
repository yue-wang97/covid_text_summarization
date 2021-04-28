This code is for the project **Text Summarization on COVID-19 Research Publications using  BertSum and BART**

# BertSum

You can find the detail instruction of running **BertSum** code in the file: `bertsum/README_bertsum`,

We use these commands for **training** and **evaluating** model:

`python src/train.py -mode train -encoder transformer -dropout 0.1 -bert_data_path bert_data/ -model_path models/bert_transformer/ -lr 2e-3 -visible_gpus 0  -gpu_ranks 0 -world_size 1 -report_every 100 -save_checkpoint_steps 1000 -batch_size 1000 -decay_method noam -train_steps 50000 -accum_count 2 -log_file logs/bert_transformer -use_interval true -warmup_steps 10000 -ff_size 2048 -inter_layers 2 -heads 8 -temp_dir temp/`



# Bart

the detail instruction of running **Bart** code in the file: `bertsum/README_bart`

We use these commands for **training** model:

`UDA_VISIBLE_DEVICES=1 fairseq-train covid_dm-bin --restore-file ../../fairseq/fairseq/models/bart/ --max-tokens 1024 --batch-size 1000 --task translation --source-lang source --target-lang target --truncate-source --layernorm-embedding --share-all-embeddings --share-decoder-input-output-embed --reset-optimizer --reset-dataloader --reset-meters --required-batch-size-multiple 1 --arch bart_large --criterion label_smoothed_cross_entropy --label-smoothing 0.1 --dropout 0.1 --attention-dropout 0.1 --weight-decay 0.01 --optimizer adam --adam-betas "(0.9, 0.999)" --adam-eps 1e-08 --clip-norm 0.1 --lr-scheduler polynomial_decay --lr 3e-05 --total-num-update 50000 --warmup-updates 10000 --update-freq 2 --num-workers 0  --save-dir checkpoin_test --log-format simple --patience 2 --memory-efficient-fp16 --skip-invalid-size-inputs-valid-test --find-unused-parameters --save-interval-updates 1000`



and use these commands for **evaluating** model:

`python infer.py`