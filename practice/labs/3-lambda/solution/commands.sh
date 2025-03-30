aws s3 cp index.zip s3://alvaro8317-course-us-east-1/laboratorio-lambda/lambda_cold_start.zip

aws cloudformation deploy \
  --template-file cold-start-lambda-lab.yaml \
  --stack-name lambda-cold-start-lab \
  --capabilities CAPABILITY_NAMED_IAM

aws lambda get-function-url-config --function-name mi-lambda-contador

awscurl -X GET https://pziomzmth4rxyjzd7uapdkawi40jppwz.lambda-url.us-east-1.on.aws/ --service lambda

aws cloudformation delete-stack --stack-name lambda-cold-start-lab
