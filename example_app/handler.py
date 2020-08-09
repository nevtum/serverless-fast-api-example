from mangum import Mangum
from app import app
import logging

logging.basicConfig()
mangum_handler = Mangum(app)


def lambda_handler(event, context):
    logging.info(f"Event: {event}")
    resp = mangum_handler(event, context)
    logging.info(f"Response: {resp}")
    return resp

