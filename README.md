# Using Docker to Containerize a Python App

![](https://github.com/eitancj/preview_images/blob/main/streamlit_app_1000.png?raw=true)

\
Just experimenting with building Docker images.  
Containerizing a Python3-Streamlit app, in this case.

Inspired by [this](https://app.pluralsight.com/guides/dockerfile-for-python-web-projects) short guide.

### Pre-installed on your machine
- Git
- Docker

*A simple way to work with Docker images locally:*\
https://www.docker.com/products/docker-desktop/

### Tech Stack
- Tested on macOS X
- Python 3.11.4
- Streamlit
- Debian-based container

### Running the App

1. Clone git repo & cd into it
```
git clone https://github.com/eitancj/python_in_docker
cd python_in_docker
```

2. Build image
```
docker build -t python_in_docker:V1 .

# May take a few minutes: Streamlit is relatively heavy
```

3. Verify image creation   
```
docker images python_in_docker
```

4. Run app
```
docker run -d --rm -p 8501:8501 --name pydock python_in_docker:V1

# Make sure no other running process is using that port on your machine
```

5. Test app\
```
open http://localhost:8501 # will open in your default web browser

# Or simply copy and paste the address into your web browser
```

6. Gracefully stop (and remove) container when you're done
```
docker container stop pydock
```

7. Remove the created image
```
docker rmi python_in_docker:V1
```

8. Clean up local copy (unless you want to keep it)
```
cd .. && rm -rf python_in_docker

# BE PRUDENT WITH 'rm -rf'.
# Make sure you're in the right directory and aiming at the right folder.
```

9. That's it
