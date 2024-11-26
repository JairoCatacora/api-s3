echo "Despliegue en dev"
sls deploy --stage dev

echo "Despliegue en test"
sls deploy --stage test

echo "Despliegue en prod"
sls deploy --stage prod

