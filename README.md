# SARS-CoV-2 processing requests

Request execution of Galaxy SARS-CoV-2 variation analysis workflows on input data you provide.

Prerequisites:

This automation system is set up to work with **ARTIC-amplified paired-end Illumina sequence data**, the most common type of SARS-CoV-2 sequencing data today.

To use, just follow these steps:
* Fork the repo and [create a new file](https://github.com/simonbray/ena-processing-requests/new/main/file_requests) in the `file_requests/` directory.
  * The file should contain a header line, followed by a list of web links to the files you want to analyze. See [the example file](https://github.com/simonbray/ena-processing-requests/blob/main/file_requests/example.txt) provided.
  * Links need to be formatted as follows: `<base_url>/<sample ID>_[12].<file_extension>` (1 representing the forward strand and 2 the reverse strand of paired-end data). If your data is not accessible in this way, or unpublished, it's not a problem - just [create an issue](https://github.com/simonbray/ena-processing-requests/issues/new) and describe what you need.
* Create a PR with your changes. We will review and merge it as soon as possible.

Analysis of your data:
* After merging, the data will be uploaded to [Galaxy Europe](https://usegalaxy.eu) and processed by our [collection of SARS-CoV-2 genomic sequence analysis workflows](https://github.com/galaxyproject/iwc/tree/main/workflows), which will produce highly-sensitive per-sample variant calls, per-batch variant reports and reliable consensus sequences for all your samples.
* Depending on the amount of other jobs running on our server and on the size of your data batch, processing may take between a few hours and a day.
* Once ready, the complete analysis will become available as a set of [published histories on the server](https://usegalaxy.eu/histories/list_published).

  Hint: Your histories will carry the filename from your pull request in their name.
* Key result files - BAM, VCF and consensus sequence FASTA files for each sample in your batch, will also be pushed automatically to a publicly readable [FTP server (ftp://xfer13.crg.eu/)](ftp://xfer13.crg.eu).
* With a delay of some days your results will also be included in the [viral Beacon project](https://covid19beacon.crg.eu) dashboard.

## Links
* [Documentation for the project](https://covid19.galaxyproject.org/genomics/global_platform/)
* [Scripts for our analysis bot](https://github.com/usegalaxy-eu/ena-cog-uk-wfs/blob/main/docs/overview.md)
* [planemo](https://github.com/galaxyproject/planemo) and [bioblend](https://github.com/galaxyproject/bioblend) tools powering the automation of the analyses.
