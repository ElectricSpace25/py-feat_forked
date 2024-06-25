Lazy fork of [py-feat](https://github.com/cosanlab/py-feat/tree/main) that adds a few features to video detection.

The following arguments are added to `detect_video()`:

## Storing videos in memory
`memory_storage` (default = `False`)

Setting this to `True` will make py-feat store the video in memory instead of continuously reopening it and seeking frames. This removes the problem of each frame taking longer than the last, which _drastically_ speeds up detection for longer videos. Do note that large videos can require a lot of memory.

## Selective feature disabling
`detect_poses, detect_aus, detect_identities, detect_emotions` (default = `True`)

Setting any of these to `False` allows you to disable detection for that specific feature, speeding up detection time and shortening the resulting FEX.
