import os, shutil, pygsheets

ESSAY_FOLDER_COLUMN = 1
ATTRIBUTION_COLUMN = 2
LABEL_COLUMN = 4
URL_COLUMN = 8

PATH_TO_KENT_REPO = os.getcwd() + "/../kent"
PATH_TO_IMAGE_REPO = os.getcwd()

OUTPUT_FILE = "output.txt"

missingLabels = []
missingFiles = []

# Converts 1-26 to values A-Z
def getChrFromValue(value):
    startingColumnValue = ord("A")
    return chr(startingColumnValue + value)

# Gets the letter for the last column in the worksheet
def getLastColumn(columns):

    # If more than 26 columns column will be 2 characters (e.g. 'AZ' or 'BH')
    if (columns > 26):
        firstCharValue = trunc(columns / 26)
        secondCharValue = columns - (firstCharValue * 26)

        return getChrFromValue(firstCharValue) + getChrFromValue(secondCharValue)
    
    else:
        return getChrFromValue(columns)

# Reads the google sheet and converts it to 2D array of images
def readGSheet(gSheetKey):
    print("Reading gSheet")

    gClient = pygsheets.authorize()
    gSheet = gClient.open_by_key(gSheetKey)

    worksheet = gSheet.sheet1

    lastColumn = getLastColumn(worksheet.cols)
    lastRow = worksheet.rows

    images = worksheet.range("A2:{}{}".format(lastColumn, lastRow))

    # Convet all elements to unformatted values
    return [[cell.value_unformatted for cell in image] for image in images]

# Filter list of images to only self hosted images
def getSelfHostedImages(images):
    selfHostedImages = []

    for image in images:
        url = image[URL_COLUMN]

        if ((not url.startswith("https://")) and (not url == "")):
            selfHostedImages.append(image)

    return selfHostedImages


# Creates list of essay folders 
def getEssayFolders(images):
    print("Getting essay folders")

    folders = []
    for image in images:
        essayFolder = image[ESSAY_FOLDER_COLUMN]
        if (not essayFolder in folders):
            folders.append(essayFolder)

    return folders

# Creates folders for essay to be stored in
def createEssayFolders(essayFolders):
    print("Creating essay folders")

    for folder in essayFolders:
        try:
            os.mkdir("{}/{}".format(PATH_TO_IMAGE_REPO, folder))      
        except FileExistsError:
            pass  

# Get the current path of the image
def getCurrentPath(image, essayFolders):
    essayFolder = image[ESSAY_FOLDER_COLUMN]
    currentPath = image[URL_COLUMN]

    startsWithEssayFolder = False

    for folder in essayFolders:
        if (currentPath.startswith(folder) or currentPath.startswith("/" + folder)):
            startsWithEssayFolder = True
    
    # Add essay folder to path (as image is in essay folder but may be referenced by an essay already in
    # that folder)
    if (not startsWithEssayFolder):
        currentPath = essayFolder + "/" + currentPath

    # Ensure consistent formatting
    if (not currentPath.startswith("/")):
        currentPath = "/" + currentPath

    return (PATH_TO_KENT_REPO + "/" + currentPath).replace("//", "/")

# Get the new path for the image, doesnt include file type
def getNewPath(image):

    essayFolder = image[ESSAY_FOLDER_COLUMN]

    # If label is missing, use files current name
    if (image[LABEL_COLUMN] == ""):

        fileName = os.path.basename(image[URL_COLUMN])
        fileName.split(".")[0].replace(" ", "_")
        missingLabels.append([image[URL_COLUMN], fileName])

    else:
        fileName = image[LABEL_COLUMN].replace(" ", "_")

    return "{}/{}/{}".format(PATH_TO_IMAGE_REPO, essayFolder, fileName)

# Copy images from old path to new path
def copyImages(images, essayFolders):
    print("Copying images")

    successfulCopies = 0
    
    for image in images:

        # Get type of image (.png or .jpg)
        fileFormat = os.path.splitext(image[URL_COLUMN])[1]

        currentPath = getCurrentPath(image, essayFolders)
        newPath = getNewPath(image) + fileFormat

        # Try and copy file
        try:
            shutil.copy(currentPath, newPath)
            successfulCopies += 1
        except FileNotFoundError:
            missingFiles.append(currentPath)

    return successfulCopies

# Create YAML files to give IIIF image required metadata
def createYAMLFiles(images):
    print("Creating YAML files")

    for image in images:

        path = getNewPath(image) + ".yaml"

        fileContent = "requiredStatement\n"
        fileContent += "label: attribution\n"
        fileContent += "value: {}\n".format(image[ATTRIBUTION_COLUMN])

        with open(path, 'w') as yamlFile:
            yamlFile.write(fileContent)

# Create report and output to screen and output file
def generateReport(successfulCopies):
    
    output = ["Successful copies: {}".format(successfulCopies)]

    # Report all files were missing
    if (len(missingFiles) > 0):
        output.append("Missing files:")
        for missingFile in missingFiles:
            output.append("\t{}".format(missingFile))
    else:
        output.append("No missing files")
    
    # Report all labels that were missing
    if (len(missingLabels) > 0):
        output.append("Missing labels:")
        for missingLabel in missingLabels:
            url = missingLabel[0]
            fileName = missingLabel[1]
            output.append("\t'{}' named '{}'".format(url, fileName))
    else:
        output.append("No missing labels")

    for line in output:
        print(line)

    # Clear output file
    with open(OUTPUT_FILE, 'w') as outputFile:
        outputFile.write("")

    with open(OUTPUT_FILE, 'a') as outputFile:
        for line in output:
            outputFile.write("{}\n".format(line))

images = readGSheet("1I_kj9EYWFJc5iR6Pxd32hV11GO86NW1vJR58D-ZcxHA")
selfHostedImages = getSelfHostedImages(images)
essayFolders = getEssayFolders(selfHostedImages)

createEssayFolders(essayFolders)
createYAMLFiles(selfHostedImages)

successfulCopies = copyImages(selfHostedImages, essayFolders)
generateReport(successfulCopies)