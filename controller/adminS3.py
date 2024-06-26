import boto3
from credentials.keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resourse = session_aws.resource('s3')
        print("Connection with S3 Service successful")
        return s3_resourse
    except Exception as err:
        print("Impossible connect to S3 services", err)
        return None
        
def save_file(photo):
    try:
        origin_path = "/tmp/photo.jpg"
        photo.save(origin_path)
        print("Photo saved")
        return origin_path
    except Exception as err:
        print("Error", err)
        return None
        
def upload_file(s3_resource, origin_path):
    bucket_name = "aws-bucket-test-nicolas.reatiga"
    target_path = "images/" + "photo.jpg"
    try:
        bucket_connection = s3_resource.meta.client.upload_file(origin_path, bucket_name, target_path)
        print("Image loaded correctly!") 
        return True
    except Exception as err:
        print("Image can't loaded", err)
        return False