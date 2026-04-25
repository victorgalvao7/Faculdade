# Biblioteca para manípulação de tabelas
import pandas as pd

# Criando um Data Frame
dados = pd.read_csv(r"D:\Faculdade\Soluções em Energias Renováveis e Sustentáveis\aula01_com_python_e_data_set\Data_sample_Oragen.csv")A

#**Análise Exploratória**#
# Visualização dos primeiros registros
dados.head()
# Dimensões do data frame
dados.shape
print(f"A tabela possui {dados.shape[0]} registros (linhas) e {dados.shape[1]} atributos (colunas)")
# Informações básicas sobre os Dados
dados.info()
dados.columns()
# Estatísticas descritivas (colunas numéricas)
# Média, mediana, desvio padrão, min, max
dados.describe()
# Separação de colunas
dados["Voltage"]
# Média, mediana e desvio padrão ---> populacionais
dados["Voltage"].mean()
dados["Voltage"].median()
dados["Voltage"].std()
# Média, mediana e desvio padrão ---> amostrais
dados["Voltage"].sample(frac=0.05).mean()
dados["Voltage"].sample(frac=0.05).median()
dados["Voltage"].sample(frac=0.05).std()