<h2 align="center">Pytest+Selenium Starter Pack</h2>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> “Better to have then not to”

Planed as pet project for educational purposes in web automation. Stack of the project: `Selenium`+`Pytest`+`Allure`

---

UI automation playground selected as SUT: [Playground](http://uitestingplayground.com/home)

---

# Installation and usage

## Installation

Python 3.6+ should be installed.

1. Clone repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

## Local Usage
### Local Test Run

To get started right away with local test run and default params. Move to project dir and invoke:

```sh
pytest
```
In addition to common pytest params, you can use the following parameters to run the tests::
* --browser=[arg]. Can be `firefox/edge/chrome`. Chrome used by default
* --headless=[arg]. Can be `True/False`. False used by default
* --log_level=[arg]. Can be `DEBUG/INFO`. INFO used by default
* -n [number]. Running test in parallel. For additional information see: [Xdist](https://pypi.org/project/pytest-xdist/)
* --env. Stab at the moment.

Example of common usage:
```shell
pytest -n 3 --browser=firefox --headless=True
```

### Local Test Run in Docker container

Build new image:

```docker build -t pytest_local_chrome -f Dockerfile_chrome .```

Run container:

```docker run pytest_local_chrome [Options]```

Options for run described above.

Do not forget to mount *volume* in result export is needed `--volume allure-results:Path/To/Dir/With/Result/Storage`

NOTE: now only *chrome* installed in container


### Results
Tool for gathering and processing results of tests: `Allure`

How to install `Allure` see: [Allure](https://docs.qameta.io/allure/#_get_started)

For gathering of test results to run command should be added `--alluredir [PATH]`. For example:
```shell
pytest -n 3 --browser=firefox --headless=True --alluredir Path/To/Dir/With/Result/Storage
```

For report generation:
```shell
allure serve Path/To/Dir/With/Result/Storage
```

## Remote Test Run

TBD!
