#!/bin/bash

# bash_completion
sudo apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends bash-completion
printf "\n# bash_completion\n. /usr/share/bash-completion/bash_completion\n" >> ~/.bashrc

# poetry install
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.create false

# package install
cd selenium_example
poetry install
