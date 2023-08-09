# Function

The Function model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaxial_id** | **object** |  | 
**description** | **object** |  | 
**function_name** | **object** |  | 
**id** | **object** |  | [optional] 

## Example

```python
from coaxial.models.function import Function

# TODO update the JSON string below
json = "{}"
# create an instance of Function from a JSON string
function_instance = Function.from_json(json)
# print the JSON string representation of the object
print Function.to_json()

# convert the object into a dict
function_dict = function_instance.to_dict()
# create an instance of Function from a dict
function_form_dict = function.from_dict(function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


