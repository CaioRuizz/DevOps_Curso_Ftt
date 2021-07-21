export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://54.91.12.208:2376"
export DOCKER_CERT_PATH="/home/ubuntu/.docker/machine/machines/cursodevops"
export DOCKER_MACHINE_NAME="cursodevops"

./ci/setup.sh
if ./ci/test.sh; then
    ./ci/build.sh
    ./ci/deploy.sh
fi