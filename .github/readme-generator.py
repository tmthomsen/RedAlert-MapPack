import subprocess
from pathlib import Path
from collections import defaultdict

NAME_README_FILE_OUTPUT = "README.md"
MAP_NAME_SPLITTER = "_v"
MAP_PREVIEW_IMAGES_FOLDER_URL = "/readme-previews/"
MAP_FOLDER_URL = "https://github.com/tmthomsen/RedAlert_TheStrandvaskerCollection/raw/main/maps/"

def GenerateReadme(outputFile):
    try:
        parentDir = Path.cwd().parent

        mapFilesPaths = list(parentDir.glob("*.mpr"))
        mapFiles = [str(f) for f in mapFilesPaths]

        #subprocess.run(["git","pull"])

        with open(parentDir / outputFile, "w") as readmeFile:
            readmeFile.write("# C&C Red Alert: The Strandvasker Collection (Map Pack)\n")
            readmeFile.write("A collection of the absolute best maps created for C&C Red Alert post anno 2020 in Jutland, Denmark.<br>\n\n")

            readmeFile.write("### Installation\n")
            readmeFile.write("For CnCNet, place the `.mpr` files inside the `...\CnCNet\RedAlert1_Online\Maps` folder.<br><br>\n\n")

            mapGroups = defaultdict(list)
            for file in mapFiles:
                if MAP_NAME_SPLITTER in file:
                    groupName = file.split(MAP_NAME_SPLITTER)[0]
                    mapGroups[groupName].append(file)

            for groupName, mapVersions in sorted(mapGroups.items()):
                readmeFile.write("## " + groupName + "\n")

                for mapNameFull in sorted(mapVersions):
                    mapNameClean = mapNameFull.replace("_", " ").replace(".mpr", "")
                    readmeFile.write(GetDownloadURL(mapNameClean, mapNameFull) + "<br>\n")
                    readmeFile.write(GetMapPreviewImageStr(mapNameClean, mapNameFull) + "<br>\n")

                readmeFile.write("<br>\n")

        #subprocess.run(["git","add", NAME_README_FILE_OUTPUT])
        #subprocess.run(["git","commit", "-m", "Readme auto-updated."])
        #subprocess.run(["git", "push"])

        print(f"Succesfully written to '{outputFile}'.\n")

    except Exception as e:
        print(f"Error: {e}")

def GetDownloadURL(mapNameClean, mapNameFull) -> str:
    return f"### [{mapNameClean}]({MAP_FOLDER_URL}{mapNameFull})"

def GetMapPreviewImageStr(mapNameClean, mapNameFull) -> str:
    mapNameAndVersion = mapNameFull.replace(".mpr", ".png")
    return f"![{mapNameClean}]({MAP_PREVIEW_IMAGES_FOLDER_URL}{mapNameAndVersion})"

if __name__ == "__main__":
    GenerateReadme(NAME_README_FILE_OUTPUT)