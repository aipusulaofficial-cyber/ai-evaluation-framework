from evaluation_domain import *
def test_eval_gate():
 s=exact_match([Case("1","a","a"),Case("2","b","x")]);assert s.passed==1;assert not regression_gate(s,.9)