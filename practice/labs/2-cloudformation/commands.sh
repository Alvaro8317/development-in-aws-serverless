aws cloudformation create-stack \
--stack-name StackLaboratorioCloudformation \
--template-body file://practice/labs/2-cloudformation/exercise.yml \
--capabilities CAPABILITY_NAMED_IAM

aws cloudformation update-stack \
 --stack-name StackLaboratorioCloudformation \
 --template-body file://practice/labs/2-cloudformation/exercise.yml \
 --capabilities CAPABILITY_NAMED

aws cloudformation delete-stack --stack-name StackLaboratorioCloudformation