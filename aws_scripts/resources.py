class Res:

	def __init__(self,resource_type):
		self.resource_type = resource_type



	def get_ec2_resources_on_taginfo(self,**kwargs):

		instance_list=[]
		tag_instance_list=[]
		# get all the running instances
		instances = self.resource_type.instances.filter(
		Filters=[
		{'Name':'instance-state-name','Values':['running','stopped']},
		]
		
		)

		#print("runninng instances",instances)
		#print("kwargs",kwargs)
		if "taginfo" in kwargs:
			print("inside taginfo")
			for instance in instances:
				#if(instance.tags == None):
				if(instance.tags):
					for tags in instance.tags:
						instance_list.append({
								"instance-id":instance.id,
								"instance-type":instance.instance_type,
								"instance-state":instance.state['Name'],
								"tagkey":tags['Key'],
								"tagvalue":tags['Value'],
								})
		

		if "tagonly" in kwargs:
			print("inside tagonly")
			key = kwargs['tagonly']
			#print("i am in tag only")
			print("key is",type(key))
			for k in key:
				
				for instance in instances:
					
					if(instance.tags != None):
						for tags in instance.tags:
							# print("key is",key)

							

							if (k == tags['Key']):
								print("k is",k,"tags is",tags['Key'])
								instance_list.append({
									"instance-id":instance.id,
									"instance-type":instance.instance_type,
									"instance-state":instance.state['Name'],
									"tagkey":k,
				              		"tagvalue":tags['Value'],
									})
							
							#print("found instance with key",key)


		if ("key" in kwargs and "value" in kwargs):
		# create a list of all the combinations of the tags and values
		# and then loop through the same
		# doing a list comprehension below to start looping afterwards
			key = kwargs['key']
			value = kwargs['value']
			l = ([(k, v) for k in key for v in value])

			for l1 in l:
				print("inside tagkey and value")
				for instance in instances:
					if(instance.tags != None):
						for tags in instance.tags:
							#print("key is",key)
							#print("Tags[Key]",tags['Key'])
							print("k is",l1[0],"v is",l1[1])
							if (l1[0] == tags['Key'] and l1[1] == tags['Value']):
								print("l10",l1[0],"l11",l1[1])
								instance_list.append({
									"instance-id":instance.id,
									"instance-type":instance.instance_type,
									"instance-state":instance.state['Name'],
									"tagkey":l1[0],
									"tagvalue":l1[1],
									})
								#print("found instance with key",key)

		return(instance_list)



def get_rds_resources_on_taginfo(self,**kwargs):

		instance_list=[]
		tag_instance_list=[]
		# get all the running instances
		instances = self.resource_type.instances.filter(
		Filters=[
		{'Name':'instance-state-name','Values':['running','stopped']},
		]
		
		)

		#print("runninng instances",instances)
		#print("kwargs",kwargs)
		if "taginfo" in kwargs:
			print("inside taginfo")
			for instance in instances:
				#if(instance.tags == None):
				if(instance.tags):
					for tags in instance.tags:
						instance_list.append({
								"instance-id":instance.id,
								"instance-type":instance.instance_type,
								"instance-state":instance.state['Name'],
								"tagkey":tags['Key'],
								"tagvalue":tags['Value'],
								})
		

		if "tagonly" in kwargs:
			print("inside tagonly")
			key = kwargs['tagonly']
			#print("i am in tag only")
			print("key is",type(key))
			for k in key:
				
				for instance in instances:
					
					if(instance.tags != None):
						for tags in instance.tags:
							# print("key is",key)

							

							if (k == tags['Key']):
								print("k is",k,"tags is",tags['Key'])
								instance_list.append({
									"instance-id":instance.id,
									"instance-type":instance.instance_type,
									"instance-state":instance.state['Name'],
									"tagkey":k,
				              		"tagvalue":tags['Value'],
									})
							
							#print("found instance with key",key)


		if ("key" in kwargs and "value" in kwargs):
		# create a list of all the combinations of the tags and values
		# and then loop through the same
		# doing a list comprehension below to start looping afterwards
			key = kwargs['key']
			value = kwargs['value']
			l = ([(k, v) for k in key for v in value])

			for l1 in l:
				print("inside tagkey and value")
				for instance in instances:
					if(instance.tags != None):
						for tags in instance.tags:
							#print("key is",key)
							#print("Tags[Key]",tags['Key'])
							print("k is",l1[0],"v is",l1[1])
							if (l1[0] == tags['Key'] and l1[1] == tags['Value']):
								print("l10",l1[0],"l11",l1[1])
								instance_list.append({
									"instance-id":instance.id,
									"instance-type":instance.instance_type,
									"instance-state":instance.state['Name'],
									"tagkey":l1[0],
									"tagvalue":l1[1],
									})
								#print("found instance with key",key)

		return(instance_list)



	