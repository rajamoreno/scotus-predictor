# scotus-predictor
Yale CPSC 477 group project to fine-tune open-source LLMs to predict SCOTUS decisions.

### SYSTEM SETUP:

Run all .ipynb files on Google Colaboratory. Connect to an A100 to run llama-2-finetune.ipynb in a reasonable amount of time. Lines that must be changed to reflect the file structure of your personal Google Drive are commented.

### REQUIREMENTS:

```
datasets==2.19.1
matplotlib==3.7.1
numpy==1.25.2
pandas==2.0.3
peft==0.10.0
protobuf==3.20.3
scikit_learn==1.2.2
torch==2.2.1+cu121
tqdm==4.66.4
transformers==4.40.1
trl==0.8.6
```
