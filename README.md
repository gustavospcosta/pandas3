<h1 align="center"> Python Pandas </h1>
<div dir="auto" align="center">
  <br>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg"><img align="center" alt="Gustavo-VSCode" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"><img align="center" alt="Gustavo-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg"><img align="center" alt="Gustavo-Pandas" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" style="max-width: 100%;"></a>
    <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg"><img align="center" alt="Gustavo-MySQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" style="max-width: 100%;"></a>
    <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/googlecloud/googlecloud-original.svg"><img align="center" alt="Gustavo-GCP" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/googlecloud/googlecloud-original.svg" style="max-width: 100%;"></a>
</br>
</div>

## Topics
* [Project Description](#project-description) :us:
* [Descrição do Projeto](#descrição-do-projeto) :brazil:
  
## Project Description
<p align="justify">
This project involves handling the New York City Airbnb open data available on Kaggle. The code performs several tasks, including downloading the dataset, authenticating with Google Cloud, uploading and downloading files to and from a specified Google Cloud Storage bucket, and preprocessing the data. NaN values within the dataset are replaced with specific values, and finally, the processed data is saved to a MySQL database.
</p>

## Code Description
<p align="justify">
The code is divided into functions, each responsible for a specific task. The `download_dataset` function downloads the Airbnb dataset from Kaggle, `authenticate_gcloud` authenticates with Google Cloud, and `select_bucket` selects a Google Cloud Storage bucket. Functions `b_upload` and `b_download` handle uploading and downloading files to and from Google Cloud Storage, respectively. The data preprocessing is handled by `read_and_preprocess_data`, and `replace_nan_values`, while `save_to_mysql` takes care of saving the processed data to a MySQL database. This separation of concerns into functions ensures maintainability and readability.
</p>

## Getting Started
<p align="justify">
To begin with this project, you'll need to have Python installed along with the required libraries such as pandas, google-cloud-storage, and SQLAlchemy. You will also need access to Google Cloud Storage and a MySQL database. Make sure to replace the placeholders in the code with your specific paths, credentials, and connection details. The dataset used is publicly available on Kaggle, and the link is provided within the code. Downloading the data might require Kaggle API authentication.
</p>

## Executing Program
<p align="justify"> 
To execute the program, simply run the script in your preferred Python environment. Make sure to have the necessary authentication files for Google Cloud and permissions to write to the MySQL database. Ensure that your paths for uploading and downloading files are set correctly in the code. Once executed, the program will download the dataset, process it, and save the processed data to the MySQL database. Log messages will provide feedback about the upload and download operations on Google Cloud Storage.
</p>

## Author
<p align="justify"> Gustavo de Souza Pessanha da Costa. 
</p>

## License
<p align="justify"> This project is licensed under the MIT license. 
</p>

:small_orange_diamond: :small_orange_diamond: :small_orange_diamond:

## Descrição do Projeto

<p align="justify">
Este projeto envolve o manuseio dos dados abertos do Airbnb de Nova York disponíveis no Kaggle. O código realiza várias tarefas, incluindo o download do conjunto de dados, autenticação com o Google Cloud, upload e download de arquivos de e para um bucket especificado no Google Cloud Storage, e pré-processamento dos dados. Valores NaN dentro do conjunto de dados são substituídos por valores específicos, e, finalmente, os dados processados são salvos em um banco de dados MySQL.
</p>

## Descrição do Código
<p align="justify">
O código é dividido em funções, cada uma responsável por uma tarefa específica. A função `download_dataset` faz o download do conjunto de dados do Airbnb do Kaggle, `authenticate_gcloud` autentica com o Google Cloud, e `select_bucket` seleciona um bucket do Google Cloud Storage. As funções `b_upload` e `b_download` lidam com o upload e download de arquivos para e do Google Cloud Storage, respectivamente. O pré-processamento dos dados é realizado pelas funções `read_and_preprocess_data` e `replace_nan_values`, enquanto `save_to_mysql` cuida de salvar os dados processados em um banco de dados MySQL. Essa separação de preocupações em funções garante manutenibilidade e legibilidade.
</p>

## Iniciando
<p align="justify">
Para começar com este projeto, você precisará ter o Python instalado juntamente com as bibliotecas necessárias, como pandas, google-cloud-storage e SQLAlchemy. Você também precisará ter acesso ao Google Cloud Storage e a um banco de dados MySQL. Certifique-se de substituir os espaços reservados no código pelos seus caminhos, credenciais e detalhes de conexão específicos. O conjunto de dados utilizado está disponível publicamente no Kaggle, e o link é fornecido dentro do código. Fazer o download dos dados pode exigir autenticação da API do Kaggle.
</p>

## Executando o Programa
<p align="justify"> 
Para executar o programa, basta executar o script em seu ambiente Python preferido. Certifique-se de ter os arquivos de autenticação necessários para o Google Cloud e permissões para escrever no banco de dados MySQL. Assegure-se de que seus caminhos para upload e download de arquivos estejam configurados corretamente no código. Uma vez executado, o programa fará o download do conjunto de dados, processará os dados e salvará os dados processados no banco de dados MySQL. Mensagens de log fornecerão feedback sobre as operações de upload e download no Google Cloud Storage.
</p>

## Autor
<p align="justify"> Gustavo de Souza Pessanha da Costa.
</p>

## Licença
<p align="justify"> Este projeto é licenciado sob a licença MIT.
</p>




