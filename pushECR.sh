aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 670843406904.dkr.ecr.us-east-2.amazonaws.com

docker build -t get-transcript-change .

docker tag get-transcript-change:latest 670843406904.dkr.ecr.us-east-2.amazonaws.com/get-transcript-change:latest

docker push 670843406904.dkr.ecr.us-east-2.amazonaws.com/get-transcript-change:latest