# Skin-lesion-classification-system

&emsp;Model's weights could be found [here](https://drive.google.com/file/d/1IYW-JIUpaeHSFyKAyB-oVjBFxCEurwUW/view?usp=sharing). A private data set (~5500) of images obtained by the RDS-2 dermatoscope exclusively for MEPhI was used to train the classifier, a small subset of [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) images was used to increase number of rare classes and solve class imbalance.<br>

## System Purpose

This system is designed to classify common skin lesions based on images obtained using [RDS-2](https://biophotonica.ru) technology. It enables high-accuracy identification of lesion types, aiding in early diagnosis and planning further actions.

Specifically, the system is capable of classifying the following lesion types:

**Benign:**

*   **Seborrheic keratosis:**  Recall > 0.85
*   **Nevus:** Recall > 0.85
*   **Dermatofibroma:** Recall > 0.85

**Malignant:**

*   **Melanoma:** Recall > 0.95
*   **Basal cell carcinoma:** Recall > 0.95

__Important Note:__ This system is a decision support tool and does not replace consultation with a qualified medical professional.
## Web Interface
&emsp; Interaction with the system can be carried out via the web interface created with [FastAPI](https://fastapi.tiangolo.com):<br>
<img src="data\front.jpg" alt="Demonstration" width="100%"><br>


## Project Structure

*   **`data`**:  This directory contains data-related files.
    *   `datasets/`: **MISSING FROM REPO.** Training and validation datasets.
    *   `test_image.jpg`: A sample melanoma image (RDS-2) taken from [here](https://biophotonica.ru/?q=rss.xml).

*   **`src`**: This directory contains the source code for the project.
    *   `web_api/`:  Contains the code for a web service that likely serves the trained model.
        *   `static/`: Holds static assets like CSS, JavaScript, and images for the web interface.
        *   `templates/`: Contains HTML templates for the web interface.
        *   `main.py`: Entry point of the web service.
        *   `router.py`: Defines the API routes and handles requests.
        *   `weights.pt`: The trained weights for the EfficientNet-B4 model. Weights could be taken from [here](https://drive.google.com/file/d/1IYW-JIUpaeHSFyKAyB-oVjBFxCEurwUW/view?usp=sharing).
    *   `config.py`:  Parses the `database.ini` file to load configuration settings.
    *   `data_preparation.py`:  Contains functions to parse, preprocess, and prepare the dataset for training and prediction.
    *   `database.ini`: **MISSING FROM REPO.** Configuration file containing database settings.
    *   `database.py`: Contains functions for interacting with the database.
    *   `h_opt.py`:  Implements hyperparameter optimization using [Optuna](https://optuna.org).
    *   `models.py`:  Defines the machine learning models used in the project.  The final pipeline uses EfficientNet-B4.
    *   `prediction.py`: Contains functions for making predictions using the trained model.
    *   `processing.py`:  Includes code related to lesion localization in the dermoscopic images.
    *   `training.py`: Contains the training loop and related functions for training the model using PyTorch.

## Installation via PIP
&emsp;Pull repo and run **pip install -r requirements.txt**<br>
&emsp;Python version: 3.9

## Run using Uvicorn
&emsp; Run **uvicorn src.web_api.main:app**<br>
&emsp; Default port: 8000<br>

## Installation

To install the project, use PIP and Python 3.9.

1.  **Clone the Repository:** Obtain the project code using Git.

2.  **Install Dependencies:**  Navigate to the project directory and execute the following command:

    ```bash
    pip install -r requirements.txt
    ```


**Important for Windows Users (Torch CUDA):** If your system is Windows and you intend to use Torch with CUDA support, you might need to perform additional installation steps according to the official PyTorch documentation. Refer to the [PyTorch website](https://pytorch.org/get-started/locally/) for detailed instructions. This typically involves installing the correct CUDA toolkit and cuDNN versions compatible with your graphics card and PyTorch version.
## Running the Application

To run the web server, use Uvicorn.

1.  **Start the Server:** Execute the following command in the project's root directory:

    ```bash
    uvicorn src.web_api.main:app
    ```

    *   `src.web_api.main:app` specifies the entry point to your Uvicorn application (the `main` module within the `src/web_api` directory and the `app` variable that contains the ASGI application instance).
    
2.  **Default Port:** The server will run on port **8000**.  You can access your application by opening `http://localhost:8000` in your browser.
