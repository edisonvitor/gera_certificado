import os
from pypdf import PdfMerger
from tqdm import tqdm

# Definindo o caminho da pasta com os certificados e o nome do PDF final
certificados_folder = "certificados"
output_pdf = "todos_certificados.pdf"

# Criando uma instância do PdfMerger
merger = PdfMerger()

# Pegando todos os arquivos PDF da pasta
pdf_files = [f for f in os.listdir(certificados_folder) if f.endswith(".pdf")]

# Ordenando os arquivos para garantir que eles sejam combinados na ordem correta
pdf_files.sort()

pbar = tqdm(total=len(pdf_files), desc="Combinando certificados", unit="certificado")

# Adicionando cada arquivo PDF ao PdfMerger
for pdf_file in pdf_files:
    pdf_path = os.path.join(certificados_folder, pdf_file)
    merger.append(pdf_path)
    
    pbar.update(1)


# Salvando o PDF final com todos os certificados
with open(output_pdf, "wb") as output_file:
    merger.write(output_file)

merger.close()

pbar.close()
print(f"Todos os certificados foram combinados em {output_pdf}")
