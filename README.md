## Introduction
This is a simple Fast API service that allows you to transcribe audio file while leveraging on Open AI whisper model.


### Setting up your environment
Run the command `poetry shell` to spin up a poetry virtual environment.

Then run the commands below to install all the package dependencies

```shell
poetry install --no-root
```

Run the command below to start up the application which would be running on port 8000
```shell
poetry run uvicorn app.main:app --reload
```

#### Note:
Supported files include: wav, mp3, m4a
