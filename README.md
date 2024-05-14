# Benchmarking inference of dynamical models

See related [GT Bioss workshop program](https://codimd.math.cnrs.fr/s/pR4cVqX7d)

This repository contains a first attempt to generate synthetic datasets from ground-truth dynamical models of cellular processes.

[Download the full repository](https://github.com/gt-bioss/benchmark-dynamical-models/archive/refs/heads/main.zip)

## Structure of the repository

- `from-boolean-networks`: datasets generated from Boolean networks
  - `{benchmark_name}/generation`: scripts used to generate the data
  - `{benchmark_name}/ground-truth`: Boolean network, influence graph, and Boolean trajectories used for data generation\
      Trajectories are stored in CSV format\
      Filenames are of the form `wt-boolean-trajectories.csv` for wild-type simulations and `MUTANT-boolean-trajectories.csv` for mutants (combinations of genes KO/UP).
  - `{benchmark_name}/traj`: synthetic scRNA-seq data for each Boolean trajectory\
      Datasets are given in four versions:
      - rawcounts and normalized
      - with and without dropouts
  - `{benchmark_name}/steady`: synthetic scRNA-seq data from steady states of each Boolean trajectory\
      (same versions as `traj`
  - `{benchmark_name}/timeseries`: timeseries of scRNA-seq data for each Boolean trajectory\
      File names are of the form `{MUTANT}-T{time}-{datatype}.csv`\
      Currently, we provide only data with dropouts and normalized pseudocounts.

## TODO
- [ ] links to other ressources containing such synthetic datasets
