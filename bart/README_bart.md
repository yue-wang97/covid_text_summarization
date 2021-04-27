# Bart

**Python version**: This code is in Python3.6

**Package Requirements**: Under our python viturual environment: `data_preprocess/bartenv`

The codes of model implement are borrowed from fairest (https://github.com/pytorch/fairseq/tree/master/examples/bart) and based on our dataset, we did some modification in **infer.py** file and saved the modified version in the `model` folder.

## Data Preparation For Covid-19 Open Research Dataset

### Option 1: download the processed data

We saved our data preprocessed by data.ipynb [here](https://drive.google.com/file/d/1wbPoNki2iMizBr4w37KrRZCaj0dIyZUS/view), it can be used in the **BART** model directly.

unzip the zipfile and save all files in **bart_data** folder



### Option 2: process the data yourself

You can use `data_preprocess/data.ipynb` to process by yourself

#### Step 1 Download data

Download and unzip the archive dictionay from [here](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) for all Covid-19 Open Research Dataset.

#### Step 2 Clean the data and process into .source and .target files

**change the path**: replacing `./archive/metadata.csv ` in the line`original_data_path = './archive/metadata.csv'` with the path to where you saved the `archive/metadata.csv` directory that you downloaded; similar for `path_to_json`

**run** data.ipynb cell by cell

The corresponding json are read from file and written to text files `train.source`, `train.target`, `val.source`, `val.target`, and `test.source` and `test.target`.

The output is now suitable for feeding to the BPE preprocessing step of BART fine-tuning.

Reference: https://github.com/artmatsak/cnn-dailymail

## Model training and evaluation

We follow the same steps in https://github.com/pytorch/fairseq/tree/master/examples/bart

In order to fit our dataset, we modify the **infer.py** file in the original [Bart](https://github.com/pytorch/fairseq/tree/master/examples/bart) code



