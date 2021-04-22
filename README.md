# ena-processing-requests
Request execution of Galaxy SARS-CoV-2 variation analysis workflows on input data you provide.

To use, just follow these steps:
* Fork the repo and [create a new file](https://github.com/simonbray/ena-processing-requests/new/main/file_requests) in the `file_requests/` directory.
  * The file should contain a header line, followed by a list of web links to the files you want to analyze. See [the example file](https://github.com/simonbray/ena-processing-requests/blob/main/file_requests/example.txt) provided.
  * Links need to be formatted as follows: `<base_url><sample ID>_[12].<file_extension>` (1 representing the forward strand and 2 the reverse strand of paired-end data). If your data is not accessible in this way, or unpublished, it's not a problem - just [create an issue](https://github.com/simonbray/ena-processing-requests/issues/new) and describe what you need.
* Create a PR with your changes. We will review and merge it as soon as possible.
* After merging, the data will be uploaded to Galaxy and processed.

## Links
* [Documentation for the project](https://covid19.galaxyproject.org/genomics/global_platform/)
* [Scripts for our analysis bot](https://github.com/simonbray/ena-cog-uk-wfs/blob/main/docs/overview.md)
* [planemo](https://github.com/galaxyproject/planemo) and [bioblend](https://github.com/galaxyproject/bioblend) tools powering the automation of the analyses.
