# coding: utf-8

"""
    PlayHT API

    The PlayHT's API API allows developers to Realtime Text to Speech streaming Stream audio bytes from text, Convert long form Text to Speech Generate audio from text, and Voice Cloning Instant Cloning.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devs@play.ht
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SPVoiceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'voices': 'list[SPVoice]'
    }

    attribute_map = {
        'voices': 'voices'
    }

    def __init__(self, voices=None):  # noqa: E501
        """SPVoiceResponse - a model defined in Swagger"""  # noqa: E501
        self._voices = None
        self.discriminator = None
        self.voices = voices

    @property
    def voices(self):
        """Gets the voices of this SPVoiceResponse.  # noqa: E501


        :return: The voices of this SPVoiceResponse.  # noqa: E501
        :rtype: list[SPVoice]
        """
        return self._voices

    @voices.setter
    def voices(self, voices):
        """Sets the voices of this SPVoiceResponse.


        :param voices: The voices of this SPVoiceResponse.  # noqa: E501
        :type: list[SPVoice]
        """
        if voices is None:
            raise ValueError("Invalid value for `voices`, must not be `None`")  # noqa: E501

        self._voices = voices

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SPVoiceResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SPVoiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other