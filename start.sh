echo "******************************************************"
echo "Starting udf-run :                                    ";
echo "******************************************************"

#!/bin/bash
app="udf-run"
docker build -t ${app} .
docker run -d -p 7076:80 \
  --name=${app} \
  -v $PWD:/app ${app}
