# CheckAccessByResourceIdRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaxial_id** | **object** |  | 
**user_id** | **object** |  | 

## Example

```python
from coaxial.models.check_access_by_resource_id_request import CheckAccessByResourceIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAccessByResourceIdRequest from a JSON string
check_access_by_resource_id_request_instance = CheckAccessByResourceIdRequest.from_json(json)
# print the JSON string representation of the object
print CheckAccessByResourceIdRequest.to_json()

# convert the object into a dict
check_access_by_resource_id_request_dict = check_access_by_resource_id_request_instance.to_dict()
# create an instance of CheckAccessByResourceIdRequest from a dict
check_access_by_resource_id_request_form_dict = check_access_by_resource_id_request.from_dict(check_access_by_resource_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


