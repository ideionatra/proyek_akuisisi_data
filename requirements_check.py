import sys, platform
print("Python :", sys.version)
print("Platform:", platform.platform())
for lib in ["pandas", "numpy", "requests", "bs4"]:
    try:
        m = __import__(lib)
        print(f"{lib:10s}: {getattr(m, '__version__', 'terpasang')}")
    except ImportError:
        print(f"{lib:10s}: BELUM TERPASANG -> pip install {lib}")