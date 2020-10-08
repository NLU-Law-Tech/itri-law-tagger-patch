
import setuptools

setuptools.setup(
    name="lt_patch", # 
    version='0.0.1',
    author="Philip Huang",
    author_email="p208p2002@gmail.com",
    description="docker-for-ai-dev-cli",
    url="https://github.com/NLU-Law-Tech/itri-law-tagger-patch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['lt-patch=lt_patch:main'],
    },
    python_requires='>=3.5',
    install_requires = ['VerdictFormat @ git+https://github.com/NLU-Law-Tech/VerdictFormat@master','rglob'],
    include_package_data=True
)