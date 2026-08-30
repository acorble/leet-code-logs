"""問題ごとの solution.py を安全に読み込むための共通設定。

problems/ 配下には同名の solution.py が多数あるため、通常の import では
モジュール名が衝突する。テストからは `solution` フィクスチャ経由で
そのテストと同じディレクトリにある solution.py を読み込む。
"""

import importlib.util
from pathlib import Path

import pytest


def _load(path: Path):
    module_name = "sol__" + path.parent.name.replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def solution(request):
    """テストファイルと同じディレクトリの solution.py モジュールを返す。"""
    path = Path(request.path).with_name("solution.py")
    if not path.exists():
        pytest.fail(f"solution.py が見つかりません: {path}")
    return _load(path)
