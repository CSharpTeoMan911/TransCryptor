from setuptools import setup, find_packages

setup(
    name='TransCryptor',
    version='1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'TransCryptor=Main_Package.Trans_Cryptor:main_entry_point',
        ]
    },
    install_requires=[
        'numpy',
        'whisper',
        'pytube'
    ]
)