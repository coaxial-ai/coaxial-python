# Dataset

The Dataset model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaxial_id** | **object** |  | 
**id** | **object** |  | [optional] 
**metadata** | **object** |  | [optional] 
**source** | **object** |  | 

## Example

```python
from coaxial.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print Dataset.to_json()

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_form_dict = dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


