import pytest
import sys
from unittest.mock import patch, MagicMock
from scripts.run_v1_gate import main

class MockProcess:
    def __init__(self, returncode, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

def get_mock_run(exact_code=0, numerical_code=0, integrity_code=0, others_code=0):
    def mock_run(command, capture_output=False, text=False):
        cmd = " ".join(command)
        if "--exact" in cmd:
            return MockProcess(exact_code)
        if "--numerical" in cmd:
            return MockProcess(numerical_code)
        if "--integrity" in cmd:
            return MockProcess(integrity_code)
        return MockProcess(others_code)
    return mock_run

def test_gate_truth_table_exact_pass(capsys):
    with patch("subprocess.run", side_effect=get_mock_run(exact_code=0)):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 0
        captured = capsys.readouterr().out
        assert "OVERALL STATUS: PASS" in captured
        assert "PASS_WITH_EXACT_REPRODUCTION_NOT_VERIFIED" not in captured

def test_gate_truth_table_exact_not_verified(capsys):
    with patch("subprocess.run", side_effect=get_mock_run(exact_code=2)):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 0
        captured = capsys.readouterr().out
        assert "OVERALL STATUS: PASS_WITH_EXACT_REPRODUCTION_NOT_VERIFIED" in captured

def test_gate_truth_table_exact_fail(capsys):
    with patch("subprocess.run", side_effect=get_mock_run(exact_code=1)):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1
        captured = capsys.readouterr().out
        assert "OVERALL STATUS: FAIL" in captured

def test_gate_truth_table_numerical_fail(capsys):
    with patch("subprocess.run", side_effect=get_mock_run(exact_code=2, numerical_code=1)):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1
        captured = capsys.readouterr().out
        assert "OVERALL STATUS: FAIL" in captured

def test_gate_truth_table_integrity_fail(capsys):
    with patch("subprocess.run", side_effect=get_mock_run(exact_code=2, integrity_code=1)):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1
        captured = capsys.readouterr().out
        assert "OVERALL STATUS: FAIL" in captured