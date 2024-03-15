import os
import io
import botocore
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    payload = json.loads(json.dumps(event))
    data = payload['instances']    
    
    #new an dictionary
    result = {}
    
    #new an empty list
    predictions = []
    
    #invoke the sagemaker endpoint to get predicted result for each data item
    for item in data:
        #new a dictionary
        prediction = {}
        
        #copy values
        prediction['id'] = item['id']
        prediction['instance'] = item['instance']
        
        
        #invoke the sagemaker endpoint to get DG category prediction 
        smresponse = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                             ContentType='text/csv',
                                             Body=item['instance'])
        
        if smresponse['ResponseMetadata']['HTTPStatusCode'] == 200:
            prediction['prediction'] = smresponse['Body'].read().decode()
        else:
            raise Exception('SageMaker Inference Failure.')
        
        #add prediction to the list
        predictions.append(prediction) 
    
    #assign value to result
    result['predictions'] = predictions
    
    return result
