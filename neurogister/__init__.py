
__version__ = '0.1.0'


def get_root():
    import os
    return os.path.realpath(f"{os.path.dirname(os.path.abspath(__file__))}/..")


STORE_ROOT = f"/store"
REGISTRY_ROOT = f"/data"
REPOSITORY = "https://github.com/AlexVCaron/scil_data.git"
PUSH_ACCESS = True