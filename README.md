# umbra-me/.github

Organisation-level GitHub files for [Umbra](https://github.com/umbra-me).

- `profile/README.md` is the public organisation page at github.com/umbra-me.
- `profile/assets/` holds its banner, project cards and avatar (`umbra-avatar.svg` and its PNG export).

Check the profile with `python3 tools/check_profile.py`: every SVG must parse and every image the profile links must exist.

The profile links images by absolute `raw/main` URLs because organisation pages do not resolve relative paths, so new assets render only after they are pushed to `main`.
