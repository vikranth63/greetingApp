import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import logging
import csv
import time
import itertools
import multiprocessing

logger = logging.getLogger()
logger.setLevel(logging.INFO)

AWS_REGION = None
AWS_REGION_POSITION_IN_ARN = 3
FIRST_RECORD_INDEX=0
DEFAULT_Cluster_ID="j-3BSG04KI6KETA"
EMPTY_STRING=''

def lambda_handler(event, context):
    conn = boto3.client("emr")
    s3 = boto3.client('s3')
    logger.info('executing lambda_handler function')
    global AWS_REGION_POSITION_IN_ARN
    global FIRST_RECORD_INDEX
    global DEFAULT_Cluster_ID
    apigee_logs_bucket = event['Records'][FIRST_RECORD_INDEX]['s3']['bucket']['name']
    apigee_log_file_name = event['Records'][FIRST_RECORD_INDEX]['s3']['object']['key']
    logger.info('Reading {} from {}'.format(apigee_log_file_name, apigee_logs_bucket))
    log_file = s3.get_object(Bucket=apigee_logs_bucket, Key=apigee_log_file_name)
    #s3_clientdata = s3_clientobj['Body'].read().decode('utf-8')
    #print(type(s3_clientdata))
    #s3clientlist=json.loads(s3_clientdata)
    log_transactions = log_file['Body'].read().split(b'\n')
    for each_log in log_transactions:
        my_dict = (json.loads(each_log.decode()))
        script_name =my_dict['scriptName']
        script_path =my_dict['scriptPath']
        script_location = script_path+'/'+script_name
        cluster_id= my_dict['emrCluster'] if 'emrCluster' in my_dict and (my_dict['emrCluster'] and my_dict['emrCluster'].strip()) else DEFAULT_Cluster_ID
        lineOfBusiness= my_dict['lineOfBusiness'] if 'lineOfBusiness' in my_dict  else EMPTY_STRING
        Source= my_dict['Source'] if 'Source' in my_dict  else EMPTY_STRING
        processDate= my_dict['processDate'] if 'processDate' in my_dict  else EMPTY_STRING
        environment= my_dict['environment'] if 'environment' in my_dict  else EMPTY_STRING
        emrCluster= my_dict['emrCluster'] if 'emrCluster' in my_dict  else EMPTY_STRING
        flowPath= my_dict['parameters']['flowPath'] if 'parameters' in my_dict and  'flowPath' in  my_dict['parameters'] else EMPTY_STRING
        flowName= my_dict['parameters']['flowName'] if 'parameters' in my_dict and  'flowName' in  my_dict['parameters'] else EMPTY_STRING
        flowVersion= my_dict['parameters']['flowVersion'] if 'parameters' in my_dict and  'flowVersion' in  my_dict['parameters'] else EMPTY_STRING
        stage_path= my_dict['parameters']['flowProperties']['stage_path'] if 'parameters' in my_dict and  'flowProperties' in  my_dict['parameters'] and  'stage_path' in  my_dict['parameters']['flowProperties'] else EMPTY_STRING
        step_args=[script_location,lineOfBusiness,Source,processDate,environment,emrCluster,flowPath,flowName,flowVersion,stage_path]
        #clusters = conn.list_clusters()
        #clusters = [c["Id"] for c in clusters["Clusters"]
        #            if c["Status"]["State"] in ["RUNNING", "WAITING"]]
        #if not clusters:
        #    sys.stderr.write("No valid clusters\n")
        #    sys.stderr.exit()
        #cluster_id = clusters[0]
        step = {"Name": "Vik_test" + time.strftime("%Y%m%d-%H:%M"),
                'ActionOnFailure': 'CONTINUE',
                'HadoopJarStep': {
                    'Jar': 's3n://elasticmapreduce/libs/script-runner/script-runner.jar',
                    'Args': step_args
                }
            }
        action = conn.add_job_flow_steps(JobFlowId=cluster_id, Steps=[step])
        logger.info(action)
