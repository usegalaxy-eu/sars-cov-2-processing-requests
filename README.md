# SARS-CoV-2 processing requests

Request execution of Galaxy SARS-CoV-2 variation analysis workflows on input data you provide.


## Prerequisites

This automation system is set up to work with **ARTIC-amplified paired-end Illumina sequence data**, the most common type of SARS-CoV-2 sequencing data today.

## Usage

* Fork the repo and [create a new file](https://github.com/simonbray/ena-processing-requests/new/main/file_requests) in the `file_requests/` directory.
  * The file should contain a header line, followed by a list of web links to the files you want to analyze. See [the example file](https://github.com/simonbray/ena-processing-requests/blob/main/file_requests/example.txt) provided.
  * Links need to be formatted as follows: `<base_url>/<sample ID>_[12].<file_extension>` (1 representing the forward strand and 2 the reverse strand of paired-end data). If your data is not accessible in this way, or unpublished, it's not a problem - just [create an issue](https://github.com/simonbray/ena-processing-requests/issues/new) and describe what you need.
* Create a PR with your changes. We will review and merge it as soon as possible.

## Analysis of your data

* After merging, the data will be uploaded to [Galaxy Europe](https://usegalaxy.eu) and processed by our [collection of SARS-CoV-2 genomic sequence analysis workflows](https://github.com/galaxyproject/iwc/tree/main/workflows), which will produce highly-sensitive per-sample variant calls, per-batch variant reports and reliable consensus sequences for all your samples.
* Depending on the amount of other jobs running on our server and on the size of your data batch, processing may take between a few hours and a day.
* Once ready, the complete analysis will become available as a set of [published histories on the server](https://usegalaxy.eu/histories/list_published).
  
  💡 Hint: Your histories will carry the filename from your pull request in their name.
* Key result files - BAM, VCF and consensus sequence FASTA files for each sample in your batch - will also be pushed automatically to a publicly readable [FTP server](ftp://xfer13.crg.eu) hosted by [BSC](https://www.bsc.es).
* After a few days your results will also be included in the [viral Beacon project](https://covid19beacon.crg.eu) dashboard.

## Links

* [Documentation for the project](https://covid19.galaxyproject.org/genomics/global_platform/)
* [Scripts for our analysis bot](https://github.com/usegalaxy-eu/ena-cog-uk-wfs/blob/main/docs/overview.md)
* [planemo](https://github.com/galaxyproject/planemo) and [bioblend](https://github.com/galaxyproject/bioblend) tools powering the automation of the analyses.


----------

The analyses will be performed using the [Galaxy](http://galaxyproject.org) platform and open source tools from [BioConda](https://bioconda.github.io) and [BioContainers](https://biocontainers.pro). The workflows will run on the [de.NBI-cloud](https://www.denbi.de) and form part of the Galaxy COVID-19 efforts with
partners around the world. For more information please visit [https://github.com/galaxyproject/SARS-CoV-2](https://github.com/galaxyproject/SARS-CoV-2).

<!--
, [XSEDE](https://www.xsede.org/) resources maintained by the Texas Advanced Computing Center ([TACC](https://www.tacc.utexas.edu/)),
Pittsburgh Supercomputing Center ([PSC](https://www.psc.edu/)), and [Indiana University](https://jetstream-cloud.org/) in the U.S., 
[VSC](https://www.vscentrum.be) cloud resources and [IFB](https://www.france-bioinformatique.fr/en/cluster) cluster resources on the European side, 
[STFC-IRIS](https://stfc.ukri.org/) at the Diamond Light Source, and [ARDC](https://ardc.edu.au) cloud resources in Australia.
-->

<p align="center">
  <a href="https://galaxyproject.org">   <img src="./img/galaxy_logo.png" width= "22%" alt="Galaxy Project" /></a> &nbsp;
  <a href="https://galaxyproject.eu">    <img src="https://raw.githubusercontent.com/usegalaxy-eu/branding/master/galaxy-eu/galaxy-eu.256.png" width= "20%" alt="European Galaxy Project" /></a> &nbsp;
  <a href="https://usegalaxy-au.github.io/">    <img src="./img/galaxy_australia.png" width="20%" alt="Australian Galaxy Project" /></a> &nbsp;
  <a href="https://bioconda.org">        <img src="./img/bioconda_logo.png" width="20%" alt="bioconda" /></a> &nbsp;
  <a href="https://xsede.org">           <img src="./img/xsede_logo.png" width="20%" alt="XSEDE" /></a> &nbsp;
  <a href="https://www.tacc.utexas.edu"> <img src="./img/tacc_logo.png" width="20%" alt="TACC" /></a> &nbsp;
  <a href="https://www.denbi.de">        <img src="./img/denbi-logo-color.svg" width="20%" alt="de.NBI" /></a> &nbsp;
  <a href="https://elixir-europe.org">   <img src="./img/elixir_logo.png" width="15%" alt="ELIXIR" /></a> &nbsp;
  <a href="https://www.psc.edu">         <img src="./img/psc_logo.jpg" width="20%" alt="PSC" /></a> &nbsp;
  <a href="https://www.iu.edu">          <img src="./img/iu_logo.jpg" width="20%" alt="Indiana University" /></a> &nbsp;
  <a href="https://training.galaxyproject.org"> <img src="./img/gtn_logo.png" width="20%" alt="Galaxy Training Network" /></a> &nbsp;
  <a href="https://bioplatforms.com">    <img src="./img/bpa_logo.png" width="20%" alt="Bio Platforms Australia" /></a> &nbsp;
  <a href="https://ardc.ed.au">          <img src="./img/ardc_logo.png" width="20%" alt="Australian Research Data Commons" /></a> &nbsp;
  <a href="http://www.vib.be/">          <img src="./img/vib_tagline_pos_rgb.png" width="15%" alt="VIB" /></a> &nbsp;
  <a href="https://www.elixir-belgium.org">          <img src="./img/ELIXIR_BELGIUM_white_background.png" width="15%" alt="ELIXIR Belgium" /></a> &nbsp;
  <a href="https://www.vscentrum.be">          <img src="./img/VSC-logo.png" width="25%" alt="Vlaams Supercomputer Center" /></a> &nbsp;
  <a href="https://www.eosc-life.eu">          <img src="./img/eosclife.png" width="10%" alt="EOSC-Life" /></a> &nbsp;
  <a href="https://datamonkey.org">          <img src="./img/datamonkey.svg" alt="Datamonkey" width = "150px" /></a> &nbsp;
  <a href="https://www.france-bioinformatique.fr/en">          <img src="./img/ifb.png" alt="IFB" width = "20%" /></a> &nbsp;
  <a href="https://www.crg.eu">          <img src="./img/crg.png" alt="CRG" width = "15%" /></a> &nbsp;
  <a href="https://www.bsc.es/">          <img src="./img/bsc.png" alt="BSC" width = "10%" /></a> &nbsp;

  <!--a href="http://galaxyp.org/">          <img src="./img/galaxyp.png" alt="GalaxyP" width = "10%" /></a> &nbsp;-->
</p>
