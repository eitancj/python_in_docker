# Interactive Investment-Growth Calculation Web App 

Just experimenting with building Docker images. A python app using Streamlit, in this case.

Based on the following guide:\
https://app.pluralsight.com/guides/python-tricks-introduction

### Pre-installed on your machine
- Docker

*Tip*: One of the simplest ways is using Docker Desktop:\
https://www.docker.com/products/docker-desktop/
### App Stack
- Python 3
- Pip 3
- Streamlit
- Debian


### Running the App
** tested on Mac OS

1. pull git repo\
--> git clone https://github.com/eitancj/streamlitApp.git

2. build image\
--> docker build -t streamlit:V1 .

3. run app\
--> docker run -d --rm -p 8501:8501 --name streamlit_ctr streamlit:V1
\
** make sure no other running process is using that port on your machine\

4. test app\
--> go to *localhost:8501* from your web browser

5. stop (and remove) container when your done\
--> docker container stop streamlit_ctr

6. remove the created images (optionally)\
--> docker rmi streamlit:V1 python:3.11.4-slim-bookworm

**Alternatively**, a pre-built image can be found at:\
docker pull eitancj/streamlit_app:V1
In that case start at step 3, after having pulled the image