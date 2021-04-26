# Maven Clinic Scheduler

A scheduler for your busy life.


## Source Code
https://github.com/mgentry612/maven_scheduler

## Installation

Install the latest version of docker. Last tested on version 20.10.5.

Pull the latest scheduler image

```bash
docker pull mgentry612/maven_scheduler:v1
```

Run the image on port 5001
```bash
docker run --name maven_scheduler -p 5001:5001 mgentry612/maven_scheduler:v1
```

## Usage
Download and install Postman. Then import the Postman collection from the root directory in the github repository: maven.postman_collection.json.

## Testing
A unit test suite is included in pytest.

Clone the github respository to your local device.

Create a new virtual environment using your favorite environment management system (conda, virtualenv, etc.) and install pytest:
```bash
pip install pytest
```
Then run:
```bash
pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
