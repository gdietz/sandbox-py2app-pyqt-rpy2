import os

# Set R environment variables
oldpath = os.environ["PATH"]
cwd = os.getcwd()
rpath = os.path.join(cwd, "..","Resources", "Resources") # second 'Resources' is R directory
os.environ["PATH"] = os.path.join(rpath, "bin") + os.pathsep + oldpath
print("new path is: %s" % os.environ["PATH"])

os.environ["R"] = os.path.join(cwd, rpath, "bin")
os.environ["R_HOME"] = os.path.join(cwd, rpath)

# we are ready to start the main program loop
import main
if __name__ == "__main__":
    main.start()