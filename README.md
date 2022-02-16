# serverless-presentation

### Development without docker requirements

* Python 3.9
* Serverless 3
* Plugins:
    * serverless-python-requirements
    * serverless-prune-plugin
    * serverless-offline (development)
    * serverless-dynamodb-local (development)

### Development with docker

* Login to Docker Hub with command `docker login -u bpolreadonly` and token `afe40a4d-26aa-4201-9042-1a8404b36e0e` as
  password
* Create `.env` based on `.env.example`
* Run offline environment command `make start`
* Install python requirements `make install-requirements`
* Http server is available on: `http://localhost:3000/local/`
