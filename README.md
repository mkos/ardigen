# Ardigen, ML Task app

irst, install the required packages (I am using python 3.6.8)
```
$ pip install -r requirements.txt
```

Then run:

```
$ python predict.py --hellpl
```

to get help on options.

Run:
```
$ python predict.py X_covariates_test.tsv X_genes_test.tsv predictions.tsv
```
to get predictions written to a file.

> **Note**: this app could use more error handling, but it is what it is and does it's job.