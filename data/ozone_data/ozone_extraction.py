import pandas as pd

# Substitua 'seu_arquivo.txt' pelo caminho real do seu arquivo de texto
caminho_arquivo = 'subset_OMTO3_003_20231116_135047_.txt'

# Ler o arquivo de texto sem cabeçalhos
data_frame = pd.read_csv(caminho_arquivo, header=None, delimiter='\t')  # Pode ajustar o delimitador conforme necessário

# Exibir o DataFrame
print(data_frame)

import requests

# Set the URL string to point to a specific data URL. Some generic examples are:
#   https://data.gesdisc.earthdata.nasa.gov/data/MERRA2/path/to/granule.nc4

URL = 'your_URL_string_goes_here'

# Set the FILENAME string to the data file name, the LABEL keyword value, or any customized name. 
FILENAME = 'your_file_string_goes_here'

import requests
result = requests.get(URL)
try:
    result.raise_for_status()
    f = open(FILENAME,'wb')
    f.write(result.content)
    f.close()
    print('contents of URL written to '+FILENAME)
except:
    print('requests.get() returned an error code '+str(result.status_code))