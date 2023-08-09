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

class PineconeInfo(BaseModel):
    """
    PineconeInfo
    """
    id: Optional[Any] = Field(...)
    index: Optional[Any] = Field(...)
    __properties = ["id", "index"]

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
    def from_json(cls, json_str: str) -> PineconeInfo:
        """Create an instance of PineconeInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if index (nullable) is None
        # and __fields_set__ contains the field
        if self.index is None and "index" in self.__fields_set__:
            _dict['index'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PineconeInfo:
        """Create an instance of PineconeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PineconeInfo.parse_obj(obj)

        _obj = PineconeInfo.parse_obj({
            "id": obj.get("id"),
            "index": obj.get("index")
        })
        return _obj


