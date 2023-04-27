from romcomma.base.definitions import *
from romcomma import gpr, run, data
from romcomma.test.utilities import repo_folder
from romcomma.test.utilities import sample
from romcomma.data.storage import Fold

BASE_FOLDER = Path('C:\\mRNA-vaccine-process-modelling')
k = 10
name = 'model'
model = 'Test_2023.03.17'
repo = data.storage.Repository.from_csv(BASE_FOLDER / model, BASE_FOLDER / f'{model}.csv')
repo.into_K_folds(k, shuffle_before_folding=True)
run.gpr(name=name, repo=repo, is_read=None, is_independent=True, is_isotropic=False, optimize=True, test=True)





