# Common Job Resource Classes

Base classes and helpers for job classes.


### _class_ google.cloud.bigquery.job.base.ReservationUsage(name, slot_ms)
Job resource usage for a reservation.

Create new instance of ReservationUsage(name, slot_ms)


#### count(value, /)
Return number of occurrences of value.


#### index(value, start=0, stop=9223372036854775807, /)
Return first index of value.

Raises ValueError if the value is not present.


#### name()
Reservation name or “unreserved” for on-demand resources usage.


#### slot_ms()
Total slot milliseconds used by the reservation for a particular job.


### _class_ google.cloud.bigquery.job.base.ScriptStackFrame(resource)
Stack frame showing the line/column/procedure name where the current
evaluation happened.


* **Parameters**

    **resource** (*Map**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Any**]*) – JSON representation of object.



#### _property_ end_column()
One-based end column.


* **Type**

    [int](https://python.readthedocs.io/en/latest/library/functions.html#int)



#### _property_ end_line()
One-based end line.


* **Type**

    [int](https://python.readthedocs.io/en/latest/library/functions.html#int)



#### _property_ procedure_id()
Name of the active procedure.

Omitted if in a top-level script.


* **Type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### _property_ start_column()
One-based start column.


* **Type**

    [int](https://python.readthedocs.io/en/latest/library/functions.html#int)



#### _property_ start_line()
One-based start line.


* **Type**

    [int](https://python.readthedocs.io/en/latest/library/functions.html#int)



#### _property_ text()
Text of the current statement/expression.


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



### _class_ google.cloud.bigquery.job.base.ScriptStatistics(resource)
Statistics for a child job of a script.


* **Parameters**

    **resource** (*Map**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Any**]*) – JSON representation of object.



#### _property_ evaluation_kind(_: Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)_ )
Indicates the type of child job.

Possible values include `STATEMENT` and `EXPRESSION`.


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ stack_frames(_: Sequence[google.cloud.bigquery.job.base.ScriptStackFrame_ )
Stack trace where the current evaluation happened.

Shows line/column/procedure name of each frame on the stack at the
point where the current evaluation happened.

The leaf frame is first, the primary script is last.


### _class_ google.cloud.bigquery.job.base.SessionInfo(resource)
[Preview] Information of the session if this job is part of one.

**Versionadded:** New in version 2.29.0.


* **Parameters**

    **resource** (*Map**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Any**]*) – JSON representation of object.



#### _property_ session_id(_: Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)_ )
The ID of the session.


### _class_ google.cloud.bigquery.job.base.TransactionInfo(transaction_id: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str))
[Alpha] Information of a multi-statement transaction.

[https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#TransactionInfo](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#TransactionInfo)

**Versionadded:** New in version 2.24.0.

Create new instance of TransactionInfo(transaction_id,)


#### count(value, /)
Return number of occurrences of value.


#### index(value, start=0, stop=9223372036854775807, /)
Return first index of value.

Raises ValueError if the value is not present.


#### transaction_id(_: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str_ )
Output only. ID of the transaction.


### _class_ google.cloud.bigquery.job.base.UnknownJob(job_id, client)
A job whose type cannot be determined.


#### add_done_callback(fn)
Add a callback to be executed when the operation is complete.

If the operation is not already complete, this will start a helper
thread to poll for the status of the operation in the background.


* **Parameters**

    **fn** (*Callable**[**Future**]*) – The callback to execute when the operation
    is complete.



#### cancel(client=None, retry: retries.Retry = <google.api_core.retry.Retry object>, timeout: float = None)
API call:  cancel job via a POST request

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/cancel)


* **Parameters**

    
    * **client** (*Optional**[*[*google.cloud.bigquery.client.Client*](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client)*]*) – the client to use.  If not passed, falls back to the
    `client` stored on the current dataset.


    * **retry** (*Optional**[*[*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)*]*) – How to retry the RPC.


    * **timeout** (*Optional**[*[*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)*]*) – The number of seconds to wait for the underlying HTTP transport
    before using `retry`



* **Returns**

    Boolean indicating that the cancel request was sent.



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



#### cancelled()
Check if the job has been cancelled.

This always returns False. It’s not possible to check if a job was
cancelled in the API. This method is here to satisfy the interface
for [`google.api_core.future.Future`](https://googleapis.dev/python/google-api-core/latest/futures.html#google.api_core.future.Future).


* **Returns**

    False



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



#### _property_ created()
Datetime at which the job was created.


* **Returns**

    the creation time (None until set from the server).



* **Return type**

    Optional[[datetime.datetime](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)]



#### done(retry: retries.Retry = <google.api_core.retry.Retry object>, timeout: float = None, reload: bool = True)
Checks if the job is complete.


* **Parameters**

    
    * **retry** (*Optional**[*[*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)*]*) – How to retry the RPC. If the job state is `DONE`, retrying is aborted
    early, as the job will not change anymore.


    * **timeout** (*Optional**[*[*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)*]*) – The number of seconds to wait for the underlying HTTP transport
    before using `retry`.


    * **reload** (*Optional**[*[*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*]*) – If `True`, make an API call to refresh the job state of
    unfinished jobs before checking. Default `True`.



* **Returns**

    True if the job is complete, False otherwise.



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



#### _property_ ended()
Datetime at which the job finished.


* **Returns**

    the end time (None until set from the server).



* **Return type**

    Optional[[datetime.datetime](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)]



#### _property_ error_result()
Error information about the job as a whole.


* **Returns**

    the error information (None until set from the server).



* **Return type**

    Optional[Mapping]



#### _property_ errors()
Information about individual errors generated by the job.


* **Returns**

    the error information (None until set from the server).



* **Return type**

    Optional[List[Mapping]]



#### _property_ etag()
ETag for the job resource.


* **Returns**

    the ETag (None until set from the server).



* **Return type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### exception(timeout=None)
Get the exception from the operation, blocking if necessary.


* **Parameters**

    **timeout** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – How long to wait for the operation to complete.
    If None, wait indefinitely.



* **Returns**

    The operation’s

        error.




* **Return type**

    Optional[google.api_core.GoogleAPICallError]



#### exists(client=None, retry: retries.Retry = <google.api_core.retry.Retry object>, timeout: float = None)
API call:  test for the existence of the job via a GET request

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get)


* **Parameters**

    
    * **client** (*Optional**[*[*google.cloud.bigquery.client.Client*](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client)*]*) – the client to use.  If not passed, falls back to the
    `client` stored on the current dataset.


    * **retry** (*Optional**[*[*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)*]*) – How to retry the RPC.


    * **timeout** (*Optional**[*[*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)*]*) – The number of seconds to wait for the underlying HTTP transport
    before using `retry`.



* **Returns**

    Boolean indicating existence of the job.



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



#### _classmethod_ from_api_repr(resource: [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict), client)
Construct an UnknownJob from the JSON representation.


* **Parameters**

    
    * **resource** (*Dict*) – JSON representation of a job.


    * **client** ([*google.cloud.bigquery.client.Client*](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client)) – Client connected to BigQuery API.



* **Returns**

    Job corresponding to the resource.



* **Return type**

    UnknownJob



#### _property_ job_id()
ID of the job.


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ job_type()
Type of job.


* **Returns**

    one of ‘load’, ‘copy’, ‘extract’, ‘query’.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ labels()
Labels for the job.


* **Type**

    Dict[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### _property_ location()
Location where the job runs.


* **Type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ num_child_jobs()
The number of child jobs executed.

See:
[https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.num_child_jobs](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.num_child_jobs)


* **Returns**

    int



#### _property_ parent_job_id()
Return the ID of the parent job.

See:
[https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.parent_job_id](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobStatistics.FIELDS.parent_job_id)


* **Returns**

    parent job id.



* **Return type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### _property_ path()
URL path for the job’s APIs.


* **Returns**

    the path based on project and job ID.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ project()
Project bound to the job.


* **Returns**

    the project (derived from the client).



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### reload(client=None, retry: retries.Retry = <google.api_core.retry.Retry object>, timeout: float = None)
API call:  refresh job properties via a GET request.

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get)


* **Parameters**

    
    * **client** (*Optional**[*[*google.cloud.bigquery.client.Client*](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client)*]*) – the client to use.  If not passed, falls back to the
    `client` stored on the current dataset.


    * **retry** (*Optional**[*[*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)*]*) – How to retry the RPC.


    * **timeout** (*Optional**[*[*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)*]*) – The number of seconds to wait for the underlying HTTP transport
    before using `retry`.



#### _property_ reservation_usage()
Job resource usage breakdown by reservation.


* **Returns**

    Reservation usage stats. Can be empty if not set from the server.



* **Return type**

    List[[google.cloud.bigquery.job.ReservationUsage](generated/google.cloud.bigquery.job.ReservationUsage.md#google.cloud.bigquery.job.ReservationUsage)]



#### result(retry: retries.Retry = <google.api_core.retry.Retry object>, timeout: float = None)
Start the job and wait for it to complete and get the result.


* **Parameters**

    
    * **retry** (*Optional**[*[*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)*]*) – How to retry the RPC. If the job state is `DONE`, retrying is aborted
    early, as the job will not change anymore.


    * **timeout** (*Optional**[*[*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)*]*) – The number of seconds to wait for the underlying HTTP transport
    before using `retry`.
    If multiple requests are made under the hood, `timeout`
    applies to each individual request.



* **Returns**

    This instance.



* **Return type**

    _AsyncJob



* **Raises**

    
    * **google.cloud.exceptions.GoogleAPICallError** – if the job failed.


    * [**concurrent.futures.TimeoutError**](https://python.readthedocs.io/en/latest/library/concurrent.futures.html#concurrent.futures.TimeoutError) – if the job did not complete in the given timeout.



#### running()
True if the operation is currently running.


#### _property_ script_statistics(_: Optional[google.cloud.bigquery.job.base.ScriptStatistics_ )
Statistics for a child job of a script.


#### _property_ self_link()
URL for the job resource.


* **Returns**

    the URL (None until set from the server).



* **Return type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### _property_ session_info(_: Optional[google.cloud.bigquery.job.base.SessionInfo_ )
[Preview] Information of the session if this job is part of one.

**Versionadded:** New in version 2.29.0.


#### set_exception(exception)
Set the Future’s exception.


#### set_result(result)
Set the Future’s result.


#### _property_ started()
Datetime at which the job was started.


* **Returns**

    the start time (None until set from the server).



* **Return type**

    Optional[[datetime.datetime](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)]



#### _property_ state()
Status of the job.


* **Returns**

    the state (None until set from the server).



* **Return type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]



#### to_api_repr()
Generate a resource for the job.


#### _property_ transaction_info(_: Optional[google.cloud.bigquery.job.base.TransactionInfo_ )
Information of the multi-statement transaction if this job is part of one.

Since a scripting query job can execute multiple transactions, this
property is only expected on child jobs. Use the
[`google.cloud.bigquery.client.Client.list_jobs()`](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client.list_jobs) method with the
`parent_job` parameter to iterate over child jobs.

**Versionadded:** New in version 2.24.0.


#### _property_ user_email()
E-mail address of user who submitted the job.


* **Returns**

    the URL (None until set from the server).



* **Return type**

    Optional[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)]
