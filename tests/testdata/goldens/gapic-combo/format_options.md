# BigQuery Format Options


### _class_ google.cloud.bigquery.format_options.AvroOptions()
Options if source format is set to AVRO.


#### _classmethod_ from_api_repr(resource: [Dict](https://python.readthedocs.io/en/latest/library/typing.html#typing.Dict)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)])
Factory: construct an instance from a resource dict.


* **Parameters**

    **resource** (*Dict**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, *[*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*]*) – Definition of a `AvroOptions` instance in
    the same representation as is returned from the API.



* **Returns**

    Configuration parsed from `resource`.



* **Return type**

    `AvroOptions`



#### to_api_repr()
Build an API representation of this object.


* **Returns**

    A dictionary in the format used by the BigQuery API.



* **Return type**

    Dict[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)]



#### _property_ use_avro_logical_types(_: Optional[[bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)_ )
[Optional] If sourceFormat is set to ‘AVRO’, indicates whether to
interpret logical types as the corresponding BigQuery data type (for
example, TIMESTAMP), instead of using the raw type (for example,
INTEGER).

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#AvroOptions.FIELDS.use_avro_logical_types](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#AvroOptions.FIELDS.use_avro_logical_types)


### _class_ google.cloud.bigquery.format_options.ParquetOptions()
Additional options if the PARQUET source format is used.


#### _property_ enable_list_inference(_: [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool_ )
Indicates whether to use schema inference specifically for Parquet LIST
logical type.

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ParquetOptions.FIELDS.enable_list_inference](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ParquetOptions.FIELDS.enable_list_inference)


#### _property_ enum_as_string(_: [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool_ )
Indicates whether to infer Parquet ENUM logical type as STRING instead of
BYTES by default.

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ParquetOptions.FIELDS.enum_as_string](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#ParquetOptions.FIELDS.enum_as_string)


#### _classmethod_ from_api_repr(resource: [Dict](https://python.readthedocs.io/en/latest/library/typing.html#typing.Dict)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)])
Factory: construct an instance from a resource dict.


* **Parameters**

    **resource** (*Dict**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, *[*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)*]*) – Definition of a `ParquetOptions` instance in
    the same representation as is returned from the API.



* **Returns**

    Configuration parsed from `resource`.



* **Return type**

    `ParquetOptions`



#### to_api_repr()
Build an API representation of this object.


* **Returns**

    A dictionary in the format used by the BigQuery API.



* **Return type**

    Dict[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)]
