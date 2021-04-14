import os
from staticjinja import Site


c_versions = os.listdir("docs/c/")


if __name__ == "__main__":
    site = Site.make_site(env_globals={
        'c_versions': c_versions,
    })
    site.render()