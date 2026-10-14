# imp was removed in Python 3.12; the vendored waf only uses imp.new_module
from types import ModuleType as new_module  # noqa: F401
