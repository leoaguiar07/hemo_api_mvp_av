# Use a imagem base oficial do Python
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Upgrade PIP
RUN pip install --upgrade pip

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código-fonte para o diretório de trabalho
COPY . .

# Expõe a porta em que o servidor Django estará escutando
EXPOSE 8000

# Comando padrão para executar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
