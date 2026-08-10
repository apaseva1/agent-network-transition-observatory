from observatory.evaluation import transfer_retention


def test_transfer_retention_is_undefined_for_weak_source_uplift():
    assert transfer_retention(0.805, 0.800, 0.82, 0.80) is None


def test_transfer_retention_reports_fraction_of_source_uplift():
    value = transfer_retention(0.90, 0.80, 0.85, 0.80)
    assert value is not None
    assert abs(value - 0.5) < 1e-12


def test_transfer_retention_is_undefined_for_negative_source_uplift():
    assert transfer_retention(0.78, 0.80, 0.85, 0.80) is None
