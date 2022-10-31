# Query Resource Classes

BigQuery query processing.


### _class_ google.cloud.bigquery.query.ArrayQueryParameter(name, array_type, values)
Named / positional query parameters for array values.


* **Parameters**

    
    * **name** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – Parameter name, used via `@foo` syntax.  If None, the
    parameter can only be addressed via position (`?`).


    * **array_type** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **ScalarQueryParameterType**, **StructQueryParameterType**]*) – The type of array elements. If given as a string, it must be one of
    ‘STRING’, ‘INT64’, ‘FLOAT64’, ‘NUMERIC’, ‘BIGNUMERIC’, ‘BOOL’,
    ‘TIMESTAMP’, ‘DATE’, or ‘STRUCT’/’RECORD’.
    If the type is `'STRUCT'`/`'RECORD'` and `values` is empty,
    the exact item type cannot be deduced, thus a `StructQueryParameterType`
    instance needs to be passed in.


    * **values** (*List**[**appropriate type**]*) – The parameter array values.



#### _classmethod_ from_api_repr(resource: [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict))
Factory: construct parameter from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.ArrayQueryParameter



#### _classmethod_ positional(array_type: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), values: [list](https://python.readthedocs.io/en/latest/library/stdtypes.html#list))
Factory for positional parameters.


* **Parameters**

    
    * **array_type** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **ScalarQueryParameterType**, **StructQueryParameterType**]*) – The type of array elements. If given as a string, it must be one of
    ‘STRING’, ‘INT64’, ‘FLOAT64’, ‘NUMERIC’, ‘BIGNUMERIC’,
    ‘BOOL’, ‘TIMESTAMP’, ‘DATE’, or ‘STRUCT’/’RECORD’.
    If the type is `'STRUCT'`/`'RECORD'` and `values` is empty,
    the exact item type cannot be deduced, thus a `StructQueryParameterType`
    instance needs to be passed in.


    * **values** (*List**[**appropriate type**]*) – The parameter array values.



* **Returns**

    Instance without name



* **Return type**

    google.cloud.bigquery.query.ArrayQueryParameter



#### to_api_repr()
Construct JSON API representation for the parameter.


* **Returns**

    JSON mapping



* **Return type**

    Dict



### _class_ google.cloud.bigquery.query.ArrayQueryParameterType(array_type, \*, name=None, description=None)
Type representation for array query parameters.


* **Parameters**

    
    * **array_type** (*Union**[**ScalarQueryParameterType**, **StructQueryParameterType**]*) – The type of array elements.


    * **name** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The name of the query parameter. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.


    * **description** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The query parameter description. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.



#### _classmethod_ from_api_repr(resource)
Factory: construct parameter type from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.ArrayQueryParameterType



#### to_api_repr()
Construct JSON API representation for the parameter type.


* **Returns**

    JSON mapping



* **Return type**

    Dict



### _class_ google.cloud.bigquery.query.ConnectionProperty(key: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str) = '', value: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str) = '')
A connection-level property to customize query behavior.

See
[https://cloud.google.com/bigquery/docs/reference/rest/v2/ConnectionProperty](https://cloud.google.com/bigquery/docs/reference/rest/v2/ConnectionProperty)


* **Parameters**

    
    * **key** – The key of the property to set, for example, `'time_zone'` or
    `'session_id'`.


    * **value** – The value of the property to set.



#### _classmethod_ from_api_repr(resource)
Construct `ConnectionProperty`
from JSON resource.


* **Parameters**

    **resource** – JSON representation.



* **Returns**

    A connection property.



#### _property_ key(_: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str_ )
Name of the property.

For example:


* `time_zone`


* `session_id`


#### to_api_repr()
Construct JSON API representation for the connection property.


* **Returns**

    JSON mapping



#### _property_ value(_: [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str_ )
Value of the property.


### _class_ google.cloud.bigquery.query.ScalarQueryParameter(name: [Optional](https://python.readthedocs.io/en/latest/library/typing.html#typing.Optional)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)], type_: [Optional](https://python.readthedocs.io/en/latest/library/typing.html#typing.Optional)[[Union](https://python.readthedocs.io/en/latest/library/typing.html#typing.Union)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), google.cloud.bigquery.query.ScalarQueryParameterType]], value: [Optional](https://python.readthedocs.io/en/latest/library/typing.html#typing.Optional)[[Union](https://python.readthedocs.io/en/latest/library/typing.html#typing.Union)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [int](https://python.readthedocs.io/en/latest/library/functions.html#int), [float](https://python.readthedocs.io/en/latest/library/functions.html#float), [decimal.Decimal](https://python.readthedocs.io/en/latest/library/decimal.html#decimal.Decimal), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool), [datetime.datetime](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime), [datetime.date](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)]])
Named / positional query parameters for scalar values.


* **Parameters**

    
    * **name** – Parameter name, used via `@foo` syntax.  If None, the
    parameter can only be addressed via position (`?`).


    * **type** – Name of parameter type. See
    [`google.cloud.bigquery.enums.SqlTypeNames`](enums.md#google.cloud.bigquery.enums.SqlTypeNames) and
    `google.cloud.bigquery.query.SqlParameterScalarTypes` for
    supported types.


    * **value** – The scalar parameter value.



#### _classmethod_ from_api_repr(resource: [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict))
Factory: construct parameter from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.ScalarQueryParameter



#### _classmethod_ positional(type_: [Union](https://python.readthedocs.io/en/latest/library/typing.html#typing.Union)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), google.cloud.bigquery.query.ScalarQueryParameterType], value: [Optional](https://python.readthedocs.io/en/latest/library/typing.html#typing.Optional)[[Union](https://python.readthedocs.io/en/latest/library/typing.html#typing.Union)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str), [int](https://python.readthedocs.io/en/latest/library/functions.html#int), [float](https://python.readthedocs.io/en/latest/library/functions.html#float), [decimal.Decimal](https://python.readthedocs.io/en/latest/library/decimal.html#decimal.Decimal), [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool), [datetime.datetime](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime), [datetime.date](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)]])
Factory for positional paramater.


* **Parameters**

    
    * **type** – Name of parameter type.  One of ‘STRING’, ‘INT64’,
    ‘FLOAT64’, ‘NUMERIC’, ‘BIGNUMERIC’, ‘BOOL’, ‘TIMESTAMP’, ‘DATETIME’, or
    ‘DATE’.


    * **value** – The scalar parameter value.



* **Returns**

    Instance without name



* **Return type**

    google.cloud.bigquery.query.ScalarQueryParameter



#### to_api_repr()
Construct JSON API representation for the parameter.


* **Returns**

    JSON mapping



* **Return type**

    Dict



### _class_ google.cloud.bigquery.query.ScalarQueryParameterType(type_, \*, name=None, description=None)
Type representation for scalar query parameters.


* **Parameters**

    
    * **type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – One of ‘STRING’, ‘INT64’, ‘FLOAT64’, ‘NUMERIC’, ‘BOOL’, ‘TIMESTAMP’,
    ‘DATETIME’, or ‘DATE’.


    * **name** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The name of the query parameter. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.


    * **description** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The query parameter description. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.



#### _classmethod_ from_api_repr(resource)
Factory: construct parameter type from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.ScalarQueryParameterType



#### to_api_repr()
Construct JSON API representation for the parameter type.


* **Returns**

    JSON mapping



* **Return type**

    Dict



#### with_name(new_name: [Optional](https://python.readthedocs.io/en/latest/library/typing.html#typing.Optional)[[str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)])
Return a copy of the instance with `name` set to `new_name`.


* **Parameters**

    **name** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **None**]*) – The new name of the query parameter type. If `None`, the existing
    name is cleared.



* **Returns**

    A new instance with updated name.



* **Return type**

    google.cloud.bigquery.query.ScalarQueryParameterType



### _class_ google.cloud.bigquery.query.SqlParameterScalarTypes()
Supported scalar SQL query parameter types as type objects.


### _class_ google.cloud.bigquery.query.StructQueryParameter(name, \*sub_params)
Named / positional query parameters for struct values.


* **Parameters**

    
    * **name** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – Parameter name, used via `@foo` syntax.  If None, the
    parameter can only be addressed via position (`?`).


    * **(****Union****[****Tuple****[** (*sub_params*) – google.cloud.bigquery.query.ScalarQueryParameter,
    google.cloud.bigquery.query.ArrayQueryParameter,
    google.cloud.bigquery.query.StructQueryParameter


    * **]****]****)** – The sub-parameters for the struct



#### _classmethod_ from_api_repr(resource: [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict))
Factory: construct parameter from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.StructQueryParameter



#### _classmethod_ positional(\*sub_params)
Factory for positional parameters.


* **Parameters**

    
    * **(****Union****[****Tuple****[** (*sub_params*) – google.cloud.bigquery.query.ScalarQueryParameter,
    google.cloud.bigquery.query.ArrayQueryParameter,
    google.cloud.bigquery.query.StructQueryParameter


    * **]****]****)** – The sub-parameters for the struct



* **Returns**

    Instance without name



* **Return type**

    google.cloud.bigquery.query.StructQueryParameter



#### to_api_repr()
Construct JSON API representation for the parameter.


* **Returns**

    JSON mapping



* **Return type**

    Dict



### _class_ google.cloud.bigquery.query.StructQueryParameterType(\*fields, name=None, description=None)
Type representation for struct query parameters.


* **Parameters**

    
    * **fields** (*Iterable**[**Union**[             **ArrayQueryParameterType**, **ScalarQueryParameterType**, **StructQueryParameterType**         ]**]*) – An non-empty iterable describing the struct’s field types.


    * **name** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The name of the query parameter. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.


    * **description** (*Optional**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]*) – The query parameter description. Primarily used if the type is
    one of the subfields in `StructQueryParameterType` instance.



#### _classmethod_ from_api_repr(resource)
Factory: construct parameter type from JSON resource.


* **Parameters**

    **resource** (*Dict*) – JSON mapping of parameter



* **Returns**

    Instance



* **Return type**

    google.cloud.bigquery.query.StructQueryParameterType



#### to_api_repr()
Construct JSON API representation for the parameter type.


* **Returns**

    JSON mapping



* **Return type**

    Dict



### _class_ google.cloud.bigquery.query.UDFResource(udf_type, value)
Describe a single user-defined function (UDF) resource.


* **Parameters**

    
    * **udf_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The type of the resource (‘inlineCode’ or ‘resourceUri’)


    * **value** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The inline code or resource URI.


See:
[https://cloud.google.com/bigquery/user-defined-functions#api](https://cloud.google.com/bigquery/user-defined-functions#api)
