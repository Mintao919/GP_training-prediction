import pandas as pd
import numpy as np
from romcomma.base.definitions import *
from romcomma import gpr, run, data
from romcomma.test.utilities import repo_folder
from romcomma.test.utilities import sample
from romcomma.data.storage import Fold
import scipy.stats
FOLDER = Path('C:\\mRNA-vaccine-process-modelling')
if __name__ == '__main__':
      model = 'Train_data_set'
      full_name = 'mRNA_GP' + '.i' + '.a'
      repo = data.storage.Repository(FOLDER / model)
      for k in repo.folds:
           GP_fold = Fold(repo, k)
           gp = gpr.models.GP(full_name, fold = GP_fold, is_read=True, is_independent = True, is_isotropic=False)
           Test_data_set = pd.read_csv(FOLDER / 'Test_data_set.csv', header=[0, 1], index_col=0) # generate inside codes
           prediction = Test_data_set.loc[:, ['Output']].copy().rename(columns={'Output': 'Prediction'}, level=0)
           X1 = GP_fold.normalization.apply_to(Test_data_set)
           predictive = gp.predict(X1.Input.values)
           X1.Output = predictive[0]
           prediction.iloc[:] = GP_fold.normalization.undo_from(X1).Output.values
           Test_data_set  = Test_data_set.join([prediction])
           Test_data_set.to_csv(GP_fold.folder / "Ioni_prediction.csv")

