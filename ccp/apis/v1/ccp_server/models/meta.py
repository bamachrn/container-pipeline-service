# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server import util


class Meta(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_version: str = None,
                 timestamp: str = None):  # noqa: E501
        """Meta - a model defined in Swagger

        :param api_version: The api_version of this Meta.  # noqa: E501
        :type api_version: str
        :param timestamp: The timestamp of this Meta.  # noqa: E501
        :type timestamp: str
        """
        self.swagger_types = {
            'api_version': str,
            'timestamp': str
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'timestamp': 'timestamp'
        }

        self._api_version = api_version
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Meta':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Meta of this Meta.  # noqa: E501
        :rtype: Meta
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_version(self) -> str:
        """Gets the api_version of this Meta.


        :return: The api_version of this Meta.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str):
        """Sets the api_version of this Meta.


        :param api_version: The api_version of this Meta.
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this Meta.


        :return: The timestamp of this Meta.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this Meta.


        :param timestamp: The timestamp of this Meta.
        :type timestamp: str
        """

        self._timestamp = timestamp
