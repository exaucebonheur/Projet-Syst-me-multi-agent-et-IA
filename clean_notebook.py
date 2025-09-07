import nbformat
from nbformat import v4

# Nom du notebook à nettoyer
notebook_filename = "Sma_avecLLM.ipynb"

# Charger le notebook
nb = nbformat.read(notebook_filename, as_version=4)

for cell in nb.cells:
    # 1️⃣ Supprimer les secrets : on ne stocke plus de token dans les cellules
    if cell.cell_type == 'code':
        if 'HUGGINGFACEHUB_API_TOKEN' in cell.source:
            lines = cell.source.splitlines()
            # On garde seulement les lignes sans token
            clean_lines = [line for line in lines if 'HUGGINGFACEHUB_API_TOKEN' not in line]
            cell.source = "\n".join(clean_lines)
    
    # 2️⃣ Supprimer les outputs volumineux
    cell.outputs = []

    # 3️⃣ Ajouter la clé 'state' aux widgets si manquante
    if 'metadata' in cell and 'widgets' in cell.metadata:
        if 'state' not in cell.metadata['widgets']:
            cell.metadata['widgets']['state'] = {}

# Sauvegarder le notebook nettoyé
nbformat.write(nb, notebook_filename)
print("Notebook nettoyé avec succès !")
