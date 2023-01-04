"""This is an example tasks module"""
from prefect import task


@task
def hello_prefect_for_testing() -> str:
    """
    Sample task that says hello!

    Returns:
        A greeting for your collection
    """
    return "Hello, prefect-for-testing!"


@task
def goodbye_prefect_for_testing() -> str:
    """
    Sample task that says goodbye!

    Returns:
        A farewell for your collection
    """
    return "Goodbye, prefect-for-testing!"
