import os.path
from flask import Flask, request, jsonify, send_file, render_template
from iiif2 import IIIF, web

# This is the path to build caches, etc
PATH = os.path.dirname(os.path.realpath(__file__))
# init flask based on this file
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    """ This is a test page so you can see that it's working it displays using open seadragon"""
    return render_template('home.html') 

@app.route('/<identifier>/info.json')
def info(identifier):
    """get info about the image and return a json blob. Need to drop URL root in"""
    return jsonify(web.info("%s%s"%(request.url_root, identifier), resolve(identifier)))

@app.route('/<identifier>/<region>/<size>/<rotation>/<quality>.<fmt>')
def iiif(**kwargs):
    """ Return a cached tile or a real tile"""
    cache_id = web.urihash(request.url)
    cached_tile = os.path.join(PATH, 'cache', '%s' %cache_id) 
    params = web.Parse.params(**kwargs)
    path = resolve(params.get('identifier'))
    if os.path.isfile(cached_tile):
        print "returning cached image"
        return send_file(open(cached_tile), mimetype="image/jpeg")
    
    else: 
        with IIIF.render(path, **params) as tile:
            print cache_id 
            tile.save(cached_tile)
            return send_file(tile, mimetype=tile.mime)

def resolve(identifier):
    """Resolves a iiif identifier to the resource's path on disk.
    This method is specific to this server's architecture and can be configured
    """
    return os.path.join(PATH, 'images', '%s.tif' % identifier)

if __name__ == "__main__":
    app.run(debug=True)
