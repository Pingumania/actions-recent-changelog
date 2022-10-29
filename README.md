# actions-recent-changelog
A GitHub Action for generating a "recent changes" file from a larger manually-curated changelog

## Behavior
The action expects to be provided with a markdown file. It will extract the first `Addon | XX.` and all lines between it and the next `Addon | XX.` or the end of the file. These lines will be written as-is to the provided output file.

## Usage
```YAML
    - uses: Pingumania/actions-recent-changelog@main
      with:
        input: CHANGELOG.md
        output: RECENT_CHANGES.md
```
