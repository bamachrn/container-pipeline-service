"""
This file contains all the classes related to validating the schema of index
file.
"""

from ci.container_index.lib import utils as index_utils
from ci.container_index.lib.checks.basevalidation \
    import Validator, BasicSchemaValidator, \
    StringFieldValidator, StateValidator
from ci.container_index.lib.constants import FieldKeys, StateKeys


class TopLevelProjectsValidator(Validator):
    """
    Validates if there is Projects: at the top level.
    """

    def __init__(self, validation_data, file_name):
        super(TopLevelProjectsValidator, self).__init__(
            validation_data, file_name)

    def _perform_validation(self):
        self.message.title = "Top level projects"
        if not self.validation_data.get(
                FieldKeys.PROJECTS
        ):
            self._invalidate(
                "Index data should begin with "
                "top level \"Projects:\""
            )
            return
        if not isinstance(
                self.validation_data.get(FieldKeys.PROJECTS),
                list
        ):
            self._invalidate(
                "Projects must be provided as a list of dictionaries."
            )
            return


class IDValidator(BasicSchemaValidator):
    """
    Checks the formatting of the id field of entry.
    """

    def __init__(self, validation_data, file_name):
        super(IDValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.ID

    def _extra_validation(self):
        self.message.title = "Id field validation"
        if not isinstance(
                self.validation_data.get(FieldKeys.ID), int
        ):
            self._invalidate("id field must be an integer.")
            return


class AppIDValidator(StringFieldValidator):
    """
    Checks the formatting of app-id field of the data
    """

    def __init__(self, validation_data, file_name):
        super(AppIDValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.APP_ID
        self.message.title = "App Id Validation"

    def _extra_validation_1(self):
        if (self.validation_data.get(self.field_name) !=
                self.file_base_name.split(".")[0]):
            self._invalidate(
                str.format(
                    """{} must be the same as the file name {},
                    without the extension.""",
                    self.field_name,
                    self.file_base_name
                )
            )
            return


class JobIDValidator(StringFieldValidator):
    """
    Checks the formatting of the job-id field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(JobIDValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.JOB_ID
        self.message.title = "Job ID Validation"


class DesiredTagValidator(BasicSchemaValidator):
    """
    Checks the formatting of the desired-tag field of data.
    """

    def __init__(self, validation_data, file_name):
        super(DesiredTagValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.DESIRED_TAG
        self.message.title = "Desired Tag Validation"

    def _extra_validation(self):
        data = str(self.validation_data.get(self.field_name))
        if len(data) == 0:
            self._invalidate("Desired tag cannot be a zero length string")
            return


class GitURLValidator(StringFieldValidator):
    """
    Checks the formatting git-url field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(GitURLValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.GIT_URL
        self.message.title = "Git URL Validation"


class PrebuildValidator(Validator):
    """
    This class validates the values of pre build parameters.
    """

    def __init__(self, validation_data, file_name):
        super(PrebuildValidator, self).__init__(validation_data, file_name)
        self.message.title = "Pre Build field validation"

    def _perform_validation(self):
        if FieldKeys.PREBUILD_SCRIPT not in self.validation_data:
            self._warn("No prebuild-script specified on this container.")
            return
        if (not isinstance(
                self.validation_data.get(FieldKeys.PREBUILD_SCRIPT), str)):
            self._invalidate("prebuild-script must be a valid string.")
        elif len(self.validation_data.get(FieldKeys.PREBUILD_SCRIPT)) == 0:
            self._invalidate("prebuild-script must be of non-zero length")
        if (not isinstance(
                self.validation_data.get(FieldKeys.PREBUILD_CONTEXT), str)):
            self._invalidate("prebuild-context must be a valid string.")
        elif len(self.validation_data.get(FieldKeys.PREBUILD_CONTEXT)) == 0:
            self._invalidate("prebuild-context must be of non-zero length")


class GitPathValidator(StringFieldValidator):
    """
    Checks the formatting git-path field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(GitPathValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.GIT_PATH
        self.message.title = "Git Path Validation"


class GitBranchValidator(StringFieldValidator):
    """
    Checks the formatting git-branch field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(GitBranchValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.GIT_BRANCH
        self.message.title = "Git Branch Validation"


class TargetFileValidator(StringFieldValidator):
    """
    Checks the formatting target-file field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(TargetFileValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.TARGET_FILE
        self.message.title = "Target File Validation"


class NotifyEmailValidator(StringFieldValidator):
    """
    Checks the formatting notify-email field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(NotifyEmailValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.NOTIFY_EMAIL
        self.message.title = "Notify Email Validation"


class BuildContextValidator(StringFieldValidator):
    """
    Checks the formatting build-context field of the data.
    """

    def __init__(self, validation_data, file_name):
        super(BuildContextValidator, self).__init__(
            validation_data, file_name)
        self.field_name = FieldKeys.BUILD_CONTEXT
        self.message.title = "Build Context Validation"


class UniqueEntryValidator(StateValidator):
    """
    This validates Uniqueness of entry by id, app-id, job-id, desired-tag
    """

    def __init__(self, validation_data, file_name):
        super(UniqueEntryValidator, self).__init__(validation_data, file_name)

    def _stateful_validation(self):
        self.message.title = "Unique ID Validation."
        if self.file_base_name not in self.state.data[StateKeys.UNIQUE_IDS]:
            self.state.data[StateKeys.UNIQUE_IDS][self.file_base_name] = []
        if self.file_base_name not in self.state.data[StateKeys.UNIQUE_AJD]:
            self.state.data[StateKeys.UNIQUE_AJD][self.file_base_name] = []

        if (self.validation_data.get(FieldKeys.ID) in
                self.state.data[StateKeys.UNIQUE_IDS][self.file_base_name]):
            self._invalidate("The id field must be unique.")
            return
        self.state.data[StateKeys.UNIQUE_IDS][self.file_base_name].append(
            self.validation_data.get(FieldKeys.ID)
        )
        new_hash = index_utils.gen_hash(
            str.format(
                "{}-{}-{}",
                str(self.validation_data.get(FieldKeys.APP_ID)),
                str(self.validation_data.get(FieldKeys.JOB_ID)),
                str(self.validation_data.get(FieldKeys.DESIRED_TAG))
            )
        )
        if (new_hash in self.state.data[StateKeys.UNIQUE_AJD]
           [self.file_base_name]):
            self._invalidate(
                "The ck app-id, job-id and desired-tag must be unique"
            )
            return

        self.state.data[StateKeys.UNIQUE_AJD][self.file_base_name].append(
            new_hash
        )
