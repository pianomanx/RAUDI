import helper

def get_config(organization, common_args):
    api_results = {
        'THEHARVESTER_GITHUB_INFO': helper.get_latest_github_release_no_browser_download('laramies/theHarvester'),
    }
    
    config = {
        'name': organization+'/restfulharvest',
        'version': helper.clean_version(api_results['THEHARVESTER_GITHUB_INFO']['version']),
        'buildargs': {
            'PYTHON3_SLIM_VERSION': common_args['PYTHON3_SLIM_VERSION'],
            'THEHARVESTER_DOWNLOAD_URL': api_results['THEHARVESTER_GITHUB_INFO']['url']
        },
        'tests': ['-h']
    }
    return config