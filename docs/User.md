# User

The User model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_user_id** | **object** |  | 
**email** | **object** |  | 
**first** | **object** |  | 
**id** | **object** |  | 
**imported_at** | **object** |  | [readonly] 
**last** | **object** |  | 
**modified_at** | **object** |  | [readonly] 
**resource_list** | **object** |  | 
**source_metadata** | [**UserInfo**](UserInfo.md) |  | 

## Example

```python
from coaxial.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


