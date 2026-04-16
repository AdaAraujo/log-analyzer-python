🔍 Analisador de Logs em Python

Projeto desenvolvido para análise de logs de autenticação, com foco na identificação de atividades suspeitas, como múltiplas tentativas de login e possíveis ataques de força bruta.

🚀 Funcionalidades
Leitura de logs de autenticação
Identificação de falhas repetidas de login
Detecção de possíveis ataques (brute force)
Exibição dos IPs com mais falhas
Geração de gráfico para visualização
Salvamento dos resultados em arquivo .txt
💻 Como executar

pip install -r requirements.txt
python analyzer.py

📁 Estrutura do Projeto
analyzer.py → script principal
sample_log.txt → arquivo de exemplo
results.txt → saída gerada
examples/ → exemplos e gráfico
📊 Exemplo de saída

[ALERTA] 192.168.0.1 teve 3 falhas
[ALERTA] 192.168.0.3 teve 4 falhas

📸 Visualização

<p align="center">
  <img src="examples/graphic.png" width="500"/>
</p>


🧠 Conceitos Aplicados
Manipulação de dados em Python
Análise de logs
Detecção de padrões (força bruta)
Visualização com matplotlib
Uso de pandas

⚠️ Observação
Projeto desenvolvido para fins educacionais.