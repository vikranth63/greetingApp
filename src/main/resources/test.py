import boto3
import json
import datetime
import random
import time
import logging
from botocore.exceptions import ClientError
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def save_to_s3(save_file, s3_file_path):
    S3_FAILED_EVENTS_STORE='tests-viks'
    logger.info('executing save to S3')
    try:
        s3_resource = boto3.resource('s3')
        s3_resource.Object(S3_FAILED_EVENTS_STORE, s3_file_path).put(
                Body=(bytes(json.dumps(save_file).encode('UTF-8'))))
    except ClientError as e:
        logger.error("Error while executing saving to s3: %s" % e)

def random_json():
    dictionary_01 ={
                "lineOfBusiness":"Auto",
                "Source":"PolicyCenterPL",
                "processDate":"20200605",
                "scriptPath":"s3://vik-scripts",
                "scriptName":"HelloWorld.sh",
                "environment":"int",
                "emrCluster":"j-3BSG04KI6KETA",
                "parameters":{
                        "flowPath":"s3://",
                        "flowName":"doozie",
                        "flowVersion":"0.3.0",
                        "flowProperties":{
                                "stage_path":"s3://"

                        }}}
    dictionary_02 ={
                "lineOfBusiness":"Property",
                "Source":"PolicyCenterPL",
                "processDate":"20200605",
                "scriptPath":"s3://vik-scripts",
                "scriptName":"HelloWorld.sh",
                "environment":"int",
                "emrCluster":"j-3BSG04KI6KETA",
                "parameters":{
                        "flowPath":"s3://",
                        "flowName":"doozie",
                        "flowVersion":"0.3.0",
                        "flowProperties":{
                                "stage_path":"s3://"

                        }}}
    dictionary_03 ={
                "lineOfBusiness":"Auto",
                "Source":"PolicyCenterPL",
                "processDate":"20200605",
                "scriptPath":"s3://vik-scripts",
                "scriptName":"HelloWorld.sh",
                "environment":"int",
                "emrCluster":"j-3BSG04KI6KETA",
                "parameters":{
                        "flowPath":"s3://",
                        "flowName":"doozie",
                        "flowVersion":"0.3.0",
                        "flowProperties":{
                                "stage_path":"s3://"

                        }}}
    dictionary_04 ={
                "lineOfBusiness":"Property",
                "Source":"PolicyCenterPL",
                "processDate":"20200605",
                "scriptPath":"s3://vik-scripts",
                "scriptName":"HelloWorld.sh",
                "environment":"int",
                "emrCluster":"j-3BSG04KI6KETA",
                "parameters":{
                        "flowPath":"s3://",
                        "flowName":"doozie",
                        "flowVersion":"0.3.0",
                        "flowProperties":{
                                "stage_path":"s3://"

                        }}}
    save_to_s3(dictionary_01, "Trigger1/A/A.json")
    save_to_s3(dictionary_02, "Trigger1/B/B.json")
    save_to_s3(dictionary_03, "Trigger1/C/C.json")
    save_to_s3(dictionary_04, "Trigger1/D/D.json")
    
def lambda_handler(event, context):
    logger.info('executing lambda_handler function for exporting Apigee Metrics to kinesis')

    try:
        random_json()

    except Exception as e:
        logger.error("Error Handeling lambda_handler function: %s" % e)
