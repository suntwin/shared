import boto3
import config as cfg
import botocore


class Connection:

	def __init__(self,region_name,profile_name,conn_type):
		try:
			if(conn_type=="session"):
				self.session = boto3.Session(region_name=region_name,profile_name=profile_name)
			if(conn_type!="session"):
				self.session = boto3.client(conn_type)

		except botocore.exceptions.BotoCoreError as e:
			raise Exception(e)

		#self.session = boto3.Session(region_name='ap-southeast-2',profile_name='default')

	def get_session(self):
		return(self.session)

	def get_aws_service(self,service):
		return(self.session.resource(service))

