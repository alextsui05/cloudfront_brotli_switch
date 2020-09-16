AWS Lambda@Edge Python script to point origin requests to brotli-compressed
files when applicable

## Run unit test

```
python -m unittest .
```

## Deploy via AWS Console

* Create AWS Lambda function with `lambda_function.py` as code
* Publish function and copy ARN
* Create Cloudfront distribution with S3 origin
* Create Behavior for `/packs/*` path pattern
* Set Cache Based on Selected Request Headers to `Whitelist`
* Add `Accept-Encoding` to whitelist headers
* Disable Compress Objects Automatically
* Enable Lambda Function Associations, and use the Lambda function ARN above
  * Cloudfront Event should be `Origin Request`

## Links

* https://dev.classmethod.jp/articles/serve-brotli-encoded-files-from-cloudfront/
* https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html
* https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html#lambda-event-structure-request
* https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html#compressed-content-S3-origin
