# Skin-lesion-classification-system

&emsp;Model's weights could be found [here](https://drive.google.com/file/d/1IYW-JIUpaeHSFyKAyB-oVjBFxCEurwUW/view?usp=sharing). A private data set (~5500) of images obtained by the RDS-2 dermatoscope exclusively for MEPhI was used to train the classifier, a small subset of [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) images was used to increase number of rare classes and solve class imbalance. A small subset of private data was used for validation.<br>
## System's Purpose
&emsp;The system can be used to classify common skin lesions using [RDS-2](https://biophotonica.ru) images:<br>
1. Seborrheic keratosis (recall > 0.85)
2. Nevus (recall > 0.85)
3. Dermatofibroma (recall > 0.85)
4. **Melanoma** (recall > 0.95)
5. **Basal cell carcinoma** (recall > 0.95)

## GUI (FastAPI)
&emsp; Interaction with the system can be carried out via the web interface:<br>
<img src="data\front.jpg" alt="Demonstration" width="90%"><br>

## Project's structure
data<br />
&emsp;├── datasets&emsp;&emsp;&emsp;&emsp;&emsp;# **MISSING FROM THE REPOSITORY**<br/>
&emsp;└── test_image.jpg&emsp;&emsp;&emsp;# Melanoma image of the RDS-2 dermatoscope taken from [here](https://biophotonica.ru/?q=rss.xml)<br/>
src<br />
&emsp;└── web_api&emsp;&emsp;&emsp;&emsp;# Service realization<br />
&emsp;&emsp;├── static/<br />
&emsp;&emsp;├── templates/<br />
&emsp;&emsp;├── main.py<br />
&emsp;&emsp;├── router.py<br />
&emsp;&emsp;└── weights.pt&emsp;&emsp;&emsp;#Could be taken [here](https://drive.google.com/file/d/1IYW-JIUpaeHSFyKAyB-oVjBFxCEurwUW/view?usp=sharing)<br />
&emsp;├── config.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#Parses database.ini<br/>
&emsp;├── data_preparation.py&emsp;&emsp;#Functions used for datasets parsing and preparation<br/>
&emsp;├── database.ini&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#**MISSING FROM THE REPOSITORY**<br/>
&emsp;├── database.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#DB functions<br/>
&emsp;├── h_opt.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;#Hyperparameters optimization using [Optuna](https://optuna.org)<br/>
&emsp;├── models.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# In the final pipeline EfficientNet-B4 is used <br />
&emsp;├── prediction.py&emsp;&emsp;&emsp;&emsp;&emsp;# Functions for prediction<br />
&emsp;├── processing&emsp;&emsp;&emsp;&emsp;&emsp;#**Lesion localization code**<br />
&emsp;└── training.py&emsp;&emsp;&emsp;&emsp;&emsp;#Training using PyTorch

## Installation via PIP
&emsp;Pull repo and run **pip install -r requirements.txt**<br>
&emsp;Python version: 3.9

## Run using Uvicorn
&emsp; Run **uvicorn src.web_api.main:app**<br>
&emsp; Default port: 8000<br>
