import os
import glob
from . import module3
from . import module4
from . import module5

# demonstration package for start import (import *, from xxx import *)

# see-also:
# - Python パッケージ作成: __init__.py の __all__ を手作業でメンテナンスしたくない - Qiita
#   - https://qiita.com/suzuki-kei/items/8fea67655abf216a5013

# except __init__.py
glob_module_py_pattern = os.path.join(os.path.dirname(__file__), "[a-zA-Z0-9]*.py")
module_py_files = []
for file in glob.glob(glob_module_py_pattern):
    module_py_files.append(file)

all_module_names = []
for fullpath in module_py_files:
    module_basename = os.path.basename(fullpath)
    module_name = os.path.splitext(module_basename)[0]
    all_module_names.append(module_name)

# __all__ = all_module_names
# -> 実際に試してみたところ、__all__ を動的に生成すると vscode 側で認識できず、自動補完などに支障が出る。
__all__ = ["module3", "module4", "module5"]
# -> 実際に import * すると、flake8 で以下のルール違反で指摘される。
# "Name may be undefined, or defined from star imports: module (F405)"
# https://www.flake8rules.com/rules/F405.html

# star import があまり歓迎されてない雰囲気。
# -> 利用する側の import を少しでも軽量にするため、パッケージ側でエイリアスを作ってみる。
module3_sub = module3.module3_sub
ClassInModule3 = module3.ClassInModule3
module4_sub = module4.module4_sub
ClassInModule4 = module4.ClassInModule4
module5_sub = module5.module5_sub
ClassInModule5 = module5.ClassInModule5
