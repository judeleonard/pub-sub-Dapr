import json
import time

from dapr.clients import DaprClient

with DaprClient() as d:
    id = 0
    while id < 3:
        id += 1
        req_data = {
            'id': id,
            'message': 'hello world'
        }

        # Create a typed message with content type and body
        resp = d.publish_event(
            pubsub_name='pubsub',
            topic_name='TOPIC_A',
            data=json.dumps(req_data),
            data_content_type='application/json',
        )

        # Print the request
        print(req_data, flush=True)

        time.sleep(1)

    # we can publish events to different topics but handle them with the same method
    # by disabling topic validation in the subscriber

    id = 3
    while id < 6:
        id += 1
        req_data = {
            'id': id,
            'message': 'hello world'
        }
        resp = d.publish_event(
            pubsub_name='pubsub',
            topic_name=f'topic/{id}',
            data=json.dumps(req_data),
            data_content_type='application/json',
        )

        # Print the request
        print(req_data, flush=True)

        time.sleep(0.5)