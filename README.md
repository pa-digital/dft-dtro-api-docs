# D-TRO Service API Documentation

This repository contains technical documentation for the D-TRO service. It consists of three sources of documentation:

* **Technical API documentation**, providing a quickstart guide on interfacing with the D-TRO API, as well as Swagger documentation on API usage
* The **Data Model User Guide**, which provides an in-depth look at the D-TRO data model
* The **User Portal Documentation**, which explains how to get started with creating an account and applications to interact with the D-TRO service

The documentation itself is served here: https://d-tro.dft.gov.uk/

This repository also contains the `dft-theme` Sphinx theme, and a landing page that directs users to the necessary documentation.

## Local Development

Developing locally can be achieved with Docker. The `docker-compose.yml` file allows you to run the documentation. The Dockerfile will create containers with `sphinx-autobuild` installed, along with the `dft-theme` and other required packages. `api_documentation` will expose port 8001, `data_model_user_guide` will expose port 8002 and `user_portal_documentation` will expose port 8003.

The containers are set to do nothing when run; this is by design, and allows ytou to exec into them and run whatever you need, e.g. `sphinx-autobuild` for live editing of the documentation, `make html` to build the documentation, etc.

If any changes are made to the underlying `dft-theme`, you will need to rebuild the Docker containers for these changes to take effect.

Steps for running the documentation locally using Docker:

**1. Open the folder with the code repository**

**2. Open a terminal and run `docker compose build`**

**3. Run command `docker compose up`**

**4. Open another terminal and run command `docker ps`**

**5. Depending on what you want to run, copy that docker id. The below table is to be used an example, as your ids might differ than these**

### Docker Containers Table

| CONTAINER ID | IMAGE                                       | COMMAND             | CREATED       | STATUS       | PORTS                                       | NAMES                                         |
|--------------|---------------------------------------------|---------------------|---------------|--------------|---------------------------------------------|-----------------------------------------------|
| fb2770ee2a88 | dft-dtro-api-docs-api-documentation         | "tail -f /dev/null" | 8 minutes ago | Up 8 minutes | 0.0.0.0:8001->8001/tcp, [::]:8001->8001/tcp | dft-dtro-api-docs-api-documentation-1         |
| 90ea783e393d | dft-dtro-api-docs-user-portal-documentation | "tail -f /dev/null" | 8 minutes ago | Up 8 minutes | 0.0.0.0:8003->8003/tcp, [::]:8003->8003/tcp | dft-dtro-api-docs-user-portal-documentation-1 |
| 314d1648f86f | dft-dtro-api-docs-landing                   | "tail -f /dev/null" | 8 minutes ago | Up 8 minutes | 0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp | dft-dtro-api-docs-landing-1                   |
| 1d22c7cfefca | dft-dtro-api-docs-data-model-user-guide     | "tail -f /dev/null" | 8 minutes ago | Up 8 minutes | 0.0.0.0:8002->8002/tcp, [::]:8002->8002/tcp | dft-dtro-api-docs-data-model-user-guide-1     |

**6. Run command `docker exec -it [CONTAINER ID]¹ bash`**

**7. Inside container run command `sphinx-autobuild -E -a source/ build/html/ --port [PORT NO]¹ --host 0.0.0.0`**

**8. Open e.g. `http://127.0.0.1:8002/`**

¹ Make sure the port number matches the container id.

## Making changes to the data model user guide

1. Make changes to `.rst` and images files in folder `data-model-user-guide\source`.
2. If you have to insert another figure, be aware that references to labels such as the following will auto-increment (so you don't need to increment any numbers in the labels themselves - the labels just need to be unique):
```
:numref:`fig8`
.. _fig8:
```
3. Once you've finished making changes, run the following:
```
./scripts/build.sh
```
See more on this script below.

4. View the changes locally at e.g. `http://127.0.0.1:8002/`.
5. Commit and push your changes - they will automatically be published to https://d-tro.dft.gov.uk/ via the job at https://github.com/pa-digital/dft-dtro-api-docs/actions

## Documentation Building

The helper script `scripts/build.sh` is provided to automate the build process. Note that the Docker containers need to be running for this script to work. This script does the following:

* deletes existing build files
* execs into each Docker container and runs `make html` to generate the build files (in the `api_documentation` project it will also run redoc to generate the interactive API documentation)
* copies the outputs to the `docs` folder

## Documentation Serving

The documentation is served through GitHub Pages, which serves the content of the `docs` folder. Currently this is served form the `main` branch, meaning source and build files exist together. At a future point the build files will be on a separate branch, and GitHub pages will serve the content of this branch, allowing the source and build files to be separated. Github Actions will then build the files from the `main` branch, and commit them to this other branch.