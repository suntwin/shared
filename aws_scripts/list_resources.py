import argparse
import sys
import os
import config as cfg
from resources import Res
from connection import Connection
from csvReader import CsvReader
from csvWriter import CsvWriter
from client_resources import Client_Resources

try:
	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		parser.add_argument("-profile","-p",help="Mandatory parameter mention a profile for adding credentials")
		parser.add_argument("-service","-s",help="Mandatory Enter the aws service, e.g ec2 or rds")
		parser.add_argument("--tag","-t",nargs = '*',help="optional parameter which when passed with tag only information, retrieves the resources")
		parser.add_argument("--value","-v",nargs = '*',help="optional parameter which when passed with tag only information, retrieves the resources")
		parser.add_argument("--file","-f",help="argument value \"get\" get all instances that matches the tag info from a input file and puts the instance information in an output file;argument value \"dump\" dump all tags into an output file ")

		args = parser.parse_args()
		region_name = cfg.settings['region_name']
		profile_name = args.profile
		#print("arguments are",args)

		# files information
		abspath = cfg.settings['ABS_PATH']
		tag_input_file = cfg.settings['input_file']
		resources_output_file = cfg.settings['output_file1']
		tags_output_file = cfg.settings['output_file2']
		fieldnames_tag_input = cfg.settings['input_file_fields']
		fieldnames_resource_output = cfg.settings['resource_output_fields']
		fieldnames_tag_output = cfg.settings['tag_output_fields']
		
		
		
		
	
		if(args.service=='ec2'):
			# get session
			conn = Connection(region_name,profile_name,"session")
			# get service
			service = conn.get_aws_service('ec2')
		

			# get resource access 
			res = Res(service)

			
		# if the script runs without any argument, it means get all the instances with notags
			
			if(args.tag ==None and args.value==None and args.file==None):
				res_list = res.get_ec2_resources_on_taginfo(taginfo="notag")
				print(res_list)
		# if the script runs with only tag key and no value
			if(args.tag and args.value==None):
				#print("inside args tag",args.tag)
				res_list = res.get_ec2_resources_on_taginfo(tagonly=args.tag)
				print(res_list)
		# if the script runs with both tag key and  value
			if(args.tag and args.value):
				#print("inside args tag value",args.tag,args.value)
				res_list = res.get_ec2_resources_on_taginfo(key=args.tag,value=args.value)
				print(res_list)
		# if the script runs in batch file mode
			if(args.file):
				if(args.file=="get"):

					#read the input file
					result_list=[]
					csvreader = CsvReader(abspath,tag_input_file,fieldnames_tag_input)
					csvwriter = CsvWriter(abspath,resources_output_file,fieldnames_resource_output)
					csvwriter.writefile_header()
					data_list = csvreader.readrows()
					for row in data_list:
						res_list=[]
						key=[]
						value=[]
						
						key.append(row['tagkey'])
						
						value.append(row['tagvalue'])
						if(key[0]!='' and value[0]!=''):
							res_list = res.get_ec2_resources_on_taginfo(key=key,value=value)
						if(key[0]!='' and value[0]==''):
							
							res_list = res.get_ec2_resources_on_taginfo(tagonly=key)
						#write the res_list to the file
						for row in res_list:
							csvwriter.writefile_row(row)

				if(args.file=="dump"):
				
					result_list=[]
					
					csvwriter = CsvWriter(abspath,tags_output_file,fieldnames_resource_output)
					csvwriter.writefile_header()
					res_list = res.get_ec2_resources_on_taginfo(taginfo="notag")
					
					#write the res_list to the file
					for row in res_list:
						csvwriter.writefile_row(row)

			# adding RDS support to the script

		if(args.service=='rds'):
			conn = Connection(region_name,profile_name,args.service)
			
			# get the client typ
			client = conn.get_session()

			# read config
			rds_output_file2 = cfg.settings['rds_output_file2']
			fieldnames_rds_output = cfg.settings['rds_output_fields']
			rds_output_file1 = cfg.settings['rds_output_file1']
			
			# get the instance of the client resource
			client_resource = Client_Resources(client)
			dbinst_list = client_resource.get_rds_db_instances()
			rds_arn_list = client_resource.get_arns_rds_instances(dbinst_list)
			rds_taglist = client_resource.get_tags_on_rds_arns(rds_arn_list)

			
	
		# if the script runs with only tag key and no value
			if(args.tag and args.value==None):
				
				res_list=[]
				for tag in rds_taglist:
					if(tag['Key'] in args.tag):
						res_list.append(tag)
				print(res_list)

				
		# # if the script runs with both tag key and  value
			if(args.tag and args.value):
		 		
		 		res_list=[]
				for tag in rds_taglist:
					if(tag['Key'] in args.tag and tag['Value'] in args.value):
						res_list.append(tag)
				print(res_list)
	

		# # if the script runs in batch file mode
			if(args.file):
				if(args.file=="get"):

					#read the input file
					result_list=[]
					csvreader = CsvReader(abspath,tag_input_file,fieldnames_tag_input)
					csvwriter = CsvWriter(abspath,rds_output_file1,fieldnames_rds_output)
					csvwriter.writefile_header()
					data_list = csvreader.readrows()
					for row in data_list:
						res_list=[]
						key=[]
						value=[]
						
						key.append(row['tagkey'])
						
						value.append(row['tagvalue'])
						if(key[0]!='' and value[0]!=''):
							for tag in rds_taglist:
								#print("tag is",tag)
								if(tag['Key'] == key[0] and tag['Value'] in value[0]):
									res_list.append(tag)
							
						if(key[0]!='' and value[0]==''):
							for tag in rds_taglist:
								if(tag['Key'] == key[0]):
									res_list.append(tag)
							
						#write the res_list to the file
						for row in res_list:
							csvwriter.writefile_row(row)
					print("Retrieved all tags based on tag input file and File updated",os.path.abspath(abspath)+rds_output_file1)

			if(args.file=="dump"):	
					csvwriter = CsvWriter(abspath,rds_output_file2,fieldnames_rds_output)
					csvwriter.writefile_header()		
					#write the rds_list to the file
					for row in rds_taglist:
						#print("row is",row)
						csvwriter.writefile_row(row)
					print("File updated with all tags",os.path.abspath(abspath)+rds_output_file2)
except Exception as e:
	print(e.message)
