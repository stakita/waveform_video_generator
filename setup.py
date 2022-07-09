from setuptools import setup, find_packages

setup(
    name = 'waveform_video_generator',
    author = 'Simon Takita',
    version = '0.1',
    package_dir = {'waveform_video': 'waveform_video'},
    packages = ['waveform_video'],
    install_requires = [
        'docopt',
        'opencv-python',
        'numpy',
        'scikit-sound',
        'matplotlib'
    ],
    entry_points = {
        'console_scripts': [
            'create_waveform_video = waveform_video.create_waveform_video:main',
        ]
    }
)