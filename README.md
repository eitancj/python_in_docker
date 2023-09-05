# Interactive Investment-Growth Calculation Web App 

![](https://github.com/eitancj/preview_images/blob/main/streamlit_app_1000.png?raw=true)
Just experimenting with building Docker images. A python app using Streamlit, in this case.


### Pre-installed on your machine
- Git
- Docker

*One of the simplest ways of starting to use Docker by installing:*\
https://www.docker.com/products/docker-desktop/

### Tech Stack
- Python 3
- Pip 3
- Streamlit
- Debian

### Running the App
*Tested on macOS X*

1. Clone git repo & cd into it
```
git clone https://github.com/eitancj/streamlit_app.git
cd streamlit_app
```

2. Build image
```
docker build -t streamlit_app:V1 .

# May take a few minutes: Streamlit is relatively heavy
```

3. Run app
```
docker run -d --rm -p 8501:8501 --name streamlit_ctr streamlit_app:V1

# Make sure no other running process is using that port on your machine
```

4. Test app\
*http://localhost:8501* from your web browser

5. Gracefully stop (and remove) container when you're done
```
docker container stop streamlit_ctr
```

6. Remove the created image
```
docker rmi streamlit_app:V1
```

7. Clean up local copy (unless you want to keep it)
```
cd .. && rm -rf streamlit_app

# Be prudent with 'rm -rf'. Make sure you're in the right directory and aiming at the right folder.
```
