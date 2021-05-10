from . import Days


def test_all_days():
    assert Days.ALL == (Days.MONDAY |
                        Days.TUESDAY |
                        Days.WEDNESDAY |
                        Days.THURSDAY |
                        Days.FRIDAY |
                        Days.SATURDAY |
                        Days.SUNDAY)


def test_weekend_days():
    assert Days.WEEKEND_DAYS == (Days.SATURDAY | Days.SUNDAY)


def test_week_days():
    assert Days.WEEK_DAYS == (Days.MONDAY |
                              Days.TUESDAY |
                              Days.WEDNESDAY |
                              Days.THURSDAY |
                              Days.FRIDAY)
