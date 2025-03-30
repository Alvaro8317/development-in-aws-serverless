aws s3 cp code-fix.zip s3://alvaro8317-course-us-east-1/practica-html/
aws s3 cp codigo.zip s3://alvaro8317-course-us-east-1/practica-html/function-html.zip
aws cloudformation create-stack --stack-name MyStackHTMLLambda --template-body html.yml

python3 -m awscurl --service lambda \
    --region us-east-1 \
    -X GET https://4dfp7sfgth7dybrdiqjwziybry0oospo.lambda-url.us-east-1.on.aws/