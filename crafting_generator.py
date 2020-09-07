# -*- coding: utf-8 -*-

# Feel free to use for your own projects!
# Please credit Berke Filiz or link this Github repository :)

import json
import glob
import os

# HELPERS #####################################################################
# Used in "generation" section

# Turn 0/1 into crafting_shapeless/crafting_shaped; return a string
def shapeText(i):
    if int(i) == 1:
        return "crafting_shaped"
    return "crafting_shapeless"

# Create the pattern instructions (SHAPED)
def createKeys(items):
    keyList = {}
    for i in range(len(items)):
        keyList[str(i)] = {
            "item": f"minecraft:{items[i]}"
        }
    return keyList

# Create the pattern instructions (SHAPELESS)
def createIngredients(items):
    keyList = []
    for item in items:
        itemDict = dict({
            "item": f"minecraft:{item}"
        })
        keyList.append(itemDict)
    return keyList

# Turn the string pattern into the crafting pattern
def extractPattern(pattern):
    # Turn X to space
    def eliminateX(char):
        if char.upper() == "X":
            return " "
        return char
    
    # Turn to the format ["###", "###", "###"]
    # Eliminate any "X" and replace with " "
    noSpacePattern = [eliminateX(c) for c in pattern]
    stringPattern = "".join(noSpacePattern)
    fixedPattern = [stringPattern[0:3], stringPattern[3:6], stringPattern[6:9]]
    return fixedPattern

# Format the result
def createResult(item, amount):
    resultDict = {
        "item": f"minecraft:{item}",
        "count": int(amount)
    }
    return resultDict

# Create a suitable JSON name for the crafting recipe
# Format as follows: [first ingredient]to[resulting item][index].json
# Index is a non-negative integer that increases if there is already a json
#   file of that name. For instance, if itemtoitem0.json already exists,
#   the new name will be itemtoitem1.json
def makeJSONName(instruction):
    instructionList = instruction.split(" ")
    item_result = instructionList[-2]
    item_lead   = instructionList[int(instructionList[0]) + 1]
    
    index = 0
    json_name = f"{item_lead}to{item_result}"
    existingFiles = [f[7:] for f in glob.glob("Output/*.json")]
    
    while f"{json_name}{index}.json" in existingFiles:
        index += 1
        
    return f"Output/{json_name}{index}.json"

# GENERATION ##################################################################
# Creation of relevant dictionaries

# Create the contents of the json file for a shapeless crafting recipe
def generateShapeless(instruction):
    
    # Separate the command
    recipe = instruction.split()
    cr_type    = recipe[0]        # Shapeless (0) or shaped (1)
    cr_items   = recipe[1:-2]     # The ingredients
    cr_result  = recipe[-2]       # The result of the recipe
    cr_count   = recipe[-1]       # Amount of cr_result
    
    # Generate the JSON
    output = {
        "type": shapeText(cr_type),
        "ingredients": createIngredients(cr_items),
        "result": createResult(cr_result, cr_count)
    }
    
    # Complete, return dictionary
    return output

# Create the contents of the json file for a shaped crafting recipe
def generateShaped(instruction):

    # Separate the command
    recipe = instruction.split()
    cr_type    = recipe[0]        # Shapeless (0) or shaped (1)
    cr_pattern = recipe[1]        # The crafting pattern
    cr_items   = recipe[2:-2]     # The ingredients
    cr_result  = recipe[-2]       # The result of the recipe
    cr_count   = recipe[-1]       # Amount of cr_result
    
    # Generate the JSON
    output = {
        "type": shapeText(cr_type),
        "pattern": extractPattern(cr_pattern),
        "key": createKeys(cr_items),
        "result": createResult(cr_result, cr_count)
    }
    
    # Complete, return dictionary
    return output

# AUTOMATIZATON ###############################################################
# Command line for automatization

# Export the dictionary as a JSON file
def makeJSON(generatedDict, instruction):
    filename = makeJSONName(instruction)
    with open(filename, "w") as outputfile:  
        json.dump(generatedDict, outputfile)
    outputfile.close()

# Run all of the code. As follows:
# 1. Import the instruction list from recipes.txt
# 2. Create a dictionary of relevant information
# 3. Export as separate JSON files in the Outpot folder.
def datapack():
    
    # Check if the folder Output exists. If not, create
    if not os.path.exists("Output"):
        os.makedirs("Output")
    
    inputFile = open('recipes.txt', 'r')
    for line in inputFile:
        instruction = line.strip() # Get rid of \n
        if instruction[0] == "0":
            makeJSON(generateShapeless(instruction), instruction)
        elif instruction[0] == "1":
            makeJSON(generateShaped(instruction), instruction)
        else:
            print("Invalid entry")
    inputFile.close()








