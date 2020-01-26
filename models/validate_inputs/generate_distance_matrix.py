from tests.errors.errors import UnitTypeError, UnitValueError


def _validate_inputs(m_length: int, min_value: int, max_value: int,
                     asym: bool = True, asym_max: int = 1) -> bool:

    # Quick unit test of user inputs
    for key, value in {'m_length': m_length, 'min_value': min_value,
                       'max_value': max_value, 'asym_max': asym_max}.items():
        if type(value) is not int:
            raise UnitTypeError(f'{key} is not an integer.')
        if value <= 0:
            raise UnitValueError(f'{key} must be greater than 0.')
        if key == 'm_length' and value == 1:
            raise UnitValueError(f'{key} must be greater than 1.')
    if type(asym) is not bool:
        raise UnitTypeError(f'{asym} is not a boolean.')
    if min_value >= max_value:
        raise UnitValueError('Min Value must be less than Max Value')

    return True
