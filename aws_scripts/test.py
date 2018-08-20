import boto3
dict = [{'arn': 'arn:aws:rds:ap-southeast-2:171331772601:db:niteshdb', u'Value': 'bajaj', u'Key': 'jamna'},
 {'arn': 'arn:aws:rds:ap-southeast-2:171331772601:db:niteshdb', u'Value': 'other', u'Key': 'workload-type'}]
keys = ['jamna','workload-type']
dict_found = []
for d in dict:
	if d['Key'] in keys:
		dict_found.append(d)





print(dict_found)