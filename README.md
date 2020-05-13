# certbot-lambda

![architecture](architecture.png "Architecture")


A lambda function to get and renew FREE SSL certificates using Certbots. I'm using it to automatically request and renew all SSL certificates of my CloudFront websites.

* Automatic S3 hosting verification
* ACM certificate import (CloudFront)
* CloudWatch daily event to check if renew is needed
* CloudFormation template to build stack

## Instructions

Use `make lambda-build` to build lambda source package.

Use `make BUCKET=your_bucket_name create-stack` to upload source package in a bucket and deploy CloudFormation stack.

More deatails on [this post](https://www.vittorionardone.it/en/2020/04/29/free-ssl-certificates-with-certbot-in-aws-lambda/) of my Digital Transformation Blog.



