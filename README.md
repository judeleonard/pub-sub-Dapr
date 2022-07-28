# Created this repository for practicing dapr
 
## Install dapr python sdk
    pip3 install dapr dapr-ext-grpc

## run the subscriber task
    dapr run --app-id python-subscriber --app-protocol grpc --app-port 50051 python3 subscriber.py
    
## run the publisher task
    dapr run --app-id python-publisher --app-protocol grpc --dapr-grpc-port=3500 python3 publisher.py
