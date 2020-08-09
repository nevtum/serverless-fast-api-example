# serverless-fast-api-example

This is a reference project that combines a web api framework and runs it on AWS lambda. Libraries
that I experimented with are the following:

* AWS SAM
* FastAPI
* Mangum

The example makes use of API Gateway's proxy integration, usage plan request throttling and API
keys... excellent, cost effective features to build secure, fault tolerant APIs (IMHO)! I also
experiment with Lambda versioning and X-ray.

## Getting set up

Make sure to have AWS SAM cli installed.

```bash
  $ pip install --upgrade aws-sam-cli
```

To build and deploy the SAM application, run the following commands:

```bash
  $ sam build --use-container --debug
  $ sam deploy --guided
```

## Local development

Install and run uvicorn to start a FastAPI app instance: 

```bash
  $ pip install -r requirements.dev.txt
  $ ENV=local uvicorn example_app.app:app --port 8080 --reload
```

