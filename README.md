
# REST API TESTING

# API Testing Framework

This is a Python-based API testing framework for testing RESTful APIs. It provides a structure for organizing test cases, managing configurations, and running tests using Pytest.

## Project Structure

api_testing_framework/
│
├── tests/
│ ├── init.py
│ ├── test_create_user.py
│ ├── test_update_user.py
│ └── ...
│
├── resources/
│ ├── init.py
│ ├── test_data.json
│
├── conftest.py
├── config.yaml
├── requirements.txt
└── README.md


- **tests/**: Directory containing test files for API endpoints.
- **resources/**: Directory containing test data files and helper functions like generating fake users.
- **conftest.py**: Common fixtures and configurations used across test files for example access token.
- **config.yaml**: Configuration settings for API base URL, authentication, etc.
- **requirements.txt**: List of Python dependencies required for the project.

## How to Run

1. Clone the repository:
    git clone https://github.com/sachinnshukla/api_testing.git
2. Navigate to the project directory:

    cd api_testing
3. Install dependencies using pip:

    pip install -r requirements.txt


4. Update the `config.yaml` file with your API base URL and authentication credentials if needed, you can login gorest.com to get access token

5. Write your test cases in the `tests/` directory using Pytest.

6. Run tests using Pytest command:

     Go to top level of repo 

     cd api_testing

     run command: pytest -s -v 

    


## Demo

link where you can see the working code.

https://photos.app.goo.gl/14sCWapFcfxyuoif9