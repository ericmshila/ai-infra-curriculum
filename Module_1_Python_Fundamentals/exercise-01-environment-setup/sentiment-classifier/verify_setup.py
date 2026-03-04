#!/usr/bin/env python3
"""
verify_setup.py - Verify development environment setup
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verify Python version is 3.11"""
    if sys.version_info[0:2] != (3,11):
        raise RuntimeError(f"Wrong Python Version. Expected 3.11. Got"
                           f"{sys.version_info.major}.{sys.version_info.minor}")

def check_virtual_environment():
    """Verify running in virtual environment"""
    if sys.prefix == sys.base_prefix:
        raise RuntimeError('Virtual environment not active. Run: source venv/bin/activate')

def check_required_packages():
    """Verify all required packages are installed"""
    required_packages = [
        "torch",
        "transformers",
        "pandas",
        "pytest",
        "black",
        "mypy"
    ]
    
    for package in required_packages:
        print(package)

    # TODO: Try importing each package
    # Report which are missing
    pass

def check_project_structure():
    """Verify project directories exist"""
    required_dirs = [
        "src",
        "tests",
        "data",
        "models",
        "configs"
    ]

    required_files = [
        "requirements.txt",
        "requirements-dev.txt",
        ".gitignore",
        ".env.example"
    ]

    # TODO: Check each directory and file exists
    # Report any missing
    pass

def check_git_setup():
    """Verify git configuration"""
    # TODO: Check if .git directory exists
    # Verify .gitignore includes venv/
    pass

def main():
    print("Verifying Development Environment Setup")
    print("=" * 50)

    checks = [
        ("Python Version", check_python_version),
        ("Virtual Environment", check_virtual_environment),
        ("Required Packages", check_required_packages),
        ("Project Structure", check_project_structure),
        ("Git Configuration", check_git_setup)
    ]

    all_passed = True

    for check_name, check_func in checks:
        try:
            check_func()
            print(f"✓ {check_name}")
        except Exception as e:
            print(f"✗ {check_name}: {e}")
            all_passed = False

    print("=" * 50)

    if all_passed:
        print("All checks passed! Environment is ready.")
        return 0
    else:
        print("Some checks failed. Please fix issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())