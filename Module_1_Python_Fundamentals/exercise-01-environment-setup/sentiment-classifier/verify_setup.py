#!/usr/bin/env python3
"""
verify_setup.py - Verify development environment setup
"""

import sys
import subprocess
from pathlib import Path
import importlib

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
    
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ModuleNotFoundError:
            missing_packages.append(package)
    if missing_packages:        
        raise RuntimeError(f"Missing packages: {', '.join(missing_packages)}")

def check_project_structure():
    """Verify project directories exist"""
    required_dirs = [
        "src",
        "tests",
        "data",
        "models",
        "configs",
    ]

    required_files = [
        "requirements.txt",
        "requirements-dev.txt",
        ".gitignore",
        ".env.example"
    ]
    root = Path(__file__).parent

    missing_dirs = []
    missing_files = []
    
    for each_dir in required_dirs:
        path = root/each_dir
        if not path.is_dir():
            missing_dirs.append(each_dir)
            
    for each_file in required_files:
        path = root/each_file
        if not path.is_file():
            missing_files.append(each_file)

    errors = [] # join the errors in case of any
    if missing_dirs:
        errors.append(f"Missing directories: {', '.join(missing_dirs)}")
        
    if missing_files:
        errors.append(f"Missing files: {', '.join(missing_files)}")
    
    if errors:
        raise RuntimeError('\n'.join(errors))


def check_git_setup():
    """Verify git configuration"""
    # I am using git to track all modules and exercises so my script checks upwards till it gets to 
    def check_git_setup():

        current = Path(__file__).parent # parent folder
        
        while True:
            git_folder = current/".git"
            if git_folder.is_dir():
                return
            if current == current.parent:
                break    
            current = current.parent
            
        raise RuntimeError("git not found. Use git init to initialize")

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