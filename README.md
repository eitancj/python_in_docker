# Interactive Investment-Growth Calculation Web App 

Just experimenting with building Docker images.
In this case for a python-based app.

## For this to work on your machine you need these to be pre-installed:
- Docker
- Docker Compose

*Tip*: One of the easiest ways is downloading Docker Desktop:
https://www.docker.com/products/docker-desktop/
## App Stack:

- Python 3
- Pip 3
- Streamlit

### Running the App (tested on Mac OS):

1. pull the git repo
--> git pull https://github.com/eitancj/streamlitApp.git

2. build the image
--> docker build -t streamlit:V1 .

3. run the app (make sure no other running process is using that port on your machine)
--> docker run -d --rm -p 8501:8501 --name streamlit_ctr streamlit:V1

4. test the app
--> go to *localhost:8501* from your web browser

5. once your done, stop the container, which will be automatically deleted
--> docker container stop streamlit_ctr

6. optionally, remove the created images
--> docker rmi streamlit:V1 python:3.11.4-slim-bookworm

*Alternatively*, an already-built image can be found at:
???
