import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='prediksicovidjatim',  
    version='0.15',
    author="Prediksi Covid Jatim",
    author_email="prediksicovidjatim@gmail.com",
    description="Core library of prediksicovidjatim",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prediksicovidjatim/prediksicovidjatim-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests-html",
        #"arcgis",
        "numpy",
        "matplotlib",
        #"mpld3",
        #"scipy",
        "psycopg2-binary",
        #"psycopg2",
        "dj-database-url",
        "python-dotenv",
        #"scikit-learn",
        #"numdifftools",
        #"statsmodels",
        #"scipy @ git+https://github.com/R-N/scipy_lite.git#egg=scipy",
        "sklearn @ git+https://github.com/R-N/sklearn_lite.git#egg=sklearn",
        "statsmodels @ git+https://github.com/R-N/statsmodels_lite.git#egg=statsmodels",
        #"arcgis @ git+https://github.com/R-N/arcgis-python-api.git#egg=arcgis",
        "lmfit @ git+https://github.com/R-N/lmfit-py.git#egg=lmfit",
    ],
)