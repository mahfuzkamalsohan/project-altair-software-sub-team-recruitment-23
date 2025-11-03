from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    	('share/ament_index/resource_index/packages', ['resource/my_package']),
    	('share/my_package', ['package.xml']),
    	('share/my_package/launch', ['launch/gazebo.launch.py']),
    	('share/my_package/urdf', ['urdf/my_robot.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pohan',
    maintainer_email='pohan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = my_package.publisher:main',
            'subscriber = my_package.subscriber:main',
            'move_turtle = my_package.moveTurtle:main',
            'move_robot = my_package.move_robot:main',
            'video_publisher = my_package.video_publisher:main',
            'video_subscriber = my_package.video_subscriber:main',
        ],
    },
)

