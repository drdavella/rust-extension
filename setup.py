from setuptools import find_packages, setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rust-extension",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7,<3.12",
    rust_extensions=[
        RustExtension(
            "mypackage.bindings._corelib",
            "src/rust/Cargo.toml",
            binding=Binding.PyO3,
            py_limited_api=True,
            rust_version=">=1.56.0",
            features=["pyo3/abi3-py37"],
        )
    ],
)
