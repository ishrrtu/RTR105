Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
SyntaxError: multiple statements found while compiling a single statement
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 1, in <module>
    from numpy import *     # Importē skaitlisko metožu bibliotēkas funkcijas
ModuleNotFoundError: No module named 'numpy'
>>> import numpy
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py'}
>>> from numpy import *
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    from numpy import *
ModuleNotFoundError: No module named 'numpy'
>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>}
>>> from numpy import *
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'add_newdocs': <module 'numpy.add_newdocs' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/add_newdocs.py'>, 'ModuleDeprecationWarning': <class 'numpy._globals.ModuleDeprecationWarning'>, 'VisibleDeprecationWarning': <class 'numpy._globals.VisibleDeprecationWarning'>, '__version__': '1.14.0', 'pkgload': <function pkgload at 0x7fc9d9120ae8>, 'PackageLoader': <class 'numpy._import_tools.PackageLoader'>, 'show_config': <function show at 0x7fc9d9120e18>, 'char': <module 'numpy.core.defchararray' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/core/defchararray.py'>, 'rec': <module 'numpy.core.records' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/core/records.py'>, 'memmap': <class 'numpy.core.memmap.memmap'>, 'newaxis': None, 'ndarray': <class 'numpy.ndarray'>, 'flatiter': <class 'numpy.flatiter'>, 'nditer': <class 'numpy.nditer'>, 'nested_iters': <built-in function nested_iters>, 'ufunc': <class 'numpy.ufunc'>, 'arange': <built-in function arange>, 'array': <built-in function array>, 'zeros': <built-in function zeros>, 'count_nonzero': <function count_nonzero at 0x7fc9d41479d8>, 'empty': <built-in function empty>, 'broadcast': <class 'numpy.broadcast'>, 'dtype': <class 'numpy.dtype'>, 'fromstring': <built-in function fromstring>, 'fromfile': <built-in function fromfile>, 'frombuffer': <built-in function frombuffer>, 'int_asbuffer': <built-in function int_asbuffer>, 'where': <built-in function where>, 'argwhere': <function argwhere at 0x7fc9d4147d90>, 'copyto': <built-in function copyto>, 'concatenate': <built-in function concatenate>, 'fastCopyAndTranspose': <built-in function _fastCopyAndTranspose>, 'lexsort': <built-in function lexsort>, 'set_numeric_ops': <built-in function set_numeric_ops>, 'can_cast': <built-in function can_cast>, 'promote_types': <built-in function promote_types>, 'min_scalar_type': <built-in function min_scalar_type>, 'result_type': <built-in function result_type>, 'asarray': <function asarray at 0x7fc9d4147a60>, 'asanyarray': <function asanyarray at 0x7fc9d4147ae8>, 'ascontiguousarray': <function ascontiguousarray at 0x7fc9d4147b70>, 'asfortranarray': <function asfortranarray at 0x7fc9d4147bf8>, 'isfortran': <function isfortran at 0x7fc9d4147d08>, 'empty_like': <built-in function empty_like>, 'zeros_like': <function zeros_like at 0x7fc9d4147730>, 'ones_like': <function ones_like at 0x7fc9d4147840>, 'correlate': <function correlate at 0x7fc9d4147f28>, 'convolve': <function convolve at 0x7fc9d4152048>, 'inner': <built-in function inner>, 'dot': <built-in function dot>, 'outer': <function outer at 0x7fc9d41520d0>, 'vdot': <built-in function vdot>, 'roll': <function roll at 0x7fc9d41521e0>, 'rollaxis': <function rollaxis at 0x7fc9d4152268>, 'moveaxis': <function moveaxis at 0x7fc9d4152378>, 'cross': <function cross at 0x7fc9d4152488>, 'tensordot': <function tensordot at 0x7fc9d4152158>, 'little_endian': True, 'require': <function require at 0x7fc9d4147c80>, 'fromiter': <built-in function fromiter>, 'array_equal': <function array_equal at 0x7fc9d4152a60>, 'array_equiv': <function array_equiv at 0x7fc9d4152ae8>, 'indices': <function indices at 0x7fc9d4152510>, 'fromfunction': <function fromfunction at 0x7fc9d4152598>, 'isclose': <function isclose at 0x7fc9d41529d8>, 'load': <function load at 0x7fc9ce1cd0d0>, 'loads': <built-in function loads>, 'isscalar': <function isscalar at 0x7fc9d4152620>, 'binary_repr': <function binary_repr at 0x7fc9d41526a8>, 'base_repr': <function base_repr at 0x7fc9d4152730>, 'ones': <function ones at 0x7fc9d41477b8>, 'identity': <function identity at 0x7fc9d41528c8>, 'allclose': <function allclose at 0x7fc9d4152950>, 'compare_chararrays': <built-in function compare_chararrays>, 'putmask': <built-in function putmask>, 'seterr': <function seterr at 0x7fc9d4152b70>, 'geterr': <function geterr at 0x7fc9d4152bf8>, 'setbufsize': <function setbufsize at 0x7fc9d4152c80>, 'getbufsize': <function getbufsize at 0x7fc9d4152d08>, 'seterrcall': <function seterrcall at 0x7fc9d4152d90>, 'geterrcall': <function geterrcall at 0x7fc9d4152e18>, 'errstate': <class 'numpy.core.numeric.errstate'>, 'flatnonzero': <function flatnonzero at 0x7fc9d4147e18>, 'Inf': inf, 'inf': inf, 'infty': inf, 'Infinity': inf, 'nan': nan, 'NaN': nan, 'False_': False, 'True_': True, 'bitwise_not': <ufunc 'invert'>, 'CLIP': 0, 'RAISE': 2, 'WRAP': 1, 'MAXDIMS': 32, 'BUFSIZE': 8192, 'ALLOW_THREADS': 1, 'ComplexWarning': <class 'numpy.core.numeric.ComplexWarning'>, 'full': <function full at 0x7fc9d41478c8>, 'full_like': <function full_like at 0x7fc9d4147950>, 'matmul': <built-in function matmul>, 'shares_memory': <built-in function shares_memory>, 'may_share_memory': <built-in function may_share_memory>, 'MAY_SHARE_BOUNDS': 0, 'MAY_SHARE_EXACT': -1, 'TooHardError': <class 'numpy.core._internal.TooHardError'>, 'AxisError': <class 'numpy.core._internal.AxisError'>, 'alen': <function alen at 0x7fc9d4161bf8>, 'all': <function all at 0x7fc9d41618c8>, 'alltrue': <function alltrue at 0x7fc9d41617b8>, 'amax': <function amax at 0x7fc9d4161ae8>, 'amin': <function amin at 0x7fc9d4161b70>, 'any': <function any at 0x7fc9d4161840>, 'argmax': <function argmax at 0x7fc9d4154f28>, 'argmin': <function argmin at 0x7fc9d4161048>, 'argpartition': <function argpartition at 0x7fc9d4154d90>, 'argsort': <function argsort at 0x7fc9d4154ea0>, 'around': <function around at 0x7fc9d4161f28>, 'choose': <function choose at 0x7fc9d4154a60>, 'clip': <function clip at 0x7fc9d4161598>, 'compress': <function compress at 0x7fc9d4161510>, 'cumprod': <function cumprod at 0x7fc9d4161d08>, 'cumproduct': <function cumproduct at 0x7fc9d41619d8>, 'cumsum': <function cumsum at 0x7fc9d4161950>, 'diagonal': <function diagonal at 0x7fc9d4161268>, 'mean': <function mean at 0x7fc9d41620d0>, 'ndim': <function ndim at 0x7fc9d4161d90>, 'nonzero': <function nonzero at 0x7fc9d4161400>, 'partition': <function partition at 0x7fc9d4154d08>, 'prod': <function prod at 0x7fc9d4161c80>, 'product': <function product at 0x7fc9d41616a8>, 'ptp': <function ptp at 0x7fc9d4161a60>, 'put': <function put at 0x7fc9d4154b70>, 'rank': <function rank at 0x7fc9d4161e18>, 'ravel': <function ravel at 0x7fc9d4161378>, 'repeat': <function repeat at 0x7fc9d4154ae8>, 'reshape': <function reshape at 0x7fc9d41549d8>, 'resize': <function resize at 0x7fc9d4161158>, 'round_': <function round_ at 0x7fc9d4162048>, 'searchsorted': <function searchsorted at 0x7fc9d41610d0>, 'shape': <function shape at 0x7fc9d4161488>, 'size': <function size at 0x7fc9d4161ea0>, 'sometrue': <function sometrue at 0x7fc9d4161730>, 'sort': <function sort at 0x7fc9d4154e18>, 'squeeze': <function squeeze at 0x7fc9d41611e0>, 'std': <function std at 0x7fc9d4162158>, 'sum': <function sum at 0x7fc9d4161620>, 'swapaxes': <function swapaxes at 0x7fc9d4154bf8>, 'take': <function take at 0x7fc9d4154950>, 'trace': <function trace at 0x7fc9d41612f0>, 'transpose': <function transpose at 0x7fc9d4154c80>, 'var': <function var at 0x7fc9d41621e0>, 'frompyfunc': <built-in function frompyfunc>, 'seterrobj': <built-in function seterrobj>, 'geterrobj': <built-in function geterrobj>, 'absolute': <ufunc 'absolute'>, 'add': <ufunc 'add'>, 'arccos': <ufunc 'arccos'>, 'arccosh': <ufunc 'arccosh'>, 'arcsin': <ufunc 'arcsin'>, 'arcsinh': <ufunc 'arcsinh'>, 'arctan': <ufunc 'arctan'>, 'arctan2': <ufunc 'arctan2'>, 'arctanh': <ufunc 'arctanh'>, 'bitwise_and': <ufunc 'bitwise_and'>, 'bitwise_or': <ufunc 'bitwise_or'>, 'bitwise_xor': <ufunc 'bitwise_xor'>, 'cbrt': <ufunc 'cbrt'>, 'ceil': <ufunc 'ceil'>, 'conjugate': <ufunc 'conjugate'>, 'copysign': <ufunc 'copysign'>, 'cos': <ufunc 'cos'>, 'cosh': <ufunc 'cosh'>, 'deg2rad': <ufunc 'deg2rad'>, 'degrees': <ufunc 'degrees'>, 'divmod': <ufunc 'divmod'>, 'equal': <ufunc 'equal'>, 'exp': <ufunc 'exp'>, 'exp2': <ufunc 'exp2'>, 'expm1': <ufunc 'expm1'>, 'fabs': <ufunc 'fabs'>, 'float_power': <ufunc 'float_power'>, 'floor': <ufunc 'floor'>, 'floor_divide': <ufunc 'floor_divide'>, 'fmax': <ufunc 'fmax'>, 'fmin': <ufunc 'fmin'>, 'fmod': <ufunc 'fmod'>, 'frexp': <ufunc 'frexp'>, 'greater': <ufunc 'greater'>, 'greater_equal': <ufunc 'greater_equal'>, 'heaviside': <ufunc 'heaviside'>, 'hypot': <ufunc 'hypot'>, 'invert': <ufunc 'invert'>, 'isfinite': <ufunc 'isfinite'>, 'isinf': <ufunc 'isinf'>, 'isnan': <ufunc 'isnan'>, 'isnat': <ufunc 'isnat'>, 'ldexp': <ufunc 'ldexp'>, 'left_shift': <ufunc 'left_shift'>, 'less': <ufunc 'less'>, 'less_equal': <ufunc 'less_equal'>, 'log': <ufunc 'log'>, 'log10': <ufunc 'log10'>, 'log1p': <ufunc 'log1p'>, 'log2': <ufunc 'log2'>, 'logaddexp': <ufunc 'logaddexp'>, 'logaddexp2': <ufunc 'logaddexp2'>, 'logical_and': <ufunc 'logical_and'>, 'logical_not': <ufunc 'logical_not'>, 'logical_or': <ufunc 'logical_or'>, 'logical_xor': <ufunc 'logical_xor'>, 'maximum': <ufunc 'maximum'>, 'minimum': <ufunc 'minimum'>, 'modf': <ufunc 'modf'>, 'multiply': <ufunc 'multiply'>, 'negative': <ufunc 'negative'>, 'nextafter': <ufunc 'nextafter'>, 'not_equal': <ufunc 'not_equal'>, 'positive': <ufunc 'positive'>, 'power': <ufunc 'power'>, 'rad2deg': <ufunc 'rad2deg'>, 'radians': <ufunc 'radians'>, 'reciprocal': <ufunc 'reciprocal'>, 'remainder': <ufunc 'remainder'>, 'right_shift': <ufunc 'right_shift'>, 'rint': <ufunc 'rint'>, 'sign': <ufunc 'sign'>, 'signbit': <ufunc 'signbit'>, 'sin': <ufunc 'sin'>, 'sinh': <ufunc 'sinh'>, 'spacing': <ufunc 'spacing'>, 'sqrt': <ufunc 'sqrt'>, 'square': <ufunc 'square'>, 'subtract': <ufunc 'subtract'>, 'tan': <ufunc 'tan'>, 'tanh': <ufunc 'tanh'>, 'true_divide': <ufunc 'true_divide'>, 'trunc': <ufunc 'trunc'>, 'pi': 3.141592653589793, 'e': 2.718281828459045, 'euler_gamma': 0.5772156649015329, 'ERR_IGNORE': 0, 'ERR_WARN': 1, 'ERR_CALL': 3, 'ERR_RAISE': 2, 'ERR_PRINT': 4, 'ERR_LOG': 5, 'ERR_DEFAULT': 521, 'SHIFT_DIVIDEBYZERO': 0, 'SHIFT_OVERFLOW': 3, 'SHIFT_UNDERFLOW': 6, 'SHIFT_INVALID': 9, 'FPE_DIVIDEBYZERO': 1, 'FPE_OVERFLOW': 2, 'FPE_UNDERFLOW': 4, 'FPE_INVALID': 8, 'FLOATING_POINT_SUPPORT': 1, 'UFUNC_PYVALS_NAME': 'UFUNC_PYVALS', 'UFUNC_BUFSIZE_DEFAULT': 8192, 'PINF': inf, 'NINF': -inf, 'PZERO': 0.0, 'NZERO': -0.0, 'NAN': nan, 'divide': <ufunc 'true_divide'>, 'conj': <ufunc 'conjugate'>, 'mod': <ufunc 'remainder'>, 'sctypeDict': {'?': <class 'numpy.bool_'>, 0: <class 'numpy.bool_'>, 'byte': <class 'numpy.int8'>, 'b': <class 'numpy.int8'>, 1: <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, 'B': <class 'numpy.uint8'>, 2: <class 'numpy.uint8'>, 'short': <class 'numpy.int16'>, 'h': <class 'numpy.int16'>, 3: <class 'numpy.int16'>, 'ushort': <class 'numpy.uint16'>, 'H': <class 'numpy.uint16'>, 4: <class 'numpy.uint16'>, 'i': <class 'numpy.int32'>, 5: <class 'numpy.int32'>, 'uint': <class 'numpy.uint64'>, 'I': <class 'numpy.uint32'>, 6: <class 'numpy.uint32'>, 'intp': <class 'numpy.int64'>, 'p': <class 'numpy.int64'>, 7: <class 'numpy.int64'>, 'uintp': <class 'numpy.uint64'>, 'P': <class 'numpy.uint64'>, 8: <class 'numpy.uint64'>, 'long': <class 'numpy.int64'>, 'l': <class 'numpy.int64'>, 'L': <class 'numpy.uint64'>, 'longlong': <class 'numpy.int64'>, 'q': <class 'numpy.int64'>, 9: <class 'numpy.int64'>, 'ulonglong': <class 'numpy.uint64'>, 'Q': <class 'numpy.uint64'>, 10: <class 'numpy.uint64'>, 'half': <class 'numpy.float16'>, 'e': <class 'numpy.float16'>, 23: <class 'numpy.float16'>, 'f': <class 'numpy.float32'>, 11: <class 'numpy.float32'>, 'double': <class 'numpy.float64'>, 'd': <class 'numpy.float64'>, 12: <class 'numpy.float64'>, 'longdouble': <class 'numpy.float128'>, 'g': <class 'numpy.float128'>, 13: <class 'numpy.float128'>, 'cfloat': <class 'numpy.complex128'>, 'F': <class 'numpy.complex64'>, 14: <class 'numpy.complex64'>, 'cdouble': <class 'numpy.complex128'>, 'D': <class 'numpy.complex128'>, 15: <class 'numpy.complex128'>, 'clongdouble': <class 'numpy.complex256'>, 'G': <class 'numpy.complex256'>, 16: <class 'numpy.complex256'>, 'O': <class 'numpy.object_'>, 17: <class 'numpy.object_'>, 'S': <class 'numpy.bytes_'>, 18: <class 'numpy.bytes_'>, 'unicode': <class 'numpy.str_'>, 'U': <class 'numpy.str_'>, 19: <class 'numpy.str_'>, 'void': <class 'numpy.void'>, 'V': <class 'numpy.void'>, 20: <class 'numpy.void'>, 'M': <class 'numpy.datetime64'>, 21: <class 'numpy.datetime64'>, 'm': <class 'numpy.timedelta64'>, 22: <class 'numpy.timedelta64'>, 'bool8': <class 'numpy.bool_'>, 'Bool': <class 'numpy.bool_'>, 'b1': <class 'numpy.bool_'>, 'float16': <class 'numpy.float16'>, 'Float16': <class 'numpy.float16'>, 'f2': <class 'numpy.float16'>, 'float32': <class 'numpy.float32'>, 'Float32': <class 'numpy.float32'>, 'f4': <class 'numpy.float32'>, 'float64': <class 'numpy.float64'>, 'Float64': <class 'numpy.float64'>, 'f8': <class 'numpy.float64'>, 'float128': <class 'numpy.float128'>, 'Float128': <class 'numpy.float128'>, 'f16': <class 'numpy.float128'>, 'complex64': <class 'numpy.complex64'>, 'Complex32': <class 'numpy.complex64'>, 'c8': <class 'numpy.complex64'>, 'complex128': <class 'numpy.complex128'>, 'Complex64': <class 'numpy.complex128'>, 'c16': <class 'numpy.complex128'>, 'complex256': <class 'numpy.complex256'>, 'Complex128': <class 'numpy.complex256'>, 'c32': <class 'numpy.complex256'>, 'object0': <class 'numpy.object_'>, 'Object0': <class 'numpy.object_'>, 'bytes0': <class 'numpy.bytes_'>, 'Bytes0': <class 'numpy.bytes_'>, 'str0': <class 'numpy.str_'>, 'Str0': <class 'numpy.str_'>, 'void0': <class 'numpy.void'>, 'Void0': <class 'numpy.void'>, 'datetime64': <class 'numpy.datetime64'>, 'Datetime64': <class 'numpy.datetime64'>, 'M8': <class 'numpy.datetime64'>, 'timedelta64': <class 'numpy.timedelta64'>, 'Timedelta64': <class 'numpy.timedelta64'>, 'm8': <class 'numpy.timedelta64'>, 'int64': <class 'numpy.int64'>, 'uint64': <class 'numpy.uint64'>, 'Int64': <class 'numpy.int64'>, 'UInt64': <class 'numpy.uint64'>, 'i8': <class 'numpy.int64'>, 'u8': <class 'numpy.uint64'>, 'int32': <class 'numpy.int32'>, 'uint32': <class 'numpy.uint32'>, 'Int32': <class 'numpy.int32'>, 'UInt32': <class 'numpy.uint32'>, 'i4': <class 'numpy.int32'>, 'u4': <class 'numpy.uint32'>, 'int16': <class 'numpy.int16'>, 'uint16': <class 'numpy.uint16'>, 'Int16': <class 'numpy.int16'>, 'UInt16': <class 'numpy.uint16'>, 'i2': <class 'numpy.int16'>, 'u2': <class 'numpy.uint16'>, 'int8': <class 'numpy.int8'>, 'uint8': <class 'numpy.uint8'>, 'Int8': <class 'numpy.int8'>, 'UInt8': <class 'numpy.uint8'>, 'i1': <class 'numpy.int8'>, 'u1': <class 'numpy.uint8'>, 'complex_': <class 'numpy.complex128'>, 'int0': <class 'numpy.int64'>, 'uint0': <class 'numpy.uint64'>, 'single': <class 'numpy.float32'>, 'csingle': <class 'numpy.complex64'>, 'singlecomplex': <class 'numpy.complex64'>, 'float_': <class 'numpy.float64'>, 'intc': <class 'numpy.int32'>, 'uintc': <class 'numpy.uint32'>, 'int_': <class 'numpy.int64'>, 'longfloat': <class 'numpy.float128'>, 'clongfloat': <class 'numpy.complex256'>, 'longcomplex': <class 'numpy.complex256'>, 'bool_': <class 'numpy.bool_'>, 'unicode_': <class 'numpy.str_'>, 'object_': <class 'numpy.object_'>, 'bytes_': <class 'numpy.bytes_'>, 'str_': <class 'numpy.str_'>, 'string_': <class 'numpy.bytes_'>, 'int': <class 'numpy.int64'>, 'float': <class 'numpy.float64'>, 'complex': <class 'numpy.complex128'>, 'bool': <class 'numpy.bool_'>, 'object': <class 'numpy.object_'>, 'str': <class 'numpy.str_'>, 'bytes': <class 'numpy.bytes_'>, 'a': <class 'numpy.bytes_'>}, 'sctypeNA': {'Bool': <class 'numpy.bool_'>, <class 'numpy.bool_'>: 'Bool', '?': 'Bool', 'b1': 'Bool', 'Float16': <class 'numpy.float16'>, <class 'numpy.float16'>: 'Float16', 'e': 'Float16', 'f2': 'Float16', 'Float32': <class 'numpy.float32'>, <class 'numpy.float32'>: 'Float32', 'f': 'Float32', 'f4': 'Float32', 'Float64': <class 'numpy.float64'>, <class 'numpy.float64'>: 'Float64', 'd': 'Float64', 'f8': 'Float64', 'Float128': <class 'numpy.float128'>, <class 'numpy.float128'>: 'Float128', 'g': 'Float128', 'f16': 'Float128', 'Complex32': <class 'numpy.complex64'>, <class 'numpy.complex64'>: 'Complex32', 'F': 'Complex32', 'c8': 'Complex32', 'Complex64': <class 'numpy.complex128'>, <class 'numpy.complex128'>: 'Complex64', 'D': 'Complex64', 'c16': 'Complex64', 'Complex128': <class 'numpy.complex256'>, <class 'numpy.complex256'>: 'Complex128', 'G': 'Complex128', 'c32': 'Complex128', 'Object0': <class 'numpy.object_'>, <class 'numpy.object_'>: 'Object0', 'O': 'Object0', 'Bytes0': <class 'numpy.bytes_'>, <class 'numpy.bytes_'>: 'Bytes0', 'S': 'Bytes0', 'Str0': <class 'numpy.str_'>, <class 'numpy.str_'>: 'Str0', 'U': 'Str0', 'Void0': <class 'numpy.void'>, <class 'numpy.void'>: 'Void0', 'V': 'Void0', 'Datetime64': <class 'numpy.datetime64'>, <class 'numpy.datetime64'>: 'Datetime64', 'M': 'Datetime64', 'M8': 'Datetime64', 'Timedelta64': <class 'numpy.timedelta64'>, <class 'numpy.timedelta64'>: 'Timedelta64', 'm': 'Timedelta64', 'm8': 'Timedelta64', 'Int64': <class 'numpy.int64'>, 'UInt64': <class 'numpy.uint64'>, 'i8': <class 'numpy.int64'>, 'u8': <class 'numpy.uint64'>, <class 'numpy.int64'>: 'Int64', <class 'numpy.uint64'>: 'UInt64', 'l': 'Int64', 'L': 'UInt64', <class 'numpy.int64'>: 'Int64', <class 'numpy.uint64'>: 'UInt64', 'q': 'Int64', 'Q': 'UInt64', 'Int32': <class 'numpy.int32'>, 'UInt32': <class 'numpy.uint32'>, 'i4': <class 'numpy.int32'>, 'u4': <class 'numpy.uint32'>, <class 'numpy.int32'>: 'Int32', <class 'numpy.uint32'>: 'UInt32', 'i': 'Int32', 'I': 'UInt32', 'Int16': <class 'numpy.int16'>, 'UInt16': <class 'numpy.uint16'>, 'i2': <class 'numpy.int16'>, 'u2': <class 'numpy.uint16'>, <class 'numpy.int16'>: 'Int16', <class 'numpy.uint16'>: 'UInt16', 'h': 'Int16', 'H': 'UInt16', 'Int8': <class 'numpy.int8'>, 'UInt8': <class 'numpy.uint8'>, 'i1': <class 'numpy.int8'>, 'u1': <class 'numpy.uint8'>, <class 'numpy.int8'>: 'Int8', <class 'numpy.uint8'>: 'UInt8', 'b': 'Int8', 'B': 'UInt8'}, 'typeDict': {'?': <class 'numpy.bool_'>, 0: <class 'numpy.bool_'>, 'byte': <class 'numpy.int8'>, 'b': <class 'numpy.int8'>, 1: <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, 'B': <class 'numpy.uint8'>, 2: <class 'numpy.uint8'>, 'short': <class 'numpy.int16'>, 'h': <class 'numpy.int16'>, 3: <class 'numpy.int16'>, 'ushort': <class 'numpy.uint16'>, 'H': <class 'numpy.uint16'>, 4: <class 'numpy.uint16'>, 'i': <class 'numpy.int32'>, 5: <class 'numpy.int32'>, 'uint': <class 'numpy.uint64'>, 'I': <class 'numpy.uint32'>, 6: <class 'numpy.uint32'>, 'intp': <class 'numpy.int64'>, 'p': <class 'numpy.int64'>, 7: <class 'numpy.int64'>, 'uintp': <class 'numpy.uint64'>, 'P': <class 'numpy.uint64'>, 8: <class 'numpy.uint64'>, 'long': <class 'numpy.int64'>, 'l': <class 'numpy.int64'>, 'L': <class 'numpy.uint64'>, 'longlong': <class 'numpy.int64'>, 'q': <class 'numpy.int64'>, 9: <class 'numpy.int64'>, 'ulonglong': <class 'numpy.uint64'>, 'Q': <class 'numpy.uint64'>, 10: <class 'numpy.uint64'>, 'half': <class 'numpy.float16'>, 'e': <class 'numpy.float16'>, 23: <class 'numpy.float16'>, 'f': <class 'numpy.float32'>, 11: <class 'numpy.float32'>, 'double': <class 'numpy.float64'>, 'd': <class 'numpy.float64'>, 12: <class 'numpy.float64'>, 'longdouble': <class 'numpy.float128'>, 'g': <class 'numpy.float128'>, 13: <class 'numpy.float128'>, 'cfloat': <class 'numpy.complex128'>, 'F': <class 'numpy.complex64'>, 14: <class 'numpy.complex64'>, 'cdouble': <class 'numpy.complex128'>, 'D': <class 'numpy.complex128'>, 15: <class 'numpy.complex128'>, 'clongdouble': <class 'numpy.complex256'>, 'G': <class 'numpy.complex256'>, 16: <class 'numpy.complex256'>, 'O': <class 'numpy.object_'>, 17: <class 'numpy.object_'>, 'S': <class 'numpy.bytes_'>, 18: <class 'numpy.bytes_'>, 'unicode': <class 'numpy.str_'>, 'U': <class 'numpy.str_'>, 19: <class 'numpy.str_'>, 'void': <class 'numpy.void'>, 'V': <class 'numpy.void'>, 20: <class 'numpy.void'>, 'M': <class 'numpy.datetime64'>, 21: <class 'numpy.datetime64'>, 'm': <class 'numpy.timedelta64'>, 22: <class 'numpy.timedelta64'>, 'bool8': <class 'numpy.bool_'>, 'Bool': <class 'numpy.bool_'>, 'b1': <class 'numpy.bool_'>, 'float16': <class 'numpy.float16'>, 'Float16': <class 'numpy.float16'>, 'f2': <class 'numpy.float16'>, 'float32': <class 'numpy.float32'>, 'Float32': <class 'numpy.float32'>, 'f4': <class 'numpy.float32'>, 'float64': <class 'numpy.float64'>, 'Float64': <class 'numpy.float64'>, 'f8': <class 'numpy.float64'>, 'float128': <class 'numpy.float128'>, 'Float128': <class 'numpy.float128'>, 'f16': <class 'numpy.float128'>, 'complex64': <class 'numpy.complex64'>, 'Complex32': <class 'numpy.complex64'>, 'c8': <class 'numpy.complex64'>, 'complex128': <class 'numpy.complex128'>, 'Complex64': <class 'numpy.complex128'>, 'c16': <class 'numpy.complex128'>, 'complex256': <class 'numpy.complex256'>, 'Complex128': <class 'numpy.complex256'>, 'c32': <class 'numpy.complex256'>, 'object0': <class 'numpy.object_'>, 'Object0': <class 'numpy.object_'>, 'bytes0': <class 'numpy.bytes_'>, 'Bytes0': <class 'numpy.bytes_'>, 'str0': <class 'numpy.str_'>, 'Str0': <class 'numpy.str_'>, 'void0': <class 'numpy.void'>, 'Void0': <class 'numpy.void'>, 'datetime64': <class 'numpy.datetime64'>, 'Datetime64': <class 'numpy.datetime64'>, 'M8': <class 'numpy.datetime64'>, 'timedelta64': <class 'numpy.timedelta64'>, 'Timedelta64': <class 'numpy.timedelta64'>, 'm8': <class 'numpy.timedelta64'>, 'int64': <class 'numpy.int64'>, 'uint64': <class 'numpy.uint64'>, 'Int64': <class 'numpy.int64'>, 'UInt64': <class 'numpy.uint64'>, 'i8': <class 'numpy.int64'>, 'u8': <class 'numpy.uint64'>, 'int32': <class 'numpy.int32'>, 'uint32': <class 'numpy.uint32'>, 'Int32': <class 'numpy.int32'>, 'UInt32': <class 'numpy.uint32'>, 'i4': <class 'numpy.int32'>, 'u4': <class 'numpy.uint32'>, 'int16': <class 'numpy.int16'>, 'uint16': <class 'numpy.uint16'>, 'Int16': <class 'numpy.int16'>, 'UInt16': <class 'numpy.uint16'>, 'i2': <class 'numpy.int16'>, 'u2': <class 'numpy.uint16'>, 'int8': <class 'numpy.int8'>, 'uint8': <class 'numpy.uint8'>, 'Int8': <class 'numpy.int8'>, 'UInt8': <class 'numpy.uint8'>, 'i1': <class 'numpy.int8'>, 'u1': <class 'numpy.uint8'>, 'complex_': <class 'numpy.complex128'>, 'int0': <class 'numpy.int64'>, 'uint0': <class 'numpy.uint64'>, 'single': <class 'numpy.float32'>, 'csingle': <class 'numpy.complex64'>, 'singlecomplex': <class 'numpy.complex64'>, 'float_': <class 'numpy.float64'>, 'intc': <class 'numpy.int32'>, 'uintc': <class 'numpy.uint32'>, 'int_': <class 'numpy.int64'>, 'longfloat': <class 'numpy.float128'>, 'clongfloat': <class 'numpy.complex256'>, 'longcomplex': <class 'numpy.complex256'>, 'bool_': <class 'numpy.bool_'>, 'unicode_': <class 'numpy.str_'>, 'object_': <class 'numpy.object_'>, 'bytes_': <class 'numpy.bytes_'>, 'str_': <class 'numpy.str_'>, 'string_': <class 'numpy.bytes_'>, 'int': <class 'numpy.int64'>, 'float': <class 'numpy.float64'>, 'complex': <class 'numpy.complex128'>, 'bool': <class 'numpy.bool_'>, 'object': <class 'numpy.object_'>, 'str': <class 'numpy.str_'>, 'bytes': <class 'numpy.bytes_'>, 'a': <class 'numpy.bytes_'>}, 'typeNA': {'Bool': <class 'numpy.bool_'>, <class 'numpy.bool_'>: 'Bool', '?': 'Bool', 'b1': 'Bool', 'Float16': <class 'numpy.float16'>, <class 'numpy.float16'>: 'Float16', 'e': 'Float16', 'f2': 'Float16', 'Float32': <class 'numpy.float32'>, <class 'numpy.float32'>: 'Float32', 'f': 'Float32', 'f4': 'Float32', 'Float64': <class 'numpy.float64'>, <class 'numpy.float64'>: 'Float64', 'd': 'Float64', 'f8': 'Float64', 'Float128': <class 'numpy.float128'>, <class 'numpy.float128'>: 'Float128', 'g': 'Float128', 'f16': 'Float128', 'Complex32': <class 'numpy.complex64'>, <class 'numpy.complex64'>: 'Complex32', 'F': 'Complex32', 'c8': 'Complex32', 'Complex64': <class 'numpy.complex128'>, <class 'numpy.complex128'>: 'Complex64', 'D': 'Complex64', 'c16': 'Complex64', 'Complex128': <class 'numpy.complex256'>, <class 'numpy.complex256'>: 'Complex128', 'G': 'Complex128', 'c32': 'Complex128', 'Object0': <class 'numpy.object_'>, <class 'numpy.object_'>: 'Object0', 'O': 'Object0', 'Bytes0': <class 'numpy.bytes_'>, <class 'numpy.bytes_'>: 'Bytes0', 'S': 'Bytes0', 'Str0': <class 'numpy.str_'>, <class 'numpy.str_'>: 'Str0', 'U': 'Str0', 'Void0': <class 'numpy.void'>, <class 'numpy.void'>: 'Void0', 'V': 'Void0', 'Datetime64': <class 'numpy.datetime64'>, <class 'numpy.datetime64'>: 'Datetime64', 'M': 'Datetime64', 'M8': 'Datetime64', 'Timedelta64': <class 'numpy.timedelta64'>, <class 'numpy.timedelta64'>: 'Timedelta64', 'm': 'Timedelta64', 'm8': 'Timedelta64', 'Int64': <class 'numpy.int64'>, 'UInt64': <class 'numpy.uint64'>, 'i8': <class 'numpy.int64'>, 'u8': <class 'numpy.uint64'>, <class 'numpy.int64'>: 'Int64', <class 'numpy.uint64'>: 'UInt64', 'l': 'Int64', 'L': 'UInt64', <class 'numpy.int64'>: 'Int64', <class 'numpy.uint64'>: 'UInt64', 'q': 'Int64', 'Q': 'UInt64', 'Int32': <class 'numpy.int32'>, 'UInt32': <class 'numpy.uint32'>, 'i4': <class 'numpy.int32'>, 'u4': <class 'numpy.uint32'>, <class 'numpy.int32'>: 'Int32', <class 'numpy.uint32'>: 'UInt32', 'i': 'Int32', 'I': 'UInt32', 'Int16': <class 'numpy.int16'>, 'UInt16': <class 'numpy.uint16'>, 'i2': <class 'numpy.int16'>, 'u2': <class 'numpy.uint16'>, <class 'numpy.int16'>: 'Int16', <class 'numpy.uint16'>: 'UInt16', 'h': 'Int16', 'H': 'UInt16', 'Int8': <class 'numpy.int8'>, 'UInt8': <class 'numpy.uint8'>, 'i1': <class 'numpy.int8'>, 'u1': <class 'numpy.uint8'>, <class 'numpy.int8'>: 'Int8', <class 'numpy.uint8'>: 'UInt8', 'b': 'Int8', 'B': 'UInt8'}, 'sctypes': {'int': [<class 'numpy.int8'>, <class 'numpy.int16'>, <class 'numpy.int32'>, <class 'numpy.int64'>], 'uint': [<class 'numpy.uint8'>, <class 'numpy.uint16'>, <class 'numpy.uint32'>, <class 'numpy.uint64'>], 'float': [<class 'numpy.float16'>, <class 'numpy.float32'>, <class 'numpy.float64'>, <class 'numpy.float128'>], 'complex': [<class 'numpy.complex64'>, <class 'numpy.complex128'>, <class 'numpy.complex256'>], 'others': [<class 'bool'>, <class 'object'>, <class 'bytes'>, <class 'str'>, <class 'numpy.void'>]}, 'ScalarType': (<class 'int'>, <class 'float'>, <class 'complex'>, <class 'int'>, <class 'bool'>, <class 'bytes'>, <class 'str'>, <class 'memoryview'>, <class 'numpy.bool_'>, <class 'numpy.int8'>, <class 'numpy.uint8'>, <class 'numpy.int16'>, <class 'numpy.uint16'>, <class 'numpy.int32'>, <class 'numpy.uint32'>, <class 'numpy.int64'>, <class 'numpy.uint64'>, <class 'numpy.int64'>, <class 'numpy.uint64'>, <class 'numpy.float16'>, <class 'numpy.float32'>, <class 'numpy.float64'>, <class 'numpy.float128'>, <class 'numpy.complex64'>, <class 'numpy.complex128'>, <class 'numpy.complex256'>, <class 'numpy.object_'>, <class 'numpy.bytes_'>, <class 'numpy.str_'>, <class 'numpy.void'>, <class 'numpy.datetime64'>, <class 'numpy.timedelta64'>), 'obj2sctype': <function obj2sctype at 0x7fc9d41c1048>, 'cast': {<class 'numpy.bool_'>: <function <lambda> at 0x7fc9d41c1400>, <class 'numpy.int8'>: <function <lambda> at 0x7fc9d41c1488>, <class 'numpy.uint8'>: <function <lambda> at 0x7fc9d41c1510>, <class 'numpy.int16'>: <function <lambda> at 0x7fc9d41c1598>, <class 'numpy.uint16'>: <function <lambda> at 0x7fc9d41c1620>, <class 'numpy.int32'>: <function <lambda> at 0x7fc9d41c16a8>, <class 'numpy.uint32'>: <function <lambda> at 0x7fc9d41c1730>, <class 'numpy.int64'>: <function <lambda> at 0x7fc9d41c17b8>, <class 'numpy.uint64'>: <function <lambda> at 0x7fc9d41c1840>, <class 'numpy.int64'>: <function <lambda> at 0x7fc9d41c18c8>, <class 'numpy.uint64'>: <function <lambda> at 0x7fc9d41c1950>, <class 'numpy.float16'>: <function <lambda> at 0x7fc9d41c19d8>, <class 'numpy.float32'>: <function <lambda> at 0x7fc9d41c1a60>, <class 'numpy.float64'>: <function <lambda> at 0x7fc9d41c1ae8>, <class 'numpy.float128'>: <function <lambda> at 0x7fc9d41c1b70>, <class 'numpy.complex64'>: <function <lambda> at 0x7fc9d41c1bf8>, <class 'numpy.complex128'>: <function <lambda> at 0x7fc9d41c1c80>, <class 'numpy.complex256'>: <function <lambda> at 0x7fc9d41c1d08>, <class 'numpy.object_'>: <function <lambda> at 0x7fc9d41c1d90>, <class 'numpy.bytes_'>: <function <lambda> at 0x7fc9d41c1e18>, <class 'numpy.str_'>: <function <lambda> at 0x7fc9d41c1ea0>, <class 'numpy.void'>: <function <lambda> at 0x7fc9d41c1f28>, <class 'numpy.datetime64'>: <function <lambda> at 0x7fc9d41c3048>, <class 'numpy.timedelta64'>: <function <lambda> at 0x7fc9d41c30d0>}, 'nbytes': {<class 'numpy.bool_'>: 1, <class 'numpy.int8'>: 1, <class 'numpy.uint8'>: 1, <class 'numpy.int16'>: 2, <class 'numpy.uint16'>: 2, <class 'numpy.int32'>: 4, <class 'numpy.uint32'>: 4, <class 'numpy.int64'>: 8, <class 'numpy.uint64'>: 8, <class 'numpy.int64'>: 8, <class 'numpy.uint64'>: 8, <class 'numpy.float16'>: 2, <class 'numpy.float32'>: 4, <class 'numpy.float64'>: 8, <class 'numpy.float128'>: 16, <class 'numpy.complex64'>: 8, <class 'numpy.complex128'>: 16, <class 'numpy.complex256'>: 32, <class 'numpy.object_'>: 8, <class 'numpy.bytes_'>: 0, <class 'numpy.str_'>: 0, <class 'numpy.void'>: 0, <class 'numpy.datetime64'>: 8, <class 'numpy.timedelta64'>: 8}, 'sctype2char': <function sctype2char at 0x7fc9d41c1378>, 'maximum_sctype': <function maximum_sctype at 0x7fc9d41bbea0>, 'issctype': <function issctype at 0x7fc9d41bbf28>, 'typecodes': {'Character': 'c', 'Integer': 'bhilqp', 'UnsignedInteger': 'BHILQP', 'Float': 'efdg', 'Complex': 'FDG', 'AllInteger': 'bBhHiIlLqQpP', 'AllFloat': 'efdgFDG', 'Datetime': 'Mm', 'All': '?bhilqpBHILQPefdgFDGSUVOMm'}, 'find_common_type': <function find_common_type at 0x7fc9d41b8a60>, 'issubdtype': <function issubdtype at 0x7fc9d41c11e0>, 'datetime_data': <built-in function datetime_data>, 'datetime_as_string': <built-in function datetime_as_string>, 'busday_offset': <built-in function busday_offset>, 'busday_count': <built-in function busday_count>, 'is_busday': <built-in function is_busday>, 'busdaycalendar': <class 'numpy.busdaycalendar'>, 'byte': <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, 'short': <class 'numpy.int16'>, 'ushort': <class 'numpy.uint16'>, 'uint': <class 'numpy.uint64'>, 'intp': <class 'numpy.int64'>, 'uintp': <class 'numpy.uint64'>, 'long': <class 'int'>, 'longlong': <class 'numpy.int64'>, 'ulonglong': <class 'numpy.uint64'>, 'half': <class 'numpy.float16'>, 'double': <class 'numpy.float64'>, 'longdouble': <class 'numpy.float128'>, 'cfloat': <class 'numpy.complex128'>, 'cdouble': <class 'numpy.complex128'>, 'clongdouble': <class 'numpy.complex256'>, 'unicode': <class 'str'>, 'void': <class 'numpy.void'>, 'generic': <class 'numpy.generic'>, 'number': <class 'numpy.number'>, 'integer': <class 'numpy.integer'>, 'inexact': <class 'numpy.inexact'>, 'signedinteger': <class 'numpy.signedinteger'>, 'unsignedinteger': <class 'numpy.unsignedinteger'>, 'floating': <class 'numpy.floating'>, 'complexfloating': <class 'numpy.complexfloating'>, 'flexible': <class 'numpy.flexible'>, 'character': <class 'numpy.character'>, 'bool8': <class 'numpy.bool_'>, 'float16': <class 'numpy.float16'>, 'float32': <class 'numpy.float32'>, 'float64': <class 'numpy.float64'>, 'float128': <class 'numpy.float128'>, 'complex64': <class 'numpy.complex64'>, 'complex128': <class 'numpy.complex128'>, 'complex256': <class 'numpy.complex256'>, 'object0': <class 'numpy.object_'>, 'bytes0': <class 'numpy.bytes_'>, 'str0': <class 'numpy.str_'>, 'void0': <class 'numpy.void'>, 'datetime64': <class 'numpy.datetime64'>, 'timedelta64': <class 'numpy.timedelta64'>, 'int64': <class 'numpy.int64'>, 'uint64': <class 'numpy.uint64'>, 'int32': <class 'numpy.int32'>, 'uint32': <class 'numpy.uint32'>, 'int16': <class 'numpy.int16'>, 'uint16': <class 'numpy.uint16'>, 'int8': <class 'numpy.int8'>, 'uint8': <class 'numpy.uint8'>, 'complex_': <class 'numpy.complex128'>, 'int0': <class 'numpy.int64'>, 'uint0': <class 'numpy.uint64'>, 'single': <class 'numpy.float32'>, 'csingle': <class 'numpy.complex64'>, 'singlecomplex': <class 'numpy.complex64'>, 'float_': <class 'numpy.float64'>, 'intc': <class 'numpy.int32'>, 'uintc': <class 'numpy.uint32'>, 'int_': <class 'numpy.int64'>, 'longfloat': <class 'numpy.float128'>, 'clongfloat': <class 'numpy.complex256'>, 'longcomplex': <class 'numpy.complex256'>, 'bool_': <class 'numpy.bool_'>, 'unicode_': <class 'numpy.str_'>, 'object_': <class 'numpy.object_'>, 'bytes_': <class 'numpy.bytes_'>, 'str_': <class 'numpy.str_'>, 'string_': <class 'numpy.bytes_'>, 'array2string': <function array2string at 0x7fc9d4162bf8>, 'array_str': <function array_str at 0x7fc9d4178048>, 'array_repr': <function array_repr at 0x7fc9d4173f28>, 'set_string_function': <function set_string_function at 0x7fc9d41780d0>, 'set_printoptions': <function set_printoptions at 0x7fc9d4162730>, 'get_printoptions': <function get_printoptions at 0x7fc9d41627b8>, 'format_float_positional': <function format_float_positional at 0x7fc9d4173268>, 'format_float_scientific': <function format_float_scientific at 0x7fc9d4162ea0>, 'record': <class 'numpy.record'>, 'recarray': <class 'numpy.recarray'>, 'format_parser': <class 'numpy.core.records.format_parser'>, 'chararray': <class 'numpy.core.defchararray.chararray'>, 'logspace': <function logspace at 0x7fc9d411a1e0>, 'linspace': <function linspace at 0x7fc9d411a158>, 'geomspace': <function geomspace at 0x7fc9d411a268>, 'MachAr': <class 'numpy.core.machar.MachAr'>, 'finfo': <class 'numpy.core.getlimits.finfo'>, 'iinfo': <class 'numpy.core.getlimits.iinfo'>, 'atleast_1d': <function atleast_1d at 0x7fc9d4127048>, 'atleast_2d': <function atleast_2d at 0x7fc9d4127598>, 'atleast_3d': <function atleast_3d at 0x7fc9d4127620>, 'block': <function block at 0x7fc9d4127950>, 'hstack': <function hstack at 0x7fc9d4127730>, 'stack': <function stack at 0x7fc9d41277b8>, 'vstack': <function vstack at 0x7fc9d41276a8>, 'einsum': <function einsum at 0x7fc9d4127e18>, 'einsum_path': <function einsum_path at 0x7fc9d4127d90>, 'matrix': <class 'numpy.matrixlib.defmatrix.matrix'>, 'bmat': <function bmat at 0x7fc9ce6118c8>, 'mat': <function asmatrix at 0x7fc9ce60a598>, 'asmatrix': <function asmatrix at 0x7fc9ce60a598>, 'emath': <module 'numpy.lib.scimath' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/lib/scimath.py'>, 'math': <module 'math' (built-in)>, 'tracemalloc_domain': 389047, 'iscomplexobj': <function iscomplexobj at 0x7fc9d402d9d8>, 'isrealobj': <function isrealobj at 0x7fc9d402da60>, 'imag': <function imag at 0x7fc9d402d840>, 'iscomplex': <function iscomplex at 0x7fc9d402d8c8>, 'isreal': <function isreal at 0x7fc9d402d950>, 'nan_to_num': <function nan_to_num at 0x7fc9d402db70>, 'real': <function real at 0x7fc9d402d7b8>, 'real_if_close': <function real_if_close at 0x7fc9d402dbf8>, 'typename': <function typename at 0x7fc9d402dd08>, 'asfarray': <function asfarray at 0x7fc9d402d730>, 'mintypecode': <function mintypecode at 0x7fc9d427cd90>, 'asscalar': <function asscalar at 0x7fc9d402dc80>, 'common_type': <function common_type at 0x7fc9d402dd90>, 'ravel_multi_index': <built-in function ravel_multi_index>, 'unravel_index': <built-in function unravel_index>, 'mgrid': <numpy.lib.index_tricks.nd_grid object at 0x7fc9d402bef0>, 'ogrid': <numpy.lib.index_tricks.nd_grid object at 0x7fc9d402bf60>, 'r_': <numpy.lib.index_tricks.RClass object at 0x7fc9ce616080>, 'c_': <numpy.lib.index_tricks.CClass object at 0x7fc9ce6160f0>, 's_': <numpy.lib.index_tricks.IndexExpression object at 0x7fc9ce616208>, 'index_exp': <numpy.lib.index_tricks.IndexExpression object at 0x7fc9ce6161d0>, 'ix_': <function ix_ at 0x7fc9d402df28>, 'ndenumerate': <class 'numpy.lib.index_tricks.ndenumerate'>, 'ndindex': <class 'numpy.lib.index_tricks.ndindex'>, 'fill_diagonal': <function fill_diagonal at 0x7fc9ce611d90>, 'diag_indices': <function diag_indices at 0x7fc9ce6177b8>, 'diag_indices_from': <function diag_indices_from at 0x7fc9ce617840>, 'select': <function select at 0x7fc9ce6088c8>, 'piecewise': <function piecewise at 0x7fc9ce608840>, 'trim_zeros': <function trim_zeros at 0x7fc9ce608d08>, 'copy': <function copy at 0x7fc9ce608950>, 'iterable': <function iterable at 0x7fc9ce6081e0>, 'percentile': <function percentile at 0x7fc9ce609ea0>, 'diff': <function diff at 0x7fc9ce608a60>, 'gradient': <function gradient at 0x7fc9ce6089d8>, 'angle': <function angle at 0x7fc9ce608b70>, 'unwrap': <function unwrap at 0x7fc9ce608bf8>, 'sort_complex': <function sort_complex at 0x7fc9ce608c80>, 'disp': <function disp at 0x7fc9ce609048>, 'flip': <function flip at 0x7fc9ce608158>, 'rot90': <function rot90 at 0x7fc9d403b730>, 'extract': <function extract at 0x7fc9ce608ea0>, 'place': <function place at 0x7fc9ce608f28>, 'vectorize': <class 'numpy.lib.function_base.vectorize'>, 'asarray_chkfinite': <function asarray_chkfinite at 0x7fc9ce6087b8>, 'average': <function average at 0x7fc9ce608730>, 'histogram': <function histogram at 0x7fc9ce608620>, 'histogramdd': <function histogramdd at 0x7fc9ce6086a8>, 'bincount': <built-in function bincount>, 'digitize': <built-in function digitize>, 'cov': <function cov at 0x7fc9ce609378>, 'corrcoef': <function corrcoef at 0x7fc9ce6096a8>, 'msort': <function msort at 0x7fc9ce609c80>, 'median': <function median at 0x7fc9ce609d90>, 'sinc': <function sinc at 0x7fc9ce609bf8>, 'hamming': <function hamming at 0x7fc9ce6098c8>, 'hanning': <function hanning at 0x7fc9ce609840>, 'bartlett': <function bartlett at 0x7fc9ce6097b8>, 'blackman': <function blackman at 0x7fc9ce609730>, 'kaiser': <function kaiser at 0x7fc9ce609b70>, 'trapz': <function trapz at 0x7fc9ce60a048>, 'i0': <function i0 at 0x7fc9ce609ae8>, 'add_newdoc': <function add_newdoc at 0x7fc9ce60a0d0>, 'add_docstring': <built-in function add_docstring>, 'meshgrid': <function meshgrid at 0x7fc9ce60a158>, 'delete': <function delete at 0x7fc9ce60a1e0>, 'insert': <function insert at 0x7fc9ce60a268>, 'append': <function append at 0x7fc9ce60a2f0>, 'interp': <function interp at 0x7fc9ce608ae8>, 'add_newdoc_ufunc': <built-in function _add_newdoc_ufunc>, 'column_stack': <function column_stack at 0x7fc9ce623620>, 'row_stack': <function vstack at 0x7fc9d41276a8>, 'dstack': <function dstack at 0x7fc9ce6236a8>, 'array_split': <function array_split at 0x7fc9ce6237b8>, 'split': <function split at 0x7fc9ce623840>, 'hsplit': <function hsplit at 0x7fc9ce6238c8>, 'vsplit': <function vsplit at 0x7fc9ce623950>, 'dsplit': <function dsplit at 0x7fc9ce6239d8>, 'apply_over_axes': <function apply_over_axes at 0x7fc9ce623510>, 'expand_dims': <function expand_dims at 0x7fc9ce623598>, 'apply_along_axis': <function apply_along_axis at 0x7fc9ce623488>, 'kron': <function kron at 0x7fc9ce623b70>, 'tile': <function tile at 0x7fc9ce623bf8>, 'get_array_wrap': <function get_array_wrap at 0x7fc9ce623ae8>, 'broadcast_to': <function broadcast_to at 0x7fc9ce611bf8>, 'broadcast_arrays': <function broadcast_arrays at 0x7fc9ce611d08>, 'diag': <function diag at 0x7fc9d403ba60>, 'diagflat': <function diagflat at 0x7fc9d403bae8>, 'eye': <function eye at 0x7fc9d403b9d8>, 'fliplr': <function fliplr at 0x7fc9d403b8c8>, 'flipud': <function flipud at 0x7fc9d403b950>, 'tri': <function tri at 0x7fc9d403bb70>, 'triu': <function triu at 0x7fc9d403bc80>, 'tril': <function tril at 0x7fc9d403bbf8>, 'vander': <function vander at 0x7fc9d403bd08>, 'histogram2d': <function histogram2d at 0x7fc9d403bd90>, 'mask_indices': <function mask_indices at 0x7fc9d403be18>, 'tril_indices': <function tril_indices at 0x7fc9d403bea0>, 'tril_indices_from': <function tril_indices_from at 0x7fc9d403bf28>, 'triu_indices': <function triu_indices at 0x7fc9ce608048>, 'triu_indices_from': <function triu_indices_from at 0x7fc9ce6080d0>, 'fix': <function fix at 0x7fc9d402d488>, 'isneginf': <function isneginf at 0x7fc9d402d6a8>, 'isposinf': <function isposinf at 0x7fc9d402d598>, 'pad': <function pad at 0x7fc9cdcfdbf8>, 'poly': <function poly at 0x7fc9ce62b510>, 'roots': <function roots at 0x7fc9ce62b620>, 'polyint': <function polyint at 0x7fc9ce1982f0>, 'polyder': <function polyder at 0x7fc9ce198378>, 'polyadd': <function polyadd at 0x7fc9ce198510>, 'polysub': <function polysub at 0x7fc9ce198598>, 'polymul': <function polymul at 0x7fc9ce198620>, 'polydiv': <function polydiv at 0x7fc9ce1986a8>, 'polyval': <function polyval at 0x7fc9ce198488>, 'poly1d': <class 'numpy.lib.polynomial.poly1d'>, 'polyfit': <function polyfit at 0x7fc9ce198400>, 'RankWarning': <class 'numpy.lib.polynomial.RankWarning'>, 'issubclass_': <function issubclass_ at 0x7fc9d41c10d0>, 'issubsctype': <function issubsctype at 0x7fc9d41c1158>, 'deprecate': <function deprecate at 0x7fc9d400d840>, 'deprecate_with_doc': <function <lambda> at 0x7fc9d400da60>, 'get_include': <function get_include at 0x7fc9d400d730>, 'info': <function info at 0x7fc9d400dd90>, 'source': <function source at 0x7fc9d400de18>, 'who': <function who at 0x7fc9d400db70>, 'lookfor': <function lookfor at 0x7fc9d400dea0>, 'byte_bounds': <function byte_bounds at 0x7fc9d400dae8>, 'safe_eval': <function safe_eval at 0x7fc9d40230d0>, 'ediff1d': <function ediff1d at 0x7fc9ce1987b8>, 'intersect1d': <function intersect1d at 0x7fc9ce1969d8>, 'setxor1d': <function setxor1d at 0x7fc9ce196a60>, 'union1d': <function union1d at 0x7fc9ce196bf8>, 'setdiff1d': <function setdiff1d at 0x7fc9ce196c80>, 'unique': <function unique at 0x7fc9ce1968c8>, 'in1d': <function in1d at 0x7fc9ce196ae8>, 'isin': <function isin at 0x7fc9ce196b70>, 'savetxt': <function savetxt at 0x7fc9ce1cdae8>, 'loadtxt': <function loadtxt at 0x7fc9ce1cda60>, 'genfromtxt': <function genfromtxt at 0x7fc9ce1cdbf8>, 'ndfromtxt': <function ndfromtxt at 0x7fc9ce1cdc80>, 'mafromtxt': <function mafromtxt at 0x7fc9ce1cdd08>, 'recfromtxt': <function recfromtxt at 0x7fc9ce1cdd90>, 'recfromcsv': <function recfromcsv at 0x7fc9ce1cde18>, 'save': <function save at 0x7fc9ce1cd7b8>, 'savez': <function savez at 0x7fc9ce1cd840>, 'savez_compressed': <function savez_compressed at 0x7fc9ce1cd8c8>, 'packbits': <built-in function packbits>, 'unpackbits': <built-in function unpackbits>, 'fromregex': <function fromregex at 0x7fc9ce1cdb70>, 'DataSource': <class 'numpy.lib._datasource.DataSource'>, 'fv': <function fv at 0x7fc9ce1d0048>, 'pmt': <function pmt at 0x7fc9ce1d0620>, 'nper': <function nper at 0x7fc9ce1d06a8>, 'ipmt': <function ipmt at 0x7fc9ce1d0730>, 'ppmt': <function ppmt at 0x7fc9ce1d0840>, 'pv': <function pv at 0x7fc9ce1d08c8>, 'rate': <function rate at 0x7fc9ce1d09d8>, 'irr': <function irr at 0x7fc9ce1d0a60>, 'npv': <function npv at 0x7fc9ce1d0ae8>, 'mirr': <function mirr at 0x7fc9ce1d0b70>, 'nansum': <function nansum at 0x7fc9ce61cb70>, 'nanmax': <function nanmax at 0x7fc9ce61c9d8>, 'nanmin': <function nanmin at 0x7fc9ce61c950>, 'nanargmax': <function nanargmax at 0x7fc9ce61cae8>, 'nanargmin': <function nanargmin at 0x7fc9ce61ca60>, 'nanmean': <function nanmean at 0x7fc9ce61cd90>, 'nanmedian': <function nanmedian at 0x7fc9ce623048>, 'nanpercentile': <function nanpercentile at 0x7fc9ce6230d0>, 'nanvar': <function nanvar at 0x7fc9ce623268>, 'nanstd': <function nanstd at 0x7fc9ce6232f0>, 'nanprod': <function nanprod at 0x7fc9ce61cbf8>, 'nancumsum': <function nancumsum at 0x7fc9ce61cc80>, 'nancumprod': <function nancumprod at 0x7fc9ce61cd08>, 'linalg': <module 'numpy.linalg' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/linalg/__init__.py'>, 'fft': <module 'numpy.fft' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/fft/__init__.py'>, 'random': <module 'numpy.random' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/random/__init__.py'>, 'ctypeslib': <module 'numpy.ctypeslib' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/ctypeslib.py'>, 'ma': <module 'numpy.ma' from '/usr/local/anaconda3/lib/python3.6/site-packages/numpy/ma/__init__.py'>}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'sin': <ufunc 'sin'>}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f649a09be18>, 'x': array([0.        , 0.10144928, 0.20289855, 0.30434783, 0.4057971 ,
       0.50724638, 0.60869565, 0.71014493, 0.8115942 , 0.91304348,
       1.01449275, 1.11594203, 1.2173913 , 1.31884058, 1.42028986,
       1.52173913, 1.62318841, 1.72463768, 1.82608696, 1.92753623,
       2.02898551, 2.13043478, 2.23188406, 2.33333333, 2.43478261,
       2.53623188, 2.63768116, 2.73913043, 2.84057971, 2.94202899,
       3.04347826, 3.14492754, 3.24637681, 3.34782609, 3.44927536,
       3.55072464, 3.65217391, 3.75362319, 3.85507246, 3.95652174,
       4.05797101, 4.15942029, 4.26086957, 4.36231884, 4.46376812,
       4.56521739, 4.66666667, 4.76811594, 4.86956522, 4.97101449,
       5.07246377, 5.17391304, 5.27536232, 5.37681159, 5.47826087,
       5.57971014, 5.68115942, 5.7826087 , 5.88405797, 5.98550725,
       6.08695652, 6.1884058 , 6.28985507, 6.39130435, 6.49275362,
       6.5942029 , 6.69565217, 6.79710145, 6.89855072, 7.        ]), 'y': array([ 1.        ,  0.99485843,  0.97948661,  0.95404259,  0.91878803,
        0.87408545,  0.82039454,  0.7582674 ,  0.6883429 ,  0.61134007,
        0.52805076,  0.43933143,  0.3460944 ,  0.24929843,  0.1499389 ,
        0.04903752, -0.05236811, -0.15323524, -0.25252663, -0.34922125,
       -0.44232479, -0.53087984, -0.61397579, -0.69075814, -0.76043733,
       -0.82229685, -0.87570058, -0.92009937, -0.95503665, -0.98015317,
       -0.99519064, -0.99999444, -0.99451516, -0.97880915, -0.95303792,
       -0.91746648, -0.8724606 , -0.8184831 , -0.75608903, -0.68592   ,
       -0.60869756, -0.5252158 , -0.43633318, -0.34296369, -0.24606746,
       -0.14664089, -0.04570638,  0.05569812,  0.15652988,  0.25575202,
        0.35234423,  0.44531323,  0.53370302,  0.61660468,  0.6931657 ,
        0.76259881,  0.82419002,  0.87730597,  0.92140047,  0.95602009,
        0.98080883,  0.99551178,  0.99997776,  0.99416083,  0.97812081,
        0.95202265,  0.91613472,  0.87082605,  0.81656256,  0.75390225])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f5d8abeae18>, 'x': array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1, 2.2, 2.3, 2.4, 2.5,
       2.6, 2.7, 2.8, 2.9, 3. , 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8,
       3.9, 4. , 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5. , 5.1,
       5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6. , 6.1, 6.2, 6.3, 6.4,
       6.5, 6.6, 6.7, 6.8, 6.9, 7. ]), 'y': array([ 1.        ,  0.99500417,  0.98006658,  0.95533649,  0.92106099,
        0.87758256,  0.82533561,  0.76484219,  0.69670671,  0.62160997,
        0.54030231,  0.45359612,  0.36235775,  0.26749883,  0.16996714,
        0.0707372 , -0.02919952, -0.12884449, -0.22720209, -0.32328957,
       -0.41614684, -0.5048461 , -0.58850112, -0.66627602, -0.73739372,
       -0.80114362, -0.85688875, -0.90407214, -0.94222234, -0.97095817,
       -0.9899925 , -0.99913515, -0.99829478, -0.98747977, -0.96679819,
       -0.93645669, -0.89675842, -0.84810003, -0.79096771, -0.7259323 ,
       -0.65364362, -0.57482395, -0.49026082, -0.40079917, -0.30733287,
       -0.2107958 , -0.11215253, -0.01238866,  0.08749898,  0.18651237,
        0.28366219,  0.37797774,  0.46851667,  0.55437434,  0.63469288,
        0.70866977,  0.77556588,  0.83471278,  0.88551952,  0.92747843,
        0.96017029,  0.98326844,  0.9965421 ,  0.99985864,  0.99318492,
        0.97658763,  0.95023259,  0.91438315,  0.86939749,  0.8157251 ,
        0.75390225])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fb39f1cce18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> x
array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ])
>>> x[0]
0.0
>>> x[10]
4.0
>>> y
array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])
>>> x[11]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x[11]
IndexError: index 11 is out of bounds for axis 0 with size 11
>>> len(y)
11
>>> len(x)
11
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f1a68129e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

Warning (from warnings module):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/font_manager.py", line 281
    'Matplotlib is building the font cache using fc-list. '
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f5051b89ea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f35304bbe18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f6859ee7e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fb7a60fce18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}



print(plt.plot.__doc__)


>>> 
>>> print(plt.plot.__doc__)
Plot lines and/or markers to the
:class:`~matplotlib.axes.Axes`.  *args* is a variable length
argument, allowing for multiple *x*, *y* pairs with an
optional format string.  For example, each of the following is
legal::

    plot(x, y)        # plot x and y using default line style and color
    plot(x, y, 'bo')  # plot x and y using blue circle markers
    plot(y)           # plot y using x as index array 0..N-1
    plot(y, 'r+')     # ditto, but with red plusses

If *x* and/or *y* is 2-dimensional, then the corresponding columns
will be plotted.

If used with labeled data, make sure that the color spec is not
included as an element in data, as otherwise the last case
``plot("v","r", data={"v":..., "r":...)``
can be interpreted as the first case which would do ``plot(v, r)``
using the default line style and color.

If not used with labeled data (i.e., without a data argument),
an arbitrary number of *x*, *y*, *fmt* groups can be specified, as in::

    a.plot(x1, y1, 'g^', x2, y2, 'g-')

Return value is a list of lines that were added.

By default, each line is assigned a different style specified by a
'style cycle'.  To change this behavior, you can edit the
axes.prop_cycle rcParam.

The following format string characters are accepted to control
the line style or marker:

================    ===============================
character           description
================    ===============================
``'-'``             solid line style
``'--'``            dashed line style
``'-.'``            dash-dot line style
``':'``             dotted line style
``'.'``             point marker
``','``             pixel marker
``'o'``             circle marker
``'v'``             triangle_down marker
``'^'``             triangle_up marker
``'<'``             triangle_left marker
``'>'``             triangle_right marker
``'1'``             tri_down marker
``'2'``             tri_up marker
``'3'``             tri_left marker
``'4'``             tri_right marker
``'s'``             square marker
``'p'``             pentagon marker
``'*'``             star marker
``'h'``             hexagon1 marker
``'H'``             hexagon2 marker
``'+'``             plus marker
``'x'``             x marker
``'D'``             diamond marker
``'d'``             thin_diamond marker
``'|'``             vline marker
``'_'``             hline marker
================    ===============================


The following color abbreviations are supported:

==========  ========
character   color
==========  ========
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
==========  ========

In addition, you can specify colors in many weird and
wonderful ways, including full names (``'green'``), hex
strings (``'#008000'``), RGB or RGBA tuples (``(0,1,0,1)``) or
grayscale intensities as a string (``'0.8'``).  Of these, the
string specifications can be used in place of a ``fmt`` group,
but the tuple forms can be used only as ``kwargs``.

Line styles and colors are combined in a single format string, as in
``'bo'`` for blue circles.

The *kwargs* can be used to set line properties (any property that has
a ``set_*`` method).  You can use this to set a line label (for auto
legends), linewidth, anitialising, marker face color, etc.  Here is an
example::

    plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
    plot([1,2,3], [1,4,9], 'rs',  label='line 2')
    axis([0, 4, 0, 10])
    legend()

If you make multiple lines with one plot command, the kwargs
apply to all those lines, e.g.::

    plot(x1, y1, x2, y2, antialiased=False)

Neither line will be antialiased.

You do not need to use format strings, which are just
abbreviations.  All of the line properties can be controlled
by keyword arguments.  For example, you can set the color,
marker, linestyle, and markercolor with::

    plot(x, y, color='green', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=12).

See :class:`~matplotlib.lines.Line2D` for details.

The kwargs are :class:`~matplotlib.lines.Line2D` properties:

  agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array 
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: bool 
  antialiased or aa: [True | False] 
  clip_box: a `~.Bbox` instance 
  clip_on: bool 
  clip_path: [(`~matplotlib.path.Path`, `~.Transform`) | `~.Patch` | None] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a `~.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: object 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: `~.AbstractPathEffect` 
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points
  rasterized: bool or None 
  sketch_params: (scale: float, length: float, randomness: float) 
  snap: bool or None 
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: bool 
  xdata: 1D array 
  ydata: 1D array 
  zorder: float 

kwargs *scalex* and *scaley*, if defined, are passed on to
:meth:`~matplotlib.axes.Axes.autoscale_view` to determine
whether the *x* and *y* axes are autoscaled; the default is
*True*.

.. note::
    In addition to the above described arguments, this function can take a
    **data** keyword argument. If such a **data** argument is given, the
    following arguments are replaced by **data[<arg>]**:

    * All arguments with the following names: 'x', 'y'.



>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fd0a01a3e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 20, in <module>
    plt.plot(x, y, bo)
NameError: name 'bo' is not defined
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f10f1f83ea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f0fa009eea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f2479bb7ea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f09731ccea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f262045aea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 20, in <module>
    plt.plot(x, y, "po")
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py", line 3261, in plot
    ret = ax.plot(*args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/__init__.py", line 1717, in inner
    return func(ax, *args, **kwargs)
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_axes.py", line 1372, in plot
    for line in self._get_lines(*args, **kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 356, in _plot_args
    linestyle, marker, color = _process_plot_format(tup[-1])
  File "/usr/local/anaconda3/lib/python3.6/site-packages/matplotlib/axes/_base.py", line 116, in _process_plot_format
    'Illegal format string "%s"; two marker symbols' % fmt)
ValueError: Illegal format string "po"; two marker symbols
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fcf809e3ea0>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7ffb7c0b1e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fbd25910e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7fb41c041e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'linspace': <function linspace at 0x7f2bad12be18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362])}
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 13, in <module>
    y1 = sin(x)
NameError: name 'sin' is not defined
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
Traceback (most recent call last):
  File "/home/user/RTR105/1B1.py", line 13, in <module>
    y1 = sin(x)
NameError: name 'sin' is not defined
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f052b840e18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), 'y1': array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f41cd64ae18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), 'y1': array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7f36c9dfee18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), 'y1': array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR105/1B1.py', 'sys': <module 'sys' (built-in)>, 'cos': <ufunc 'cos'>, 'sin': <ufunc 'sin'>, 'linspace': <function linspace at 0x7fd4e705fe18>, 'x': array([0. , 0.4, 0.8, 1.2, 1.6, 2. , 2.4, 2.8, 3.2, 3.6, 4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), 'y1': array([ 0.        ,  0.38941834,  0.71735609,  0.93203909,  0.9995736 ,
        0.90929743,  0.67546318,  0.33498815, -0.05837414, -0.44252044,
       -0.7568025 ])}

===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================

===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B1.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B2.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B2.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B2.py =====================
>>> 
===================== RESTART: /home/user/RTR105/1B2.py =====================

===================== RESTART: /home/user/RTR105/1B2.py =====================

===================== RESTART: /home/user/RTR105/1B2.py =====================

===================== RESTART: /home/user/RTR105/1B2.py =====================

===================== RESTART: /home/user/RTR105/1B2.py =====================

===================== RESTART: /home/user/RTR105/1B2.py =====================
