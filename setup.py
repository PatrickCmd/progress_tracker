from setuptools import setup

setup(
    name='Progress Tracker',
    version='1.0.0',
    python_modules=['tracker'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        tracker=tracker:cli
    '''
)