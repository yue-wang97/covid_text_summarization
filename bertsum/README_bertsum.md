# BertSum

**Python version**: This code is in Python3.6

**Package Requirements**: Under our python viturual environment: `data_preprocess/bertsumenv`

The codes of model implement are borrowed from https://github.com/nlpyang/BertSum and based on our dataset, but we did some modification in **infer.py** file and saved the modified version in the `model/data_builder.py` file.

## Data Preparation For Covid-19 Open Research Dataset

### Option 1: download the processed data

We saved our data preprocessed by data.ipynb [here](https://drive.google.com/file/d/1wbPoNki2iMizBr4w37KrRZCaj0dIyZUS/view), unzip the zipfile and download files in **bertsum_data** folder and save the files in one folder. I will call this folder `bertsum_data` in the following steps.

it can be used for feeding to the Data Preparation For `CNN/Dailymail step/Option 2/step 2 of BertSum`



### Option 2: process the data yourself

You can use `data_preprocess/data.ipynb` to process by yourself

#### Step 1 Download data 

Since we wanted to do comparation between BertSum and BART, the **training, test, evaluation** dataset have to keep exactly same for both models. So we use the data that was processed and spited in the **Bart** model part, and transfer the format into `.story` format. 

You can download the data that was processed in Bart model [here](https://drive.google.com/file/d/1wbPoNki2iMizBr4w37KrRZCaj0dIyZUS/view)

#### Step 2 process into .story files

**run** data.ipynb cell by cell

The corresponding json are read from file and written to text files `.story`

Save the files in one folder. I will call this folder `bertsum_data` in the following steps.

The output is now suitable for feeding to the Data Preparation For `CNN/Dailymail step/Option 2/step 2 of BertSum`

## Model training and evaluation

First you should download the code from [BertSum](https://github.com/nlpyang/BertSum) and replace the original `data_builder.py` file with our `model/data_builder.py` file

We follow the same steps in [steps](https://github.com/nlpyang/BertSum) and did the following modification:

- In **Step 3. Sentence Splitting and Tokenization**:

  - Run `python preprocess.py -mode tokenize -raw_path RAW_PATH -save_path TOKENIZED_PATH` 3 times specifically on `bertsum_data/train/`, `bertsum_data/test/`, `bertsum_data/val/`and save the generated files in `../merged_stories_tokenized/train_data/`, `../merged_stories_tokenized/test_data/`, `../merged_stories_tokenized/val_data/`specifically.

  - `RAW_PATH` is the directory containing story files ( `bertsum_data/train/`, `bertsum_data/test/`, `bertsum_data/val/`) `JSON_PATH` is the target directory to save the generated json files ( `../merged_stories_tokenized/train_data/`, `../merged_stories_tokenized/test_data/`, `../merged_stories_tokenized/val_data/`)

- In **Step 4. Format to Simpler Json Files**:

  - Run `python preprocess.py -mode format_to_lines -raw_path RAW_PATH -save_path JSON_PATH -map_path MAP_PATH -lower` three times specifically on ``../merged_stories_tokenized/train_data/`, `../merged_stories_tokenized/test_data/`, `../merged_stories_tokenized/val_data/`
  - Make sure the `RAW_PATH` is the directory containing tokenized files (``../merged_stories_tokenized/train_data/`, `../merged_stories_tokenized/test_data/`, `../merged_stories_tokenized/val_data/`)

- For the rest, just follow the same steps.
