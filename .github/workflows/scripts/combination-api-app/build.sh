#!/bin/bash

main() {
  LAMBDA_ARTIFACT_NAME=$1

  cd combination-api-app/source || exit

  echo "Creating a directory for artifact."
  mkdir target

  echo "Creating a package with dependencies."
  (
    cd venv/lib/python3.9/site-packages/ || exit
    zip -q -r ../../../../target/"${LAMBDA_ARTIFACT_NAME}" .
  )

  echo "Adding source code to the package."
  (
    cd api_composer || exit
    zip -q -g ../target/"${LAMBDA_ARTIFACT_NAME}" composer.py service.py constants.py
  )

  echo "Created artifact."
  ls -l target/"${LAMBDA_ARTIFACT_NAME}"
}

main "$@"; exit
