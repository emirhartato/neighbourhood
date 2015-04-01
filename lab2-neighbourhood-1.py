# ----------------------------------------------------------------------------------
# PURPOSE: CALCULATE DISTANCES BETWEEN LOCATIONS
# ----------------------------------------------------------------------------------

# This script is designed to read in a series of locations from a text file and
# produce an output text file that contains the distances to those locations
# given a user specified location.

# ----------------------------------------------------------------------------------
# STEP 1: CREATE A FUNCTION TO CALCULATE THE DISTANCE BETWEEN TWO COORDINATE TUPLES
# ----------------------------------------------------------------------------------

# Define a function called "calcDistance" that has inputs of two coordinates tuples
def calcDistance(coordTuple1, coordTuple2):
    # Extract the x value of the first coordinate as "x1"
    x1 = coordTuple1[0]
    # Extract the y value of the first coordinate as "y1"
    y1 = coordTuple1[1]
    # Extract the x value of the second coordinate as "x2"
    x2 = coordTuple2[0]
    # Extract the y value of the second coordinate as "y2"
    y2 = coordTuple2[1]    
    # Calculate the difference between x1 and x2 as "xDif"
    xDif = x1 - x2
    # Calculate the difference between y1 and y2 as "yDif"
    yDif = y1 - y2
     # Import the math Python module
    import math
    # Using the math.hypot function calculate the distance between the coordinate
    # tuples given the differences between the x and y values
    distance = math.hypot(xDif, yDif)
    # Use the return function to return the distance value
    return(distance)

# ----------------------------------------------------------------------------------
# STEP 2: READ IN THE LOCATION DATA INTO A LIST
# ----------------------------------------------------------------------------------

# Create an empty list called "locationData" that will hold the location information
locationData = []

# Open up a connection to read in data from the locations text file
inFile = open("locations.txt", 'r')

# Read in the first line from the text file, which is the header line
inLine = inFile.readline()
# Read in the next line from the text file, which is the first line of data
inLine = inFile.readline()
# Begin a while loop using the not equal to assessment (!=) that will continue until
# a blank line of text is read in
while inLine != "":
    # Split the text line up based on tabs "\t"
    dataLine = inLine.split("\t")
    # Create a label called "name" that is equal to the name of the location
    name = (dataLine[0])
    # Create a label called "easting" that is an integer equal to the easting of the
    # location
    easting = int(dataLine[1])
    # Create a label called "northing" that is an integr equal to the northing of 
    # the location
    northing = int(dataLine[2])
    
    # Append to the locationData list another list the first index of which will be 
    # the name of the location and the second index will be a tuple of the easting
    # and northing integers.
    locationData.append([name, (easting, northing)])
    # Read in the next line from the text file
    inLine = inFile.readline()
    
# Close the connection to the locations text file
inFile.close()

# ----------------------------------------------------------------------------------
# STEP 3: CALCULATE DISTANCES TO ANOTHER LOCATION
# ----------------------------------------------------------------------------------

# Create a label called "toLocation" with a coordinate tuple to measure distance to
toLocation = (1656422, 5305326)  

# Create a new empty list called "distanceData" that will contain the results of the distance calculation
distanceData = list()

# For each location in the locationData list
for Location in locationData:
    # Create a label called "name" that is the name of the location
    name = Location[0]
    # Create a label called "coordinate" for the coordinate tuple of the location
    coordinate = Location[1]
    # Create a label called "distance" that is the distance to the location
    distance = calcDistance(toLocation, coordinate)
    # Append to the distance data list a new list that consists of: the name of the
    # location, the coordinate tuple of the location, and the distance of the
    # location to X
    distanceData.append([name, coordinate, distance])

# ----------------------------------------------------------------------------------
# STEP 4: WRITE OUT THE DISTANCE VALUES
# ----------------------------------------------------------------------------------

# Open up a connection to a new output text file
outFile = open("distanceResults.txt", 'w')
# Create a header line that is a string consisting of the column headings (name, 
# easting, northing, distance) each of which is separated by a tab ("\t") and 
# finsihes with a new line ("\n")
headerLine = "name" + "\t" + "easting" + "\t" + "northing" + "\t" + "distance" + "\n"
# Write out the header line to the text file
outFile.write(headerLine)
# For each location in the locationData list
for Location in distanceData:
    # Get the location name
    name = Location[0]
    # A string of the location easting
    easting = (Location[1][0])
    # A string of the location northing
    northing = (Location[1][1])
    # A string of the distance to X
    distance = (Location[2])
    # Create a string that consists of the name, easting, northing, and distance
    # each of which is separated by a tab and finshes with a new line
    outLine = name + "\t" + easting + "\t" + northing + "\t" + distance + "\n"
    # Write out the string to the text file
    outFile.write(outLine)
# Close the connection to the output text file
outFile.close()

# ----------------------------------------------------------------------------------
