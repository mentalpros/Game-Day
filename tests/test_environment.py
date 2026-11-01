import sys

import joblib
import numpy as np
import pandas as pd
import pyarrow
import requests
import scipy
import sklearn
import xgboost
from xgboost import XGBRegressor


def test_python_version():
    assert sys.version_info[:2] == (3, 12)


def test_core_dependencies_import():
    assert np.__version__
    assert pd.__version__
    assert pyarrow.__version__
    assert scipy.__version__
    assert sklearn.__version__
    assert xgboost.__version__
    assert joblib.__version__
    assert requests.__version__


def test_parquet_round_trip(tmp_path):
    original = pd.DataFrame(
        {
            "game_id": [101, 102],
            "home_score": [28, 17],
            "away_score": [21, 24],
        }
    )

    path = tmp_path / "environment_test.parquet"
    original.to_parquet(path, index=False)
    restored = pd.read_parquet(path)

    pd.testing.assert_frame_equal(original, restored)


def test_xgboost_cpu_training():
    features = np.arange(48, dtype=float).reshape(24, 2)
    target = features[:, 0] * 0.1 + features[:, 1] * 0.2

    model = XGBRegressor(
        n_estimators=10,
        max_depth=2,
        learning_rate=0.1,
        tree_method="hist",
        n_jobs=1,
        random_state=42,
        verbosity=0,
    )

    model.fit(features, target)
    predictions = model.predict(features)

    assert predictions.shape == target.shape
    assert np.isfinite(predictions).all()
