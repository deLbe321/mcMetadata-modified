# Modified carrotwaxr's mcMetadata plugin

This repository holds modified version of mcMetadata by carrotwaxr for extending the functionality of [Stash](https://github.com/stashapp/stash) adult media manager.

Modification made to increase compability and interobility between mcMetadata, nfSceneParser (other stash plugin) Jellyfin.Plugin.Stash.

I didn't create pull request to the original repository and created fork instead because some modifications felt arbitrary, tailored to my specific needs and could break other people's workflows (eg. removal of stashId requirement or custom_tags field).

## What was added or changed:

- added hook on performer update that extracts new image, so you don't have to run it manually or update scene
- added possibility to change batch size (there is an unknown bug when batch size is bigger than 1)
- removed requirement for scene to have stashId
- added posibility to change the name of generated nfo file, so now it can be movie.nfo which can be automatically updated by Jellyfin
- added posibility to change the name of generated poster image, so now you can name it folder.jpg and Jellyfin won't generate additional file
- added posibility to generate backdrop.jpg which can be read by Jellyfin
- added posibility to modify which rating field to use so you can export your ratings into "rating" field instead of "userrating", which can be read and correctly displayed by Jellyfin.
- added exporting of director for scene
- removed custom_rating field
- added posibility to change default genere for scenes
