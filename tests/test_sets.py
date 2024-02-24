from nolib import sets

def test_sets_over_k():
    expected = [
        {2, 3, 4}, {2, 3, 5}, {2, 3, 6}, {2, 4, 5}, {2, 4, 6}, {2, 5, 6}, {3, 4, 5}, {3, 4, 6}, {3, 5, 6}, {4, 5, 6}
    ]
    actual = list(sets.sets_over_k(6, 3, 2))
    assert expected == actual
