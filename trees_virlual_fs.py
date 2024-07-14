# Реализуйте функцию generate, которая создает
#  такую файловую структуру:

# # Обратите внимание на метаданные ниже

# python-package  # Директория (метаданные:
#  {'hidden': True})
# ├── Makefile  # Файл
# ├── README.md  # Файл
# ├── dist  # Пустая директория
# ├── tests  # Директория
# │   └── test_solution.py  # Файл
# ├── pyproject.toml  # Файл
# └── .venv  # Директория (метаданные: {'owner':
#  'root', 'hidden': False})
#     └── lib  # Директория
#         └── python3.6  # Директория
#             └── site-packages  # Директория
#                 └── hexlet-python-package.egg-link  # Файл


from hexlet.fs import mkdir, mkfile


# BEGIN (write your solution here)
def generate():
    Makefile = mkfile('Makefile')
    README = mkfile('README.md')
    dist = mkdir('dist')
    tests = mkdir('tests', [mkfile('test_solution.py')])
    pyproject = mkfile('pyproject.toml')
    in_python36 = mkdir('site-packages',
                        [mkfile('hexlet-python-package.egg-link')]
                        )
    in_lib = mkdir('python3.6', [in_python36])
    in_venv = mkdir('lib', [in_lib])
    venv = mkdir('.venv', [in_venv], {'owner': 'root', 'hidden': False})
    children = [Makefile, README, dist, tests, pyproject, venv]
    fs = mkdir('python-package', children, {'hidden': True})
    return fs
# END


# BEGIN reference solution
def generate_ref():
    return mkdir(
        'python-package',
        [
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist'),
            mkdir('tests', [
                mkfile('test_solution.py'),
            ]),
            mkfile('pyproject.toml'),
            mkdir(
                '.venv',
                [
                    mkdir('lib', [
                        mkdir('python3.6', [
                            mkdir('site-packages', [
                                mkfile('hexlet-python-package.egg-link'),
                            ]),
                        ]),
                    ]),
                ],
                {'owner': 'root', 'hidden': False},
            ),
        ],
        {'hidden': True},
    )
# END reference solution
