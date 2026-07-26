# actions-recent-changelog
A GitHub Action for generating a "recent changes" file from a larger manually-curated changelog

## Behavior
The action expects to be provided with a markdown file. It will extract all lines from the start of the file up to (but not including) the first separator line (`*****` by default), or the end of the file if no separator is found. Blank lines are dropped; the rest are written to the provided output file.

## Usage
```YAML
    - uses: Pingumania/actions-recent-changelog@v2
      with:
        input: CHANGELOG.md
        output: RECENT_CHANGES.md
        separator: '*****'
```
