from setuptools import setup

package_name = 'avatar2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='walleed',
    maintainer_email='walleed@todo.todo',
    description='TODO',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sound_capture = avatar2.audio_input:main',
            'sound_dump = avatar2.audio_dump:main',
            'avatar_camera = avatar2.opencv_camera:main',
            'head_info = avatar2.yolo_head:main',
        ],
    },
)
