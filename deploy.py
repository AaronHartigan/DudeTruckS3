import config
import boto3
from botocore.client import Config
import os
import sys

if __name__ == "__main__":
	s3 = boto3.resource('s3', 'us-west-1')
	bucket = s3.Bucket('dudetruck')
	
	filesUploaded = 0
	print('Loading files to AWS...')
	for file in os.listdir(''):
		if file.endswith('.json'):
			fileData = open(filePath + file, 'rb')
			bucket.put_object(Key=file, ACL='public-read', Body=fileData, ContentType='application/json')
			filesUploaded += 1
		elif file.endswith('.html'):
			fileData = open(filePath + file, 'rb')
			bucket.put_object(Key=file, ACL='public-read', Body=fileData, ContentType='text/html')
			filesUploaded += 1
		elif file.endswith('.css'):
			fileData = open(filePath + file, 'rb')
			bucket.put_object(Key=file, ACL='public-read', Body=fileData, ContentType='text/css')
			filesUploaded += 1
		elif file.endswith('.js'):
			fileData = open(filePath + file, 'rb')
			bucket.put_object(Key=file, ACL='public-read', Body=fileData, ContentType='application/javascript')
			filesUploaded += 1
	print('Successfully loaded', filesUploaded, 'files.\n')