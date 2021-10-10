FROM python:3-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

#RUN apk update && apk add --no-cache \
    # Required for installing/upgrading postgres, Pillow, etc:
 #   gcc python3-dev

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev


# Set work directory
RUN mkdir /code
WORKDIR /code
# to enaple docker to see it
ADD requirements.txt /code/

# Install dependencies into a virtualenv
RUN pip install -r requirements.txt
#todo
ADD . /code/
# Copy project code
#COPY . /code/
