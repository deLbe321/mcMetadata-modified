# Modified carrotwaxr's mcMetadata plugin

This repository holds modified version of mcMetadata by carrotwaxr for extending the functionality of [Stash](https://github.com/stashapp/stash) adult media manager.

Modification made to increase compability and interobility between [mcMetadata](https://github.com/carrotwaxr/stash-plugins), [nfoSceneParser](https://github.com/stashapp/CommunityScripts) (other stash plugin) and [Jellyfin.Plugin.Stash](https://github.com/DirtyRacer1337/Jellyfin.Plugin.Stash/).

Here is my workflow for stash, nfo files and Jellyfin:
- Create two folders: `/video/organized` and `/video/unorganized`
- Stash reads files from both folders while Jellyfin reads only from organized
- Place new content to `/video/unorganized`
- Once all the information are filled and video is marked as organized mcMetadata plugin kicks in
- mcMetada moves files from unorganized folder to organized, each movie in separate folder eg `/videos/organized/<Studio>/<Title> (<Date>)/<Title> (<Date>).mp4`
- Once the file has been moved, in the same folder `movie.nfo`, `folder.jpg` and `backdrop.jpg` are being generated
- Jellyfin scans `/video/organized` folder and load data from movie.nfo, folder.jpg and backdrop.jpg files
- Jellyfin displays rating from `rating` field and pulls any additional data from Stash using Jellyfin.Plugin.Stash
- Jellyfin.Plugin.Stash can be set to load tags for scenes and performers which then can be used to filter content
- Jellyfin updates `movie.nfo` file if necessary
- nfoSceneParser can read `movie.nfo` file and fill most of the information back if necessary (including rating, studio and tags)

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

## Disclaimers

I didn't create pull request to the original repository and created fork instead because some modifications felt arbitrary, tailored to my specific needs and could break other people's workflows (eg. removal of stashId requirement or custom_tags field).

Additional modifications has been merged to Jellyfin.Plugin.Stash repository to make the workflow possible.

Additional modifications has been made and are waiting to be merge into Stash CummunityScripts/nfoSceneParser.
