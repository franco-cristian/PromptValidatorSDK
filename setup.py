from setuptools import setup, find_packages

setup(
    name="azure-prompt-sdk",
    version="1.0.0",
    description="SDK para validar, corregir y optimizar prompts utilizando Azure OpenAI, AI Content Safety y Cosmos DB.",
    author="Tu Nombre",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "openai",
        "azure-identity",
        "azure-keyvault-secrets",
        "azure-ai-contentsafety",
        "azure-cosmos"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)