## delete pycache, build files
clean:		
	@rm -rf build.zip
	@rm -rf __pycache__

## prepares build.zip archive for AWS Lambda deploy 
## remember to set in lambda definition:
##		 PYTHONPATH : "/var/task/src:/var/task/lib" 
## 		 Handler: src/lambda_function.lambda_handler
lambda-build: clean 
	cp lib/certbot-1.3.0.zip ./build.zip
	zip build.zip *.py 

## create CloudFormation stack with lambda function and role.
## usage:	make BUCKET=your_bucket_name create-stack 
create-stack: 
	aws s3 cp build.zip s3://${BUCKET}/src/CertbotFunction.zip
	aws cloudformation create-stack --stack-name CertbotLambda --template-body file://cloud.yaml --parameters ParameterKey=BucketName,ParameterValue=${BUCKET} --capabilities CAPABILITY_IAM