from modules.memory.memory import load_memory, save_memory


memory = load_memory()

memory["developer"] = "Shankar"

save_memory(memory)

print(load_memory())