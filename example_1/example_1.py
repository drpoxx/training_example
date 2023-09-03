# =======================
#   Import Packages
# =======================

import pathlib
from module_1 import guemlinas_greetings, guemlinas_recipe

if __name__ == "__main__":
    # The Basics
    print("Hello!")
    print(guemlinas_greetings())
    print(guemlinas_recipe())
  
    top_secret_recipe = guemlinas_recipe(recipe="pasta", ingredient="octapodi")
    print("\nStrictly Confidential: ")
    print(top_secret_recipe)
    print("")

    file_path = pathlib.Path.cwd()
    print(file_path.joinpath("data", "FILENAME.CSV"))