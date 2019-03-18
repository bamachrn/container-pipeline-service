# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server.models.meta import Meta  # noqa: F401,E501
from ccp.apis.v1.ccp_server import util


class TargetFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, meta: Meta=None, prebuild: bool=None,
                 target_file_path: str=None, source_repo: str=None,
                 source_branch: str=None, latest_build_number: str=None):  # noqa: E501
        """TargetFile - a model defined in Swagger

        :param meta: The meta of this TargetFile.  # noqa: E501
        :type meta: Meta
        :param prebuild: The prebuild of this TargetFile.  # noqa: E501
        :type prebuild: bool
        :param target_file_path: The target_file_path of this TargetFile.  # noqa: E501
        :type target_file_path: str
        :param source_repo: The source_repo of this TargetFile.  # noqa: E501
        :type source_repo: str
        :param source_branch: The source_branch of this TargetFile.  # noqa: E501
        :type source_branch: str
        :param latest_build_number: The latest_build_number of this TargetFile.  # noqa: E501
        :type latest_build_number: str
        """
        self.swagger_types = {
            'meta': Meta,
            'prebuild': bool,
            'target_file_path': str,
            'source_repo': str,
            'source_branch': str,
            'latest_build_number': str
        }

        self.attribute_map = {
            'meta': 'meta',
            'prebuild': 'prebuild',
            'target_file_path': 'target_file_path',
            'source_repo': 'source_repo',
            'source_branch': 'source_branch',
            'latest_build_number': 'latest_build_number'
        }

        self._meta = meta
        self._prebuild = prebuild
        self._target_file_path = target_file_path
        self._source_repo = source_repo
        self._source_branch = source_branch
        self._latest_build_number = latest_build_number

    @classmethod
    def from_dict(cls, dikt) -> 'TargetFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TargetFile of this TargetFile.  # noqa: E501
        :rtype: TargetFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> Meta:
        """Gets the meta of this TargetFile.


        :return: The meta of this TargetFile.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this TargetFile.


        :param meta: The meta of this TargetFile.
        :type meta: Meta
        """

        self._meta = meta

    @property
    def prebuild(self) -> bool:
        """Gets the prebuild of this TargetFile.


        :return: The prebuild of this TargetFile.
        :rtype: bool
        """
        return self._prebuild

    @prebuild.setter
    def prebuild(self, prebuild: bool):
        """Sets the prebuild of this TargetFile.


        :param prebuild: The prebuild of this TargetFile.
        :type prebuild: bool
        """

        self._prebuild = prebuild

    @property
    def target_file_path(self) -> str:
        """Gets the target_file_path of this TargetFile.


        :return: The target_file_path of this TargetFile.
        :rtype: str
        """
        return self._target_file_path

    @target_file_path.setter
    def target_file_path(self, target_file_path: str):
        """Sets the target_file_path of this TargetFile.


        :param target_file_path: The target_file_path of this TargetFile.
        :type target_file_path: str
        """

        self._target_file_path = target_file_path

    @property
    def source_repo(self) -> str:
        """Gets the source_repo of this TargetFile.


        :return: The source_repo of this TargetFile.
        :rtype: str
        """
        return self._source_repo

    @source_repo.setter
    def source_repo(self, source_repo: str):
        """Sets the source_repo of this TargetFile.


        :param source_repo: The source_repo of this TargetFile.
        :type source_repo: str
        """

        self._source_repo = source_repo

    @property
    def source_branch(self) -> str:
        """Gets the source_branch of this TargetFile.


        :return: The source_branch of this TargetFile.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch: str):
        """Sets the source_branch of this TargetFile.


        :param source_branch: The source_branch of this TargetFile.
        :type source_branch: str
        """

        self._source_branch = source_branch

    @property
    def latest_build_number(self) -> str:
        """Gets the latest_build_number of this TargetFile.


        :return: The latest_build_number of this TargetFile.
        :rtype: str
        """
        return self._latest_build_number

    @latest_build_number.setter
    def latest_build_number(self, latest_build_number: str):
        """Sets the latest_build_number of this TargetFile.


        :param latest_build_number: The latest_build_number of this TargetFile.
        :type latest_build_number: str
        """

        self._latest_build_number = latest_build_number
