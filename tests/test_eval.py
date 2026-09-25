from ai_eval import *
import pytest
def test_exact_match(): assert exact_match([Case("1","A","a"),Case("2","B","C")])==.5
def test_gate(): RegressionGate(.8).check(.8)
def test_gate_blocks_regression():
 with pytest.raises(AssertionError):RegressionGate(.8).check(.79)
def test_empty_dataset(): assert exact_match([])==0
