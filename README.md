# Fafnir Scraper

## Development Setup

### Option 1: Docker
#### Build
`docker build -t fafnir_scraper:latest .`

#### Run
`docker run -d -p fafnir_scraper [COMMAND]`

### Option 2: virtualenv
#### Init virtualenv
```shell
rm -rf venv
virtualenv venv
```
#### Activate virtualenv
`. venv/bin/activate`

#### Install Dependencies
`python setup.py develop`

#### Run Tests
`nosetests`
