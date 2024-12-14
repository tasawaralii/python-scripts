import os
import zipfile


def extractZip(zipPath,outputDir = ''):

    # if no output folder is provided use the the directory containing zip file
    if not outputDir:
        outputDir = os.path.dirname(zipPath)

    # if output directory dont exist make one
    os.makedirs(outputDir,exist_ok=True)

    # open zip file with mode 'r' (read-only)
    with zipfile.ZipFile(zipPath,'r') as zip:
        zip.extractall(outputDir)
