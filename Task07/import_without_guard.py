"""Shows what happens WITHOUT `if __name__ == "__main__":` - the table prints on import."""
print("importing milkrate_noguard ...")
import milkrate_noguard
print("done importing - the rows above were printed by the module itself, which is unwanted.")
