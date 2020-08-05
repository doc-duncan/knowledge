# Pipenv

### Installation
`pip install pipenv`

### Set Up
1. `cd <project-dir>`
2. `pipenv shell # activates environment`

### Helpful Commands
* `pipenv install <dependency> # installs dependency`
* `pipenv install # installs from pipfile`
* `pipenv install <dependency> --dev # installs dev dependency`
* `pipenv install -r requirements.txt # installs dependencies from requirements.txt`
* `pipenv uninstall <dependency> # uninstalls dependency`
* `pipenv lock # writes to pipfile.lock`
* `pipenv lock -r > requirements.txt # writes to requirements.txt`
* `pipenv run # run python command using env interpreter`
* `pipenv --venv # gives path to virtualenv`
* `pipenv check # checks for security vulnerabilities of dependencies`
* `pipenv --rm # removes virtualenv but keeps pipfile`