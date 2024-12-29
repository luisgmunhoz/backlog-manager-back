# fastapi_clean
## Work in progress template for fastapi projects with clean arch

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)](https://graphql.org/)
[![Typed with: pydantic](https://img.shields.io/badge/typed%20with-pydantic-BA600F.svg?style=for-the-badge)](https://docs.pydantic.dev/)
## Description

_Example Application Interface using FastAPI framework in Python 3.10_

## Installation

- Install all the project dependency using [Poetry](https://python-poetry.org/):

  ```sh
  $ poetry install
  ```

- Run the application from command prompt:

  ```sh
  $ poetry run uvicorn main:app --reload
  ```

- You can also open a shell inside virtual environment:

  ```sh
  $ poetry shell
  ```

- Open `localhost:8000/docs` for API Documentation

- Open `localhost:8000/graphql` for GraphQL Documentation

_*Note:* In case you are not able to access `poetry` from you `PATH` locations, replace all instances of `poetry` with `python3 -m poetry`._

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ poetry run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ poetry run pytest --cov-report xml --cov .
  ```

## License

&copy; MIT License
