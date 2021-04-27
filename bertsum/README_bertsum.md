# BertSum

**Python version**: This code is in Python3.6

**Package Requirements**: Under our python viturual environment: `data_preprocess/bertsumenv`

The codes of model implement are borrowed from https://github.com/nlpyang/BertSum and based on our dataset, we did some modification and saved the modified version in the `model` folder.

## Data Preparation For Covid-19 Open Research Dataset

### Option 1: download the processed data

We saved our data preprocessed by data.ipynb [here](https://drive.google.com/file/d/1wbPoNki2iMizBr4w37KrRZCaj0dIyZUS/view), it can be used in the **BertSum** model directly.

unzip the zipfile and save all files in **bertsum_data** folder



### Option 2: process the data yourself

You can use `data_preprocess/data.ipynb` to process by yourself

#### Step 1 Download data 

Since we wanted to do comparation between BertSum and BART, the **training, test, evaluation** dataset have to keep exactly same for both models. So we use the data that was processed and spited in the **Bart** model part, and transfer the format into `.story` format. 

You can download the data that was processed in Bart model [here](https://drive.google.com/file/d/1wbPoNki2iMizBr4w37KrRZCaj0dIyZUS/view)

#### Step 2 process into .story files

**run** data.ipynb cell by cell

The corresponding json are read from file and written to text files `.story`

The output is now suitable for feeding to the Data Preparation For CNN/Dailymail step/Option 2/step 2 of BertSum

## Model training and evaluation

We follow the same steps in https://github.com/nlpyang/BertSum

In order to fit our dataset, we modify some code based on [BertSum](https://github.com/nlpyang/BertSum) saved the modified version in the `model` folder.



