# coaxial-python
The Coaxial REST API. Please see https://docs.coaxial.ai for more details.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import coaxial
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import coaxial
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import coaxial
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
    api_instance = coaxial.AuthIntegrationApi(api_client)
    integrate_okta_request = coaxial.IntegrateOktaRequest() # IntegrateOktaRequest | 

    try:
        # Integrate Okta
        api_response = api_instance.integrate_okta(integrate_okta_request)
        print("The response of AuthIntegrationApi->integrate_okta:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthIntegrationApi->integrate_okta: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.coaxial.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthIntegrationApi* | [**integrate_okta**](docs/AuthIntegrationApi.md#integrate_okta) | **POST** /auth_integration/okta/init | Integrate Okta
*AuthIntegrationApi* | [**list_auth_integrations**](docs/AuthIntegrationApi.md#list_auth_integrations) | **GET** /auth_integration/list | List auth integrations
*AuthIntegrationApi* | [**list_users**](docs/AuthIntegrationApi.md#list_users) | **GET** /users/list | List users
*DataIntegrationApi* | [**integrate_custom_dataset**](docs/DataIntegrationApi.md#integrate_custom_dataset) | **POST** /data_integration/custom | Integrate custom datasets
*DataIntegrationApi* | [**integrate_pinecone**](docs/DataIntegrationApi.md#integrate_pinecone) | **POST** /data_integration/pinecone/integrate | Integrate pinecone datasets
*DataIntegrationApi* | [**list_data_integrations**](docs/DataIntegrationApi.md#list_data_integrations) | **GET** /data_integration/list/ | List dataset integrations
*DataIntegrationApi* | [**remove_data_integration**](docs/DataIntegrationApi.md#remove_data_integration) | **POST** /data_integration/remove | Remove dataset integrations
*FunctionApi* | [**integrate_function**](docs/FunctionApi.md#integrate_function) | **POST** /functions/create | Integrate model functions
*FunctionApi* | [**list_functions**](docs/FunctionApi.md#list_functions) | **GET** /functions/list/ | List model functions
*FunctionApi* | [**remove_function**](docs/FunctionApi.md#remove_function) | **POST** /functions/remove | Remove model functions
*ModelIntegrationApi* | [**integrate_custom_model**](docs/ModelIntegrationApi.md#integrate_custom_model) | **POST** /llm_integration/custom_model | Integrate custom models
*ModelIntegrationApi* | [**integrate_openai**](docs/ModelIntegrationApi.md#integrate_openai) | **POST** /llm_integration/openai | Integrate OpenAI models
*ModelIntegrationApi* | [**list_model_integrations**](docs/ModelIntegrationApi.md#list_model_integrations) | **GET** /llm_integration/list/ | List models
*ModelIntegrationApi* | [**remove_model_integration**](docs/ModelIntegrationApi.md#remove_model_integration) | **POST** /llm_integration/remove | Remove models
*ProvisionApi* | [**check_access_by_resource_id**](docs/ProvisionApi.md#check_access_by_resource_id) | **POST** /provisions/can_user_access | Check user access by resource id
*ProvisionApi* | [**check_access_for_all**](docs/ProvisionApi.md#check_access_for_all) | **POST** /provisions/can_user_access_all | Check user access for many resources
*ProvisionApi* | [**grant_access**](docs/ProvisionApi.md#grant_access) | **POST** /provisions/add_to_user | Grant resource access to user
*ProvisionApi* | [**revoke_access**](docs/ProvisionApi.md#revoke_access) | **POST** /provisions/remove_from_user | Revoke resource access for user


## Documentation For Models

 - [AuthIntegration](docs/AuthIntegration.md)
 - [CheckAccessByResourceIdRequest](docs/CheckAccessByResourceIdRequest.md)
 - [CheckAccessForAllRequest](docs/CheckAccessForAllRequest.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetInfo](docs/DatasetInfo.md)
 - [Function](docs/Function.md)
 - [GrantAccessRequest](docs/GrantAccessRequest.md)
 - [GrantAccessResponse](docs/GrantAccessResponse.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [IntegrateCustomDatasetRequest](docs/IntegrateCustomDatasetRequest.md)
 - [IntegrateCustomDatasetResponse](docs/IntegrateCustomDatasetResponse.md)
 - [IntegrateCustomModelRequest](docs/IntegrateCustomModelRequest.md)
 - [IntegrateCustomModelResponse](docs/IntegrateCustomModelResponse.md)
 - [IntegrateFunctionRequest](docs/IntegrateFunctionRequest.md)
 - [IntegrateFunctionResponse](docs/IntegrateFunctionResponse.md)
 - [IntegrateOktaRequest](docs/IntegrateOktaRequest.md)
 - [IntegrateOktaResponse](docs/IntegrateOktaResponse.md)
 - [IntegrateOpenaiRequest](docs/IntegrateOpenaiRequest.md)
 - [IntegrateOpenaiResponse](docs/IntegrateOpenaiResponse.md)
 - [IntegratePineconeRequest](docs/IntegratePineconeRequest.md)
 - [IntegratePineconeResponse](docs/IntegratePineconeResponse.md)
 - [ListAuthIntegrationsResponse](docs/ListAuthIntegrationsResponse.md)
 - [ListDataIntegrationsResponse](docs/ListDataIntegrationsResponse.md)
 - [ListFunctionsResponse](docs/ListFunctionsResponse.md)
 - [ListModelIntegrationsResponse](docs/ListModelIntegrationsResponse.md)
 - [ListUsersResponse](docs/ListUsersResponse.md)
 - [Model](docs/Model.md)
 - [PineconeInfo](docs/PineconeInfo.md)
 - [RemoveDataIntegrationRequest](docs/RemoveDataIntegrationRequest.md)
 - [RemoveDataIntegrationResponse](docs/RemoveDataIntegrationResponse.md)
 - [RemoveFunctionRequest](docs/RemoveFunctionRequest.md)
 - [RemoveFunctionResponse](docs/RemoveFunctionResponse.md)
 - [RemoveModelRequest](docs/RemoveModelRequest.md)
 - [RemoveModelResponse](docs/RemoveModelResponse.md)
 - [RevokeAccessRequest](docs/RevokeAccessRequest.md)
 - [RevokeAccessResponse](docs/RevokeAccessResponse.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)
 - [UserInfo](docs/UserInfo.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: Bearer authentication


## Author

team@coaxial.ai


