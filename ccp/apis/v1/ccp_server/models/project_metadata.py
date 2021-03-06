# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ccp.apis.v1.ccp_server.models.base_model_ import Model
from ccp.apis.v1.ccp_server.models.meta import Meta  # noqa: F401,E501
from ccp.apis.v1.ccp_server import util


class ProjectMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, meta: Meta = None, app_id: str = None,
                 job_id: str = None, desired_tag: str = None,
                 git_url: str = None, git_branch: str = None,
                 git_path: str = None, target_file: str = None,
                 build_context: str = None, notify_email: str = None,
                 depends_on: str = None, prebuild_script: str = None,
                 prebuild_context: str = None):  # noqa: E501
        """ProjectMetadata - a model defined in Swagger

        :param meta: The meta of this ProjectMetadata.  # noqa: E501
        :type meta: Meta
        :param app_id: The app_id of this ProjectMetadata.  # noqa: E501
        :type app_id: str
        :param job_id: The job_id of this ProjectMetadata.  # noqa: E501
        :type job_id: str
        :param desired_tag: The desired_tag of this ProjectMetadata.  # noqa: E501
        :type desired_tag: str
        :param git_url: The git_url of this ProjectMetadata.  # noqa: E501
        :type git_url: str
        :param git_branch: The git_branch of this ProjectMetadata.  # noqa: E501
        :type git_branch: str
        :param git_path: The git_path of this ProjectMetadata.  # noqa: E501
        :type git_path: str
        :param target_file: The target_file of this ProjectMetadata.  # noqa: E501
        :type target_file: str
        :param build_context: The build_context of this ProjectMetadata.  # noqa: E501
        :type build_context: str
        :param notify_email: The notify_email of this ProjectMetadata.  # noqa: E501
        :type notify_email: str
        :param depends_on: The depends_on of this ProjectMetadata.  # noqa: E501
        :type depends_on: str
        :param prebuild_script: The prebuild_script of this ProjectMetadata.  # noqa: E501
        :type prebuild_script: str
        :param prebuild_context: The prebuild_context of this ProjectMetadata.  # noqa: E501
        :type prebuild_context: str
        """
        self.swagger_types = {
            'meta': Meta,
            'app_id': str,
            'job_id': str,
            'desired_tag': str,
            'git_url': str,
            'git_branch': str,
            'git_path': str,
            'target_file': str,
            'build_context': str,
            'notify_email': str,
            'depends_on': str,
            'prebuild_script': str,
            'prebuild_context': str
        }

        self.attribute_map = {
            'meta': 'meta',
            'app_id': 'app_id',
            'job_id': 'job_id',
            'desired_tag': 'desired_tag',
            'git_url': 'git_url',
            'git_branch': 'git_branch',
            'git_path': 'git_path',
            'target_file': 'target_file',
            'build_context': 'build_context',
            'notify_email': 'notify_email',
            'depends_on': 'depends_on',
            'prebuild_script': 'prebuild_script',
            'prebuild_context': 'prebuild_context'
        }

        self._meta = meta
        self._app_id = app_id
        self._job_id = job_id
        self._desired_tag = desired_tag
        self._git_url = git_url
        self._git_branch = git_branch
        self._git_path = git_path
        self._target_file = target_file
        self._build_context = build_context
        self._notify_email = notify_email
        self._depends_on = depends_on
        self._prebuild_script = prebuild_script
        self._prebuild_context = prebuild_context

    @classmethod
    def from_dict(cls, dikt) -> 'ProjectMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProjectMetadata of this ProjectMetadata.  # noqa: E501
        :rtype: ProjectMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> Meta:
        """Gets the meta of this ProjectMetadata.


        :return: The meta of this ProjectMetadata.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        """Sets the meta of this ProjectMetadata.


        :param meta: The meta of this ProjectMetadata.
        :type meta: Meta
        """

        self._meta = meta

    @property
    def app_id(self) -> str:
        """Gets the app_id of this ProjectMetadata.


        :return: The app_id of this ProjectMetadata.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: str):
        """Sets the app_id of this ProjectMetadata.


        :param app_id: The app_id of this ProjectMetadata.
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def job_id(self) -> str:
        """Gets the job_id of this ProjectMetadata.


        :return: The job_id of this ProjectMetadata.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: str):
        """Sets the job_id of this ProjectMetadata.


        :param job_id: The job_id of this ProjectMetadata.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def desired_tag(self) -> str:
        """Gets the desired_tag of this ProjectMetadata.


        :return: The desired_tag of this ProjectMetadata.
        :rtype: str
        """
        return self._desired_tag

    @desired_tag.setter
    def desired_tag(self, desired_tag: str):
        """Sets the desired_tag of this ProjectMetadata.


        :param desired_tag: The desired_tag of this ProjectMetadata.
        :type desired_tag: str
        """

        self._desired_tag = desired_tag

    @property
    def git_url(self) -> str:
        """Gets the git_url of this ProjectMetadata.


        :return: The git_url of this ProjectMetadata.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url: str):
        """Sets the git_url of this ProjectMetadata.


        :param git_url: The git_url of this ProjectMetadata.
        :type git_url: str
        """

        self._git_url = git_url

    @property
    def git_branch(self) -> str:
        """Gets the git_branch of this ProjectMetadata.


        :return: The git_branch of this ProjectMetadata.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch: str):
        """Sets the git_branch of this ProjectMetadata.


        :param git_branch: The git_branch of this ProjectMetadata.
        :type git_branch: str
        """

        self._git_branch = git_branch

    @property
    def git_path(self) -> str:
        """Gets the git_path of this ProjectMetadata.


        :return: The git_path of this ProjectMetadata.
        :rtype: str
        """
        return self._git_path

    @git_path.setter
    def git_path(self, git_path: str):
        """Sets the git_path of this ProjectMetadata.


        :param git_path: The git_path of this ProjectMetadata.
        :type git_path: str
        """

        self._git_path = git_path

    @property
    def target_file(self) -> str:
        """Gets the target_file of this ProjectMetadata.


        :return: The target_file of this ProjectMetadata.
        :rtype: str
        """
        return self._target_file

    @target_file.setter
    def target_file(self, target_file: str):
        """Sets the target_file of this ProjectMetadata.


        :param target_file: The target_file of this ProjectMetadata.
        :type target_file: str
        """

        self._target_file = target_file

    @property
    def build_context(self) -> str:
        """Gets the build_context of this ProjectMetadata.


        :return: The build_context of this ProjectMetadata.
        :rtype: str
        """
        return self._build_context

    @build_context.setter
    def build_context(self, build_context: str):
        """Sets the build_context of this ProjectMetadata.


        :param build_context: The build_context of this ProjectMetadata.
        :type build_context: str
        """

        self._build_context = build_context

    @property
    def notify_email(self) -> str:
        """Gets the notify_email of this ProjectMetadata.


        :return: The notify_email of this ProjectMetadata.
        :rtype: str
        """
        return self._notify_email

    @notify_email.setter
    def notify_email(self, notify_email: str):
        """Sets the notify_email of this ProjectMetadata.


        :param notify_email: The notify_email of this ProjectMetadata.
        :type notify_email: str
        """

        self._notify_email = notify_email

    @property
    def depends_on(self) -> str:
        """Gets the depends_on of this ProjectMetadata.


        :return: The depends_on of this ProjectMetadata.
        :rtype: str
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on: str):
        """Sets the depends_on of this ProjectMetadata.


        :param depends_on: The depends_on of this ProjectMetadata.
        :type depends_on: str
        """

        self._depends_on = depends_on

    @property
    def prebuild_script(self) -> str:
        """Gets the prebuild_script of this ProjectMetadata.


        :return: The prebuild_script of this ProjectMetadata.
        :rtype: str
        """
        return self._prebuild_script

    @prebuild_script.setter
    def prebuild_script(self, prebuild_script: str):
        """Sets the prebuild_script of this ProjectMetadata.


        :param prebuild_script: The prebuild_script of this ProjectMetadata.
        :type prebuild_script: str
        """

        self._prebuild_script = prebuild_script

    @property
    def prebuild_context(self) -> str:
        """Gets the prebuild_context of this ProjectMetadata.


        :return: The prebuild_context of this ProjectMetadata.
        :rtype: str
        """
        return self._prebuild_context

    @prebuild_context.setter
    def prebuild_context(self, prebuild_context: str):
        """Sets the prebuild_context of this ProjectMetadata.


        :param prebuild_context: The prebuild_context of this ProjectMetadata.
        :type prebuild_context: str
        """

        self._prebuild_context = prebuild_context
