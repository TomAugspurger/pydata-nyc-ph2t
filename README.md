# Pandas .head() to .tail()

Materials for my [PyData NYC 2017 tutorail](https://pydata.org/nyc2017/schedule/presentation/5/)

## First-Time Setup

1. [Install Miniconda for your platform](https://conda.io/miniconda.html) ([instructions](https://conda.io/docs/install/quick.html))
  + If you already have conda, you can skip this step; It's also fine to use virtualenv + pip.
  You should be able to `pip install -r requirements.txt` to get the same package versions as step 4.
  + Make sure to open a new terminal shell after installing, so that `conda` is on your path
2. Clone the repository at https://github.com/tomaugspurger/pydata-nyc-ph2t
  - `git clone https://github.com/tomaugspurger/pydata-nyc-ph2t`
  - If you don't have git installed, you can download the zip using the green "Clone or download" button, and then "Download ZIP". Note that the filename will be "pydata-nyc-ph2t-master"
3. Change into the repository
  - `cd pydata-nyc-ph2t`
4. Create the conda environment
  - `conda env create`
5. Activate the environment
  - `conda activate ph2t` if you have a new enough `conda`
  - `source activate ph2t` on Linux or MacOS
  - `activate ph2t` on Windows
6. Start the Jupyter notebook server
  - `jupyter notebook`

## Notebooks

Once your notebook server is running, (`jupyter notebook`) your browser should open up to the webpage (`http://localhost:8888` by default).
Open the notebook `notebooks/00-README.ipynb` and familiarize yourself with using notebook.

## Issue

```
conda create -n ph2t python=3.6
# activate / source activate ph2t
conda install numpy=1.13 pandas=0.21.0 matplotlib=2.1 seaborn=0.8 ipython=6.2 jupyter=1.0.0 notebook=5.2 dask=0.15.4 distributed=1.19 toolz=0.8 pandas-datareader=0.5 scikit-learn=0.19 scipy=0.19 statsmodels=0.8 pyarrow=0.7.1 -c conda-forge
pip install lifetime altair
```
