tamanhoArquivo = float(input("Informe o tamanho do arquivo em questão em Mb: "))
velocidadeDownload = float(input("Informe a velocidade de download do site em questão em Mb/s: "))
tempoEstimado = tamanhoArquivo / (velocidadeDownload / 8)
print(f"O tempo estimado para o download deste arquivo é: {tempoEstimado:.1f} segundos")