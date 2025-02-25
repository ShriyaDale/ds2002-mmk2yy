import boto3
import requests

#retrieving image
gif = "https://canada1.discourse-cdn.com/flex036/uploads/gazebo/original/1X/75c7585358>
file = "gif.gif"
bucket = "ds2002-mmk2yy"
expires_in = 60

retrieved = requests.get(gif)

s3 = boto3.client("s3", region_name="us-east-1")
s3.put_object(Body = file, Bucket = bucket, Key = file)
presigned_url = s3.generate_presigned_url("get_object", Params={"Bucket": bucket, "Key>

print(presigned_url)
