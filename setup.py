from setuptools import setup, find_packages

setup(
    name = 'src',
    author = 'Saara Sugandh',
    version='0.1',
    packages=find_packages(),
    author_email = 'saara.sugandh@gmail.com',
    description = 'A machine learning-based movie recommendation system that suggests films based on user preferences.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = ['src'],
    python_requires = '>=3.8',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'nltk',
        'streamlit'
    ],
)
with open('/Users/saarasugandh/Movie_Recommendation_System/README.md', 'r') as f:
    long_description = f.read()
 

