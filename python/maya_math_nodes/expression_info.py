# Copyright (c) 2018 Serguei Kalentchouk et al. All rights reserved.
# Use of this source code is governed by an MIT license that can be found in the LICENSE file.

NUMERIC_POD_TYPES = ['double', 'int', 'doubleAngle', 'doubleLinear']

TYPE_SUFFIX_PER_TYPE = {
    'double': '',
    'double3': 'Vector',
    'double3Angle': 'Rotation',
    'double4': 'Quaternion',
    'doubleAngle': 'Angle',
    'doubleLinear': '',
    'int': 'Int',
    'matrix': 'Matrix'
}

OPERATORS = ['+', '/', '%', '*', '-']
CONDITION = ['<', '>', '=', '!']
TERNARY = ['?', ':']

PRECEDENCE = {
    '<': 10, '>': 10, '<=': 10, '>=': 10, '==': 10, '!=': 10,
    '+': 20, '-': 20,
    '*': 30, '/': 30, '%': 30,
}

CompareOp = {
    'name': 'math_Compare{0}',
    'attributes': ['input1', 'input2'],
    'types': ['double', 'doubleAngle'],
    'mixed_types': {}
}

FUNCTIONS = {
    # operators
    '+': {
        'name': 'math_Add{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'double3', 'doubleAngle', 'doubleLinear', 'int'],
        'mixed_types': {}
    },
    '/': {
        'name': 'math_Divide{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'doubleAngle', 'doubleLinear'],
        'mixed_types': {'double': ['int'], 'doubleAngle': ['int']}
    },
    '%': {
        'name': 'math_ModulusInt',
        'attributes': ['input'],
        'types': ['int'],
        'mixed_types': {}
    },
    '*': {
        'name': 'math_Multiply{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'double3', 'double4', 'doubleAngle', 'doubleLinear', 'int', 'matrix'],
        'mixed_types': {'double': ['int'], 'double3': ['int', 'matrix'], 'doubleAngle': ['int'], 'doubleLinear': ['int']}
    },
    '-': {
        'name': 'math_Subtract{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'double3', 'doubleAngle', 'doubleLinear', 'int'],
        'mixed_types': {}
    },
    '>': CompareOp,
    '<': CompareOp,
    '>=': CompareOp,
    '<=': CompareOp,
    '==': CompareOp,
    '!=': CompareOp,

    # functions
    'abs': {
        'name': 'math_Absolute{0}',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle', 'doubleLinear', 'int'],
        'mixed_types': {}
    },
    'acos': {
        'name': 'math_Acos',
        'attributes': ['input'],
        'types': ['double'],
        'mixed_types': {}
    },
    'anglebetween': {
        'name': 'math_AngleBetweenVectors',
        'attributes': ['input1', 'input2'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'asin': {
        'name': 'math_Asin',
        'attributes': ['input'],
        'types': ['double'],
        'mixed_types': {}
    },
    'atan': {
        'name': 'math_Atan',
        'attributes': ['input'],
        'types': ['double'],
        'mixed_types': {}
    },
    'atan2': {
        'name': 'math_Atan2',
        'attributes': ['input1', 'input2'],
        'types': ['double'],
        'mixed_types': {}
    },
    'axis': {
        'name': 'math_AxisFromMatrix',
        'attributes': ['input', 'axis'],
        'types': ['matrix'],
        'mixed_types': {}
    },
    'ceil': {
        'name': 'math_Ceil{0}',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle'],
        'mixed_types': {}
    },
    'clamp': {
        'name': 'math_Clamp{0}',
        'attributes': ['input', 'inputMin', 'inputMax'],
        'types': ['double', 'doubleAngle', 'doubleLinear', 'int'],
        'mixed_types': {}
    },
    'compare': CompareOp,
    'cos': {
        'name': 'math_CosAngle',
        'attributes': ['input'],
        'types': ['doubleAngle'],
        'mixed_types': {}
    },
    'cross': {
        'name': 'math_CrossProduct',
        'attributes': ['input1', 'input2'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'dot': {
        'name': 'math_DotProduct',
        'attributes': ['input1', 'input2'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'distance': {
        'name': 'math_Distance{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double3', 'matrix'],
        'mixed_types': {}
    },
    'floor': {
        'name': 'math_Floor{0}',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle'],
        'mixed_types': {}
    },
    'inverse': {
        'name': 'math_Inverse{0}',
        'attributes': ['input'],
        'types': ['matrix', 'quaternion', 'double3Angle'],
        'mixed_types': {}
    },
    'lerp': {
        'name': 'math_Lerp{0}',
        'attributes': ['input1', 'input2', 'alpha'],
        'types': ['double', 'double3', 'doubleAngle', 'matrix'],
        'mixed_types': {}
    },
    'length': {
        'name': 'math_VectorLength',
        'attributes': ['input'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'lengthsquared': {
        'name': 'math_VectorLengthSquared',
        'attributes': ['input'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'max': {
        'name': 'math_Max{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'doubleAngle', 'int'],
        'mixed_types': {}
    },
    'maxelement': {
        'name': 'math_Max{0}Element',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle', 'int'],
        'mixed_types': {}
    },
    'min': {
        'name': 'math_Min{0}',
        'attributes': ['input1', 'input2'],
        'types': ['double', 'doubleAngle', 'int'],
        'mixed_types': {}
    },
    'minelement': {
        'name': 'math_Min{0}Element',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle', 'int'],
        'mixed_types': {}
    },
    'negate': {
        'name': 'math_Negate{0}',
        'attributes': ['input'],
        'types': ['double', 'double3', 'doubleAngle', 'int'],
        'mixed_types': {}
    },
    'normalize': {
        'name': 'math_NormalizeVector',
        'attributes': ['input'],
        'types': ['double3'],
        'mixed_types': {}
    },
    'normalizearray': {
        'name': 'math_NormalizeArray',
        'attributes': ['input'],
        'types': ['double'],
        'mixed_types': {}
    },
    'pow': {
        'name': 'math_Power',
        'attributes': ['input', 'exponent'],
        'types': ['double'],
        'mixed_types': {}
    },
    'quat': {
        'name': 'math_QuaternionFrom{0}',
        'attributes': ['input', 'rotationOrder'],
        'types': ['matrix', 'double3Angle'],
        'mixed_types': {}
    },
    'rot': {
        'name': 'math_RotationFrom{0}',
        'attributes': ['input', 'rotationOrder'],
        'types': ['matrix', 'quaternion'],
        'mixed_types': {}
    },
    'round': {
        'name': 'math_Round',
        'attributes': ['input'],
        'types': ['double', 'doubleAngle'],
        'mixed_types': {}
    },
    'select': {
        'name': 'math_Select{0}',
        'attributes': ['input1', 'input2', 'condition'],
        'types': ['double', 'double3', 'double3Angle', 'double4', 'doubleAngle', 'doubleLinear', 'int', 'matrix'],
        'mixed_types': {}
    },
    'sin': {
        'name': 'math_SinAngle',
        'attributes': ['input'],
        'types': ['doubleAngle'],
        'mixed_types': {}
    },
    'tan': {
        'name': 'math_TanAngle',
        'attributes': ['input'],
        'types': ['doubleAngle'],
        'mixed_types': {}
    },
    'slerp': {
        'name': 'math_SlerpQuaternion',
        'attributes': ['input1', 'input2', 'alpha', 'interpolationType'],
        'types': ['quaternion'],
        'mixed_types': {}
    },
    'twist': {
        'name': 'math_TwistFrom{0}',
        'attributes': ['input', 'axis', 'rotationOrder'],
        'types': ['matrix', 'double3Angle'],
        'mixed_types': {}
    },
}
