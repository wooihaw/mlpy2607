# mlpy2607

This repository contains the code and data for the Machine Learning with Python course.

> A course landing page (in [`docs/`](docs)) can be published with GitHub Pages, including a live clone/download infographic. Setup instructions are in [Create_PAT.md](Create_PAT.md).

## Setup

### 1. Install uv

`uv` is a fast Python package installer.

#### Windows

Open a PowerShell terminal and run the following command:

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatively, you can use the `winget` package manager if you have it installed:

```shell
winget install --id=astral-sh.uv -e
```

After installation, you need to restart your PowerShell session for the `uv` command to be recognized.

#### Linux

On Linux, you can install `uv` using `curl` or `wget`. Open your terminal and execute one of the following commands:

Using `curl` (most common):

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Using `wget`:

```shell
wget -qO- https://astral.sh/uv/install.sh | sh
```

After running the installation script, you need to restart your shell or source your profile file (e.g., `source ~/.bashrc` or `source ~/.zshrc`) for the `uv` command to become available in your `PATH`.

### 2. Clone the repository

Clone the repository to your local machine:

```shell
git clone https://github.com/wooihaw/mlpy2607.git
cd mlpy2607
```

#### Don't have git installed?

If you do not have `git` installed, you can download the repository as a ZIP file instead:

1. Open https://github.com/wooihaw/mlpy2607 in your web browser.
2. Click the green **Code** button, then select **Download ZIP**.
3. Extract the downloaded ZIP file to a folder of your choice.
4. Open a terminal in the extracted `mlpy2607` folder before continuing with the next step.

### 3. Restore the dependencies

Run the following command to restore the dependencies:

```shell
uv sync
```

### 4. Launch Jupyter Lab

Run the following command to launch Jupyter Lab:

```shell
uv run jupyter-lab
```

## Notebook Descriptions
| Filename | Description |
| --- | --- |
| [Getting_started.ipynb](Getting_started.ipynb) | Verify that the development environment is set up correctly by walking through the 6 stages of a machine learning workflow (predicting gender from height and weight). |
| [Python_libraries.ipynb](Python_libraries.ipynb) | Introduction to JupyterLab and a quick refresher on the core Python libraries used throughout the workshop. |
| [index.ipynb](index.ipynb) | In-notebook index of all the `ml*.py` example scripts with their descriptions. |
| [day1.ipynb](day1.ipynb) | Working notebook for running and experimenting with the Day 1 examples. |
| [day2.ipynb](day2.ipynb) | Working notebook for running and experimenting with the Day 2 examples. |
| [day3.ipynb](day3.ipynb) | Working notebook for running and experimenting with the Day 3 examples. |
| [exercise1.ipynb](exercise1.ipynb) | Exercise on encoding categorical data and imputing missing values (income dataset). |
| [exercise2.ipynb](exercise2.ipynb) | Exercise on the importance of feature scaling for distance-based algorithms such as k-NN. |
| [exercise3.ipynb](exercise3.ipynb) | Exercise building a machine learning model to predict Titanic passenger survival. |
| [handson/handson_1.ipynb](handson/handson_1.ipynb) | Hands-on classification of penguin species using the Palmer Penguin dataset. |
| [handson/handson_2.ipynb](handson/handson_2.ipynb) | Hands-on clustering to group truck drivers, using the Elbow method and silhouette score to choose the number of clusters. |
| [handson/handson_3.ipynb](handson/handson_3.ipynb) | Hands-on face recognition on the Olivetti faces dataset with PCA dimensionality reduction and a tuned classification pipeline. |

## Python Script Descriptions
| Filename | Description |
| --- | --- |
| [ml01.py](ml01.py) | Generate a synthetic binary classification dataset with make_classification. |
| [ml02.py](ml02.py) | Generate a synthetic blob-cluster dataset with make_blobs. |
| [ml03.py](ml03.py) | Load the Iris dataset and print feature and target names. |
| [ml04.py](ml04.py) | Load CDC diabetes CSV, split into features/target, and print shapes. |
| [ml05.py](ml05.py) | Print statistical summary and class distribution of the diabetes dataset. |
| [ml06.py](ml06.py) | Produce EDA plots (histogram, boxplot, scatter, correlation heatmap, density, pie) for the diabetes dataset. |
| [ml07.py](ml07.py) | Clean data: remove duplicates, coerce to numeric/NaN, drop zero-variance columns, detect and clip outliers. |
| [ml08.py](ml08.py) | Demonstrate handling missing values by replacing zeros with NaN and dropping rows. |
| [ml09.py](ml09.py) | Impute missing values with median/mean in a small example DataFrame. |
| [ml10.py](ml10.py) | Encode categorical data: ordinal mapping and one‑hot encoding for car attributes. |
| [ml11.py](ml11.py) | Apply Min‑Max scaling to height/weight features and print per‑feature min/max. |
| [ml12.py](ml12.py) | Standardize features (zero mean, unit variance) and report mean/variance. |
| [ml13.py](ml13.py) | Apply robust scaling (median=0, IQR=1) and report median/IQR. |
| [ml14.py](ml14.py) | Create new features via height binning and rolling mean of weight. |
| [ml15.py](ml15.py) | Select top features using univariate SelectKBest on the diabetes dataset. |
| [ml16.py](ml16.py) | Perform model‑based feature selection with RandomForest and SelectFromModel. |
| [ml17.py](ml17.py) | Use Recursive Feature Elimination with a Decision Tree to select features. |
| [ml18.py](ml18.py) | Train/test split evaluation using KNN classifier; report accuracy. |
| [ml19.py](ml19.py) | Stratified train/test split with KNN classifier; report accuracy. |
| [ml20.py](ml20.py) | 3‑fold cross‑validation accuracy using KNN classifier. |
| [ml21.py](ml21.py) | Linear regression on real‑estate data; report R² on the test set. |
| [ml22.py](ml22.py) | KNN regressor on real‑estate data; report R² on the test set. |
| [ml23.py](ml23.py) | Logistic regression classification on diabetes data; report accuracy. |
| [ml24.py](ml24.py) | k‑NN classification on diabetes data; report accuracy. |
| [ml25.py](ml25.py) | Gaussian Naive Bayes classification on diabetes data; report accuracy. |
| [ml26.py](ml26.py) | Support Vector Machine classification on diabetes data; report accuracy. |
| [ml27.py](ml27.py) | Decision Tree classifier; print train/test accuracy and plot the tree. |
| [ml28.py](ml28.py) | Decision Tree with pre‑pruning (max_depth=2); plot the pruned tree. |
| [ml29.py](ml29.py) | Random Forest classifier on diabetes data; report accuracy. |
| [ml30.py](ml30.py) | Gradient Boosting classifier on diabetes data; report accuracy. |
| [ml31.py](ml31.py) | Voting classifier combining Logistic Regression, GaussianNB, and SVC; report accuracy. |
| [ml32.py](ml32.py) | MLP (neural network) classifier on diabetes data; report accuracy. |
| [ml33.py](ml33.py) | Hyperparameter tuning of Decision Tree with GridSearchCV and KFold; compare accuracy before/after. |
| [ml34.py](ml34.py) | Pipeline with StandardScaler and LogisticRegression; evaluate accuracy. |
| [ml35.py](ml35.py) | GridSearchCV over pipelines varying scalers and classifiers; select best and evaluate. |
| [ml36.py](ml36.py) | KMeans elbow method: plot inertia across k=2..10 on synthetic blobs. |
| [ml37.py](ml37.py) | Visualize KMeans clustering results before and after clustering. |
| [ml38.py](ml38.py) | Visualize Gaussian Mixture Model clustering before and after clustering. |
| [ml39.py](ml39.py) | Compare KMeans vs GMM on non‑spherical clusters from CSV data. |
| [ml40.py](ml40.py) | Apply PCA to digits dataset; print shape reduction and explained variance ratio sum. |
