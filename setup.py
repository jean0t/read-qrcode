from setuptools import setup, find_packages

setup(
    name="read-qrcode",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["read_qrcode"],
    entry_points={
        "console_scripts": [
            "read-qrcode=read_qrcode:main",
        ],
    },
    install_requires=[
        "opencv-python",
        "pyautogui",
        "numpy",
    ],
    python_requires=">=3.11.2",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    author="jean0t",
    description="A script to capture screenshots and read QR codes using OpenCV.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jean0t/read-qrcode",
    include_package_data=True,
)

