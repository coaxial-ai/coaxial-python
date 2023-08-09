# coding: utf-8

"""
    The Coaxial API

    The Coaxial REST API. Please see https://docs.coaxial.ai for more details.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: team@coaxial.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class ListAuthIntegrationsResponse(BaseModel):
    """
    ListAuthIntegrationsResponse
    """
    auth_integrations: Optional[Any] = Field(...)
    __properties = ["auth_integrations"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ListAuthIntegrationsResponse:
        """Create an instance of ListAuthIntegrationsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if auth_integrations (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_integrations is None and "auth_integrations" in self.__fields_set__:
            _dict['auth_integrations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAuthIntegrationsResponse:
        """Create an instance of ListAuthIntegrationsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAuthIntegrationsResponse.parse_obj(obj)

        _obj = ListAuthIntegrationsResponse.parse_obj({
            "auth_integrations": obj.get("auth_integrations")
        })
        return _obj

