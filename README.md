# Interactive Investment-Growth Calculation Web App 

![](https://github.com/eitancj/preview_images/blob/main/streamlit_app_1000.png?raw=true)
Just experimenting with building Docker images. A python app using Streamlit, in this case.

Based on the following guide:\
https://app.pluralsight.com/guides/python-tricks-introduction

### Pre-installed on your machine
- Git
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

1. clone git repo & cd into it
```
git clone https://github.com/eitancj/streamlit_app.git
cd streamlit_app
```

2. build image
```
docker build -t streamlit_app:V1 .
```
** may take a few minutes: Streamlit is relatively heavy

3. run app
```
docker run -d --rm -p 8501:8501 --name streamlit_ctr streamlit_app:V1
```
** make sure no other running process is using that port on your machine

4. test app\
*http://localhost:8501* from your web browser

5. gracefully stop (and remove) container when you're done
```
docker container stop streamlit_ctr
```

6. remove the created image
```
docker rmi streamlit_app:V1
```

7. clean up local copy (unless you want to keep it)
```
cd .. && rm -rf streamlit_app
```
** be prudent with 'rm -rf'. Make sure you're in the right directory and aiming at the right folder.
