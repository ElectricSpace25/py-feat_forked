Lazy fork of [py-feat](https://github.com/cosanlab/py-feat/tree/main) that adds a few features to video detection.

The following arguments are added to `detect_video()`:

## Store video in memory
`memory_storage` (default = `False`)

Setting this to `True` will make py-feat store the video in memory instead of continuously reopening it and seeking frames. This removes the problem of each frame taking longer than the last, which **drastically speeds up detection for longer videos**. Do note that large videos can require a lot of memory.

## Disable detection for specific features
`detect_poses, detect_aus, detect_identities, detect_emotions` (default = `True`)

Setting any of these to `False` allows you to disable detection for that specific feature, speeding up detection time and shortening the resulting FEX.

## Disable identity computation
`compute_identities` (default = `True`)

Setting this to `False` will disable the `compute_identities()` function, which uses identity data to calculate "person_0", "person_1", etc, usually seen in the "Identity" column of the FEX. This calculation can take a lot of memory, so it may be useful to disable it. Note that the "Identity" column will still exist in the FEX, it will just have all blank entries. 
