import setuptools

setuptools.setup(
    name="gen_strong_pw",
    version="0.0.1",
    author="Ben Southcott",
    author_email="",
    description="tool for generating a strong password",
    url="https://github.com/blsouthcott/gen-strong-pw",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pyperclip==1.8.2',
                      'PySimpleGUI==4.57.0'
                      ]
)
