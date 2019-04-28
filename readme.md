This is a simple python eve project that provides an API for the 5th edition SRD for Dungeons and Dragons. It includes a modified verision of eve-docs to provide information on the API endpoints

It does not include the mongodb databases with the actual SRD information, those are in https://github.com/Cschlaefli/5e-db

It relys on a mongodb instance running on the default port on the same machine, which you can change in the settings.py. If you want the database populated, clone the 5e-db repository and run mongorestore.

