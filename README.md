# mc-crafting-datapack-generator
An automatized way of creating crafting datapacks for Minecraft


## What does this script do?
It takes a text file (recipes.txt) which is formatted in a specific way, and automatically generates separate datapacks for every item listed. This script only works for "shaped" and "shapeless" crafting recipes which do NOT include any "tag" elements such as planks. See "how to use" for detailed instructions.


## How to use

### recipes.txt
This file contains information about the datapack elements. Every line is a separate crafting recipe. The formation of lines must follow a specific syntax:
- The lines start with a 0 or 1, for shapeless and shaped crafting recipes respectively.
  - If it is a shaped recipe (1), the crafting pattern must follow:
    - It must be a 9-digit key for all slots on a crafting table; left to right, top to bottom.
    - Keys must be numbers, starting from 0: 0, 1, 2, 3...
    - For empty slots, there must be a lowercase/uppercase letter X.
    - For instance "0X00000X0" is a letter H in the crafting grid.
    - See the examples for more information.
- Then the ingredients must follow. Use Minecraft name IDs without the "minecraft:" prefix.
  - If it is a shapeless recipe (0), all elements can be listed in order.
    - The recipe for flint and steel can be written as "iron_ingot flint"
    - The recipe for gold nuggets can be written as "gold_ingot"
  - If it is a shaped recipe (1), all keys must be followed by a value respective of the amount of different numbers in the crafting pattern.
    - For instance, TNT crafting pattern is "010101010" for this script. The pattern consists of 0 and 1, so the following elements must be in increasing order: 0 is gunpowder and 1 is sand. So: "gunpowder sand"
    - Do not specify any item for empty slots, namely "X"
- Second-to-last element must be the resulting item.
  - For instance, if the crafting recipe is for diamonds, simply put "diamond"
- Last element must be the amount of the resulting item.
  - For instance, if the crafting recipe results in 2 diamonds, simply put 2.
  
#### Examples for "crafting instructions"
1 00X01XX1X cobblestone stick stone_axe 1
- 1: Shaped crafting
- 00X01XX1X: The pattern in the shape of axe crafting recipe
- cobblestone stick: Ingredients
  - 0 -> cobblestone
  - 1 -> stick
- stone_axe: The recipe is for stone axe
- 1: The recipe gives 1 stone axe

0 iron_ingot iron_nugget 9
- 0: Shapeless crafting
- iron_ingot: The ingredient
- iron_nugget: The recipe is for iron nuggets
- 9: The recipe gives 9 iron nuggets

0 white_dye gravel gravel gravel gravel sand sand sand sand white_concrete_powder 8
- 0: Shapeless crafting
- gravel ... sand: The ingredients
- white_concrete_powder: The recipe is for white concrete powder
- 8: The recipe gives 8 white concrete powder

#### Example recipes.txt
You can simply put every recipe into new lines:
```
1 00X01XX1X cobblestone stick stone_axe 1
0 iron_ingot iron_nugget 9
0 white_dye gravel gravel gravel gravel sand sand sand sand white_concrete_powder 8
```


### The script
This script works on Python and dependent on 3 libraries: **json** for converting Python dictionary into a JSON text, **os** for managing directories, and **glob** for reading the output file directory. Once it is all set up, **make sure that recipes.txt is in the same directory with crafting_generator.py!**

Call **datapack()** to read recipes.txt and generate the datapacks. All separate JSON files will be exported in a folder named Output in the same directory. (If such directory does not exist, the function will create it.

### Setting up the datapack
For a datapack to work, the folders need to be in a specific hierarchy. Below is a sample file directory, which you can find in this repository.
```
 datapackname (folder)
   pack.mcmeta (see below for explanation)
   data (folder)
     crafting (folder)
       recipes (folder)
         datapackname.json
         datapackname.json
         datapackname.json
```
Then, you will need to put the datapack inside your world's datapack folder:
- Open "Roaming" directory. (For Windows: Win+R, then type %appdata%)
- Go to .minecraft
- Go to saves
- Select a world
- Go to datapack
- Copy and paste your datapack folder in this directory.
- Update your datapacks
  - If the world is already on, type "/reload" or restart the world.
  - If the world is not on, no further action required.
- You can check if the datapack is enabled by typing "/datapack list enabled" in chat.

#### Information about pack.mcmeta
This is a file that holds meta information of your datapack: e.g. its name and description. You can find a sample mcmeta document in this repository.

## Credits
I hope you find this tool useful. Thanks to Animagician for the idea!

All code is written by me, Berke Filiz.

Feel free to use the script, as long as you credit to this Github repository.
