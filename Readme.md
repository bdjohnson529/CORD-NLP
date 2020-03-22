# CORD-NLP
NLP library for understanding the CORD-19 dataset


CORD-19 is a resource of over 44,000 scholarly articles, including over 29,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses. <a href="https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge">[1] COVID-19 Open Research Dataset Challenge</a>

Mining this literature is of great interest to any scientist interested in studying COVID-19.


## Dataset Composition

1. 9,118 articles licensed for commercial use
2. 2,353 articles licensed for non-commercial use
3. 16,959 articles with custom licenses
4. 885 pre-print articles


# Setup

We will be using <a href="https://github.com/deepset-ai/haystack">Haystack</a> for question answering and NLP search functionality. The setup was tested on Windows x64 bit.


## Haystack Installation

- Clone and/or fork the <a href="https://github.com/deepset-ai/haystack">Haystack repository</a>. 
- Launch an Anaconda prompt as an administrator. Navigate to the root of Haystack directory.
- Run the following commands

`conda install pytorch torchvision cpuonly -c pytorch
pip install seqeval sklearn boto3 sqlparse gitpython simplejson
pip install -r requirements.txt
pip install -e .`

To test your installation, try running one of the Haystack tutorial notebooks.