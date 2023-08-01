# Interactive Investment-Growth Calculation Web App 

Just experimenting with building Docker images.\
In this case for a python-based app using Streamlit.\

Based on the following guide:\
https://app.pluralsight.com/guides/python-tricks-introduction

### Pre-installed on your machine
- Docker
- Docker Compose

*Tip*: One of the easiest ways is downloading Docker Desktop:\
https://www.docker.com/products/docker-desktop/
### App Stack
- Python 3
- Pip 3
- Streamlit

### Running the App (tested on Mac OS)

1. pull git repo\
--> git pull https://github.com/eitancj/streamlitApp.git

2. build image\
--> docker build -t streamlit:V1 .

3. run app\
--> docker run -d --rm -p 8501:8501 --name streamlit_ctr streamlit:V1
\
* make sure no other running process is using that port on your machine\

4. test app\
--> go to *localhost:8501* from your web browser

5. stop (and remove) container when your done\
--> docker container stop streamlit_ctr

6. remove the created images (optionally)
--> docker rmi streamlit:V1 python:3.11.4-slim-bookworm

**Alternatively**, a pre-built image can be found at:\
???\
In that case start at step 3