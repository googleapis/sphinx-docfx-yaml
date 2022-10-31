# BigQuery Enums


### _class_ google.cloud.bigquery.enums.AutoRowIDs(value)
How to handle automatic insert IDs when inserting rows as a stream.


#### DISABLED(_ = _ )

#### GENERATE_UUID(_ = _ )

### _class_ google.cloud.bigquery.enums.Compression()
The compression type to use for exported files. The default value is
`NONE`.

`DEFLATE` and `SNAPPY` are
only supported for Avro.


#### DEFLATE(_ = 'DEFLATE_ )
Specifies DEFLATE format.


#### GZIP(_ = 'GZIP_ )
Specifies GZIP format.


#### NONE(_ = 'NONE_ )
Specifies no compression.


#### SNAPPY(_ = 'SNAPPY_ )
Specifies SNAPPY format.


### _class_ google.cloud.bigquery.enums.CreateDisposition()
Specifies whether the job is allowed to create new tables. The default
value is `CREATE_IF_NEEDED`.

Creation, truncation and append actions occur as one atomic update
upon job completion.


#### CREATE_IF_NEEDED(_ = 'CREATE_IF_NEEDED_ )
If the table does not exist, BigQuery creates the table.


#### CREATE_NEVER(_ = 'CREATE_NEVER_ )
The table must already exist. If it does not, a ‘notFound’ error is
returned in the job result.


### _class_ google.cloud.bigquery.enums.DecimalTargetType()
The data types that could be used as a target type when converting decimal values.

[https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#DecimalTargetType](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#DecimalTargetType)

**Versionadded:** New in version 2.21.0.


#### BIGNUMERIC(_ = 'BIGNUMERIC_ )
Decimal values could be converted to BIGNUMERIC type.


#### NUMERIC(_ = 'NUMERIC_ )
Decimal values could be converted to NUMERIC type.


#### STRING(_ = 'STRING_ )
Decimal values could be converted to STRING type.


### _class_ google.cloud.bigquery.enums.DestinationFormat()
The exported file format. The default value is `CSV`.

Tables with nested or repeated fields cannot be exported as CSV.


#### AVRO(_ = 'AVRO_ )
Specifies Avro format.


#### CSV(_ = 'CSV_ )
Specifies CSV format.


#### NEWLINE_DELIMITED_JSON(_ = 'NEWLINE_DELIMITED_JSON_ )
Specifies newline delimited JSON format.


#### PARQUET(_ = 'PARQUET_ )
Specifies Parquet format.


### _class_ google.cloud.bigquery.enums.DeterminismLevel()
Specifies determinism level for JavaScript user-defined functions (UDFs).

[https://cloud.google.com/bigquery/docs/reference/rest/v2/routines#DeterminismLevel](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines#DeterminismLevel)


#### DETERMINISM_LEVEL_UNSPECIFIED(_ = 'DETERMINISM_LEVEL_UNSPECIFIED_ )
The determinism of the UDF is unspecified.


#### DETERMINISTIC(_ = 'DETERMINISTIC_ )
The UDF is deterministic, meaning that 2 function calls with the same inputs
always produce the same result, even across 2 query runs.


#### NOT_DETERMINISTIC(_ = 'NOT_DETERMINISTIC_ )
The UDF is not deterministic.


### _class_ google.cloud.bigquery.enums.Encoding()
The character encoding of the data. The default is `UTF_8`.

BigQuery decodes the data after the raw, binary data has been
split using the values of the quote and fieldDelimiter properties.


#### ISO_8859_1(_ = 'ISO-8859-1_ )
Specifies ISO-8859-1 encoding.


#### UTF_8(_ = 'UTF-8_ )
Specifies UTF-8 encoding.


### _class_ google.cloud.bigquery.enums.EntityTypes(value)
Enum of allowed entity type names in AccessEntry


#### DATASET(_ = 'dataset_ )

#### DOMAIN(_ = 'domain_ )

#### GROUP_BY_EMAIL(_ = 'groupByEmail_ )

#### IAM_MEMBER(_ = 'iamMember_ )

#### ROUTINE(_ = 'routine_ )

#### SPECIAL_GROUP(_ = 'specialGroup_ )

#### USER_BY_EMAIL(_ = 'userByEmail_ )

#### VIEW(_ = 'view_ )

### _class_ google.cloud.bigquery.enums.KeyResultStatementKind()
Determines which statement in the script represents the “key result”.

The “key result” is used to populate the schema and query results of the script job.

[https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#keyresultstatementkind](https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#keyresultstatementkind)


#### FIRST_SELECT(_ = 'FIRST_SELECT_ )

#### KEY_RESULT_STATEMENT_KIND_UNSPECIFIED(_ = 'KEY_RESULT_STATEMENT_KIND_UNSPECIFIED_ )

#### LAST(_ = 'LAST_ )

### _class_ google.cloud.bigquery.enums.QueryApiMethod(value)
API method used to start the query. The default value is
`INSERT`.


#### INSERT(_ = 'INSERT_ )
Submit a query job by using the [jobs.insert REST API method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/insert).

This supports all job configuration options.


#### QUERY(_ = 'QUERY_ )
Submit a query job by using the [jobs.query REST API method](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query).

Differences from `INSERT`:


* Many parameters and job configuration options, including job ID and
destination table, cannot be used
with this API method. See the [jobs.query REST API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query) for
the complete list of supported configuration options.


* API blocks up to a specified timeout, waiting for the query to
finish.


* The full job resource (including job statistics) may not be available.
Call [`reload()`](generated/google.cloud.bigquery.job.QueryJob.md#google.cloud.bigquery.job.QueryJob.reload) or
[`get_job()`](generated/google.cloud.bigquery.client.Client.md#google.cloud.bigquery.client.Client.get_job) to get full job
statistics and configuration.


* `query()` can raise API exceptions if
the query fails, whereas the same errors don’t appear until calling
[`result()`](generated/google.cloud.bigquery.job.QueryJob.md#google.cloud.bigquery.job.QueryJob.result) when the `INSERT`
API method is used.


### _class_ google.cloud.bigquery.enums.QueryPriority()
Specifies a priority for the query. The default value is
`INTERACTIVE`.


#### BATCH(_ = 'BATCH_ )
Specifies batch priority.


#### INTERACTIVE(_ = 'INTERACTIVE_ )
Specifies interactive priority.


### _class_ google.cloud.bigquery.enums.SchemaUpdateOption()
Specifies an update to the destination table schema as a side effect of
a load job.


#### ALLOW_FIELD_ADDITION(_ = 'ALLOW_FIELD_ADDITION_ )
Allow adding a nullable field to the schema.


#### ALLOW_FIELD_RELAXATION(_ = 'ALLOW_FIELD_RELAXATION_ )
Allow relaxing a required field in the original schema to nullable.


### _class_ google.cloud.bigquery.enums.SourceFormat()
The format of the data files. The default value is `CSV`.

Note that the set of allowed values for loading data is different
than the set used for external data sources (see
[`ExternalSourceFormat`](generated/google.cloud.bigquery.external_config.ExternalSourceFormat.md#google.cloud.bigquery.external_config.ExternalSourceFormat)).


#### AVRO(_ = 'AVRO_ )
Specifies Avro format.


#### CSV(_ = 'CSV_ )
Specifies CSV format.


#### DATASTORE_BACKUP(_ = 'DATASTORE_BACKUP_ )
Specifies datastore backup format


#### NEWLINE_DELIMITED_JSON(_ = 'NEWLINE_DELIMITED_JSON_ )
Specifies newline delimited JSON format.


#### ORC(_ = 'ORC_ )
Specifies Orc format.


#### PARQUET(_ = 'PARQUET_ )
Specifies Parquet format.


### _class_ google.cloud.bigquery.enums.SqlTypeNames(value)
Enum of allowed SQL type names in schema.SchemaField.


#### BIGDECIMAL(_ = 'BIGNUMERIC_ )

#### BIGNUMERIC(_ = 'BIGNUMERIC_ )

#### BOOL(_ = 'BOOLEAN_ )

#### BOOLEAN(_ = 'BOOLEAN_ )

#### BYTES(_ = 'BYTES_ )

#### DATE(_ = 'DATE_ )

#### DATETIME(_ = 'DATETIME_ )

#### DECIMAL(_ = 'NUMERIC_ )

#### FLOAT(_ = 'FLOAT_ )

#### FLOAT64(_ = 'FLOAT_ )

#### GEOGRAPHY(_ = 'GEOGRAPHY_ )

#### INT64(_ = 'INTEGER_ )

#### INTEGER(_ = 'INTEGER_ )

#### INTERVAL(_ = 'INTERVAL_ )

#### NUMERIC(_ = 'NUMERIC_ )

#### RECORD(_ = 'RECORD_ )

#### STRING(_ = 'STRING_ )

#### STRUCT(_ = 'RECORD_ )

#### TIME(_ = 'TIME_ )

#### TIMESTAMP(_ = 'TIMESTAMP_ )

### _class_ google.cloud.bigquery.enums.StandardSqlTypeNames(value)
An enumeration.


#### ARRAY(_ = 'ARRAY_ )

#### BIGNUMERIC(_ = 'BIGNUMERIC_ )

#### BOOL(_ = 'BOOL_ )

#### BYTES(_ = 'BYTES_ )

#### DATE(_ = 'DATE_ )

#### DATETIME(_ = 'DATETIME_ )

#### FLOAT64(_ = 'FLOAT64_ )

#### GEOGRAPHY(_ = 'GEOGRAPHY_ )

#### INT64(_ = 'INT64_ )

#### INTERVAL(_ = 'INTERVAL_ )

#### JSON(_ = 'JSON_ )

#### NUMERIC(_ = 'NUMERIC_ )

#### STRING(_ = 'STRING_ )

#### STRUCT(_ = 'STRUCT_ )

#### TIME(_ = 'TIME_ )

#### TIMESTAMP(_ = 'TIMESTAMP_ )

#### TYPE_KIND_UNSPECIFIED(_ = 'TYPE_KIND_UNSPECIFIED_ )

### _class_ google.cloud.bigquery.enums.WriteDisposition()
Specifies the action that occurs if destination table already exists.

The default value is `WRITE_APPEND`.

Each action is atomic and only occurs if BigQuery is able to complete
the job successfully. Creation, truncation and append actions occur as one
atomic update upon job completion.


#### WRITE_APPEND(_ = 'WRITE_APPEND_ )
If the table already exists, BigQuery appends the data to the table.


#### WRITE_EMPTY(_ = 'WRITE_EMPTY_ )
If the table already exists and contains data, a ‘duplicate’ error is
returned in the job result.


#### WRITE_TRUNCATE(_ = 'WRITE_TRUNCATE_ )
If the table already exists, BigQuery overwrites the table data.
