# This code is a part of MagicCap which is a MPL-2.0 licensed project.
# Copyright (C) Jake Gealer <jake@gealer.email> 2018.

from flask import Flask
from pluginbase import PluginBase
from flask_cors import CORS
# Imports go here.

app = Flask(__name__)
# Defines the app.

CORS(app)
# Allows CORS.

plugin_base = PluginBase(package="main.plugins")
plugin_source = plugin_base.make_plugin_source(
    searchpath=["./plugins"]
)
for plugin in plugin_source.list_plugins():
    loaded = plugin_source.load_plugin(plugin)
    loaded.setup(app)
# Loads all of the plugins.

if __name__ == "__main__":
    app.run(port=7575, debug=True)
# Starts the app if this isn't a Lambda instance.
