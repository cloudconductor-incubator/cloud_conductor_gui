from enum import Enum


class Error(Enum):

    Authentication = 'Email address, or password is incorrect.'
    DuplicationCloud = 'Cloud priority should not be duplicated.'
    PasswordMismatch = 'Passwords do not match.'
    CheckboxNotSelected = 'Not selected'
