import pandas as pd
import joblib
import fire
import os.path

NUM_COLUMNS = 31102
MODEL_PATH = 'ardigen_final_model.joblib'

def predict(covariates_path, genes_path, output_path=None):

    # load data
    assert os.path.exists(covariates_path), "Covariates file does not exist"
    assert os.path.exists(genes_path), "Genes file does not exist"
    X_covariates = pd.read_table(covariates_path)
    X_genes = pd.read_table(genes_path)
    X = pd.concat((X_covariates, X_genes), axis=1)
    assert X.shape[1] == NUM_COLUMNS, "Improper shape of input file(s)."

    # load model
    clf = joblib.load(MODEL_PATH)

    # predict
    preds = clf.predict_proba(X)
    response_class_index = clf.classes_.tolist().index(1)
    response_probas = preds[:, response_class_index]

    # write output
    print(response_probas)

    if output_path is not None:
        response_probas.tofile(output_path, sep='\n')
        print("Written output to: \'{}\'".format(output_path))


if __name__ == '__main__':
    fire.Fire(predict)