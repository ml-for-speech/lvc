from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()
setup(
    name="lvc",
    version="1.0.1",
    author="mrfakename",
    description="Unofficial pip package for zero-shot voice conversion",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/fakerybakery/lvc",
    packages=find_packages(),
    install_requires=[
        "librosa",
        "soundfile",
        "matplotlib",
        "numpy",
        "omegaconf",
        "praat-parselmouth",
        "scipy",
        "tensorboard",
        "torch",
        "torchaudio",
        "tqdm",
        "transformers",
        "cached_path",
    ]
)
