import torch
from fairseq.models.bart import BARTModel

bart = BARTModel.from_pretrained('checkpoin_test/',checkpoint_file='checkpoint_best.pt',data_name_or_path='covid_dm-bin/')
#bart = torch.hub.load(source='local',path='covid_checkpoints/checkpoint_best.pt',model='checkpoint_best.pt')
print('loaded model')
bart.cuda()
bart.eval()
bart.half()
count = 1
bsz = 8
with open('covid_dm/test.source') as source, open('covid_dm/test.hypo', 'w') as fout:
    sline = source.readline().strip()
    slines = [sline]
    for sline in source:
        if count % bsz == 0:
            with torch.no_grad():
                hypotheses_batch = bart.sample(slines, beam=4, lenpen=2.0, max_len_b=140, min_len=55, no_repeat_ngram_size=3)

            for hypothesis in hypotheses_batch:
                fout.write(hypothesis + '\n')
                fout.flush()
            slines = []

        slines.append(sline.strip())
        count += 1
        print(count)

    if slines != []:
        hypotheses_batch = bart.sample(slines, beam=4, lenpen=2.0, max_len_b=140, min_len=55, no_repeat_ngram_size=3)
        for hypothesis in hypotheses_batch:
            fout.write(hypothesis + '\n')
            fout.flush()
