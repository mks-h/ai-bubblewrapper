#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import override
import unittest


ROOT = Path(__file__).resolve().parent
ESCAPES = sorted((ROOT / "escapes").glob("*.py"))
RUN_DIR = ROOT / ".test-run"
MARK_DIR = ROOT / ".test-marks"


class SandboxEscapeTest(unittest.TestCase):
    @override
    @classmethod
    def setUpClass(cls):
        for dir in (RUN_DIR, MARK_DIR):
            shutil.rmtree(dir, ignore_errors=True)
            dir.mkdir()

    @override
    @classmethod
    def tearDownClass(cls):
        for dir in (RUN_DIR, MARK_DIR):
            shutil.rmtree(dir, ignore_errors=True)

    def test_escapes_ineffective(self):
        for escape in ESCAPES:
            with self.subTest(escape=escape.name):
                target = MARK_DIR / f"{escape.stem}-{os.getpid()}"

                try:
                    _ = subprocess.run(
                        [str(ROOT / "ai-bwrap"), sys.executable,
                         str(escape), str(target)],
                        cwd=RUN_DIR,
                        check=True,
                    )
                    self.assertFalse(target.exists(), "escape was effective")
                finally:
                    pass
                    target.unlink(missing_ok=True)


class NumbersTestResult(unittest.TextTestResult):
    testsRun: int

    @override
    def addSubTest(self, test: unittest.TestCase, subtest: unittest.TestCase,
                   err):  # pyright: ignore[reportMissingParameterType]
        super(NumbersTestResult, self).addSubTest(test, subtest, err)
        self.testsRun += 1


if __name__ == "__main__":
    _ = unittest.main(testRunner=unittest.TextTestRunner(
        resultclass=NumbersTestResult))  # pyright: ignore[reportArgumentType]
