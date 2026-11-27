import time


def test_zz_wait_for_upstream_sync():
    # injected hang: sleeps past the job's own timeout-minutes
    time.sleep(900)
