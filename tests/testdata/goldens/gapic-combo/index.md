# Python Client for Google Cloud Pub / Sub

[![image](https://img.shields.io/badge/support-GA-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability) [![image](https://img.shields.io/pypi/v/google-cloud-pubsub.svg)](https://pypi.org/project/google-cloud-pubsub/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg)](https://pypi.org/project/google-cloud-pubsub/)

[Google Cloud Pub / Sub](https://cloud.google.com/pubsub/) is a fully-managed real-time messaging service that
allows you to send and receive messages between independent applications. You
can leverage Cloud Pub/Sub’s flexibility to decouple systems and components
hosted on Google Cloud Platform or elsewhere on the Internet. By building on
the same technology Google uses, Cloud Pub / Sub is designed to provide “at
least once” delivery at low latency with on-demand scalability to 1 million
messages per second (and beyond).

Publisher applications can send messages to a `topic` and other applications
can subscribe to that topic to receive the messages. By decoupling senders and
receivers, Google Cloud Pub/Sub allows developers to communicate between
independently written applications.


* [Product Documentation](https://cloud.google.com/pubsub/docs)


* [Client Library Documentation](https://cloud.google.com/python/docs/reference/pubsub/latest)

## Quick Start

In order to use this library, you first need to go through the following steps:


1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)


2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)


3. [Enable the Google Cloud Pub / Sub API.](https://cloud.google.com/pubsub)


4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

#### Supported Python Versions

Python >= 3.7

#### Deprecated Python Versions

Python <= 3.6.

The last version of this library compatible with Python 2.7 is google-cloud-pubsub==1.7.0.

#### Mac/Linux

```console
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-cloud-pubsub
```

#### Windows

```console
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-cloud-pubsub
```

### Example Usage

#### Publishing

To publish data to Cloud Pub/Sub you must create a topic, and then publish
messages to it

```python
import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME',  # Set this to something appropriate.
)
publisher.create_topic(name=topic_name)
future = publisher.publish(topic_name, b'My first message!', spam='eggs')
future.result()
```

To learn more, consult the [publishing documentation](https://cloud.google.com/python/docs/reference/pubsub/latest).

#### Subscribing

To subscribe to data in Cloud Pub/Sub, you create a subscription based on
the topic, and subscribe to that, passing a callback function.

```python
import os
from google.cloud import pubsub_v1

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='MY_TOPIC_NAME',  # Set this to something appropriate.
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub='MY_SUBSCRIPTION_NAME',  # Set this to something appropriate.
)

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.create_subscription(
        name=subscription_name, topic=topic_name)
    future = subscriber.subscribe(subscription_name, callback)
```

The future returned by the call to `subscriber.subscribe` can be used to
block the current thread until a given condition obtains:

```python
try:
    future.result()
except KeyboardInterrupt:
    future.cancel()
```

It is also possible to pull messages in a synchronous (blocking) fashion. To
learn more about subscribing, consult the [subscriber documentation](https://cloud.google.com/python/docs/reference/pubsub/latest).

#### Authentication

It is possible to specify the authentication method to use with the Pub/Sub
clients. This can be done by providing an explicit [Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials) instance. Support
for various authentication methods is available from the [google-auth](https://google-auth.readthedocs.io/en/latest/index.html) library.

For example, to use JSON Web Tokens, provide a [google.auth.jwt.Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.auth.jwt.html#google.auth.jwt.Credentials) instance:

```python
import json
from google.auth import jwt

service_account_info = json.load(open("service-account-info.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

# The same for the publisher, except that the "audience" claim needs to be adjusted
publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
credentials_pub = credentials.with_claims(audience=publisher_audience)
publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)
```

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

It is currently in major version one (1.y.z), which means that the public API should be considered stable.

## Contributing

Contributions to this library are always welcome and highly encouraged.

See the [CONTRIBUTING doc](https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst) for more information on how to get started.

## Community

Google Cloud Platform Python developers hang out in [Slack](https://googlecloud-community.slack.com) in the `#python`
channel, click here to [get an invitation](https://gcp-slack.appspot.com/).

## License

Apache 2.0 - See [the LICENSE](https://github.com/googleapis/google-cloud-python/blob/main/LICENSE) for more information.
