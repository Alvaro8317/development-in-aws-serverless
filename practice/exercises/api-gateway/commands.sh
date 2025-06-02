aws cloudformation package \
  --template-file plantilla-api-rest.yml \
  --s3-bucket alvaro8317-course-us-east-1 \
  --output-template-file packaged-api-rest.yml

aws cloudformation deploy \
  --template-file packaged-api-rest.yml \
  --stack-name stack-api-gateway-rest \
  --capabilities CAPABILITY_IAM

aws lambda get-function-configuration --function-name DEVELOPER_SERVERLESS_IN_AWS_LAMBDA_API_GATEWAY

alias deploy-api-rest='aws cloudformation package \
  --template-file plantilla-api-rest.yml \
  --s3-bucket alvaro8317-course-us-east-1 \
  --output-template-file packaged-api-rest.yml && \
aws cloudformation deploy \
  --template-file packaged-api-rest.yml \
  --stack-name stack-api-gateway-rest \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides NameProjectParam=UdemyCourse Timestamp=$(date +%Y%m%d%H%M%S)'
