from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestRepoDemoMode(unittest.TestCase):
    def test_problem_statement_present(self) -> None:
        content = (REPO_ROOT / "03-problem-statement.txt").read_text(encoding="utf-8")
        self.assertIn("Top 3 pain points", content)

    def test_scripts_are_strict_bash(self) -> None:
        for script in ("backup.sh", "restore.sh", "check_replication.sh"):
            content = (REPO_ROOT / "scripts" / script).read_text(encoding="utf-8")
            self.assertTrue(content.startswith("#!/usr/bin/env bash\n"))
            self.assertIn("set -euo pipefail", content)

    def test_readme_mentions_test_modes_and_license(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Test modes (demo vs production)", readme)
        self.assertIn("## License", readme)

    def test_notice_present(self) -> None:
        notice = (REPO_ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("CloudForgeLabs", notice)
        self.assertIn("Freddy D. Alvarez", notice)

    def test_license_is_noncommercial(self) -> None:
        license_text = (REPO_ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Noncommercial", license_text)
        self.assertIn("Commercial use requires paid permission", license_text)

    def test_no_company_or_role_markers_in_readme(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        forbidden = [
            r"greenhouse\\.io",
        ]
        for pattern in forbidden:
            self.assertIsNone(re.search(pattern, readme, flags=re.IGNORECASE))

