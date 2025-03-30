aws iam create-role \
    --role-name rol-lambda-con-cli \
    --assume-role-policy-document file://explanations/lambda/trust-policy.json

aws lambda create-function \
    --function-name mi-primera-lambda-con-cli \
    --runtime python3.13 \
    --handler code.lambda_handler \
    --zip-file fileb://explanations/lambda/code.zip \
    --role arn:aws:iam::490004645449:role/rol-lambda-con-cli