import os
import zipfile

def makeZip(folder, outputDir = ''):

    # remove trailing slashes and backslashes
    folder = folder.rstrip("/\\")

    # if output path is not specified make zip in working directory
    if not outputDir:

        outputDir = os.path.dirname(folder)

    # make output directory if not exists
    os.makedirs(outputDir, exist_ok=True)

    # get name of folder to be compressed
    folderName = os.path.basename(folder)

    # make zip file name
    zipName = "[BabyxBoss] {}.zip".format(folderName)

    # make zip path
    outputPath = os.path.join(outputDir,zipName)

    # open zipfile with mode 'w' (create or overwrite)
    with zipfile.ZipFile(outputPath,mode='w',compression=zipfile.ZIP_DEFLATED) as zip:
        
        # loop to all files in the specified folder and make relative path to keep orignal strusture
        for root,dirs,files in os.walk(folder):
            for file in files:
                filePath = os.path.join(root,file)
                relPath = os.path.relpath(filePath,folder)
                zip.write(filePath,os.path.join(folderName,relPath))
