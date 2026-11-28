def test_zz_order_totals_match():
    # injected deterministic test failure (outside the six fault modes)
    assert 1 + 1 == 3, "order total does not match line items"
