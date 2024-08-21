import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"

REPO_NAME = "text-summarizer"
AUTHOR_USER_NAME = "mikemayuare"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mike.mayuare@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python text summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)