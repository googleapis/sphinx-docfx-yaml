# IPython Magics for BigQuery

To use these magics, you must first register them. Run the `%load_ext` magic
in a Jupyter notebook cell.

```default
%load_ext google.cloud.bigquery
```

This makes the `%%bigquery` magic available.

## Code Samples

Running a query:

Running a parameterized query:

## API Reference

IPython Magics


### %%bigquery()
IPython cell magic to run a query and display the result as a DataFrame

```python
%%bigquery [<destination_var>] [--project <project>] [--use_legacy_sql]
           [--verbose] [--params <params>]
<query>
```

Parameters:


* `<destination_var>` (Optional[line argument]):

    variable to store the query results. The results are not displayed if
    this parameter is used. If an error occurs during the query execution,
    the corresponding `QueryJob` instance (if available) is stored in
    the variable instead.


* `--destination_table` (Optional[line argument]):

    A dataset and table to store the query results. If table does not exists,
    it will be created. If table already exists, its data will be overwritten.
    Variable should be in a format <dataset_id>.<table_id>.


* `--no_query_cache` (Optional[line argument]):

    Do not use cached query results.


* `--project <project>` (Optional[line argument]):

    Project to use for running the query. Defaults to the context
    `project`.


* `--use_bqstorage_api` (Optional[line argument]):

    [Deprecated] Not used anymore, as BigQuery Storage API is used by default.


* `--use_rest_api` (Optional[line argument]):

    Use the BigQuery REST API instead of the Storage API.


* `--use_legacy_sql` (Optional[line argument]):

    Runs the query using Legacy SQL syntax. Defaults to Standard SQL if
    this argument not used.


* `--verbose` (Optional[line argument]):

    If this flag is used, information including the query job ID and the
    amount of time for the query to complete will not be cleared after the
    query is finished. By default, this information will be displayed but
    will be cleared after the query is finished.


* `--params <params>` (Optional[line argument]):

    If present, the argument following the `--params` flag must be
    either:


        * [`str`](https://python.readthedocs.io/en/latest/library/stdtypes.html#str) - A JSON string representation of a dictionary in the
    format `{"param_name": "param_value"}` (ex. `{"num": 17}`). Use
    of the parameter in the query should be indicated with
    `@param_name`. See `In[5]` in the Examples section below.


        * [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict) reference - A reference to a `dict` in the format
    `{"param_name": "param_value"}`, where the value types must be JSON
    serializable. The variable reference is indicated by a `$` before
    the variable name (ex. `$my_dict_var`). See `In[6]` and `In[7]`
    in the Examples section below.


* `<query>` (required, cell argument):

    SQL query to run. If the query does not contain any whitespace (aside
    from leading and trailing whitespace), it is assumed to represent a
    fully-qualified table ID, and the latter’s data will be fetched.

Returns:

    A [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) with the query results.

**NOTE**: All queries run using this magic will run using the context
`credentials`.


### _class_ google.cloud.bigquery.magics.magics.Context()
Storage for objects to be used throughout an IPython notebook session.

A Context object is initialized when the `magics` module is imported,
and can be found at `google.cloud.bigquery.magics.context`.


#### _property_ bigquery_client_options()
client options to be
used through IPython magics.

Note::

    The client options do not need to be explicitly defined if no
    special network connections are required. Normally you would be
    using the [https://bigquery.googleapis.com/](https://bigquery.googleapis.com/) end point.

### Example

Manually setting the endpoint:

```python
>>> from google.cloud.bigquery import magics
>>> client_options = {}
>>> client_options['api_endpoint'] = "https://some.special.url"
>>> magics.context.bigquery_client_options = client_options
```


* **Type**

    [google.api_core.client_options.ClientOptions](https://googleapis.dev/python/google-api-core/latest/client_options.html#google.api_core.client_options.ClientOptions)



#### _property_ bqstorage_client_options()
client options to be
used through IPython magics for the storage client.

Note::

    The client options do not need to be explicitly defined if no
    special network connections are required. Normally you would be
    using the [https://bigquerystorage.googleapis.com/](https://bigquerystorage.googleapis.com/) end point.

### Example

Manually setting the endpoint:

```python
>>> from google.cloud.bigquery import magics
>>> client_options = {}
>>> client_options['api_endpoint'] = "https://some.special.url"
>>> magics.context.bqstorage_client_options = client_options
```


* **Type**

    [google.api_core.client_options.ClientOptions](https://googleapis.dev/python/google-api-core/latest/client_options.html#google.api_core.client_options.ClientOptions)



#### _property_ credentials()
Credentials to use for queries
performed through IPython magics.

**NOTE**: These credentials do not need to be explicitly defined if you are
using Application Default Credentials. If you are not using
Application Default Credentials, manually construct a
[`google.auth.credentials.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials) object and set it as
the context credentials as demonstrated in the example below. See
[auth docs](http://google-auth.readthedocs.io/en/latest/user-guide.html#obtaining-credentials) for more information on obtaining credentials.

### Example

Manually setting the context credentials:

```python
>>> from google.cloud.bigquery import magics
>>> from google.oauth2 import service_account
>>> credentials = (service_account
...     .Credentials.from_service_account_file(
...         '/path/to/key.json'))
>>> magics.context.credentials = credentials
```


* **Type**

    [google.auth.credentials.Credentials](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials)



#### _property_ default_query_job_config()
Default job
configuration for queries.

The context’s [`QueryJobConfig`](generated/google.cloud.bigquery.job.QueryJobConfig.md#google.cloud.bigquery.job.QueryJobConfig) is
used for queries. Some properties can be overridden with arguments to
the magics.

### Example

Manually setting the default value for `maximum_bytes_billed`
to 100 MB:

```python
>>> from google.cloud.bigquery import magics
>>> magics.context.default_query_job_config.maximum_bytes_billed = 100000000
```


* **Type**

    [google.cloud.bigquery.job.QueryJobConfig](generated/google.cloud.bigquery.job.QueryJobConfig.md#google.cloud.bigquery.job.QueryJobConfig)



#### _property_ progress_bar_type()
Default progress bar type to use to display progress bar while
executing queries through IPython magics.

Note::

    Install the `tqdm` package to use this feature.

### Example

Manually setting the progress_bar_type:

```python
>>> from google.cloud.bigquery import magics
>>> magics.context.progress_bar_type = "tqdm_notebook"
```


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ project()
Default project to use for queries performed through IPython
magics.

**NOTE**: The project does not need to be explicitly defined if you have an
environment default project set. If you do not have a default
project set in your environment, manually assign the project as
demonstrated in the example below.

### Example

Manually setting the context project:

```python
>>> from google.cloud.bigquery import magics
>>> magics.context.project = 'my-project'
```


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)
