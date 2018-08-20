class Client_Resources:

	def __init__(self,client):
		self.client = client

	def get_rds_db_instances(self):
		return(self.client.describe_db_instances()['DBInstances'])

	def get_arns_rds_instances(self,dblist):
		arnlist=[]
		for db in dblist:
			arnlist.append(db['DBInstanceArn'])
		return(arnlist)

	def get_tags_on_rds_arns(self,arnlist):
		taglist=[]
		for arn in arnlist:
			response = self.client.list_tags_for_resource(ResourceName=arn)
			#parse taglist and the resource in it
			taglist = response['TagList']
			for tag in taglist:
				tag.update({"arn":arn})

			return(taglist)


	