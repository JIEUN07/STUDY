import json
with open('config.json') as f:
    config = json.load(f)
    print('Theme: {}'.format(config['theme']))
    print('Size: {}'.format(config['size']))
    print('splash screen : {}'.format(config['splashscreen']))

# Theme: bluespring
# Size: small
# splash screen : false