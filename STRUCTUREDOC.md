# Skyguard Pipeline Documentation
In this md, I go through each file and explain its function, as well as the order of operations when the pipe is run, and also general tips

## pipeline folder

#### pipeline/__main__.py

#### pipeline/env_sg.py

#### pipeline/env.py

#### pipeline/env.py.md

### pipeline/lib (folder)

#### pipeline/lib/icon

- The icon folder holds various images the pipe will use for icons.

#### pipeline/lib/sbs (normal2height.sbsar)

- Unsure for now, ask Scott.

#### pipeline/lib/sp_assets

- Various folder for alphas, effects, emitters, etc. Each have their own folder with a readme file. None of them seem to have much context except perhaps font. Ask Scott about how this is implemented. I assume the use is for substance painter.

#### pipeline/lib/splash
- Contains a folder that seems to be a custume image for the loading screen for Houdini, Used for love and dungeons. Replace this image with something Skygaurd related.

#### pipeline/lib/normal2height.sbs
- Substance binary source file. Obvously used for substance designer to store and share materials. Contains the editable graph of a material with nodes. Unsure Why it is here in this folder and how it is used. Ask Scott

### pipeline/pipe (folder)
- The pipefolder contains various folders representing pipe code that will be used. Ask Scott about why and how
1. db: Contains Database python files. The database is implemented using shockgrid
2. glui: empty init file, massive dialog file that appears to give useful messages? Explore the code Further and ask Scott. 
3. h: h is for houdini! Implements hipfiles and imports the hou library, which adds houdini functions. 
4. m: m is for maya! Obviously there are a lot of Maya files in here. 
5. sp: this folder contains many substance painter related files. 
6. struct: Contains 4 files: __init__.py, db.py, marerials.py, and util.py
7. __init__.py: an initializing file for the pipe folder. checks the dcc and appends the appropriate dcc to the __all__ list. 
8. textconverter.py: Not too sure about this, ask Scott. 
9. util.py: Not too sure about this either. Ask Scott. 

#### pipeline/pipe/db (folder)

##### pipeline/pipe/dbshotfun_api3

###### pipeline/pipe/db/dbshotfun_api3/axure-pipeline-templates/run-tests.yml

###### pipeline/pipe/db/dbshotfun_api3/docs/advanced/iron_python.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/advaced/packaging.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/ami_handler.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/ami_version_packager.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_create_shot_task_template.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_create_shot.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_create_version_link_shot.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_delete_shot.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_find_shot.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_sg_instance.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_update_shot.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/basic_update_thumbnail_version.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/examples/svn_integration.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/tasks/split_tasks.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/tasks/task_dependencies.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/tasks/updating_tasks.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/attachments.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/smart_cut_fields.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/tasks.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/tutorials.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook/usage_tips.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/images/

###### pipeline/pipe/db/dbshotfun_api3/docs/advanced.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/authentication.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/changelog.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/cookbook.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/indext.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/installation.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/reference.rst

###### pipeline/pipe/db/dbshotfun_api3/docs/shotgun_api3

###### pipeline/pipe/db/dbshotfun_api3/docs/tests

###### pipeline/pipe/db/dbshotfun_api3/docs

