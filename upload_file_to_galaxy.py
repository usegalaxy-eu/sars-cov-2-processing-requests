"""
Takes a list of ftp links and converts to a yaml file ready for upload with planemo run

(Slightly modified version here compared to ena-cog-uk-wfs)
"""
import argparse

from bioblend import galaxy


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'links_file',
        help='File with links to upload'
    )
    parser.add_argument(
        'collection_name',
        help='The yml key to use for the collection element'
    )
    parser.add_argument(
        '-g', '--galaxy-url', required=True,
        help='URL of the Galaxy instance to run query against'
    )
    parser.add_argument(
        '-a', '--api-key', required=True,
        help='API key to use for authenticating on the Galaxy server'
    )
    parser.add_argument(
        '-i', '--history_id',
        help='History ID for uploading datasets'
    )
    args = parser.parse_args()

    gi = galaxy.GalaxyInstance(args.galaxy_url, args.api_key)
    dataset_id = gi.tools.upload_file(args.links_file, args.history_id)['outputs'][0]['id']
    collection_description = {'collection_type': 'list',
                              'element_identifiers': [{'id': dataset_id,
                                                       'name': 'File with FTP links',
                                                       'src': 'hda'}],
                              'name': args.collection_name}
    gi.histories.create_dataset_collection(args.history_id, collection_description)
