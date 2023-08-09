# coaxial.ModelIntegrationApi

All URIs are relative to *https://api.coaxial.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrate_custom_model**](ModelIntegrationApi.md#integrate_custom_model) | **POST** /llm_integration/custom_model | Integrate custom models
[**integrate_openai**](ModelIntegrationApi.md#integrate_openai) | **POST** /llm_integration/openai | Integrate OpenAI models
[**list_model_integrations**](ModelIntegrationApi.md#list_model_integrations) | **GET** /llm_integration/list/ | List models
[**remove_model_integration**](ModelIntegrationApi.md#remove_model_integration) | **POST** /llm_integration/remove | Remove models


# **integrate_custom_model**
> IntegrateCustomModelResponse integrate_custom_model(integrate_custom_model_request)

Integrate custom models

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_custom_model_request import IntegrateCustomModelRequest
from coaxial.models.integrate_custom_model_response import IntegrateCustomModelResponse
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
    api_instance = coaxial.ModelIntegrationApi(api_client)
    integrate_custom_model_request = coaxial.IntegrateCustomModelRequest() # IntegrateCustomModelRequest | 

    try:
        # Integrate custom models
        api_response = api_instance.integrate_custom_model(integrate_custom_model_request)
        print("The response of ModelIntegrationApi->integrate_custom_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelIntegrationApi->integrate_custom_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_custom_model_request** | [**IntegrateCustomModelRequest**](IntegrateCustomModelRequest.md)|  | 

### Return type

[**IntegrateCustomModelResponse**](IntegrateCustomModelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The model information (including its id) |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrate_openai**
> IntegrateOpenaiResponse integrate_openai(integrate_openai_request)

Integrate OpenAI models

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.integrate_openai_request import IntegrateOpenaiRequest
from coaxial.models.integrate_openai_response import IntegrateOpenaiResponse
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
    api_instance = coaxial.ModelIntegrationApi(api_client)
    integrate_openai_request = coaxial.IntegrateOpenaiRequest() # IntegrateOpenaiRequest | 

    try:
        # Integrate OpenAI models
        api_response = api_instance.integrate_openai(integrate_openai_request)
        print("The response of ModelIntegrationApi->integrate_openai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelIntegrationApi->integrate_openai: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_openai_request** | [**IntegrateOpenaiRequest**](IntegrateOpenaiRequest.md)|  | 

### Return type

[**IntegrateOpenaiResponse**](IntegrateOpenaiResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of LLM information |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_integrations**
> ListModelIntegrationsResponse list_model_integrations(user_id=user_id)

List models

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.list_model_integrations_response import ListModelIntegrationsResponse
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
    api_instance = coaxial.ModelIntegrationApi(api_client)
    user_id = None # object |  (optional)

    try:
        # List models
        api_response = api_instance.list_model_integrations(user_id=user_id)
        print("The response of ModelIntegrationApi->list_model_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelIntegrationApi->list_model_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | [optional] 

### Return type

[**ListModelIntegrationsResponse**](ListModelIntegrationsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of LLM information |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_model_integration**
> RemoveModelResponse remove_model_integration(remove_model_request)

Remove models

### Example

* Bearer Authentication (Authorization):
```python
import time
import os
import coaxial
from coaxial.models.remove_model_request import RemoveModelRequest
from coaxial.models.remove_model_response import RemoveModelResponse
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
    api_instance = coaxial.ModelIntegrationApi(api_client)
    remove_model_request = coaxial.RemoveModelRequest() # RemoveModelRequest | 

    try:
        # Remove models
        api_response = api_instance.remove_model_integration(remove_model_request)
        print("The response of ModelIntegrationApi->remove_model_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelIntegrationApi->remove_model_integration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_model_request** | [**RemoveModelRequest**](RemoveModelRequest.md)|  | 

### Return type

[**RemoveModelResponse**](RemoveModelResponse.md)

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

