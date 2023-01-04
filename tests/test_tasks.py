from prefect import flow

from prefect_for_testing.tasks import (
    goodbye_prefect_for_testing,
    hello_prefect_for_testing,
)


def test_hello_prefect_for_testing():
    @flow
    def test_flow():
        return hello_prefect_for_testing()

    result = test_flow()
    assert result == "Hello, prefect-for-testing!"


def goodbye_hello_prefect_for_testing():
    @flow
    def test_flow():
        return goodbye_prefect_for_testing()

    result = test_flow()
    assert result == "Goodbye, prefect-for-testing!"
