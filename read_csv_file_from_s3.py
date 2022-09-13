#Importing packages
import boto3
import pandas as pd

#declaring acess key and secret key 
ACCESS_KEY = r'your-access-key'
SECRET_KEY = r'your-secret-key'

#creating s3 instances
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)


#get the list of bucket
response = s3.list_buckets()
#collected the list of bucket name which i have created
#list of name of bucket
bucket_list = [bucket["Name"] for bucket in response['Buckets']]
print(bucket_list) #display the list of bucket
bucket_name = r's3-event-lambda-demo-v1'
#get the list of file inside bucket
object_list = [key['Key'] for key in s3.list_objects(Bucket= bucket_name)['Contents']]

for key_name in object_list:
  #downloading file from s3 bucket i.e. object file
    obj = s3.get_object(
            Bucket = bucket_name,
            Key = key_name
        )
    # # Read data from the S3 object
    df = pd.read_csv(obj['Body'])
    print(df) #print the content of dataframe
