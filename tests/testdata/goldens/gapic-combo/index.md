# Python Client for Google BigQuery

[![image](https://img.shields.io/badge/support-GA-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability) [![image](https://img.shields.io/pypi/v/google-cloud-bigquery.svg)](https://pypi.org/project/google-cloud-bigquery/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-bigquery.svg)](https://pypi.org/project/google-cloud-bigquery/)

Querying massive datasets can be time consuming and expensive without the
right hardware and infrastructure. Google [BigQuery](https://cloud.google.com/bigquery/what-is-bigquery) solves this problem by
enabling super-fast, SQL queries against append-mostly tables, using the
processing power of Google’s infrastructure.


* [Client Library Documentation](https://googleapis.dev/python/bigquery/latest)


* [Product Documentation](https://cloud.google.com/bigquery/docs/reference/v2/)

## Quick Start

In order to use this library, you first need to go through the following steps:


1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)


2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)


3. [Enable the Google Cloud BigQuery API.](https://cloud.google.com/bigquery)


4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)

### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

#### Supported Python Versions

Python >= 3.7, < 3.11

#### Unsupported Python Versions

Python == 2.7, Python == 3.5, Python == 3.6.

The last version of this library compatible with Python 2.7 and 3.5 is
google-cloud-bigquery==1.28.0.

#### Mac/Linux

```console
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-cloud-bigquery
```

#### Windows

```console
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-cloud-bigquery
```

## Example Usage

### Perform a query

```python
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
```

## Instrumenting With OpenTelemetry

This application uses [OpenTelemetry](https://opentelemetry.io) to output tracing data from
API calls to BigQuery. To enable OpenTelemetry tracing in
the BigQuery client the following PyPI packages need to be installed:

```console
pip install google-cloud-bigquery[opentelemetry] opentelemetry-exporter-google-cloud
```

After installation, OpenTelemetry can be used in the BigQuery
client and in BigQuery jobs. First, however, an exporter must be
specified for where the trace data will be outputted to. An
example of this can be found here:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(CloudTraceSpanExporter())
)
```

In this example all tracing data will be published to the Google
[Cloud Trace](https://cloud.google.com/trace) console. For more information on OpenTelemetry, please consult the [OpenTelemetry documentation](https://opentelemetry-python.readthedocs.io).
