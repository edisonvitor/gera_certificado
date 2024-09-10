import json
import os
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

template_path = "template.png"
font_path = "fonts/OpenSans-Bold.ttf"
font_size = 42
output_folder = "certificados"
font = ImageFont.truetype(font_path, font_size)

os.makedirs(output_folder, exist_ok=True)

with open("alunos.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
pbar = tqdm(total=len(data["alunos"]), desc="Gerando certificados", unit="certificado")

for aluno in data["alunos"]:
    nome_aluno = aluno["nome"]
    graduacao = aluno["corda"]
    genero = aluno["genero"]

    texto = (
        f"A Associação de Capoeira Guerreiros de Zumbi confere "
        f"{'ao aluno' if genero == 'Masculino' else 'à aluna'} "
        f"{'\n' if len(nome_aluno) > 20 else ' '}{nome_aluno}"
        f"{' ' if len(nome_aluno) > 20 else '\n'}"
        f"o presente certificado em reconhecimento à sua"
        f"{'\n' if len(nome_aluno) > 20 else ' '}dedicação e compromisso com"
        f"{'\n' if len(nome_aluno) <= 20 else ' '}a arte da Capoeira, "
        f"{'graduando-o' if genero == 'Masculino' else 'graduando-a'} com a corda"
        f"{'\n' if len(nome_aluno) > 20 else ' '}{graduacao}.\n"
        "\n"
        "Este certificado atesta o progresso contínuo e a superação dos desafios \nenfrentados durante o aprendizado, "
        "refletindo o espírito e a tradição da Capoeira."
    )

    template = Image.open(template_path)

    texto_position = (120, 520)

    draw = ImageDraw.Draw(template)
    draw.text(texto_position, texto, font=font, fill="black")

    output_pdf_path = os.path.join(output_folder, f"certificado_{nome_aluno.replace(' ', '_').lower()}.pdf")
    template.convert('RGB').save(output_pdf_path, "PDF", resolution=100.0)

    pbar.update(1)

pbar.close()

print("Todos os certificados foram gerados com sucesso!")
input("Pressione Enter para sair...")