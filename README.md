# kioptipack-schema

Documentation of the ontology and metamodels for the KIOptipack project

## Website

[https://lcomet.github.io/docskioptiapck/](https://lcomet.github.io/docskioptiapck/)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [kioptipack_schema](src/kioptipack_schema)
    * [schema](src/kioptipack_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/kioptipack_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
