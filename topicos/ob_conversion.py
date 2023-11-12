import os
import subprocess

def convert_sdf_to_mol(input_file_path, output_file_path):
  """Converte um arquivo SDF para o formato MOL.

  Args:
    input_file_path: O caminho do arquivo SDF de entrada.
    output_file_path: O caminho do arquivo MOL de saída.
  """

  # Cria um comando para converter o arquivo SDF para o formato MOL.
  command = ["obabel", input_file_path, "-O", output_file_path]

  # Inicia o processo de conversão.
  subprocess.run(command)

def main():
  # Pasta de entrada.
  input_dir = "SDF"

  # Pasta de saída.
  output_dir = "MOL"

  # Converte os arquivos SDF.
  for input_file_path in os.listdir(input_dir ):
    filename = os.path.basename(input_file_path).replace('.sdf', '')
    input_file_path = os.path.join(input_dir, os.path.basename(input_file_path))
    output_file_path = os.path.join(output_dir, filename + ".mol2")
    convert_sdf_to_mol(input_file_path, output_file_path)



if __name__ == "__main__":
  main()
