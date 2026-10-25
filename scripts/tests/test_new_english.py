"""new_english.py (英語で話した記録の雛形) のテスト。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _review  # noqa: E402
import new_english  # noqa: E402

TEMPLATE = (new_english.TEMPLATES / "README.md").read_text(encoding="utf-8")


def make_readme(tmp_path, text):
    readme = tmp_path / "README.md"
    readme.write_text(text, encoding="utf-8")
    return readme


def new_template(tmp_path):
    fields = dict(number="84", title="T", url="u", difficulty="hard", category="stack", date="2026-10-30", recall="△")
    return make_readme(tmp_path, TEMPLATE.format(**fields))


def test_links_go_under_the_heading_in_order(tmp_path):
    readme = new_template(tmp_path)
    new_english.add_link(readme, "- 2026-10-30 mock: [a](a)")
    new_english.add_link(readme, "- 2026-11-02 一人練習: [b](b)")
    text = readme.read_text(encoding="utf-8")
    section = text[text.index("## 英語での説明") : text.index("## 問題の要約")]
    assert section.endswith("-->\n\n- 2026-10-30 mock: [a](a)\n- 2026-11-02 一人練習: [b](b)\n\n")


def test_old_readme_gets_the_section_before_summary(tmp_path):
    readme = make_readme(tmp_path, "# 84. T\n\n## 次回やること\n\n- [ ] x\n\n## 問題の要約\n\n要約\n")
    new_english.add_link(readme, "- 2026-10-30 一人練習: [b](b)")
    text = readme.read_text(encoding="utf-8")
    assert "- [ ] x\n\n## 英語での説明\n\n- 2026-10-30 一人練習: [b](b)\n\n## 問題の要約" in text
    # 「次回やること」の読み取りに影響しない
    assert _review.parse_next_steps(text) == ["x"]


def test_mock_link_goes_to_todays_attempt_only(tmp_path):
    readme = new_template(tmp_path)
    assert new_english.link_attempt(readme, "2026-10-30", "[mock 記録](english/2026-10-30-mock.md)")
    assert "| [solution.py](solution.py) | [mock 記録](english/2026-10-30-mock.md) |" in readme.read_text(
        encoding="utf-8"
    )
    assert not new_english.link_attempt(readme, "2026-11-05", "[mock 記録](x)")


def test_same_day_records_are_numbered(tmp_path):
    first = new_english.record_path(tmp_path, "2026-10-30", "solo")
    first.write_text("", encoding="utf-8")
    assert new_english.record_path(tmp_path, "2026-10-30", "solo").name == "2026-10-30-solo-2.md"
    assert new_english.record_path(tmp_path, "2026-10-30", "mock").name == "2026-10-30-mock.md"
