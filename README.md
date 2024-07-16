# TOQIO

This project has been done with the intention of creating an end-to-end automated test suite for a technical test for TOQIO.

## Before starting

You need to have Docker installed to be able to run the tests on your premises without having to install anything else separately.

Here is the documentation to install docker: [Install Docker](https://docs.docker.com/engine/install/)

## Usage

You have 2 ways to execute the project tests.

### Docker

To run the tests using Docker you can use the following commands:

```
docker-compose run app pytest ./tests/{{FILE_NAME}}.py
```

Example:

```
docker-compose run app pytest ./tests/test_home.py  

```

If you make changes to files and need to apply them, you should use the following command to apply them before running the tests again:

```
docker-compose build
```

### Pytest

To run the tests without Docker you will need to install the necessary dependencies first using the following command:

```
pip install -r requirements.txt
```

After that you should be able to use this command to run the tests (while being in the "tests" directory):

```
Example:

pytest -v -s -rA {{FILE_NAME}}.py # To run a specific test script


If you wish to run all the test scripts toghether, use the above command without specifing the file.
```

### Reports

The creation of a HTML report is automated in the code and, after each run, it updates in the "reports" directory.

The HTML report displays the console output and logging for debugging and a screnshot of the browser at the moment of the failure.
