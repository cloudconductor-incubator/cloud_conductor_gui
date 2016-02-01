from enum import Enum


class Error(Enum):

    Authentication = 'Email address, or password is incorrect.'
    DuplicationCloud = 'Cloud priority should not be duplicated.'
    PasswordMismatch = 'Passwords do not match.'
    CheckboxNotSelected = 'Not selected'
    NoAssginment = 'This account is not assigned to the project.'
    NoRole = 'This account does not have Role is assigned.'
    Required = 'This field is required.'


class Info(Enum):
    WizardSystem = 'Wizard is terminated. Do you want to move to New?'
