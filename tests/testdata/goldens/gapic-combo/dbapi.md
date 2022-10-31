# DB-API Reference

Google BigQuery implementation of the Database API Specification v2.0.

This module implements the [Python Database API Specification v2.0 (DB-API)](https://www.python.org/dev/peps/pep-0249/)
for Google BigQuery.


### google.cloud.bigquery.dbapi.Binary(data)
Contruct a DB-API binary value.


* **Parameters**

    **data** (*bytes-like*) – An object containing binary data and that
    can be converted to bytes with the bytes builtin.



* **Returns**

    The binary data as a bytes object.



* **Return type**

    [bytes](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)



### _class_ google.cloud.bigquery.dbapi.Connection(client=None, bqstorage_client=None)
Bases: [`object`](https://python.readthedocs.io/en/latest/library/functions.html#object)

DB-API Connection to Google BigQuery.


* **Parameters**

    
    * **client** (*Optional**[**google.cloud.bigquery.Client**]*) – A REST API client used to connect to BigQuery. If not passed, a
    client is created using default options inferred from the environment.


    * **bqstorage_client** (*Optional**[**google.cloud.bigquery_storage_v1.BigQueryReadClient**]*) – A client that uses the faster BigQuery Storage API to fetch rows from
    BigQuery. If not passed, it is created using the same credentials
    as `client` (provided that BigQuery Storage dependencies are installed).

    If both clients are available, `bqstorage_client` is used for
    fetching query results.




#### close()
Close the connection and any cursors created from it.

Any BigQuery clients explicitly passed to the constructor are *not*
closed, only those created by the connection instance itself.


#### commit()
No-op, but for consistency raise an error if connection is closed.


#### cursor()
Return a new cursor object.


* **Returns**

    A DB-API cursor that uses this connection.



* **Return type**

    google.cloud.bigquery.dbapi.Cursor



### _class_ google.cloud.bigquery.dbapi.Cursor(connection)
Bases: [`object`](https://python.readthedocs.io/en/latest/library/functions.html#object)

DB-API Cursor to Google BigQuery.


* **Parameters**

    **connection** (*google.cloud.bigquery.dbapi.Connection*) – A DB-API connection to Google BigQuery.



#### close()
Mark the cursor as closed, preventing its further use.


#### execute(operation, parameters=None, job_id=None, job_config=None)
Prepare and execute a database operation.

**NOTE**: When setting query parameters, values which are “text”
(`unicode` in Python2, `str` in Python3) will use
the ‘STRING’ BigQuery type. Values which are “bytes” (`str` in
Python2, `bytes` in Python3), will use using the ‘BYTES’ type.

A ~datetime.datetime parameter without timezone information uses
the ‘DATETIME’ BigQuery type (example: Global Pi Day Celebration
March 14, 2017 at 1:59pm). A ~datetime.datetime parameter with
timezone information uses the ‘TIMESTAMP’ BigQuery type (example:
a wedding on April 29, 2011 at 11am, British Summer Time).

For more information about BigQuery data types, see:
[https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

`STRUCT`/`RECORD` and `REPEATED` query parameters are not
yet supported. See:
[https://github.com/GoogleCloudPlatform/google-cloud-python/issues/3524](https://github.com/GoogleCloudPlatform/google-cloud-python/issues/3524)


* **Parameters**

    
    * **operation** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – A Google BigQuery query string.


    * **parameters** (*Union**[**Mapping**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Any**]**, **Sequence**[**Any**]**]*) – (Optional) dictionary or sequence of parameter values.


    * **job_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The job_id to use. If not set, a job ID
    is generated at random.


    * **job_config** ([*google.cloud.bigquery.job.QueryJobConfig*](generated/google.cloud.bigquery.job.QueryJobConfig.md#google.cloud.bigquery.job.QueryJobConfig)) – (Optional) Extra configuration options for the query job.



#### executemany(operation, seq_of_parameters)
Prepare and execute a database operation multiple times.


* **Parameters**

    
    * **operation** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – A Google BigQuery query string.


    * **seq_of_parameters** (*Union**[**Sequence**[**Mapping**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Any**]**, **Sequence**[**Any**]**]**]*) – Sequence of many sets of parameter values.



#### fetchall()
Fetch all remaining results from the last `execute\*()` call.

**NOTE**: If a dry run query was executed, no rows are returned.


* **Returns**

    A list of all the rows in the results.



* **Return type**

    List[Tuple]



* **Raises**

    **google.cloud.bigquery.dbapi.InterfaceError** – if called before `execute()`.



#### fetchmany(size=None)
Fetch multiple results from the last `execute\*()` call.

**NOTE**: If a dry run query was executed, no rows are returned.

**NOTE**: The size parameter is not used for the request/response size.
Set the `arraysize` attribute before calling `execute()` to
set the batch size.


* **Parameters**

    **size** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) Maximum number of rows to return. Defaults to the
    `arraysize` property value. If `arraysize` is not set, it
    defaults to `1`.



* **Returns**

    A list of rows.



* **Return type**

    List[Tuple]



* **Raises**

    **google.cloud.bigquery.dbapi.InterfaceError** – if called before `execute()`.



#### fetchone()
Fetch a single row from the results of the last `execute\*()` call.

**NOTE**: If a dry run query was executed, no rows are returned.


* **Returns**

    A tuple representing a row or `None` if no more data is
    available.



* **Return type**

    Tuple



* **Raises**

    **google.cloud.bigquery.dbapi.InterfaceError** – if called before `execute()`.



#### setinputsizes(sizes)
No-op, but for consistency raise an error if cursor is closed.


#### setoutputsize(size, column=None)
No-op, but for consistency raise an error if cursor is closed.


### _exception_ google.cloud.bigquery.dbapi.DataError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API error due to problems with the processed data.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.DatabaseError()
Bases: `google.cloud.bigquery.dbapi.exceptions.Error`

DB-API error related to the database.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### google.cloud.bigquery.dbapi.Date()
alias of [`datetime.date`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)


### google.cloud.bigquery.dbapi.DateFromTicks(timestamp, /)
Create a date from a POSIX timestamp.

The timestamp is a number, e.g. created via time.time(), that is interpreted
as local time.


### _exception_ google.cloud.bigquery.dbapi.Error()
Bases: [`Exception`](https://python.readthedocs.io/en/latest/library/exceptions.html#Exception)

Exception representing all non-warning DB-API errors.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.IntegrityError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API error when integrity of the database is affected.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.InterfaceError()
Bases: `google.cloud.bigquery.dbapi.exceptions.Error`

DB-API error related to the database interface.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.InternalError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API error when the database encounters an internal error.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.NotSupportedError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API error for operations not supported by the database or API.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.OperationalError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API error related to the database operation.

These errors are not necessarily under the control of the programmer.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### _exception_ google.cloud.bigquery.dbapi.ProgrammingError()
Bases: `google.cloud.bigquery.dbapi.exceptions.DatabaseError`

DB-API exception raised for programming errors.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### google.cloud.bigquery.dbapi.Time()
alias of [`datetime.time`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.time)


### google.cloud.bigquery.dbapi.TimeFromTicks(ticks, tz=None)
Construct a DB-API time value from the given ticks value.


* **Parameters**

    
    * **ticks** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)) – a number of seconds since the epoch; see the documentation of the
    standard Python time module for details.


    * **tz** ([*datetime.tzinfo*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.tzinfo)) – (Optional) time zone to use for conversion



* **Returns**

    time represented by ticks.



* **Return type**

    [datetime.time](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.time)



### google.cloud.bigquery.dbapi.Timestamp()
alias of [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)


### google.cloud.bigquery.dbapi.TimestampFromTicks()
timestamp[, tz] -> tz’s local time from POSIX timestamp.


### _exception_ google.cloud.bigquery.dbapi.Warning()
Bases: [`Exception`](https://python.readthedocs.io/en/latest/library/exceptions.html#Exception)

Exception raised for important DB-API warnings.


#### with_traceback()
Exception.with_traceback(tb) –
set self.__traceback__ to tb and return self.


### google.cloud.bigquery.dbapi.connect(client=None, bqstorage_client=None)
Construct a DB-API connection to Google BigQuery.


* **Parameters**

    
    * **client** (*Optional**[**google.cloud.bigquery.Client**]*) – A REST API client used to connect to BigQuery. If not passed, a
    client is created using default options inferred from the environment.


    * **bqstorage_client** (*Optional**[**google.cloud.bigquery_storage_v1.BigQueryReadClient**]*) – A client that uses the faster BigQuery Storage API to fetch rows from
    BigQuery. If not passed, it is created using the same credentials
    as `client` (provided that BigQuery Storage dependencies are installed).

    If both clients are available, `bqstorage_client` is used for
    fetching query results.




* **Returns**

    A new DB-API connection to BigQuery.



* **Return type**

    google.cloud.bigquery.dbapi.Connection


# DB-API Query-Parameter Syntax

The BigQuery DB-API uses the qmark [parameter style](https://www.python.org/dev/peps/pep-0249/#paramstyle) for
unnamed/positional parameters and the pyformat parameter style for
named parameters.

An example of a query using unnamed parameters:

```default
insert into people (name, income) values (?, ?)
```

and using named parameters:

```default
insert into people (name, income) values (%(name)s, %(income)s)
```

## Providing explicit type information

BigQuery requires type information for parameters.  The BigQuery
DB-API can usually determine parameter types for parameters based on
provided values.  Sometimes, however, types can’t be determined (for
example when None is passed) or are determined incorrectly (for
example when passing a floating-point value to a numeric column).

The BigQuery DB-API provides an extended parameter syntax.  For named
parameters, a BigQuery type is provided after the name separated by a
colon, as in:

```default
insert into people (name, income) values (%(name:string)s, %(income:numeric)s)
```

For unnamed parameters, use the named syntax with a type, but no
name, as in:

```default
insert into people (name, income) values (%(:string)s, %(:numeric)s)
```

Providing type information is the *only* way to pass struct data:

```default
cursor.execute(
  "insert into points (point) values (%(:struct<x float64, y float64>)s)",
  [{"x": 10, "y": 20}],
  )
```
