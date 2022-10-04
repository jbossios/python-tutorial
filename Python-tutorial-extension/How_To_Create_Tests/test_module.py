from module import compute

def test_compute():
    x = -2
    assert compute(x) >= 0, f'compute({x}) < 0 but it should be positive'
