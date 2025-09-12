# Sam package y su relación con cloudformation

sam package --output-template-file packaged.yaml

# Linux

sudo apt install jq
sudo apt install yq

aws cloudformation get-template \
  --stack-name expense-app-manager-aws \
  --template-stage Processed \
  --output json \
| jq -r '.TemplateBody' \
| yq -y > processed-cfn.yaml

# MacOS

brew install jq yq

aws cloudformation get-template \
  --stack-name expense-app-manager-aws \
  --template-stage Processed \
  --output json \
| jq -r '.TemplateBody' \
| yq -P > processed-cfn.yaml

# Windows

aws cloudformation get-template `
  --stack-name expense-app-manager-aws `
  --template-stage Processed `
  --output json |
jq -r ".TemplateBody" |
yq -y |
Out-File -FilePath processed-cfn.yaml -Encoding utf8
