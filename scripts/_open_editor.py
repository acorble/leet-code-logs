"""問題の README をエディタで開くための小さなヘルパー。

VS Code の CLI が PATH に無い環境もあるので、次の順に試す:
  1. PATH 上の `code`
  2. VS Code アプリに同梱されている `code`
  3. macOS の `open`（既定のアプリで開く）
"""

import shutil
import subprocess
import sys
from pathlib import Path

VSCODE_BUNDLED = Path("/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code")


def _command(path: Path) -> list | None:
    binary = shutil.which("code") or shutil.which("cursor")
    if binary:
        return [binary, str(path)]
    if VSCODE_BUNDLED.exists():
        return [str(VSCODE_BUNDLED), str(path)]
    if shutil.which("open"):
        return ["open", str(path)]
    return None


def open_in_editor(path: Path) -> None:
    """開けなくても処理は止めない（記録が本体で、これはおまけ）。"""
    command = _command(path)
    if not command:
        print(f"  (エディタが見つからないので開けませんでした: {path})", file=sys.stderr)
        return
    try:
        subprocess.run(command, check=True, capture_output=True)
        print(f"  README を開きました: {path.name}")
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"  (README を開けませんでした: {e})", file=sys.stderr)
