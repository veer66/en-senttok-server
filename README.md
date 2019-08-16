## Prerequisite
* conda
* import nltk
* nltk.download('punkt')
* pip install starlette
* pip install uvicorn
* pip install gunicorn

## RUN

### DEV

* uvicorn --reload --host 0.0.0.0 server:app

## Usage

### Using Httpie

```
$ echo '{"text":"I like a cat. I like a dog."}' | http post localhost:8000/sent-tok
HTTP/1.1 200 OK
content-length: 47
content-type: application/json
date: Fri, 16 Aug 2019 17:32:21 GMT
server: uvicorn

{
    "sentences": [
        "I like a cat.",
        "I like a dog."
    ]
}
```

