Why do we include __init__.py files?
-Marks a folder as a python package. Allows module imports from sub directories

What is the purpose of .gitkeep files?
-To track otherwise empty folders
NB: Git does not track folders. So this allows others to get the folder when they clone

Why separate src/ from tests/?
-for safer refactoring


What directories are created inside the virtual environment?
-bin
-include
-lib

Where are packages installed when the environment is active?
site_packages

Before activation:
  Python location: /usr/bin/python
  Pip location: ~/.local/bin/pip

After activation:
  Python location: ~/PROJECTS/AI_ENG/AI_ENG_LABS/Module_1_Python_Fundamentals/exercise-01-environment-setup/.venv/bin/python 
  Pip location: ~/PROJECTS/AI_ENG/AI_ENG_LABS/Module_1_Python_Fundamentals/exercise-01-environment-setup/.venv/bin/pip

Why do we pin exact versions (==) instead of using >= or ~=?
- exact reproducability.
- same behaviour in dev and production  

What happens if we don't pin versions?
- loss of reproducibility. the application breaks in other environments 

Reproducability in ML is Fragile!! Requires control of all these:
- requirements.txt freeze → controls Python layer
- Docker base image → controls OS layer
- Pinned CUDA image → controls GPU runtime
- Seed control + deterministic flags → controls algorithm randomness


Why does requirements-frozen.txt have more packages?
- it contains transitive dependencies

What are transitive dependencies?
- These are packages required by another package to run 

When should you use frozen vs. unpinned requirements?
- frozen is for total  reproducability while unpinned allows installation of the latest version(when you want flexibility e.g. when building a library)

Never commit .env to Git. Even if you remove the file, it will remain in git history