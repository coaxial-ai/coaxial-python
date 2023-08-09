# coaxial.DataIntegrationApi

All URIs are relative to *https://api.coaxial.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrate_custom_dataset**](DataIntegrationApi.md#integrate_custom_dataset) | **POST** /data_integration/custom | Integrate custom datasets
[**integrate_pinecone**](DataIntegrationApi.md#integrate_pinecone) | **POST** /data_integration/pinecone/integrate | Integrate pinecone datasets
[**list_data_integrations**](DataIntegrationApi.md#list_data_integrations) | **GET** /data_integration/list/ | List dataset integrations
[**remove_data_integration**](DataIntegrationApi.md#remove_data_integration) | **POST** /data_integration/remove | Remove dataset integrations


# **integrate_custom_dataset**
> IntegrateCustomDatasetResponse integrate_custom_dataset(integrate_custom_dataset_request)

Integrate custom datasets

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_custom_dataset_request import IntegrateCustomDatasetRequest
from coaxial.models.integrate_custom_dataset_response import IntegrateCustomDatasetResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.DataIntegrationApi(api_client)
    integrate_custom_dataset_request = coaxial.IntegrateCustomDatasetRequest() # IntegrateCustomDatasetRequest | 

    try:
        # Integrate custom datasets
        api_response = api_instance.integrate_custom_dataset(integrate_custom_dataset_request)
        print("The response of DataIntegrationApi->integrate_custom_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntegrationApi->integrate_custom_dataset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_custom_dataset_request** | [**IntegrateCustomDatasetRequest**](IntegrateCustomDatasetRequest.md)|  | 

### Return type

[**IntegrateCustomDatasetResponse**](IntegrateCustomDatasetResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom dataset names in an array of strings |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrate_pinecone**
> IntegratePineconeResponse integrate_pinecone(integrate_pinecone_request)

Integrate pinecone datasets

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_pinecone_request import IntegratePineconeRequest
from coaxial.models.integrate_pinecone_response import IntegratePineconeResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.DataIntegrationApi(api_client)
    integrate_pinecone_request = coaxial.IntegratePineconeRequest() # IntegratePineconeRequest | 

    try:
        # Integrate pinecone datasets
        api_response = api_instance.integrate_pinecone(integrate_pinecone_request)
        print("The response of DataIntegrationApi->integrate_pinecone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntegrationApi->integrate_pinecone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_pinecone_request** | [**IntegratePineconeRequest**](IntegratePineconeRequest.md)|  | 

### Return type

[**IntegratePineconeResponse**](IntegratePineconeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index names in an array of strings |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_integrations**
> ListDataIntegrationsResponse list_data_integrations(user_id=user_id)

List dataset integrations

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.list_data_integrations_response import ListDataIntegrationsResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.DataIntegrationApi(api_client)
    user_id = None # object |  (optional)

    try:
        # List dataset integrations
        api_response = api_instance.list_data_integrations(user_id=user_id)
        print("The response of DataIntegrationApi->list_data_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntegrationApi->list_data_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**ListDataIntegrationsResponse**](ListDataIntegrationsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_data_integration**
> RemoveDataIntegrationResponse remove_data_integration(remove_data_integration_request)

Remove dataset integrations

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.remove_data_integration_request import RemoveDataIntegrationRequest
from coaxial.models.remove_data_integration_response import RemoveDataIntegrationResponse
from coaxial.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coaxial.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = coaxial.Configuration(
    host = "https://api.coaxial.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Authorization
configuration = coaxial.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with coaxial.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = coaxial.DataIntegrationApi(api_client)
    remove_data_integration_request = coaxial.RemoveDataIntegrationRequest() # RemoveDataIntegrationRequest | 

    try:
        # Remove dataset integrations
        api_response = api_instance.remove_data_integration(remove_data_integration_request)
        print("The response of DataIntegrationApi->remove_data_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntegrationApi->remove_data_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_data_integration_request** | [**RemoveDataIntegrationRequest**](RemoveDataIntegrationRequest.md)|  | 

### Return type

[**RemoveDataIntegrationResponse**](RemoveDataIntegrationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

