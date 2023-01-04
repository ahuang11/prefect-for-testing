# prefect-for-testing

Visit the full docs [here](https://ahuang11.github.io/prefect-for-testing) to see additional examples and the API reference.

<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-for-testing/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-for-testing?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/ahuang11/prefect-for-testing/" alt="Stars">
        <img src="https://img.shields.io/github/stars/ahuang11/prefect-for-testing?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-for-testing/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-for-testing?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/ahuang11/prefect-for-testing/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/ahuang11/prefect-for-testing?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>


## Welcome!

My personal sandbox for testing!

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@desertaxle/Python#main.py?embed=true"></iframe>
<iframe src="https://pythonsandbox.dev/embed/jlxcrlibf975?file=main.py" width="800px" height="547px" allow="clipboard-read; clipboard-write" ></iframe>

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-for-testing` with `pip`:

```bash
pip install prefect-for-testing
```

A list of available blocks in `prefect-for-testing` and their setup instructions can be found [here](https://ahuang11.github.io/prefect-for-testing/#blocks-catalog).

### Write and run a flow

```python
from prefect import flow
from prefect_for_testing.tasks import (
    goodbye_prefect_for_testing,
    hello_prefect_for_testing,
)

# Use `with_options` to customize options on any existing task or flow

custom_goodbye_prefect_for_testing = goodbye_prefect_for_testing.with_options(
    name="My custom task name",
    retries=2,
    retry_delay_seconds=10,
)

@flow
def example_flow():
    hello_prefect_for_testing
    custom_goodbye_prefect_for_testing

example_flow()
```

For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://orion-docs.prefect.io/collections/usage/)!

## Resources

If you encounter any bugs while using `prefect-for-testing`, feel free to open an issue in the [prefect-for-testing](https://github.com/ahuang11/prefect-for-testing) repository.

If you have any questions or issues while using `prefect-for-testing`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`prefect-for-testing`](https://github.com/ahuang11/prefect-for-testing) for updates too!

## Contributing

If you'd like to help contribute to fix an issue or add a feature to `prefect-for-testing`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:
1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/ahuang11/prefect-for-testing/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request
