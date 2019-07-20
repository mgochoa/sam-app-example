sam package --output-template-file template-packaged.yaml --template-file template.yaml --s3-bucket "S3_DEPLOY_BUCKET"

sam deploy --template-file template-packaged.yaml \
  --stack-name "STACK_NAME" \
  --parameter-overrides "bucket=S3_DEPLOY_BUCKET" \
  --region "us-east-1"  \
  --capabilities CAPABILITY_IAM 