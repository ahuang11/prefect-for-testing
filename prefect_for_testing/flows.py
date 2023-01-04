"""This is an example flows module"""
from prefect import flow

from prefect_for_testing.blocks import FortestingBlock
from prefect_for_testing.tasks import (
    goodbye_prefect_for_testing,
    hello_prefect_for_testing,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    FortestingBlock.seed_value_for_example()
    block = FortestingBlock.load("sample-block")

    print(hello_prefect_for_testing())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_for_testing())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
